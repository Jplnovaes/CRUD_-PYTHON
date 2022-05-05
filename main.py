# arquivo app.py

import db
import mensagens as msg

def main():
    NOVO_USUARIO     = 1
    VALIDAR_USUARIO = 2
    REMOVER_USUARIO = 3
    
    while True:
        msg.exibir_cabecalho()
        msg.exibir_usuarios()
        try:
            # exibe as opções disponíveis
            opcao = int(input("O que deseja fazer?\n 1 = Adicionar usuario \n 2 = Validar usuario \n 3 = Remover usuario\n "))

            # verifica qual opção o usuário escolheu
            if opcao == NOVO_USUARIO:
                msg.mostrar_opcao_novo_usuario()
            elif opcao == VALIDAR_USUARIO:
                msg.mostrar_opcao_validar_usuario()
            elif opcao == REMOVER_USUARIO:
                msg.mostrar_opcao_remover_usuario()
            else:
                print ("Opção não reconhecida, por favor informar um número")    
        except ValueError as e :
            print ("Opção não reconhecida, por favor informar um número")
        except Exception:
            exit(0)

if __name__ == "__main__":
    db.criar_tabela_todo()

    main()