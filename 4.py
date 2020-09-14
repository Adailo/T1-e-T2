def numeros(n):
    for i in range(10, n, 10):
        if i < 999:
            print(i, end=', ')
        else:
            print(i, end='.')

def main():
    n = 1001
    numeros(n)

if __name__ == '__main__':
    main()
