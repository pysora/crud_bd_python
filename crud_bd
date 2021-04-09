import mysql.connector

cnx = mysql.connector.connect(user='', host='localhost', password="", database='crud_python')
cursor = cnx.cursor()

def incluir():
    print("Incluir disciplina")
    print("-------------------------------------------------")

    sigla = input("Digite a sigla da disciplina: ")
    nome = input("Digite o nome da disciplina: ")
    num_ch_disc = input("Digite a carga horária da disciplina: ")
    sql = "INSERT INTO tb_dis(sgl_disc, nme_disc, num_ch_disc) VALUES(%s, %s, %s);"
    cursor.execute(sql, (sigla, nome, num_ch_disc))
    idt = cursor.lastrowid
    print(f"Criada a disciplina= {idt}")
    cnx.commit()

    print("-------------------------------------------------")
    input("[Enter] para menu")

def consultar():
    print("Consultar disciplina")
    print("-------------------------------------------------")

    sql = "SELECT * FROM tb_dis;"
    cursor.execute(sql)
    print("idt sigla nome carga horária")
    for (idt, sgl, nome, num_ch_disc) in cursor:
        print(f"{idt} / {sgl} / {nome} / {num_ch_disc}")
    print("-------------------------------------------------")
    input("[Enter] para menu")

def alterar():
    print("Alterar disciplina")
    print("-------------------------------------------------")

    idt = int(input("Qual o identificador da disciplina para alterar? "))
    sql = "SELECT * FROM tb_dis WHERE idt_disc=%s;"
    cursor.execute(sql, [idt])
    (idt, sgl, nme, num_ch_disc) = cursor.fetchone()

    sigla = input(f"Digite a nova sigla da disciplina [{sgl}]: ")
    nome = input(f"Digite o novo nome da disciplina [{nme}]: ")
    num_ch_disc = input(f"Digite a nova carga horária da disciplina [{num_ch_disc}]: ")
    sql = "UPDATE tb_dis SET sgl_disc=%s, nme_disc=%s, num_ch_disc=%s WHERE idt_disc=%s;"
    cursor.execute(sql, (sigla, nome, num_ch_disc, idt))
    print("Disciplina alterada.")
    cnx.commit()

    print("-------------------------------------------------")
    input("[Enter] para menu")

def excluir():
    print("Excluir disciplina")
    print("-------------------------------------------------")

    idt = int(input("Qual o identificador da disciplina para excluir? "))
    sql = "SELECT * FROM tb_dis WHERE idt_disc=%s;"
    cursor.execute(sql, [idt])
    (idt, sgl, nme, num_ch_disc) = cursor.fetchone()

    print(f"Identificador: {idt}")
    print(f"Sigla: {sgl}")
    print(f"Nome: {nme}")
    print(f"Carga horária: {num_ch_disc}")

    exc = input("Deseja realmente excluir essa disciplina? [S/N]: ")
    if exc == "S" or exc == "s":
        sql = "DELETE FROM tb_dis WHERE idt_disc=%s;"
        cursor.execute(sql, [idt])
        print("Disciplina excluída!")
        cnx.commit()
    elif exc == "N" or exc == "n":
        print("\nVamos tentar novamente.")
        excluir()


    print("-------------------------------------------------")
    input("[Enter] para menu")


continuar = True
while continuar:

    print('\n' * 10)

    print('''
    CRUD de Disciplina
    1 - Incluir
    2 - Consultar
    3 - Alterar
    4 - Excluir
    5 - Sair
    ''')

    opcao = int(input("Qual a sua opção? "))

    print('\n' * 30)
    if opcao == 1:
       incluir()

    elif opcao == 2:
       consultar()

    elif opcao == 3:
       alterar()

    elif opcao == 4:
       excluir()

    elif opcao == 5:
       print("--- FIM DO CRUD ---")
       continuar = False
       cnx.close()
