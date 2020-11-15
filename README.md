# Docker Basics

To list all containers
``` bash
docker images
```
Pull a specific image
``` bash
docker pull image:tag
```
List running containers
``` bash
docker ps
docker container ls
```
List all containers
``` bash
docker ps -a
docker container ls -a
```
Run container from image
``` bash
docker run --name name image:tag
```

Run container in background
``` bash
docker run -d --name name image:tag
```

Start a container / Stop a container
``` bash
docker start/stop
```

DOCKER INTERACTIONS
-------------------
Port forward
```bash
docker run --name nginx1 -p 80:80 -d nginx
```

 Execute command inside running container
```bash
docker exec nginx touch new.txt
```

Execute command Interactivity inside running container

```bash
docker exec -it nginx bash
```

Get logs from runing container
``` bash
docker logs -t nginx
```


Get information on runnning container
```bash
docker inspect nginx
```

Pass env variable to container
```bash
docker run -e REDIS_HOST=172.17.0.6  goapp-network
```

# Creating Dockerfiles

Use the official image as a parent image.
``` bash
FROM node:current-slim
```

Set the working directory.
``` bash
WORKDIR /usr/src/app
```

Copy the file from your host to your current location.
``` bash
COPY package.json .
```

Run the command inside your image filesystem.
``` bash
RUN npm install
```
 Add metadata to the image to describe which port the container is listening on at runtime.
``` bash
EXPOSE 8080
```
 Run the specified command within the container.
``` bash
CMD [ "npm", "start" ]
```

Running the dockerfile
```bash
docker build -t helloapp:v1 .
```

# DOCKER IMAGES
---
Build image
``` bash
docker built -t image:tag .
```
Run container from image
``` bash
docker run image:tag
```
Run container in background
``` bash
docker run -d image:tag
```
Stop container
``` bash
docker stop container-id/name
```
Create tag
``` bash
docker tag currentImage:tag newImage:newTag
```
Push image to docker hub
``` bash
docker push namespace/image:tag
```

# Docker Multistaage Build

## Build Stage
First stage to build the application
``` bash
FROM golang as build

WORKDIR /usr/src

COPY . .

RUN make build-linux
```

## Run Stage
Second stage to run the application
``` bash
FROM alpine

COPY --from=build /usr/src/out/ .

CMD ["./go-app"]
```


# DOCKER VOLUMES
--------------
Create a volume
```bash
docker volume create demo
```
List all volumes
```bash
docker volume ls
```

Llist info of volume
```bash
docker inspect demo
```

 remove a volume
```bash
docker volume rm demo
```

attach volume to container
```bash
docker run -it -v my-volume:/data --name my-container ubuntu:latest
```

Detach volume from container
```bash
docker rm -v <container_sha>
```

DOCKER NETWORK
--------------
create a network
```bash
docker network create my_network
```
list all network
```bash
docker network ls
```

list info of network
```bash
docker network inspect my_network
```

remove network
```bash
docker network rm my_network
```

connect network
```bash
docker network connect my_network nginx
```

disconnect network
```bash
docker network disconnect my_network nginx
```


DOCKER COMPOSE:
---
run compose file
``` bash
docker-compose up
```

run compose file in background
```bash
docker-compose up -d
```

only build
```bash
docker-compose build
```

scale up/down
```bash
docker-compose scale web=2
docker-compose scale redis=2
```

destroy compose
```bash
docker-compose down
```