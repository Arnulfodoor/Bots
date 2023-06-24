import requests
from bs4 import BeautifulSoup

url = input("Ingrese la dirección del sitio web: ")

response = requests.get(url)

if response.status_code == 200:
    html_content = response.content

    soup = BeautifulSoup(html_content, "html.parser")

    links = soup.find_all("a")
    for link in links:
        print(link.get("href"))

    elements = soup.find_all(class_="nombre-clase")
    for element in elements:
        print(element.text)
else:
    print("Error al obtener la página:", response.status_code)
