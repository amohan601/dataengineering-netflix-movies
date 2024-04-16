set -e

echo 'starting the automatic resource creation script' 

TERRAFORM_HOME=$1
GCP_CREDS=$2
PROJECT_ID=$3
REGION=$4
LOCATION=$5
BUCKET_NAME=$6
BIGQUERY_DATASET_NAME=$7

echo 'Variables received '
echo 'TERRAFORM_HOME:  ' $TERRAFORM_HOME
echo 'GCP_CREDS:  ' $GCP_CREDS
echo 'PROJECT_ID:  ' $PROJECT_ID
echo 'REGION:  ' $REGION
echo 'LOCATION:  ' $LOCATION
echo 'BUCKET_NAME:  ' $BUCKET_NAME
echo 'BIGQUERY_DATASET_NAME:  ' $BIGQUERY_DATASET_NAME


export PATH="${TERRAFORM_HOME}/:$PATH"
echo $PATH

cd terraform

terraform destroy \
-auto-approve \
-var credentials=${GCP_CREDS} \
-var project=${PROJECT_ID} \
-var region=${REGION} \
-var location=${LOCATION} \
-var gcs_bucket_name=${BUCKET_NAME} \
-var bq_dataset_name=${BIGQUERY_DATASET_NAME}

echo 'finished destroying resources'
cd ..