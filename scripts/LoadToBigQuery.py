import pyspark
import argparse
from pyspark.sql import SparkSession

parser = argparse.ArgumentParser()
parser.add_argument('--dataproc_temporaryGcsBucket', required=True)
parser.add_argument('--bigquery_schema', required=True)
parser.add_argument('--bucket_name', required=True)
parser.add_argument('--bigquerytable_writemode', nargs = '?' , required=False, choices=['overwrite','append'], const='overwrite')

args = parser.parse_args()
dataproc_temporaryGcsBucket = args.dataproc_temporaryGcsBucket
bigquery_schema = args.bigquery_schema+'.'
bucket_name = args.bucket_name
bigquerytable_writemode = args.bigquerytable_writemode

print('input arguments')
print('dataproc_temporaryGcsBucket ',dataproc_temporaryGcsBucket)
print('bigquery_schema ',bigquery_schema)
print('bucket_name ',bucket_name)
print('bigquerytable_writemode ',bigquerytable_writemode)


spark = SparkSession.builder \
    .appName('test') \
    .getOrCreate()

spark.conf.set('temporaryGcsBucket',dataproc_temporaryGcsBucket)

input_datasource = 'gs://'+bucket_name+'/netflix_data_modified/*/*'
print(input_datasource)
df = spark.read.parquet(input_datasource)

df.createOrReplaceTempView('netflix_movies')

#all netflix movies in the dataset
df_netflix_movies = spark.sql("""
SELECT 
title , 
availability ,
release_date , 
hours_viewed , 
number_of_ratings , 
rating , 
year, 
month,
concat(year,'/',month) yearandmonth,
rank
    from 
        (
        SELECT *, 
        YEAR(TO_DATE(release_date)) year, 
        MONTH(TO_DATE(release_date)) month ,  
        DENSE_RANK() OVER (
        PARTITION BY 
        YEAR(TO_DATE(release_date)), MONTH(TO_DATE(release_date)) 
        ORDER BY number_of_ratings DESC, rating DESC) as rank
        from netflix_movies 
        )  
        order by year DESC, month DESC, rank ASC
""")

df_netflix_movies.write.format('bigquery') \
    .option('table', bigquery_schema+'netflix_movies') \
    .mode(bigquerytable_writemode) \
    .save()


df_netflix_top_movies = spark.sql("""
SELECT 
title , 
concat(year,'/',month) yearandmonth,
rank
    from 
        (
        SELECT *, 
        YEAR(TO_DATE(release_date)) year, 
        MONTH(TO_DATE(release_date)) month ,  
        DENSE_RANK() OVER (
        PARTITION BY 
        YEAR(TO_DATE(release_date)), MONTH(TO_DATE(release_date)) 
        ORDER BY number_of_ratings DESC, rating DESC) as rank
        from netflix_movies 
        )  
        where rank <= 3                       
""")

df_netflix_top_movies.write.format('bigquery') \
    .option('table', bigquery_schema+'netflix_top_movies') \
    .mode(bigquerytable_writemode) \
    .save()


#all netflix genres
df_netflix_genres = spark.sql("""
SELECT 
REPLACE(genre_type, "'", "") genre_type, 
title ,  
availability , 
release_date ,  
hours_viewed , 
number_of_ratings ,  
rating ,  
year , 
month , 
concat(year,'/',month) yearandmonth
from 
(
    SELECT explode(split(genre, ',')) AS genre_type, 
    title , 
    availability ,
    release_date , 
    hours_viewed , 
    number_of_ratings , 
    rating , 
    YEAR(TO_DATE(release_date)) year, 
    MONTH(TO_DATE(release_date)) month 
    FROM netflix_movies
)
""")

df_netflix_genres.write.format('bigquery') \
    .option('table', bigquery_schema+'netflix_genre') \
    .mode(bigquerytable_writemode) \
    .save()
