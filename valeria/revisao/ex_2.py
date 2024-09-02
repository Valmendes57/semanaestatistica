# O problema do chocolate
'''
Um professor precsia sortear bombons para diversos alunos. Esses alunos serão sorteados randomicamente.
O número deve corresponder ao número do diário.
'''
import random

# Looping - iteração - repetição - laço
# O objeto iterable vai substituir o for?
# modulos sao chamados pelo pondo .
while True:
    # Padrão snace_case ( seguindo as normas PEP-8 )
    sorteio_turma = random.randint(1,27)
    # A pergunta vai dentro do loop
    print(sorteio_turma)
    resposta=input(" Deseja sortear outro número? (s/n)").strip().lower()
    # Usamos os métodos strip para remover espaços em branco e transformar para minusculo.
    if resposta != "s":
        print(" Encerrando o sorteio...")
        break