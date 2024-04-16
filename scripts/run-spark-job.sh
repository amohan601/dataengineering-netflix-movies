set -e

echo 'starting spark job execution' 

GCP_CREDS=$1
BUCKET_NAME=$2
GCLOUD_UTIL_PATH=$3
DATAPROC_CLUSTER_NAME=$4
DATAPROC_CLUSTER_REGION=$5
DATAPROC_TEMPBUCKET_NAME=$6
BIGQUERY_SCHEMA_NAME=$7

echo 'Variables received '
echo 'GCP_CREDS:  ' $GCP_CREDS
echo 'BUCKET_NAME:  ' $BUCKET_NAME
echo 'GCLOUD_UTIL_PATH:  ' $GCLOUD_UTIL_PATH
echo 'DATAPROC_CLUSTER_NAME: ' $DATAPROC_CLUSTER_NAME
echo 'DATAPROC_CLUSTER_REGION: ' $DATAPROC_CLUSTER_REGION
echo 'DATAPROC_TEMPBUCKET_NAME: ' $DATAPROC_TEMPBUCKET_NAME
echo 'BIGQUERY_SCHEMA_NAME: ' $BIGQUERY_SCHEMA_NAME

echo ''

echo 'gcloud  path'
export PATH="${GCLOUD_UTIL_PATH}/:$PATH"
echo $PATH

echo ''

SPARK_CODE_PATH='gs://'+${BUCKET_NAME}+'/code/LoadToBigQuery.py'

echo 'SPARK_CODE_PATH ' ${SPARK_CODE_PATH}

gcloud dataproc jobs submit pyspark \
--cluster=${DATAPROC_CLUSTER_NAME} \
--region=$DATAPROC_CLUSTER_REGION \
--jars=gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar \
scripts/LoadToBigQuery.py     \
-- \
    --dataproc_temporaryGcsBucket=$DATAPROC_TEMPBUCKET_NAME \
    --bigquery_schema=$BIGQUERY_SCHEMA_NAME \
    --bucket_name=$BUCKET_NAME


echo 'finished spark job execution' 