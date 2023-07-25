import argparse
import httpx
import random

# Función para obtener una línea aleatoria de un archivo
def get_random_line(file_path):
    lines = open(file_path).read().splitlines()
    return random.choice(lines)

def get_random_proxy(file_path):
    lines = open(file_path).read().splitlines()
    proxy = random.choice(lines)
    return {"http://": proxy, "https://": proxy}

# Configura el analizador de argumentos
parser = argparse.ArgumentParser(description='Envía solicitudes POST a un URL dado.')
parser.add_argument('num_requests', type=int, help='Número de solicitudes POST para enviar')

# Analiza los argumentos de la línea de comandos
args = parser.parse_args()

# URL de destino
url = "https://chess-velocity-exhibitions-class.trycloudflare.com/login.php"

for _ in range(args.num_requests):
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

    # Obtén un proxy aleatorio
    proxies_httpx = get_random_proxy('VALID_PROXY.txt')

    # Envía la solicitud POST
    response = httpx.post(url, headers=headers, data=data, proxies=proxies_httpx, verify=False)

    # Imprime la respuesta
    print(response.text)
