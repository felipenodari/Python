import itertools
import time
import os


def header():
    print('=-=-=-=-=-=-=-=-=-=-=-= ')
    print('   Wordlist generator   ')
    print('=-=-=-=-=-=-=-=-=-=-=-= ')


def manual():
    os.system('cls')
    print('Bem vindo ao tutorial:')
    print('\tEste software tem como propósito gerar wordlist baseada no input do usuário.')
    print('\t1. É solicitado para digitar uma string que se queira combinar.')
    print('\t2. Após, digite a combinação mínima e a máxima que deseja combinar os caracteres da string.')
    print('\t3. Escolha se você deseja criar a wordlist por combinação ou permutação.')
    print('\t\tOBS: combinação repete os caracteres, fazendo todas as possibilidades')
    print('\t\t     permutação realiza todas as combinações respeitando a quantidade máxima de cada caracter digitado.')
    print('\t4. Escolha se deseja adicionar uma string fixa a estas combinações.')
    print('\t5. Escolha se deseja adicionar essa string ao início ou ao final das combinações.')
    input('Pressione ENTER para sair...')
    os.system('cls')


wordlist = []
resp = add = op = ''
cont = 0
os.system('cls')
header()
print('Input characters to combine')
print('[-man] for tutorial')
frase = str(input('>>> '))
if frase == '-man':
    manual()
    print('\nInput characters to combine')
    frase = str(input('>>> '))
min = int(input('Minimum size of combination: '))
max = int(input('Maximum size of combination: '))
tam = len(frase)
total = 0
fatorial = 1
total2 = 1
cont = tam
for i in range(min, max+1): # calcula combinação
    fatorial = tam
    fatorial = fatorial**i
    total = total + fatorial
print(f'\033[1;32m[+] {total} passwords by [c]ombination\033[0;0m')
#print(f'\033[1;32m[+] {total2} password permutations\033[0;0m')
print('''Create:
[c] - By combination
[p] - By permutation''')
while resp != 'p' and resp != 'c':
            resp = str(input('>>> '))
            if resp == 'p': # by permutation
                while add != 'y' and add != 'n':
                    add = str(input('Do you wanna combine with another string [y / n]: '))
                if add == 'y':
                    string = str(input('String: '))
                    while op != 'b' and op != 'a':
                        op = str(input(f'Put {string} [b]efore or [a]fter: '))
                    if op == 'b':
                        print('\033[1;32m[+] Generating wordlist...\033[0;0m')  
                        file = open('C:/Users/felip/Desktop/My hacking tools/wordlist.txt', 'w')
                        n = 2
                        ini = time.time()
                        for n in range(min, max+1):
                            for word in itertools.permutations(frase, n):
                                file.write(''.join(string) + ''.join(word) + '\n')
                        fim = time.time()
                        file.close()
                        print(f'\033[1;32m\n[+] Wordlist created in {fim-ini:.2f} sec.\033[0;0m\n')  
                        input('... ENTER to exit ...')
                        print()
                        break
                    elif op == 'a':
                        print('\033[1;32m[+] Generating wordlist...\033[0;0m')  
                        file = open('C:/Users/felip/Desktop/My hacking tools/wordlist.txt', 'w')
                        n = 2
                        ini = time.time()
                        for n in range(min, max+1):
                            for word in itertools.permutations(frase, n):
                                file.write(''.join(word) + ''.join(string) + '\n')
                        fim = time.time()
                        file.close()
                        print(f'\033[1;32m\n[+] Wordlist created in {fim-ini:.2f} sec.\033[0;0m\n')  
                        input('... ENTER to exit ...')
                        print()
                        break
                if add == 'n':
                    print('\033[1;32m[+] Generating wordlist...\033[0;0m')  
                    file = open('C:/Users/felip/Desktop/My hacking tools/wordlist.txt', 'w')
                    n = 2
                    ini = time.time()
                    for n in range(min, max+1):
                        for word in itertools.permutations(frase, n):
                            file.write(''.join(word) + '\n')
                    fim = time.time()
                    file.close()
                    print(f'\033[1;32m\n[+] Wordlist created in {fim-ini:.2f} sec.\033[0;0m\n')  
                    input('... ENTER to exit ...')
                    print()
                    break
            if resp == 'c': # by combination
                while add != 'y' and add != 'n':
                    add = str(input('Do you wanna combine with another string [y / n]: '))
                if add == 'y':
                    string = str(input('String: '))
                    while op != 'b' and op != 'a':
                        op = str(input(f'Put {string} [b]efore or [a]fter: '))
                    if op == 'b':
                        print('\033[1;32m[+] Generating wordlist...\033[0;0m')  
                        file = open('C:/Users/felip/Desktop/My hacking tools/wordlist.txt', 'w')
                        n = 2
                        ini = time.time()
                        for n in range(min, max+1):
                            for word in itertools.product(frase, repeat=n):
                                file.write(''.join(string) + ''.join(word) + '\n')
                        fim = time.time()
                        file.close()
                        print(f'\033[1;32m\n[+] Wordlist created in {fim-ini:.2f} sec.\033[0;0m\n')  
                        input('... ENTER to exit ...')
                        print()
                        break
                    if op == 'a':
                        print('\033[1;32m[+] Generating wordlist...\033[0;0m')  
                        file = open('C:/Users/felip/Desktop/My hacking tools/wordlist.txt', 'w')
                        n = 2
                        ini = time.time()
                        for n in range(min, max+1):
                            for word in itertools.product(frase, repeat=n):
                                file.write(''.join(word) + ''.join(string) + '\n')
                                cont = cont + 1
                                if cont % 100000000 == 0:
                                    print(f'{cont} words have been generated.')
                        fim = time.time()
                        file.close()
                        print(f'\033[1;32m\n[+] Wordlist created in {fim-ini:.2f} sec.\033[0;0m\n')  
                        input('... ENTER to exit ...')
                        print()
                        break
                if add == 'n':
                    print('\033[1;32m[+] Generating wordlist...\033[0;0m')  
                    file = open('C:/Users/felip/Desktop/My hacking tools/wordlist.txt', 'w')
                    n = 2
                    ini = time.time()
                    for n in range(min, max+1):
                        for word in itertools.product(frase, repeat=n):
                            file.write(''.join(word) + '\n')
                            cont = cont + 1
                            if cont % 100000000 == 0:
                                print(f'{cont} words have been generated.')
                    fim = time.time()
                    file.close()
                    print(f'\033[1;32m\n[+] Wordlist created in {fim-ini:.2f} sec.\033[0;0m\n')  
                    input('.... ENTER to exit ....')
                    print()
                    break
