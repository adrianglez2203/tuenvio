# import requests
# # https://www.tuenvio.cu/carlos3/Products?depPid=52
# from bs4 import BeautifulSoup
# url_to_parse = "https://en.wikipedia.org/wiki/Python_(programming_language)"
# url_to_parse1 = "https://www.tuenvio.cu/carlos3/Products?depPid=0"
# response = requests.get(url_to_parse1)
# response_text = response.text
# soup = BeautifulSoup(response_text, 'lxml')
# print(url_to_parse1)
#
from bs4 import BeautifulSoup
import urllib.request
datos=urllib.request.urlopen('https://www.tuenvio.cu/carlos3/Products?depPid=52').read().decode()
# print(datos)
soup = BeautifulSoup(datos, 'lxml')
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href'))
titulos = soup.find_all("div", class_='thumbTitle')
for titulo in titulos:
    print(titulo.text)
