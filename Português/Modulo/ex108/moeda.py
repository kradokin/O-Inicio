def metade(preco=0):
    return preco / 2


def dobro(preco=0):
    return preco * 2


def aumentar(preco=0):
    return preco * 1.25


def diminuir(preco=0):
    return preco * 0.75


def moeda(preco=0, simb='R$'):
    return f'{simb}{preco:.2f}'.replace('.', ',')
