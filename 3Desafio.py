import random
senha = random.randint(1000000,2000000)
senhad = int(input("digite a sua senha>> "))
if senha == senhad:
    print('Você pode acessar a sua conta!')
else:
    print("Senha incorreta!")