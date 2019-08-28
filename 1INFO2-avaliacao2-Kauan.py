def calcula_idade_canina(idade_humana, porte_do_cao):
    '''
    :param idade_humana: uma idade em formato int, para ser convertida
    :param porte_do_cao: o porte do cão, em format string. Valores possíveis:
        'pequeno', 'médio' ou 'grande'
    :returns: a idade canina, em formato float, com duas casas
            decimais de arredondamento

    Calcule sua idade canina:
    - cães de porte pequeno: dividir sua idade por 5
    - cães de porte médio: dividir sua idade por 6
    - cães grandes: dividir sua idade por 7
    Exemplo: se a idade humana informada for 50 anos,
        e se deseja descobrir a idade canina,
        considerando um cão de porte pequeno, tem-se o seguinte
        cálculo:
        idade_canina = idade_humana / 5, ou seja,
        idade_canina = 50 / 5 = 10
        Nesse caso, o programa deve devolver o valor 10.

    Os possíveis valores para porte_do_cao são: 'pequeno', 'médio' e 'grande'.

    Devolva a idade canina, com arredondamento de duas casas decimais
    Dica: use a função round()
    '''
    if porte_do_cao == 'medio': 
        return round (idade_humana / 6,2)
    elif porte_do_cao == 'pequeno':
        return round (idade_humana / 5,2)
    else: 
        return round (idade_humana / 7,2)

def calcula_aumento_salario(salario_atual):
    '''
    :param salario_atual: um salário de um funcionário, em formato float
    :returns: o novo salário, em formato float, com arrendamento
             de duas casas decimais

    Calcule o novo salário, depois de um aumento salarial,
    de acordo com a seguinte tabela:

    - até 1 Salário Mínimo (inclusive): aumento de 20%
    - de 1 até 2 Salários Mínimos (inclusive): aumento de 15%
    - de 2 até 5 Salários Mínimos (inclusive): aumento de 10%
    - acima de 5 Salários Mínimos: aumento de 5%

    Salário mínimo para referência: R$ 724.00

    Exemplo:
        Se o salario_atual for 800.00.
        Nesse caso, o valor está entre 1 e 2 Salários Mínimos.
        O valor do aumento será de 15%, de acordo com a tabela informada.
        aumento = (salario atual * percentual_aumento) / 100
        aumento = (800 * 15) / 100 = 120.00
        novo_salario = salario_atual + aumento = 800 + 120 = 920

        No caso desse exemplo, o programa deve devolver o valor de 920.00

    Devolva o novo salário com arredondamento de duas casas decimais
    Dica: use a função round()
    '''
    sal_min = 724.00
    
    if salario_atual <= sal_min:
        return round ((salario_atual * 0.20) + salario_atual,2)
    elif salario_atual > sal_min and salario_atual <= sal_min *2:
        return round ((salario_atual * 0.15) + salario_atual,2)
    elif salario_atual > sal_min *2 and salario_atual <= sal_min *5:
        return round ((salario_atual * 0.10) + salario_atual,2)
    else:
        return round ((salario_atual * 0.05)+ salario_atual,2)
        



def nota_para_conceito(nota):
    """
    :param nota: uma nota de uma disciplina, em float
    :returns: o conceito no formato string, de A até E, conforme a tabela:
    Nota                     Conceito
    Entre 10.0 e 9.0            A
    Entre 8.9 e 8.0             B
    Entre 7.9 e 7.0             C
    Entre 6.9 e 6.0             D
    Entre 5.9 e zero            E

    Exemplo: Se for informada a nota 8.5, o programa deve retornar 'B'
    """
    if nota >= 9.0 and nota <= 10.0:
        return 'A'
    elif nota >= 8.0 and nota <= 8.9:
        return 'B'
    elif nota >= 7.0 and nota <= 7.9:
        return 'C'
    elif nota >= 6.0 and nota <= 6.9:
        return 'D'
    else:
        return 'E'


def menor_preco(p1, p2, p3):
    '''
    param p1: um valor de preço 1, em formato float
    param p2: um valor de preço 2, em formato float
    param p2: um valor de preço 3, em formato float
    returns: o menor dos preços, na lista informada.

    Receba o  preço de três produtos e retorne o menor preço.
    Os três preços são diferentes.

    Exemplo:
        se forem informados os valores, p1=10.0, p2=2.50, p3=25,
        o programa deve devolver o valor 2.50.

    Não utilize nenhuma função de ordenação, apenas if-elif-else.'''
    if p1 < p2 and p1 < p3:
        return p1
    elif p2 < p1 and p2 < p3:
        return p2
    else: 
        return p3
    
# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = '\033[31m%s' % ('Falhou')
    else:
        prefixo = '\033[32m%s' % ('Passou')
        acertos += 1
    print('%s Esperado: %s \tObtido: %s\033[1;m' % (prefixo, repr(esperado),
                                                    repr(obtido)))


def main():
    print('Idade canina:')
    test(calcula_idade_canina(40, 'pequeno'), 8)
    test(calcula_idade_canina(40, 'medio'), 6.67)
    test(calcula_idade_canina(40, 'grande'), 5.71)

    print('Aumento salarial:')
    # até 1 SM: 20%
    test(calcula_aumento_salario(500.00), 600.00)
    test(calcula_aumento_salario(724.00), 868.80)
    # 1-2 SM: 15%
    test(calcula_aumento_salario(725.00), 833.75)
    test(calcula_aumento_salario(1448.00), 1665.20)
    # 2-5 SM: 10%
    test(calcula_aumento_salario(1449.00), 1593.90)
    test(calcula_aumento_salario(3620.00), 3982.00)
    # >5 SM: 5%
    test(calcula_aumento_salario(3621.00), 3802.05)
    test(calcula_aumento_salario(4000.00), 4200.00)

    print('Nota para conceito:')
    test(nota_para_conceito(10.0), 'A')
    test(nota_para_conceito(9.1), 'A')
    test(nota_para_conceito(9.0), 'A')
    test(nota_para_conceito(8.9), 'B')
    test(nota_para_conceito(8.1), 'B')
    test(nota_para_conceito(8.0), 'B')
    test(nota_para_conceito(7.9), 'C')
    test(nota_para_conceito(7.1), 'C')
    test(nota_para_conceito(7.0), 'C')
    test(nota_para_conceito(6.9), 'D')
    test(nota_para_conceito(6.1), 'D')
    test(nota_para_conceito(6.0), 'D')
    test(nota_para_conceito(5.9), 'E')
    test(nota_para_conceito(5.1), 'E')
    test(nota_para_conceito(5.0), 'E')
    test(nota_para_conceito(4.9), 'E')
    test(nota_para_conceito(4.0), 'E')

    print('Menor preço:')
    test(menor_preco(1, 2, 3), 1)
    test(menor_preco(1, 3, 2), 1)
    test(menor_preco(2, 1, 3), 1)
    test(menor_preco(2, 3, 1), 1)
    test(menor_preco(3, 1, 2), 1)
    test(menor_preco(3, 2, 1), 1)


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" % (
        total, acertos, total - acertos, float(acertos * 10) / total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")