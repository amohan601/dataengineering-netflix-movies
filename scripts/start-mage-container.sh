set -e

echo 'starting the mage container set up process' 

PROJECT_ID=$1
BUCKET_NAME=$2
GCP_CREDS=$3

echo 'Variables received '
echo 'PROJECT_ID:  ' $PROJECT_ID
echo 'BUCKET_NAME:  ' $BUCKET_NAME

echo ''

cd mage_orchestrator

docker build --tag magetest:latest . 

docker run -it -p 6789:6789  \
-e INPUT_URL=https://raw.githubusercontent.com/amohan601/dataengineering-zoomcamp2024/main/total_netflix_2023.csv \
-e PROJECT_ID=${PROJECT_ID} \
-e BUCKET_NAME=${BUCKET_NAME} \
-v .:/home/src/ \
magetest:latest /app/run_app.sh mage start mage-netflix-movies
