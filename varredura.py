import requests
from bs4 import BeautifulSoup
from googlesearch import search
import time
import random

headers = {"User-Agent": "Mozilla/5.0"}

def buscar():
    query = '"estágio front-end OR estagiário front-end"'
    resultados_do_google = search(query, num=20)

    def verificar_e_adicionar(resultados, fonte):
        for url in resultados:
            print(f"Verificando ({fonte}): {url}")
            try:
                # Adicionando o cabeçalho nas requisições
                resposta = requests.get(url, timeout=10, headers=headers)
                time.sleep(random.uniform(2, 7))  
                soup = BeautifulSoup(resposta.text, 'html.parser')

                if any(keyword in soup.text.lower() for keyword in [
                    "estágio front-end",
                    "estagiário front-end",
                    "pessoa front-end",
                    "front-end",
                    "vaga front-end"
                ]):
                    print(f"Oportunidade encontrada ({fonte}): {url}")

            except requests.exceptions.RequestException as e:
                print(f"Erro ao acessar {url}: {e}")

    verificar_e_adicionar(resultados_do_google, "Google")

buscar()
