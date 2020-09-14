def parcela (preco):
    for i in range (1,25):
        valor = ("%.2f" % (preco/(i)))
        print(f'{i}x de R$ {valor}')

def main():
    preco = float(input())
    parcela(preco)
    
if __name__ == '__main__':
    main()