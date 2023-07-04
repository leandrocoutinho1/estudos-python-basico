# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
acertos = 0

for dicionario in perguntas:
    print(f"\nPergunta: {dicionario['Pergunta']}")
    print("Opções:")
    for i, opcao in enumerate(dicionario['Opções']):
        print(f"{i}) {opcao}")
        
    resp = input('Escolha uma opção: ')
    try:
        resp = int(resp)
        if dicionario['Opções'][resp] == dicionario['Resposta']:
            acertos += 1
            print("Acertou 👍")
        else:
            print("Errou ❌")
    except ValueError:
        print("Errou ❌")

print(f"\nVocê acertou {acertos}"
        f" de {len(perguntas)} perguntas.")