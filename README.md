![DockerFile](https://raw.githubusercontent.com/ggjiuw/2_homework271123_docker/main/github_assets/DockerLogo.png)
```DockerFile
FROM python:3.10.3-slim

WORKDIR /app

COPY . .

CMD ["python", "main.py"]
```

## How to build docker image?
```sh
docker build current_dir -t image_name
```
- or
```sh
docker build current_dir -t image_name -f DockerFile_path
```

## How to run?
```sh
docker run -it image_name
```
