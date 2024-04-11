Mage dataengineering zoomcamp documentation [Get Started with Mage here](https://github.com/mage-ai/mage-zoomcamp)

## Steps to spin up netflix-movies orchestrator in local machine

1. clone this repo
```
git clone https://github.com/amohan601/dataengineering-netflix-movies.git
```
2. navigate to mage project folder
```
cd dataengineering-netflix-movies/mage_orchestrator/mage-netflix-movies
```
3. copy dev.env file to env
```
cp dev.env .env 
```
4. build docker file
```
docker compose build
```
5. start the container
```
docker compose up
```

Wait for few minutes. You should see a message in terminal like Mage is running at http://localhost:6789 and serving project /home/src/magic-zoomcamp
Then access mage with the  URL http://localhost:6789

To tear down the docker container
1. navigate to mage project folder
```
cd dataengineering-netflix-movies/mage_orchestrator/mage-netflix-movies
```
2. stop the container
```
docker compose down
```