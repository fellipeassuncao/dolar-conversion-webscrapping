import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.remessaonline.com.br/cotacao/cotacao-dolar')
soup = BeautifulSoup(url.text, 'html.parser')

# Coletar o preço do dolar e fazer as correcoes
# BeautifulSoap
soup = BeautifulSoup(url.text, 'html.parser')
dolar = soup.find('div',{'class':'style__Text-sc-15flwue-2 cSuXFv'}).text[0:4]

dolar = dolar.replace(',','.')
dolar = float(dolar)
dolar = round(dolar, 2)
print(type(dolar))

while True:
    try:
        dolares = int(input("Digite a quantidade de dolares que você possui: "))
    except:
        print("ERROR: Tente novamente!" )
    else:
        break
    
reais = dolares * str(dolar)
reais_final = round(reais,2)
print(f'A quantidade de {dolares} dolares resulta em {reais_final} reais')