
frutas_vermelhas = set()

while True:
    
    nome_fruta = str(input(('Digite o nome da fruta ou "sair" para encerrar: '))).lower()
    frutas_vermelhas.add(nome_fruta)    
    if nome_fruta == 'sair':
        frutas_vermelhas.remove('sair')
        print(frutas_vermelhas)
        break

fruta_remover = str(input("Digite o nome da fruta que deseja remover: ")).lower()
if fruta_remover in frutas_vermelhas:
    frutas_vermelhas.remove(fruta_remover)
    print(frutas_vermelhas)
else:
    print("Fruta não encontrada!")