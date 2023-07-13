[//]: # (Copyright \(c\) 2023 by Delphix. All rights reserved.)

# Mongo

MongoDB Hyperscale Compliance Connector

## Pre-requisite

Download the delphix hyperscale masking tar.gz from [downloads.delphix](https://download.delphix.com/folder/2224/Delphix%20Product%20Releases/Hyperscale%20Compliance)
and unzip it inside `mongo-hsm` folder

Folder structure should look like below:
```commandline
- mongo-hsm
    - delphix-hyperscale-masking-10.0.0
        - controller-service.tar
        - masking-service.tar
        - proxy.tar
```


## Usage

Use the make commands to automatically create the virtual environment and docker images for the services

```commandline
make help
```

All the functionalities of make file will be listed here.

Use the below command to start all the docker containers using docker-compose file.

```
make compose-up VERSION=10.0.0
```

<u>**Note**</u>: <i> Default VERSION is 8.0.0 if not supplied</i>

Output:
```commandline
NAME                             IMAGE                                     COMMAND                  SERVICE              CREATED             STATUS                                     PORTS
mongo-hsm-controller-service-1   delphix-controller-service-app:10.0.0     "java -XX:+HeapDumpO…"   controller-service   1 second ago        Up Less than a second (health: starting)   
mongo-hsm-load-service-1         delphix-mongo-load-service-app:latest     "../start.sh"            load-service         1 second ago        Up Less than a second                      0.0.0.0:8081->8080/tcp
mongo-hsm-masking-service-1      delphix-masking-service-app:10.0.0        "java -XX:+HeapDumpO…"   masking-service      1 second ago        Up Less than a second                      0.0.0.0:8083->8080/tcp
mongo-hsm-proxy-1                delphix-hyperscale-masking-proxy:10.0.0   "/bootstrap.sh"          proxy                1 second ago        Up Less than a second                      0.0.0.0:80->80/tcp, 0.0.0.0:443->443/tcp
mongo-hsm-unload-service-1       delphix-mongo-unload-service-app:latest   "../start.sh"            unload-service       1 second ago        Up Less than a second                      0.0.0.0:8082->8080/tcp
```

Here 10.0.0 is the delphix hyperscale masking version from the downloaded tar.gz file

We can test the same mongo services with different delphix hyperscale masking versions by following the same approach as mentioned above

When we re-run the command with `VERSION=8.0.0` it will replace the 10.0.0 containers with 8.0.0 containers

```
make compose-up VERSION=8.0.0
```

Output:
```commandline
NAME                             IMAGE                                     COMMAND                  SERVICE              CREATED             STATUS                           PORTS
mongo-hsm-controller-service-1   delphix-controller-service-app:8.0.0      "java -jar /opt/delp…"   controller-service   2 seconds ago       Up 1 second (health: starting)   
mongo-hsm-load-service-1         delphix-mongo-load-service-app:latest     "../start.sh"            load-service         2 seconds ago       Up 1 second                      0.0.0.0:8081->8080/tcp
mongo-hsm-masking-service-1      delphix-masking-service-app:8.0.0         "java -XX:+HeapDumpO…"   masking-service      2 seconds ago       Up 1 second                      0.0.0.0:8083->8080/tcp
mongo-hsm-proxy-1                delphix-hyperscale-masking-proxy:8.0.0    "/bootstrap.sh"          proxy                2 seconds ago       Up Less than a second            0.0.0.0:80->80/tcp, 0.0.0.0:443->443/tcp
mongo-hsm-unload-service-1       delphix-mongo-unload-service-app:latest   "../start.sh"            unload-service       2 seconds ago       Up 1 second                      0.0.0.0:8082->8080/tcp
```

