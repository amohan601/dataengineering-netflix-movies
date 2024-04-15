from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
import os
import pyarrow as pa
import pyarrow.parquet as pq

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =  '/home/src/gcp-creds.json'
    #bucket_name = kwargs['BUCKET_NAME']
    bucket_name = os.environ.get('BUCKET_NAME')
    print('bucket name selected ',bucket_name)
    #project_id = kwargs['PROJECT_ID']
    project_id = os.environ.get('PROJECT_ID')
    print('project_id selected ',project_id)
    table_name = 'netflix_data_modified'
    print('table_name ',table_name)
    root_path = f'{bucket_name}/{table_name}'
    table = pa.Table.from_pandas(df)
    gcs = pa.fs.GcsFileSystem()
   

    pq.write_to_dataset(
        table,
        root_path = root_path,
        partition_cols =  ['year','month'],
        filesystem = gcs
    )
