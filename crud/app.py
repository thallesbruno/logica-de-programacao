import db
import mensagens as msg

def main():
    NOVA_TAREFA = 1
    CONCLUIR_TAREFA = 2

    while True:
        msg.exibir_cabecalho()
        msg.exibir_tarefas()
        try:
            # exibe as opções disponíveis
            opcao = int(input("O que deseja fazer? 1 = Nova Tarefa, 2 = Concluir tarefa => "))

            # verifica a opção selecionada
            if opcao == NOVA_TAREFA:
                msg.mostrar_opcao_nova_tarefa()
            elif opcao == CONCLUIR_TAREFA:
                msg.mostrar_opcao_concluir_tarefa()
            else:
                print("Opção não reconhecida")
        except ValueError as e:
            print("Opção não reconhecida, informe um número")
        except Exception:
            exit(0)

if __name__ == "__main__":
    db.criar_tabela_todo()

    main()