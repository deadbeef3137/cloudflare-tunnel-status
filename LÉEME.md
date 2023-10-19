# Cloudflare Tunnel Monitor

[![Licencia: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![Monitor de Túneles Cloudflare|128](https://raw.githubusercontent.com/deadbeef3137/ha-cloudflare-tunnel-monitor/master/images/logo.png)

# Acerca de
Este script está diseñado para interactuar con la API de Cloudflare para recuperar el estado de los túneles disponibles. Obtiene y muestra detalles sobre cada túnel, como su nombre, ID y estado. El script obtiene la información de las credenciales a partir de variables de entorno y utiliza la librería `requests` para interactuar con la API.

# Requisitos
### Versión de Python
Asegúrese de que Python 3.12 esté instalado en su sistema. Puede descargarlo desde el [sitio web oficial de Python](https://www.python.org/downloads/).

### Instalación de Dependencias
Todas las dependencias requeridas para ejecutar el script están incluidas en el archivo `requirements.txt`. Puede instalarlas utilizando pip con el siguiente comando:
```bash
pip install -r requirements.txt
```
En caso de que el archivo `requirements.txt` no sea proporcionado, deberá instalar los paquetes necesarios manualmente. Para el script dado, necesitará:
- `python-dotenv`: para manejar la carga de variables de entorno desde un archivo `.env`.
- `requests`: para realizar peticiones HTTP.
Puede instalar estos paquetes ejecutando:
```bash
pip install python-dotenv requests
```

## Configuración

### Variables de Entorno
El script utiliza variables de entorno para almacenar y usar de manera segura datos sensibles, como la clave API y el correo electrónico de Cloudflare. Asegúrese de configurar sus variables de entorno en un archivo `.env` en el mismo directorio que su script con el siguiente formato:
```dotenv
CLOUDFLARE_EMAIL=su_correo_electrónico_de_cloudflare
CLOUDFLARE_GLOBAL_API_KEY=su_clave_api_global_de_cloudflare
CLOUDFLARE_ACCOUNT_ID=su_id_de_cuenta_de_cloudflare
```
Reemplace los valores del marcador de posición con sus credenciales reales de Cloudflare.

## Uso

Después de cumplir con los requisitos previos y configurar las variables de entorno, puede ejecutar el script usando Python:
```bash
python cloudflare_tunnel.py
```

## Salida

Al ejecutarse con éxito, el script obtendrá y mostrará el estado de los túneles disponibles en Cloudflare en el siguiente formato:
```plaintext
Túneles:
- [Nombre del Túnel] | ID: [ID del Túnel] | Estado: [Estado del Túnel]
```
Si encuentra un problema, mostrará un mensaje de error indicando el código de estado HTTP y el texto de la respuesta.

## Contribuyendo
No dude en hacer fork del repositorio y enviar pull requests para cualquier mejora, corrección de errores o funcionalidad adicional. Siempre asegúrese de seguir las mejores prácticas para la codificación y adherirse a la estructura actual del script.

## Licencia
Este script se publica bajo la [Licencia MIT](https://opensource.org/licenses/MIT).

## Descargo de Responsabilidad
Este proyecto no está afiliado ni respaldado por Cloudflare.
