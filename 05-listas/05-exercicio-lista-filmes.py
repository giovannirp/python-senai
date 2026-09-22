# Crie um programa que permita cadastrar filmes em uma lista.

# O programa deve pedir o nome de um filme.

# Enquanto o usuário não digitar "sair", adicione o filme na lista.

# Se o filme for "Batman", mostre:
# "Você adicionou Batman!"

# Quando o usuário digitar "sair", mostre todos os filmes cadastrados.

# Exemplo:

# Digite um filme: Avatar
# Digite outro filme ou sair: Batman
# Você adicionou Batman!
# Digite outro filme ou sair: Titanic
# Digite outro filme ou sair: sair

# Filmes cadastrados:
# ['Avatar', 'Batman', 'Titanic']

# filmes.append(filmes)

listaFilmes = []

filmes = input("Digite um filme: ")

while filmes != "sair":
    listaFilmes.append(filmes)

    if filmes == "Batman":
        print("Você adicionou Batman!")

    filmes = input("Digite outro filme ou sair: ")

print("Filmes cadastrados:")

for listaCompleta in listaFilmes:
    print(f"- {listaCompleta}")




