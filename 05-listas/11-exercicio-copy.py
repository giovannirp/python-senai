# Crie uma lista com algumas linguagens de programação.

# Crie uma cópia dessa lista usando copy().

# Use um for/while para mostrar as linguagens da lista copiada.

# Lista de linguagens
linguagens = ["Python", "JavaScript", "Java", "PHP"]

# Cria uma cópia da lista
copia = linguagens.copy()

# # Mostra as linguagens
# for linguagem in copia:
#     print("-", linguagem)

i = 0;

while i < len(copia):
    print("-", copia[i])
    i += 1