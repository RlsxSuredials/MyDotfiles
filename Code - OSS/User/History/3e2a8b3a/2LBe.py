import httpx
import random
import sys

# Función para obtener una línea aleatoria de un archivo
def get_random_line(file_path):
    lines = open(file_path).read().splitlines()
    return random.choice(lines)

# URL de destino
url = "https://chess-velocity-exhibitions-class.trycloudflare.com/login.php"

# Cargar los proxies válidos desde el archivo
with open('VALID_PROXY.txt') as f:
    proxies = [line.strip() for line in f]

# El número de veces que se debe ejecutar el código se pasa como argumento de línea de comandos
num_runs = int(sys.argv[1]) if len(sys.argv) > 1 else 1

for _ in range(num_runs):

    # Lee un email y una contraseña aleatoria de los archivos de texto
    email = get_random_line('data/emails.txt')
    password = get_random_line('data/passwords.txt')

    # Datos a enviar por POST
    data = {
        "jazoest": "2888",
        "lsd": "AVqK7GczFT0",
        "email": email,
        "pass": password,
        "login_source": "comet_headerless_login",
        "next": "",
        "login": "1"
    }

    # Encabezados HTTP
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://chess-velocity-exhibitions-class.trycloudflare.com/",
        "Content-Type": "application/x-www-form-urlencoded",
        "Dnt": "1",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Te": "trailers",
        "Connection": "close",
        "Host": "bt-org-dell-mysql.trycloudflare.com",
        "Origin": "https://chess-velocity-exhibitions-class.trycloudflare.com/",
    }

    # Selecciona un proxy aleatorio
    proxy = random.choice(proxies)
    proxies_httpx = {
        "http://": proxy,
        "https://": proxy,
    }

    # Envía la solicitud POST
    response = httpx.post(url, headers=headers, data=data, proxies=proxies_httpx)

    # Imprime la respuesta
    print(response.text)