#computadores = 30
#alunos = 20
#computadoresLivres = computadores - alunos
#
#print(f"Quantidade de computadores disponíveis: {computadoresLivres}")
# --------------------------------------------------------------------------------------

#nota1 = float(input("Digite a nota da prova 1: "))
#nota2 = float(input("Digite a nota da prova 2: "))
#nota3 = float(input("Digite a nota da prova 3: "))
#media = (nota1 + nota2 + nota3)/3
#
#print(f"Média das notas é de: {media}")
#print(media >= 7 and media < 10)
#---------------------------------------------------------------------------------------

#idade = int(input("Digite sua idade: "))
#autorizacao = input("Possui autorização para viajar? s/n: ")

#print("Permissão para viajar:", idade >= 18 or autorizacao == 's')

#if idade >= 18 or autorizacao == 's':
#    print("Autorizado para viajar.")
#else:
#    print("Não autorizado")
#---------------------------------------------------------------------------------------

#idade = int(input("Qual sua idade?"))
#
#if idade < 12:
#    print("Criança")
#elif idade < 18:
#    print("Adolescente")
#elif idade < 60:
#    print("Adulto")
#else:
#    print("Idoso")
#---------------------------------------------------------------------------------------

#idades = [8, 9, 29, 21, 25]
#idades.append(30)
#print(idades)
#idades.remove(9)
#print(idades)
#idades.pop(1)
#print(idades)
#print(idades[-1])

nomes = ["Alberto", "Bruno", "Carlos", "Diogo", "Eduardo", "Fernando", "Gustavo", "Heitor", "Igor"]
nomes.append("Juau")
print(nomes)
nomes.remove("Bruno")
nomes.insert(1, "Brendo")
print(nomes)

for nome in nomes:
    print(f"Posição do nome {nome}: {nomes.index(nome)}")