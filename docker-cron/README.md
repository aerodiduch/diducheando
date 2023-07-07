# Docker-Cron

Una pequeña imagen para correr crontab en docker.

# 

Buildear la imagen
```
docker build -t "docker-cron" .
```

Ejecutar la imagen en background
```
docker run --name docker-cron -d docker-cron
```

Ver los logs del contenedor:
```
docker logs docker-cron --follow
```