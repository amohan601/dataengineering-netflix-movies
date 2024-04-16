set -e

echo 'starting the automatic resource creation script' 

TERRAFORM_HOME=$1
GCP_CREDS=$2
PROJECT_ID=$3
REGION=$4
LOCATION=$5
BUCKET_NAME=$6
BIGQUERY_SCHEMA_NAME=$7

echo 'Variables received '
echo 'TERRAFORM_HOME:  ' $TERRAFORM_HOME
echo 'GCP_CREDS_JSON PATH:  ' $GCP_CREDS
echo 'PROJECT_ID:  ' $PROJECT_ID
echo 'REGION:  ' $REGION
echo 'LOCATION:  ' $LOCATION
echo 'BUCKET_NAME:  ' $BUCKET_NAME
echo 'BIGQUERY_SCHEMA_NAME:  ' $BIGQUERY_SCHEMA_NAME

echo ''

echo 'terraform path'
export PATH="${TERRAFORM_HOME}/:$PATH"
echo $PATH


cd terraform

echo 'starting terraform init' 

terraform init

echo 'starting terraform plan' 

terraform apply \
-auto-approve \
-input=false \
-var credentials=${GCP_CREDS} \
-var project=${PROJECT_ID} \
-var region=${REGION} \
-var location=${LOCATION} \
-var gcs_bucket_name=${BUCKET_NAME} \
-var bq_dataset_name=${BIGQUERY_SCHEMA_NAME}

cd ..

BUCKET_PATH='gs://'${BUCKET_NAME}'/code/'

echo 'the full path to deploy spark code is GCS: ' $BUCKET_PATH

echo 'uploading pyspark code to GCS: ' ${BUCKET_PATH}

gsutil cp scripts/LoadToBigQuery.py ${BUCKET_PATH}

echo 'uploaded pyspark code to GCS: ' ${BUCKET_PATH}
