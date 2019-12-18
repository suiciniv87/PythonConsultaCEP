import requests

print ('''#############################
########Consulta CEP#########
#############################
''')
print()

def consulta(numero_cep):
    consulta_cep = requests.get('https://viacep.com.br/ws/{}/json/'.format(numero_cep))
    consultaCep = consulta_cep.json()
    print('CEP {} encontrado!'.format(numero_cep))
    print('Logradouro: {}'.format(consultaCep['logradouro']))
    print('Bairro: {}'.format(consultaCep['bairro']))
    print('Cidade: {} - Estado: {}'.format(consultaCep['localidade'], consultaCep['uf']))


numero_cep = input('Digite o CEP a ser consultado: ')
if len(numero_cep) != 8:
    print('O CEP é inválido!')
else: 
    consulta(numero_cep)

