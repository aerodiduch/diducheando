import requests

url = "https://mercados.ambito.com//dolar/informal/variacion"
response = requests.get(url)

respuesta_linda = response.json()

print(respuesta_linda['venta'])
