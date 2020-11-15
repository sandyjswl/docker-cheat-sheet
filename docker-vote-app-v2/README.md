# Project to create two containers one for vote app and a redis container to store the votes


## To build the vote app image

```bash
docker build -t vote_app:v1 .
```

## Create a network

```bash
1. docker network create vote_network
2. docker network ls
```

## Create Redis Container and connect it to the network

```bash
1.  docker run --name vote_redis --net=vote_network -e ALLOW_EMPTY_PASSWORD=yes -p 7001:6379 -d  bitnami/redis
```

Note:- Port forwarding is not necessary here and we'll connect from one container to another. so we can remove that

## Create the vote app container and pass the redis container ports and name as parameters

```bash
docker run --name vote_app --net=vote_network  -e REDIS_HOST=vote_redis_2 -e REDIS_PORT=6379 -p 5000:5000 -d  flask_vote_app:v2.0

```
## Check if it's working

```bash
curl localhost:5000
```