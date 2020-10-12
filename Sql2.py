import sqlite3

SENHA_PRINCIPAL = "32714071"  # Senha principal

senha = input("Insira a senha principal:  ")
if senha != SENHA_PRINCIPAL:
    print("Senha incorreta...Encerrando")
    print("Insira corretamente na próxima vez")
    exit()

conn = sqlite3.connect('passwords.db')

cursor = conn.cursor()

cursor.execute('''
create table if not exists users (
     service TEXT NOT NULL,
     username TEXT NOT NULL,
     password TEXT NOT NULL
);
      ''')


def menu():  # Função menu
    print("***********MAIN**************")
    print("Escolhe as primeiras letras para executar o serviço")
    print("*****************************")
    print("*N: inserir nova senha")
    print("*L: listar serviços")
    print("*R: Recuperar senha")
    print("*x: Sair")

    print("*****************************")


def get_pasword(service):
    cursor.execute(f'''
    SELECT username, password FROM users
     WHERE service = '{service}'
''')


if cursor.rowcount == 0:
    print("Serviço não reconhecido (use 'L' para verificar o serviço")
else:
    for user in cursor.fetchall():
        print(user)


def insert_password(service, username, password):
    cursor.execute(f'''
        INSERT INTO users (service, username, password) 
        VALUES ('{service}', '{username}', '{password}')
    ''')
    conn.commit()


def show_services():
    cursor.execute('''
        SELECT  service     FROM  users;
    ''')


for service in cursor.fetchall():
    print(service)

while True:  # Enquanto Verdadeiro
    menu()
    op = input("O que deseja? ")  # Operador de entrada
    if op not in ['N', 'L', 'R', 'x']:  # Se operando não for as opções
        print("Opção inválida")  # Saida " invalida"
        continue

    if op == 'x':  # Se for igualmente X... Parar
        break

    if op == 'N':
        service = input('Qual o nome do serviço? ')
        username = input('Nome do usuario? ')
        password = input('Qual a senha? ')
        insert_password(service, username, password)

    if op == 'L':
        show_services()
    if op == 'R':
        service = input('Qual o serviço para o qual deseja recuperar a senha? ')
        get_pasword(service)

conn.close()
