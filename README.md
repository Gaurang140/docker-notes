# Docker and Docker Compose Cheat Sheet


## Why Choose Docker?

Docker provides developers with the flexibility to create applications using any programming language and toolchain. Applications that are containerized with Docker are highly portable, capable of running seamlessly on various platforms, including macOS, Windows laptops, cloud servers operating on Ubuntu, and VMs within production data centers powered by Red Hat.

Developers can jump-start their projects by leveraging over 13,000 pre-existing applications from Docker Hub. Docker simplifies the management of changes and dependencies, facilitating sysadmins' comprehension of how these applications function. Through Docker Hub, developers can automate their building process, sharing their creations with collaborators via public or private repositories.

Ultimately, Docker empowers developers to construct and deliver applications of superior quality at an accelerated pace.


## Docker Commands

### Pulling Images

To pull the PostgreSQL Docker image, you can use the following command:

```sh
docker pull postgres
```

### Running Containers

To run a PostgreSQL Docker container, you can use the following command:

```sh
docker run -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```

## Running Containers in Detached Mode (`-d`) with Custom Names

Running Docker containers in detached mode (`-d`) allows them to operate in the background, separated from your terminal session. Combining this with the `--name` option provides a powerful way to manage and differentiate your containers.

For example, to launch a PostgreSQL container in detached mode with a specified custom name:

```sh
docker run --name my-postgres-container -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```

### Using the `--name` Option in Docker Containers

When running Docker containers, the `--name` option allows you to specify a custom name for the container. This name serves as an identifier that makes managing and interacting with containers more intuitive and organized.

For instance, consider the following example where you're creating multiple PostgreSQL containers for different purposes:

```sh
docker run -d --name development-db -e POSTGRES_PASSWORD=mysecretpassword postgres
docker run -d --name production-db -e POSTGRES_PASSWORD=supersecret postgres
```

## Checking Running Containers

After starting a container, you can use the following command to check all running containers:

```sh
docker ps
```

This command will provide a list of all the running containers, including their details such as Container ID, Image, Command, Created time, Status, Ports, and Names (if specified).

For example:

```sql
CONTAINER ID   IMAGE      COMMAND                  CREATED              STATUS              PORTS      NAMES
d088653c4e52   postgres   "docker-entrypoint.s…"   About a minute ago   Up About a minute   5432/tcp   my-postgres-container
```

This information is valuable for monitoring and managing your running Docker containers.



## Stopping Containers 

To halt a running container, you can use the `docker stop` command followed by the container's name or ID. This will gracefully stop the container, allowing it to perform any necessary cleanup before shutting down.

### Syntax:

```sh
docker stop <container_name_or_id>
```

For instance, if you have a container named "my-postgres-container" that you want to stop, you would execute the following command:

```sh
docker stop my-postgres-container
```

Once stopped, the container will exit, and you can verify its status using other Docker commands like `docker ps -a` to list all containers, including the stopped ones.


## Viewing Stopped Containers

After stopping a container using the `docker stop` command, you can use the `docker ps -a` command to view a list of all containers, including those that have exited or stopped. This command provides valuable information about the status, creation time, and other details of each container.

### Syntax:

```sh
docker ps -a
```

For example, running the `docker ps -a` command might yield an output similar to the following:

```sh
CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS                         PORTS     NAMES
d088653c4e52   postgres   "docker-entrypoint.s…"   21 minutes ago   Exited (0) 17 minutes ago                my-postgres-container
904f40453641   postgres   "docker-entrypoint.s…"   2 hours ago      Exited (0) 2 hours ago                   my-post-gres-three
104563e710e2   postgres   "docker-entrypoint.s…"   2 hours ago      Exited (0) About an hour ago             my-postgre-two
133eb2c38c48   postgres   "docker-entrypoint.s…"   2 hours ago      Exited (0) About an hour ago             my-postgre-one
28d7098af8f4   postgres   "docker-entrypoint.s…"   2 hours ago      Exited (0) 2 hours ago                   sweet_sanderson
665d39b1a5ec   postgres   "docker-entrypoint.s…"   2 hours ago      Exited (0) 2 hours ago                   blissful_swanson
ca1d4c5f498e   postgres   "docker-entrypoint.s…"   2 hours ago      Exited (1) 2 hours ago                   busy_moore
```

In this output, you can see a list of containers along with their Container IDs, Images used, the command executed, creation time, exit status, and the custom names assigned to the containers (if any). This information can be helpful for tracking and managing your containers' lifecycles.

The `docker ps -a` command is especially useful for viewing both running and stopped containers.




### Building Images

- Build an image: `docker build -t image_name:tag .`
- List images: `docker images`

### Managing Containers

- Run a container: `docker run -d --name container_name image_name:tag`
- List running containers: `docker ps`
- List all containers (including stopped ones): `docker ps -a`
- Stop a container: `docker stop container_name`
- Start a stopped container: `docker start container_name`
- Remove a container: `docker rm container_name`

### Working with Images and Containers

- Inspect a container or image: `docker inspect container_or_image_id`
- View logs of a container: `docker logs container_name`
- Enter a running container: `docker exec -it container_name /bin/bash`
- Copy files between host and container: `docker cp /path/to/file container_name:/path/in/container`

### Port Mapping

- Run a container with port mapping: `docker run -p host_port:container_port image_name:tag`
- Example: `docker run -p 8080:80 nginx`

### Removing Resources

- Remove an image: `docker rmi image_name:tag`
- Remove all stopped containers: `docker container prune`
- Remove all unused images: `docker image prune`
- Remove all unused volumes: `docker volume prune`

## Docker Compose Commands

### Basic Operations

- Start services defined in docker-compose.yml: `docker-compose up`
- Start services in detached mode: `docker-compose up -d`
- Stop services: `docker-compose down`

### Building and Running

- Build and start services: `docker-compose up --build`
- Build specific service: `docker-compose build service_name`
- Build and run specific service: `docker-compose up --build service_name`

### Managing Services

- List running services: `docker-compose ps`
- Execute a command in a running service: `docker-compose exec service_name command`
- View service logs: `docker-compose logs service_name`

### Scaling Services

- Scale a service to N replicas: `docker-compose up --scale service_name=N`

### Port Mapping

- Define port mapping in docker-compose.yml:
  ```yaml
  services:
  mongo:
    image: mongo
    ports:
      - "27017:27017"
  web:
    build: ./
    ports:
      - "5000:5000"
    depends_on:
      - mongo
    environment:
      uri :   "mongodb+srv://gaurang:khkhkhk@cluster0.ogtv1f4.mongodb.net/?retryWrites=true&w=majority"
    image: myflaskapp:1.0
