import db

MENU_INICIAL = 99

def exibir_cabecalho():
    """ imprime o cabeçalho no terminal utilizando o tamanho máximo de 60 caracteres """
    QTD_COLUNAS = 60 # evita uso de magic number
    print("-" * QTD_COLUNAS)
    print("{:^60}".format("TAREFAS"))
    print("-" * QTD_COLUNAS)
    print("{:^60}".format("tecle 99 para voltar ao menu inicial, [CTRL+C] para sair"))
    print("-" * QTD_COLUNAS)

def exibir_tarefas():
    """ exibe a lista de tarefas cadastradas, com formatações básicas """
    for tarefa in db.get_tarefas():
        check = u'\u2713' if tarefa[2] == 1 else ""
        """
            os parâmetros passados para esse format() são os seguintes:
            {:<4} = 4 posições alinhado a esquerda
            {:<47} = 47 posições, alinhado a esquerda
            {:^3} = 3 posições, centralizado
        """
        t = "- [{:>4}] {:<47} {:^3}".format(tarefa[0], tarefa[1], check)
        print(t)
    print("-" * 60)

def mostrar_opcao_nova_tarefa():
    texto_nova_tarefa = input("Descreva a tarefa => ")
    print("adicionando tarefa -> " + str(texto_nova_tarefa))
    if texto_nova_tarefa != str(MENU_INICIAL):
        db.add_tarefa(texto_nova_tarefa)

def mostrar_opcao_concluir_tarefa():
    cd_tarefa = int(input("Qual tarefa deseja concluir? Digite o código => "))
    print("concluindo tarefa -> " + str(cd_tarefa))
    if cd_tarefa != MENU_INICIAL:
        db.concluir_tarefa(cd_tarefa)