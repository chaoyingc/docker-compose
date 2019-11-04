### docker-compose
#### This repository will create a python API running on docker-compose,the application uses the Flask framework and has an image Redis.

### Requirements:
- docker-compose

### how it works?
1, download all files in this repository:
```
git clone https://github.com/chaoyingc/docker-compose.git
```
2,Run the application:
```
docker-compose up
```
3,to test the app:
```
curl --header "Content-Type: application/json" --request POST --data '{"text":"Hello Oscaro !!"}' localhost:5000
```

4, to stop the app:
```
docker-compose down
```
5,to remove volumes:
```
docker-compose down --volume
```
