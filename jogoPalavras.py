#Jogo de palavra, sistema esconde a palavra e a pessoa deve ir digitando letras até acertar toda a palavra
import os
cls = lambda: os.system('cls') #Limpar o terminal

def jogoPalavras(palavra, chances): 
    digitadas = []
    while True:
        if chances <=0:
            print()
            print("**Você esgotou suas chances!**")
            break
        letra = input('Digite uma letra: ')
        
        if len(letra) > 1:
            print()
            print('Digite apenas uma letra. ')
            continue
        
        digitadas.append(letra)
        
        if letra in palavra:
            print()
            print('Acertou uma letra. ')
        else:
            print()
            print(f'A letra {letra} não tem na palavra. ')
            digitadas.pop()
            
        palavra_temp = ''
        for letra_secreta in palavra:
            if letra_secreta in digitadas:
                palavra_temp += letra_secreta
            else:
                palavra_temp += '*'
        
        if palavra_temp == palavra:
            print()
            print(f'***VOCÊ GANHOU!!*** A palavra era {palavra_temp}.')
            break
        else:
            print()
            print(f'Palavra: {palavra_temp}')
        
        if letra not in palavra:
            chances -= 1
        print()    
        print(f'Você tem mais {chances} chances.')
        print()
    
        
print()
palavra = input('Informa uma palavra: ')
print()
chances = int(input('Informe o total de chances: '))
cls()
jogoPalavras(palavra, chances)