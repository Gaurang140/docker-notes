# Docker and Docker Compose Cheat Sheet

## Docker Commands

### Pulling Images

To pull the PostgreSQL Docker image, you can use the following command:

```sh
docker pull postgres
```

To run a PostgreSQL container with a specified password, you can use the following command:

```sh
docker run -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```

## Running Containers in Detached Mode (`-d`) with Custom Names

Running Docker containers in detached mode (`-d`) allows them to operate in the background, separated from your terminal session. Combining this with the `--name` option provides a powerful way to manage and differentiate your containers.

For example, to launch a PostgreSQL container in detached mode with a specified custom name:

```sh
docker run -d --name my-postgres-container -e POSTGRES_PASSWORD=mysecretpassword postgres
```

## Using the `--name` Option in Docker Containers

When running Docker containers, the `--name` option allows you to specify a custom name for the container. This name serves as an identifier that makes managing and interacting with containers more intuitive and organized.

For instance, consider the following example where you're creating multiple PostgreSQL containers for different purposes:

```sh
docker run -d --name development-db -e POSTGRES_PASSWORD=mysecretpassword postgres
docker run -d --name production-db -e POSTGRES_PASSWORD=supersecret postgres
```

