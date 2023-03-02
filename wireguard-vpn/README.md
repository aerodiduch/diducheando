
# Wireguard VPN

Guia del video para poder instalar la VPN con Wireguard

## Recomendaciones
Por medidas de seguridad siempre es bueno poder crear un usuario separado que se encargue de los deploys grandes como es este.

Para crear un nuevo usuario
```sh
sudo useradd <user>
```
Aca vamos a tener que ingresar la contraseña del nuevo usuario.

Para darle permisos de `sudoer`
```sh
sudo usermod -aG sudo <user>
```

Ahora o bien podemos switchear a ese nuevo usuario con `su <user>` o bien dumpear nuestras ssh keys y logearnos con ese nuevo usuario.

## Instalando Wireguard
```sh
sudo apt-get install wireguard
```
Por defecto el directorio `/etc/wireguard` esta owneado por `root`
```sh
sudo chown -R user:user /etc/wireguard 
cd /etc/wireguard
```

## Configurando Wireguard 

### Servidor

Creamos llave publica y privada **para el server**.

```sh
umask 077; wg genkey | tee privatekey | wg pubkey > publickey
```

Creamos el archivo de configuración del servidor
```sh
touch wg0.conf
```

Dentro del archivo colocamos esta configuración.


```
[Interface]
PrivateKey = <llave privada del servidor>
Address = 192.168.69.1/24 # rango de ips dentro de la vpn
ListenPort = 51820 # puerto a la escucha
PostUp = iptables -A FORWARD -i wg0 -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PostDown = iptables -D FORWARD -i wg0 -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE


[Peer]
# Cliente 1
PublicKey= <llave publica cliente>
AllowedIPs=192.168.69.2 # ip asignada para el cliente
PersistentKeepalive=25
```
**IMPORTANTE**: En `PostUp` y `PostDown` es **sumamente importante** que donde dice **wg0** pongamos el nombre que le pusimos al archivo de configuración que estamos editando. Si el archivo se llama **wg0** hay que poner ese nombre.

Por otro lado, la flag `-o eth0` tenemos que cambiar ese `eth0` con la interfaz de red de nuestra pc. En muchas ocasiones va a ser `eth0`, en muchas otras `enp2s0` y si usamos adaptador wifi va a tener otro.

### Cliente

Hacemos un dir `clientes` y generamos nuevamente llaves.
```sh
mkdir clients && cd $_
umask 077; wg genkey | tee privatekey | wg pubkey > publickey
```

Creamos el archivo de configuración para el cliente `cliente.conf`
```
[Interface]
PrivateKey = <llave privada cliente>
Address=192.168.69.2 # ip asignada para el cliente 

[Peer]
# Servidor VPN
PublicKey = <llave publica servidor>
Endpoint = <ip del servidor>:<ListenPort>
AllowedIPs = 0.0.0.0/24 # para ruteo completo. Split tunneling seria solo con IP del servidor, ej 192.168.69.1

```

Con todos estos datos podemos generar ambos archivos. 

### Arrancar VPN Server
Arrancarlo
```sh
sudo wg-quick up wg0
```
Apagarlo
```sh
sudo wg-quick down wg0
```

Enablear el servicio para que siempre este activo.

> **Importante** apagar antes la interfaz para evitar conflictos.
```
sudo systemctl enable wg-quick@wg0
sudo systemctl restart wg-quick@wg0
sudo systemctl status wg-quick@wg0
```

## Conectarnos como cliente
```sh
sudo wg-quick up client
wg show
```

Para verificar la conexion, podemos pinguear al cliente desde el servidor o al servidor desde el cliente
```sh
ping 192.168.69.1
```
