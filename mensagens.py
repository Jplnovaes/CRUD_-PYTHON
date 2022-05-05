import db

MENU_INICIAL = 99

def exibir_cabecalho():
    """ imprimi o cabeçalho no terminal utilizando o tamanho maximo de 60 caracteres """
    QTD_COLUNAS = 60
    print ("-" * QTD_COLUNAS)
    print ("{:^60}".format("USUARIOS"))
    print ("-" * QTD_COLUNAS)
    print ("{:^60}".format("tecle 99 volta para o menu inicial, [CTRL+C] sai"))
    print ("-" * QTD_COLUNAS)

def exibir_usuarios():    
    """ exibe a lista de usuarios cadastrados, com algumas formatações básicas """
    for usuario in db.get_usuarios():
        # check = \u2713 é o caracter unicode que representa o concluido
        check = u'\u2713' if usuario[2] == 1 else ""
        """
            os parametros passados para esse format() são o seguinte
            {:>4}  = 4 posições, alinhado a direita
            {:<47} = 47 posições, alinhado a esquerda
            {:^3}  = 3 posições, centralizado
        """
        t = "- [{:>4}] {:<47} {:^3}".format(usuario[0], usuario[1], check)
        print (t)
    print ("-" * 60)

def mostrar_opcao_novo_usuario():
    texto_novo_usuario = input("Digite o nome completo do usuario => ")
    print ("Adicionando usuario -> " + str(texto_novo_usuario))
    if texto_novo_usuario != str(MENU_INICIAL):
        db.add_usuario(texto_novo_usuario)    

def mostrar_opcao_validar_usuario():
    cd_usuario = int(input("Qual usuario deseja validar? digite o código => "))
    print ("Usuario validado -> " + str(cd_usuario))
    if cd_usuario != MENU_INICIAL:
        db.concluir_usuario(cd_usuario)

def mostrar_opcao_remover_usuario():
    cd_usuario = int(input("Qual usuario quer remover? digite o código => "))
    print ("Removendo usuario" + str(cd_usuario))
    if db.remover_usuario != str(MENU_INICIAL):
        db.remover_usuario(cd_usuario) 