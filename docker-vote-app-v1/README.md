# Beginner docker project to build a image and a container

## Build a sample app which has three endpoints
1. root 
2. check
3. vote -> Increments the number of votes by 1


## To build the image

```bash
docker build -t vote_app:v1 .
```

## To create the container

```bash
docker run --name vote_app -p 5000:5000 -d  vote_app:v1
```

## Check if it's working

```bash
curl localhost:5000
```