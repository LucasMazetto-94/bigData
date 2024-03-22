import urllib.request
import shutil
import csv
import json
import datetime
    
url = r'https://www.jodidata.org/_resources/files/downloads/gas-data/jodi_gas_csv_beta.zip'

# Faz o download do arquivo e salva o arquivo zip na pasta do codigo
urllib.request.urlretrieve(url, 'jodi_gas_beta.zip')

# Extrai o arquivo
shutil.unpack_archive('jodi_gas_beta.zip', extract_dir='.')

# Abre o arquivo
with open('jodi_gas_beta.csv') as f:
    reader = csv.reader(f)
    
    # Criar um array e fazer um append
    i=0
    lista_json = []
    for row in reader:
        if i==0:
            chaves = row
        else:
            row[1] = datetime.datetime.strptime(row[1],'%Y-%m')
            row[1] = f'{row[1].day}/{row[1].month}/{row[1].year} {row[1].hour}:{row[1].minute}:{row[1].second}'
            obj_json = dict(zip(chaves, row))
            lista_json.append(obj_json)                           
        i+=1

    #Converte o objeto Json em String
    obj_json = json.dumps(lista_json)
    #Grava em stdout
    print(obj_json)
# Fecha o arquivo
f.close()
#Cria lista de datas
lista_datas = []
for dic in lista_json:
    lista_datas.append(dic['TIME_PERIOD'])
# Formata datas
datas_for = []
for valor in lista_datas:
    valor = datetime.datetime.strptime(valor, '%d/%m/%Y %H:%M:%S')
    datas_for.append(valor)
data_atual = max(datas_for)
ultima_entrada = f"{data_atual.day}/{data_atual.month}/{data_atual.year}"
print(f'A última data de entrada foi: {ultima_entrada}')


    