# Docker and Docker Compose notes


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



## Port Mapping in Docker - Practical Example

Here's a practical example of using port mapping in Docker:

1. **Run MongoDB Container with Port Mapping**:

You are running a MongoDB container named "mymongodb" and mapping port 5000 on your host machine to port 27017 within the container. This will allow you to access the MongoDB service running inside the container from your host machine through port 5000.

```sh
docker run --name mymongodb -p 5000:27017 -d mongo
```

In this command:
- `--name mymongodb`: Sets the name of the container as "mymongodb".
- `-p 5000:27017`: Maps port 5000 on the host to port 27017 in the container.
- `-d`: Runs the container in detached mode.
- `mongo`: Specifies the Docker image to use (MongoDB).

2. **Check Running Containers**:

After running the container, you can use the `docker ps` command to view the list of running containers:

```sh
docker ps
```

In your case, the output shows that the "mymongodb" container is running:
```sh
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                     NAMES
3b4ff2c4261c   mongo     "docker-entrypoint.s…"   11 seconds ago   Up 10 seconds   0.0.0.0:5000->27017/tcp   mymongodb
```

The information indicates that the container is using the "mongo" image, is up and running, and port 5000 on your host machine is mapped to port 27017 within the container.

Now, you can access your MongoDB service from your host machine using `localhost:5000` or `127.0.0.1:5000`.

Port mapping in Docker facilitates the communication between your host machine and containers, enabling seamless interaction with services inside the containers.

## Docker Prune Command

The `docker container prune` command is used to clean up stopped containers, releasing disk space by removing containers that are no longer in use. This can help to keep your system more organized and prevent unnecessary resource consumption.

### Usage:

```sh
docker container prune
```

### Warning:

When you run `docker container prune`, you will be prompted with a warning message:

```sh
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
```

This warning is to ensure that you are aware of the action you're about to take. If you proceed by typing `y` and pressing Enter, Docker will start removing all stopped containers.

### Example Output:

After running the command and confirming the removal, Docker will display the IDs of the containers that have been deleted, along with the total amount of space reclaimed:

```sh
Deleted Containers:
5789e8b4c8b3973c67f5a414e50171e04c8a804a3854f2af44e738bf5a809de3

Total reclaimed space: 0B
```

This output shows that the container with the ID `5789e8b4c8b3973c67f5a414e50171e04c8a804a3854f2af44e738bf5a809de3` has been deleted, and no space was reclaimed in this case.

Remember that cleaning up stopped containers using `docker container prune` can be especially helpful in environments where containers are frequently started and stopped, preventing unused containers from consuming unnecessary disk space.




## Docker Logs Command

The `docker logs` command allows you to view the logs generated by a running container. These logs provide valuable information about the container's activities, such as application output, errors, warnings, and debugging messages.

### Usage:

```sh
docker logs <container_name_or_id>
```

### Example:

For instance, to view the logs of a container named "my-container":

```sh
docker logs my-container
```

This command will display the logs generated by the specified container in your terminal.

### Options:

| Option         | Description                                                        |
|----------------|--------------------------------------------------------------------|
| `-f`, `--follow` | Stream the logs in real-time, similar to the `tail -f` command.  |
| `--since`       | Show logs since a specific timestamp or relative time.           |
| `--until`       | Show logs until a specific timestamp or relative time.           |
| `--tail`        | Show a specific number of lines from the end of the logs.       |


### Example with Options:

To follow the logs of a container and stream them in real-time:

```sh
docker logs -f my-container
```

To view logs from the last hour:

```sh
docker logs --since 1h my-container
```
Viewing container logs can help you troubleshoot issues, monitor application output, and gain insights into how your containerized applications are performing.

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
