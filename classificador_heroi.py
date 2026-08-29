# ============================================
# Classificador de Nível de Herói
# Desafio DIO - Lógica de Programação
# ============================================

# Laço de repetição: permite classificar vários heróis seguidos
continuar = "s"

while continuar == "s":
    # Variáveis: armazenam o nome e o XP do herói
    nome = input("Digite o nome do herói: ")
    xp = int(input("Digite a quantidade de XP do herói: "))

    # Estrutura de decisão: define o nível de acordo com o XP
    if xp < 1000:
        nivel = "Ferro"
    elif xp <= 2000:
        nivel = "Bronze"
    elif xp <= 5000:
        nivel = "Prata"
    elif xp <= 7000:
        nivel = "Ouro"
    elif xp <= 8000:
        nivel = "Platina"
    elif xp <= 9000:
        nivel = "Ascendente"
    elif xp <= 10000:
        nivel = "Imortal"
    else:
        nivel = "Radiante"

    # Saída: exibe a mensagem final
    print(f"O Herói de nome {nome} está no nível de {nivel}")

    # Pergunta se o usuário quer testar outro herói
    continuar = input("Deseja classificar outro herói? (s/n): ").lower()

print("Programa encerrado. Até a próxima!")
