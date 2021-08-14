import mysql.connector
from mysql.connector import Error


def conectar():
    try:
        global con
        con = mysql.connector.connect(host='localhost', database='db_conteiner', user='root', password='#Brasil111')
        return 1
    except Error as erro:
        print(f'Erro de conexão ao banco: {erro}')
        return 0


def cria_tabela(id_cliente, nro_container, tipo, status, categoria, movimentacao, data_ini, hora_ini, data_fim, hora_fim):
    try:
        con = mysql.connector.connect(host='localhost', database='db_conteiner', user='root', password='#Brasil111')
        cria_tabela_sql = """CREATE TABLE """ + id_cliente + """ (
                            id SMALLINT PRIMARY KEY AUTO_INCREMENT,
                            nro_container VARCHAR(70) NOT NULL,
                            tipo VARCHAR(70) NOT NULL,
                            status VARCHAR(40) NOT NULL,
                            categoria VARCHAR(30) NOT NULL,
                            movimentacao VARCHAR(30) NOT NULL,
                            data_ini VARCHAR(30) NOT NULL,
                            hora_ini VARCHAR(30) NOT NULL,
                            data_fim VARCHAR(30) NOT NULL,
                            hora_fim VARCHAR(30) NOT NULL
                            )"""
        cursor = con.cursor()
        cursor.execute(cria_tabela_sql)
        dados = '\'' + nro_container + '\',\'' + tipo + '\',\'' + status + '\',\'' + categoria + '\',\'' \
                + movimentacao + '\',\'' + data_ini + '\',\'' + hora_ini + '\',\'' + data_fim + '\',\'' + hora_fim + '\')'
        declaracao = """INSERT INTO """ +id_cliente + """ 
        (nro_container, tipo, status, categoria, movimentacao, data_ini, hora_ini, data_fim, hora_fim)
        VALUES ("""
        sql = declaracao + dados
        inserir_produtos = sql
        cursor = con.cursor()
        cursor.execute(inserir_produtos)
        con.commit()
        print(cursor.rowcount, 'registros inseridos na tabela!')
        print(f'Registro do cliente [{id_cliente}] inserido com sucesso!')
        cursor.close()
    except Error as erro:
        con = mysql.connector.connect(host='localhost', database='db_conteiner', user='root', password='#Brasil111')
        inserir_produtos = """INSERT INTO """ + id_cliente + """ (nro_container, tipo, status, categoria, movimentacao, data_ini, hora_ini, data_fim, hora_fim)
                                    VALUES ("""'\'' + nro_container + '\',\'' + tipo + '\',\'' + status + '\',\'' + categoria + '\',\'' + movimentacao + '\',\'' + data_ini + '\',\'' + hora_ini + '\',\'' + data_fim + '\',\'' + hora_fim + '\''""")"""
        cursor = con.cursor()
        cursor.execute(inserir_produtos)
        con.commit()
        cursor.close()
        print(f'\nNovo registro do cliente [{id_cliente}] inserido com sucesso!')
    finally:
        if con.is_connected():  # se estiver conectado
            cursor.close()  # fecha o cursor
            con.close()  # fecha a conexão também para liberar recursos
            print('Conexão ao MySQL finalizada.')


def insere_registro():
    con = mysql.connector.connect(host='localhost', database='db_conteiner', user='root', password='#Brasil111')
    print('=-= Inserir dados do cliente =-=')
    id_cliente = str(input('Cliente: '))
    nro_container = str(input('Número do container (4 letras e 7 números): '))
    tipo = str(input('Tipo [20/40]: '))
    status = str(input('Status [c]heio [v]azio: '))
    categoria = str(input('Categoria [i]mportação [e]xportação: '))
    print(f'---- Registro de movimentação do cliente {id_cliente} ----')
    print('Selecione o tipo de movimentação:')
    print('[1] - Embarque')
    print('[2] - Descarga')
    print('[3] - Gate in')
    print('[4] - Gate out')
    print('[5] - Posicionamento pilha')
    print('[6] - Pesagem')
    print('[7] - Scanner')
    movimentacao = str(input('>>> '))
    data_ini = str(input('Digite a data de início: '))
    hora_ini = str(input('Digite a hora de início: '))
    data_fim = str(input('Digite a data de conclusão: '))
    hora_fim = str(input('Digite a hora da conclusão: '))
    if status == 'c':
        status = 'Cheio'
    else:
        status = 'Vazio'
    if categoria == 'i':
        categoria = 'Importação'
    else:
        categoria = 'Exportação'
    try:
        cria_tabela(id_cliente, nro_container, tipo, status, categoria, movimentacao, data_ini, hora_ini, data_fim, hora_fim)
    except Error as erro:
        print(f'Erro ao inserir dados: {erro}')
    finally:
        if con.is_connected():
            con.close()


def ler_registro():
    try:
        con = mysql.connector.connect(host='localhost', database='db_conteiner', user='root', password='#Brasil111')
        print('--------------')
        print('Os clientes cadastrados no banco de dados são:')
        imprime_clientes()
        tabela = str(input('Digite o cliente a ser consultado: '))
        consulta_sql = 'select * from ' + tabela
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        print(f'Número total de registros deste cliente: {cursor.rowcount}')
        print(f'\nMostrando as informações de --[{tabela}]--')
        for linha in linhas:
            print(f'Id: {linha[0]}')
            print(f'Número do container: {linha[1]}')
            print(f'Status: {linha[2]}')
            print(f'Categoria: {linha[3]}')
            print(f'Tipo de movimentação: {linha[4]}')
            print(f'Data de início: {linha[5]}')
            print(f'Hora de início: {linha[6]}')
            print(f'Data de término: {linha[7]}')
            print(f'Hora de término: {linha[8]}')
            print('--------------------------------------------------')
    except Error as erro:
        print(f'Erro ao ler tabela no banco de dados: {erro}')
    finally:
        if con.is_connected():
            con.close()
            cursor.close()


def atualiza(declaracao):
    try:
        con = mysql.connector.connect(host='localhost', database='db_conteiner', user='root', password='#Brasil111')
        altera = declaracao
        cursor = con.cursor()
        cursor.execute(altera)
        con.commit()
        print('Registro alterado com sucesso!')
    except Error as erro:
        print(f'Falha ao inserir dados na tabela {erro}')
    finally:
        if con.is_connected():
            cursor.close()
            con.close()


def altera_container():
    try:
        con = mysql.connector.connect(host='localhost', database='db_conteiner', user='root', password='#Brasil111')
        print('--------------')
        print('Os clientes cadastrados no banco de dados são:')
        imprime_clientes()
        cliente = str(input('Digite o nome do cliente para alterar dados do container: '))
        print('----------------------------------------------')
        consulta_sql = 'select * from ' + cliente
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        for linha in linhas:
            print('ID:', linha[0])
            print('Número do conteiner: ', linha[1])
            print('Tipo: ', linha[2])
            print('Status: ', linha[3])
            print('Categoria ', linha[4])
            print('----------------------------------------------')
        print('[x] - Retornar ao menu')
        id = str(input('Você deseja alterar qual ID: '))
        print('Qual dado deseja alterar deste Id?')
        print('[1] - Número do conteiner')
        print('[2] - Tipo')
        print('[3] - Status')
        print('[4] - Categoria')
        escolha = str(input('>>> '))
        if escolha == '1':
            numero = str(input('Digite o novo número de container para substituir: '))
            declaracao = """UPDATE """+ cliente +""" SET nro_container = """ + '\'' + numero + '\'' + """ WHERE id = """ + id
            atualiza(declaracao)
        elif escolha == '2':
            tipo = str(input('Digite o novo tipo a substituir [20/40]: '))
            declaracao = """UPDATE """+ cliente +""" SET tipo = """ + '\'' + tipo + '\'' + """ WHERE id = """ + id
            atualiza(declaracao)
        elif escolha == '3':
            status = str(input('Digite o novo status [cheio/vazio]: '))
            declaracao = """UPDATE """+ cliente +""" SET status = """ + '\'' + status + '\'' + """ WHERE id = """ + id
            atualiza(declaracao)
        elif escolha == '4':
            categoria = str(input('Digite a nova categoria [importação/exportação]: '))
            declaracao = """UPDATE """+ cliente +""" SET categoria = """ + '\'' + categoria + '\'' + """ WHERE id = """ + id
            atualiza(declaracao)
    except Error as erro:
        print(f'Falha ao consultar a tabela {erro}')


def altera_movimentacao():
    try:
        con = mysql.connector.connect(host='localhost', database='db_conteiner', user='root', password='#Brasil111')
        print('--------------')
        print('Os clientes cadastrados no banco de dados são:')
        imprime_clientes()
        cliente = str(input('Digite o nome do cliente para alterar dados da movimentação: '))
        print('----------------------------------------------')
        consulta_sql = 'select * from ' + cliente
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        for linha in linhas:
            print('ID:', linha[0])
            print('Movimentação: ', linha[5])
            print('Data de início: ', linha[6])
            print('Hora de início: ', linha[7])
            print('Data de término: ', linha[8])
            print('Hora de término: ', linha[9])
            print('----------------------------------------------')
        print('[x] - Retornar ao menu')
        id = str(input('Você deseja alterar qual ID: '))
        print('Qual dado deseja alterar deste Id?')
        print('[1] - Movimentação')
        print('[2] - Data de início')
        print('[3] - Hora de início')
        print('[4] - Data de término')
        print('[5] - Hora de término')
        escolha = str(input('>>> '))
        if escolha == '1':
            movimentacao = str(input('Digite a nova movimentação: '))
            declaracao = """UPDATE """+ cliente +""" SET movimentacao = """ + '\'' + movimentacao + '\'' + """ WHERE id = """ + id
            atualiza(declaracao)
        elif escolha == '2':
            data_ini = str(input('Digite nova data de início: '))
            declaracao = """UPDATE """+ cliente +""" SET data_ini = """ + '\'' + data_ini + '\'' + """ WHERE id = """ + id
            atualiza(declaracao)
        elif escolha == '3':
            hora_ini = str(input('Digite nova hora de início: '))
            declaracao = """UPDATE """+ cliente +""" SET hora_ini = """ + '\'' + hora_ini + '\'' + """ WHERE id = """ + id
            atualiza(declaracao)
        elif escolha == '4':
            data_fim = str(input('Digite nova data de término: '))
            declaracao = """UPDATE """+ cliente +""" SET data_fim = """ + '\'' + data_fim + '\'' + """ WHERE id = """ + id
            atualiza(declaracao)
        elif escolha == '5':
            hora_fim = str(input('Digite nova hora de término: '))
            declaracao = """UPDATE """ + cliente + """ SET hora_fim = """ + '\'' + hora_fim + '\'' + """ WHERE id = """ + id
            atualiza(declaracao)
    except Error as erro:
        print(f'Falha ao consultar a tabela {erro}')


def imprime_clientes():
    try:
        con = mysql.connector.connect(host='localhost', database='db_conteiner', user='root', password='#Brasil111')
        consulta_sql = 'SHOW TABLES;'
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        for linha in linhas:
            print(f'Cliente: {linha[0]}')
    except Error as erro:
        print(f'Registro não encontrado: {erro}')
    finally:
        if con.is_connected():
            con.close()
            cursor.close()


def exclui_cliente():
    print('---------------')
    print('Os clientes cadastrados são')
    imprime_clientes()
    cliente = str(input('Qual cliente deseja excluir: '))
    try:
        con = mysql.connector.connect(host='localhost', database='db_conteiner', user='root', password='#Brasil111')
        consulta_sql = 'DROP TABLE ' + cliente
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        print(f'Cliente [{cliente}] excluído com sucesso!')
    except Error as erro:
        print(f'Não foi possível excluir este cliente: {erro}')
    finally:
        if con.is_connected():
            con.close()
            cursor.close()


def exclui_registro():
    try:
        ler_registro()
        con = mysql.connector.connect(host='localhost', database='db_conteiner', user='root', password='#Brasil111')
        consulta_sql = 'SHOW TABLES;'
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        for linha in linhas:
            print(f'Cliente: {linha[0]}')
        cliente = str(input('Confirme novamente o nome do cliente: '))
        id = str(input('Id a ser excluido: '))
        sql = """DELETE FROM """ + cliente + """ WHERE id = """ + '\'' + id + '\''
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print('Registro excluído com sucesso!')
    except Error as erro:
        print(f'Registro não encontrado: {erro}')
    finally:
        if con.is_connected():
            con.close()
            cursor.close()


def relatorio_movimentacao():
    try:
        con = mysql.connector.connect(host='localhost', database='db_conteiner', user='root', password='#Brasil111')
        consulta_sql = 'SHOW TABLES;'
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        print('Os clientes cadastrados são:')
        for linha in linhas:
            print(f'-> {linha[0]}')
        print('   Qual cliente deseja visualizar a movimentação?')
        escolha = str(input('   >>> '))
        consulta_id = 'SELECT id, movimentacao FROM ' + escolha
        cursor.execute(consulta_id)
        linhas = cursor.fetchall()
        print('RELATÓRIO DE MOVIMENTAÇÕES TOTAIS ')
        for linha in linhas:
            print(f'Movimentação número: {linhas[0]} || Tipo de movimentação: {linha[1]}')
        print(f'\nO TOTAL DE IMPORTAÇÕES E EXPORTAÇÕES DE -[{escolha}]-:')
        consulta_sql = """SELECT count(*) FROM """ + escolha + """ where categoria = 'Importação'"""
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        print(f'Total de Importações: {linhas[0]} ')
        consulta_sql = """SELECT count(*) FROM """ + escolha + """ where categoria = 'Exportação'"""
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        print(f'Total de Exportações: {linhas[0]}')
    except Error as erro:
        print(f'Não foi possível gerar o relatório: {erro}')
    finally:
        if con.is_connected():
            con.close()
            cursor.close()


print('-=-=' * 10)
print('Sistema de administração de Contêiners')
print('-=-=' * 10)
try:
    if conectar() == 1:
        while True:
            print('--- BANCO DE DADOS CONECTADO ---')
            print('--- ESCOLHA UMA OPÇÃO ---')
            print('[1] Inserir/Criar registro')
            print('[2] Ler um registro já inserido')
            print('[3] Alterar um registro')
            print('[4] Excluir um registro')
            print('[5] Gerar relatório de movimentação')
            print('[6] Sair')
            escolha = int(input('>>> '))
            if escolha == 1:
                insere_registro() #arrumar caso o registro já exista para inserir novas informações.
            elif escolha == 2:
                ler_registro()
            elif escolha == 3:
                print('Deseja alterar qual tipo de registro: ')
                print('[1] - Container')
                print('[2] - Movimentação')
                print('[3] - Retorna ao menu principal')
                escolha = str(input('>>> '))
                if escolha == '1':
                    altera_container()
                elif escolha == '2':
                    altera_movimentacao()
                else:
                    continue
            elif escolha == 4: #arrumar para excluir o cliente total ou alguma linha da tabela
                print('Você deseja exluir:')
                print('[1] - Cliente')
                print('[2] - Excluir um registro específico de um cliente')
                print('[3] - Voltar ao menu principal')
                escolha = str(input('>>> '))
                if escolha == '1':
                    exclui_cliente()
                elif escolha == '2':
                    exclui_registro()
                else:
                    continue
            elif escolha == 5:
                relatorio_movimentacao()
            else:
                break
            continua = ''
            while continua != 's' and continua != 'n':
                continua = str(input('\nDeseja continuar? [s/n]: '))
            if continua == 'n':
                break
except Error as erro:
    print(f'Infelizmente não foi possível se conectar ao banco: {erro} \nProcesso encerrado.')
finally:
    print('Obrigado por usar nosso sistema!')
