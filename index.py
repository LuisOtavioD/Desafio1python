# Missão 1: Restaurando as Regras Escolares 📝 

nota = 6
if nota >= 6 :
    print(" Você foi aprovado")
elif nota <=5 :
    print("Você foi reprovado")

# Missão 2: O Sistema Eleitoral Secreto 📝 

idade = int(input("Qual a sua idade?"))
if idade >= 16:
    print("Você pode votar")
elif idade <= 16:
    print("Você não pode votar")

# Missão 3: Recuperando o Sistema de Notas 📊

nota_prova = int(input("Qual sua nota? "))
if  90 <= nota_prova >= 100 :
    print("Parabéns, você tirou A!")
elif 80 <= nota_prova <= 89 :
    print("Muito bem, você tirou B.")
elif 70 <= nota_prova <= 79 :
    print("Bom trabalho, você tirou C.")
elif 60 <= nota_prova <=  69 :
    print("Fique atento, você tirou D")
else :
    print("Estude um pouco mais, você tirou F.")

# Missão 4: Restaurando a Identificação de Números ⚖️

primeiro_Numero = float(input("Qual o primeiro valor?"))
segundo_Numero = float(input("Qual o segundo valor?"))
print(f'resultado: {primeiro_Numero + segundo_Numero}')

# Missão 5: Recuperando o Cofre de Segurança 🔒

senha = input("Insira a senha:")
if senha == "Python123":
    print('Acesso consedido')
else:
    print("Senha incorreta")

# Missão 6: Reforçando a Segurança e a Contagem do Sistema 💾

numero = 1

while numero <= 10 :
    print(numero)
    numero+=1

# Missão 7: Organizando a Lista📋

numeros = [8, 3, 10, 1, 5] 
numeros.sort()
print(numeros)

# Missão 8: Acessando os Registros de Alunos 🏷️

nomes = ('Ana', 'Bruno', 'Carla', 'Daniel', 'Eduardo')
print(nomes[0])
print(nomes[-1])

# Missão 9: Calculando Dobro de um Número 🛠️

numero_dobro = float(input("Insira um numero: "))
print(f'O dobro deste numero é {2 * numero_dobro}')

# Missão 10: Contando Letras 🔄

nome = input("Digite seu nome: ")
contar_letras = len(nome)
print(f"{nome} tem {contar_letras} letras ")