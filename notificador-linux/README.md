# notificador-linux

[Creá un NOTIFICADOR por EMAIL cada vez que tu SERVIDOR se REINICIA!](https://www.youtube.com/watch?v=bMazoGWsnNc)

Este proyecto apunta a crear un pequeño sistema de notificacion por email cada vez que nuestro servidor linux se reinicia, ya sea intencionalmente o porque hubo una caida de tensión que lo llevo a eso.



# Requisitos
- Una intalación de Linux
- Python
- Pip
- Paquete python-dotenv

# Paso a paso

Primero clonarmos el archivo `main.py` y lo dejamos tal como está.

A continuamos creamos un archivo en el mismo directorio donde existe `main.py` llamado `.env`.

Instalamos el paquete dotenv
```
pip intall python-dotenv
```

Dentro de este archivo vamos a colocar lo siguiente:

```bash
EMAIL="micorreo@miproveedor.com"
EMAIL_PASSWD="micontraseñasegura"
```
> Importante. Si usamos gmail como proveedor, hay que crear una "Contraseña de aplicación". Ver el video.

Finalmente, si ejecutamos el `main.py` veremos como nos llega un email.

## Seteandolo a nivel sistema

Para añadir esto para que se ejecute cada vez que nuestro sistema se reinicie, tenemos que añadirlo como una tarea en el cron.

```
crontab -e
```

Añadimos la tarea:

```
@reboot sleep 60 && cd /directorio/al/archivo && python3 /directorio/al/archivo/main.py
```
> El "sleep 60" es importante ya que de esta forma le damos al sistema operativo el tiempo suficiente para que cargue todas sus servicios y dependencias necesarias para que todo funciona correctamente.