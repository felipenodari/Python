import mysql.connector
from mysql.connector import Error
def conectar():
    try:
        global co
        con = mysql.connector.connect(host='localhost', database='db_conteiner', user='root', password='#Brasil111')
        return 1
    except:
        print('Erro de conexão!')
        return 0


def cria_tabela(id_cliente, nro_container, tipo, status, categoria, movimentacao, data_ini, hora_ini, data_fim, hora_fim):
    try:
        con = mysql.connector.connect(host='localhost', database='db_conteiner', user='root', password='#Brasil111')
        cria_tabela_sql = """CREATE TABLE """ + id_cliente + """ (
                            id SMALLINT PRIMARY KEY AUTO_INCREMENT,
                            nro_container VARCHAR(20) NOT NULL,
                            tipo VARCHAR(20) NOT NULL,
                            status VARCHAR(20) NOT NULL,
                            categoria VARCHAR(20) NOT NULL,
                            movimentacao VARCHAR(20) NOT NULL,
                            data_ini VARCHAR(20) NOT NULL,
                            hora_ini VARCHAR(20) NOT NULL,
                            data_fim VARCHAR(20) NOT NULL,
                            hora_fim VARCHAR(20) NOT NULL
                            )"""
        cursor = con.cursor()
        cursor.execute(cria_tabela_sql)
        dados = '\''+ nro_container + '\',\''+ tipo +'\',\''+ status +'\',\''+ categoria +'\',\''+ movimentacao +'\',\''+ data_ini +'\',\''+ hora_ini +'\',\''+ data_fim +'\',\''+ hora_fim +'\')'
        declaracao = """INSERT INTO """ + '\''+id_cliente +'\''+ """ (nro_container, tipo, status, categoria, movimentacao, data_ini, hora_ini, data_fim, hora_fim) VALUES ("""
        sql = declaracao + dados
        inserir_produtos = sql
        cursor = con.cursor()
        cursor.execute(inserir_produtos)
        con.commit()
        print('Registro inserido com sucesso!')
        cursor.close()
    except:
        con = mysql.connector.connect(host='localhost', database='db_conteiner', user='root', password='#Brasil111')
        inserir_produtos = """INSERT INTO """ +id_cliente+ """ (nro_container, tipo, status, categoria, movimentacao, data_ini, hora_ini, data_fim, hora_fim) 
                            VALUES ("""'\''+ nro_container + '\',\''+ tipo +'\',\''+ status +'\',\''+ categoria +'\',\''+ movimentacao +'\',\''+ data_ini +'\',\''+ hora_ini +'\',\''+ data_fim +'\',\''+ hora_fim +'\')'
        cursor = con.cursor()
        cursor.execute(inserir_produtos)
        con.commit()
        cursor.close()
        print('Novo registro inserido com sucesso!')
    finally:
        if con.is_connected():
            cursor.close()
            con.close()
            print('Conexão ao MySQL finalizada')



def insere_registro():
    con = mysql.connector.connect(host='localhost', database='db_conteiner', user='root', password='#Brasil111')
    print('Inserir os dasdos do cliente:')
    id_cliente = str(input('Cliente: '))
    nro_container = str(input('Digite o número do container: '))
    tipo = str(input('Tipo: '))
    status = str(input('Status: '))
    categoria = str(input('Categoria: '))
    movimentacao = str(input('Movimentação: '))
    data_ini = str(input('Digite a data inicial: '))
    hora_ini = str(input('Hora inicial: '))
    data_fim = str(input('Digita a data final: '))
    hora_fim = str(input('Hora final: '))
    try:
        cria_tabela(id_cliente, nro_container, tipo, status, categoria, movimentacao, data_ini, hora_ini, data_fim, hora_fim)
    except Error as erro:
        print(f'Erro: {erro}')


def atualiza(declaracao):
    try:
        con = mysql.connector.connect(host='localhost', database='db_conteiner', user='root', password='#Brasil111')
        altera = declaracao
        cursor = con.cursor()
        cursor.execute(altera)
        con.commit()
        print('Registro altera dom sucesso!')
    except Error as erro:
        print(f'Erro: {erro}')


def ler_registro():
    try:
        con = mysql.connector.connect(host='localhost', database='db_conteiner', user='root', password='#Brasil111')
        print('-----------')
        imprime_clientes()
        tabela = str(input('Digite o cliente a ser consultado: '))
        consulta_sql = 'SELECT * FROM ' + tabela
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        print(f'mostrando as informações de {tabela}')
        for linha in linhas:
            print(f'id: {linha[0]}')
            print(f'Número do container: {linha[1]}')
            print(f'Status: {linha[2]}')
            print(f'Categoria: {linha[3]}')
            print(f'Tipo de movimentação: {linha[4]}')
            print(f'Data inicial: {linha[5]}')
            print(f'Hora inicial: {linha[6]}')
            print(f'Data final: {linha[7]}')
            print(f'Hora final: {linha[8]}')
            print('--------------')
    except Error as erro:
        print(f'Erro: {erro}')
    finally:
        if con.is_connected():
            con.close()
            cursor.close()



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
        print(f'Erro: {erro}')
    finally:
        if con.is_connected():
            con.close()
            cursor.close()


def altera_container():
    try:
        con = mysql.connector.connect(host='localhost', database='db_conteiner', user='root', password='#Brasil111')
        print('os clientes cadastrados no banco de dados são: ')
        imprime_clientes()
        cliente = str(input('Digite o nome do cliente para alterar dados do container: '))
        print('------------')
        consulta_sql = 'SELECT * FROM ' +cliente
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        for linha in linhas:
            print(f'ID: {linha[0]}')
            print(f'Número do container: {linha[1]}')
            print(f'Tipo: {linha[2]}')
            print(f'Status: {linha[3]}')
            print(f'Categoria: {linha[4]}')
            print('--------------')
        print('x - retornar ao menu')
        id = str(input('Você deseja alterar qual id: '))
        print('Qual dado deseja alterar deste id? ')
        print('1 - número do container')
        print('2 - tipo')
        print('3 - status')
        print('4 - categoria')
        escolha = str(input('>>> '))
        if escolha == '1':
            numero = str(input('Digite o novo número de container para substituir: '))
            declaracao = """UPDATE """ +cliente+""" SET nro_container = """ + '\'' + numero + '\''+ """ WHERE id = """+id
            atualiza(declaracao)
        elif escolha == '2':
            tipo = str(input('Digite o novo tipo: '))
            declaracao = """UPDATE """ + cliente + """ SET tipo = """ + '\'' + tipo + '\'' + """ WHERE id = """ + id
            atualiza(declaracao)
        elif escolha == '3':
            status = str(input('Digite o novo status: '))
            declaracao = """UPDATE """ + cliente + """ SET status = """ + '\'' + status + '\'' + """ WHERE id = """ + id
            atualiza(declaracao)
        elif escolha == '4':
            categoria = str(input('Digite a nova categoria: '))
            declaracao = """UPDATE """ + cliente + """ SET categoria = """ + '\'' + categoria + '\'' + """ WHERE id = """ + id
            atualiza(declaracao)
    except Error as erro:
        print(f'Erro: {erro}')
    finally:
        if con.is_connected():
            con.close()
            cursor.close()


def exclui_cliente():
    print('-=--------')
    print('os clientes cadastrados são:')
    imprime_clientes()
    cliente = str(input('Qual cliente deseja excluir: '))
    try:
        con = mysql.connector.connect(host='localhost', database='db_conteiner', user='root', password='#Brasil111')
        consulta_sql = 'DROP TABLE ' +cliente
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        print(f'cliente {cliente} excluido com sucesso')
    except Error as erro:
        print(f'Erro: {erro}')
    finally:
        if con.is_connected():
            con.close()
            cursor.close()

def exclui_registro():
    try:
        con = mysql.connector.connect(host='localhost', database='db_conteiner', user='root', password='#Brasil111')
        consulta_sql = 'SHOW TABLES;'
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        for linha in linhas:
            print(f'Cliente: {linha[0]}')
        cliente = str(input('Confirme novamente o nome do cliente: '))
        id = str(input('Id a ser excluido: '))
        sql = """DELETE FROM """ + cliente + """ WHERE id = """+'\''+id+'\''
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print('Registro excluído com sucesso')
    except Error as erro:
        print(f'Erro: {erro}')
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
        print('Os clientes cadastrados são: ')
        for linha in linhas:
            print(f'-> {linha[0]}')
        print('Qual cliente deseja visualizar a movimentação: ')
        escolha = str(input('>>> '))
        consulta_id = 'SELECT id, movimentacao FROM '+escolha
        cursor.execute(consulta_id)
        linhas = cursor.fetchall()
        print('RELATÓRIO DE MOVIMENTAÇÕES TOTAIS:')
        for linha in linhas:
            print(f'Movimentação número {linha[0]} || Tipo de movimentação: {linha[1]}')
        print(f'O TOTAL DE IMPORTAÇÕES E EXPORTAÇÕES DE {escolha}')
        consulta_sql = """SELECT COUNT(*) FROM """ + escolha + """ where categoria = 'Importação'"""
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        print(f'Total de importações: {linhas[0]}')

        consulta_sql = """SELECT COUNT(*) FROM """ + escolha + """ where categoria = 'Exportação'"""
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        print(f'Total de exportações {linhas[0]}')
    except Error as erro:
        print(f'Erro: {erro}')
    finally:
        if con.is_connected():
            con.close()
            cursor.close()


#######
print('Sistema de administração de conteiners')
try:
    if conectar() == 1:
        while True:
            print('BANCO DE DADOS CONECTADO')
            print('Escolha uma opção')
            print('1 - Inserir/criar registro')
            print('2 - ler um registro já inserido')
            print('3 - alterar um registro')
            print('4 - excluir um registro')
            print('5 - gerar relatório de movimentação')
            print('6 - sair')
            escolha = int(input('>>> '))
            if escolha == 1:
                insere_registro()
            elif escolha ==2:
                ler_registro()
            elif escolha == 3:
                print('Deseja alterar qual tipo de registro: ')
                print('1 - container')
                print('2 - movimentação')
                print('3 Retornar ao menu')
                escolha = str(input('>>> '))
                if escolha == '1':
                    altera_container()
                elif escolha == '2':
                    print('Movimentação alterada via função')
            elif escolha == 4:
                print('Você deseja excluir: ')
                print('1 - cliente')
                print('2 - excluir um registro de um cliente específico')
                print('3 - retorna ao menu')
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
                continua = str(input('Deseja continuar: [s/n/]: '))
                if continua == 'n':
                    break

except:
    print('Infelizmente não foi possível se conectar ao banco...')
finally:
    print('Obrigado po usar nosso sistema!')