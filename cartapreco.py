import requests
from bs4 import BeautifulSoup


# Os URL do site do ligamagic mudam após escolher uma carta específica e caem nos padrões abaixo:
 
#  https://www.ligamagic.com.br/?view=cards%2Fcard&card=     Niv-Mizzet%2C+Dracogênio      &tipo=1
#                                                            Niv-Mizzet, Dracogênio 
# 
#  https://www.ligamagic.com.br/?view=cards%2Fcard&card=     Niv-Mizzet+Reborn      &tipo=1
#                                                            Niv-Mizzet Reborn


# Tratamento do input para encaiaxar corretamente no URL
nomecarta = input('nome da carta: ')
nomecarta = nomecarta.title()
nome = nomecarta.replace(', ', '%2C+')
nome = nome.replace(' ', '+')

# Montagem do URL para o requests 
url = 'https://www.ligamagic.com.br/?view=cards%2Fcard&card=' + nome + '&tipo=1'


r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# O preço nem sempre vai estar na tela principal, o codigo vai tentar achar um preço mas no momento apenas os que tem desconto são achados.
# Os preços vão aparecer colados um no outro com o preço sem o desconto primeiro.

# Extração do preço da carta específica
try:
    preco = soup.find('div', {'class' : 'col-prc col-prc-menor'})
    if '0,00' in preco.get_text():
        preco = soup.find('div', {'class' : 'e-mob-preco e-mob-preco-desconto'})
        print(f'O menor preço da sua carta {nomecarta} no LigaMagic é: {preco.get_text()}')
    else:
        print(f'O menor preço da sua carta {nomecarta} no LigaMagic é: {preco.get_text()}')
except:
    print('Nome escrito de froma incompleta ou incorretamente.')