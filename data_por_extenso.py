mes_extenso ={
    1: 'jan',
    2: 'fev',
    3: 'mar',
    4: 'abr',
    5: 'maio',
    6: 'jun',
    7: 'jul',
}

data = "05/06/2019
data2 = data.split('/')

dia = data2[0]
mes = data2[1]
ano = data2[2]

print(dia, ' de ', mes_extenso[mes], ' de ', ano)
