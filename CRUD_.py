
# sudo apt update && sudo apt install python3-venv python3-pip
# pip install mysql-connector-python
# python -m pip install --upgrade pip

from Keys import senha 
import mysql.connector

con = mysql.connector.connect(host='localhost',
                      user='Dikson',
                      password=senha,
                      database='DB_01')


cursor = con.cursor()

# CRUD:                 SEMPRE COMENTE UM BLOCO ANTES DE RODAR O PRÓXIMO:

# Create
"""
show databases;
use DB_01;
select * from DB_01;

CREATE TABLE  Venda( nome_produto varchar(30) not NULL,
valor varchar(30) not null);

"""

# INSERT INTO TABLES:
Produto = 'Neogeo_CD'
Valor = 2.000
# Insere na TAB Venda (Col, Col) Valores (DETALHES NAS ASPAS DUPLS , MAIS_ASPAS_DUP)
# comando = f'INSERT INTO Venda (nome_produto, valor) VALUES ("{Produto}","{Valor}" )'  # -> SEMPRE EM ASPAS SIMPLES !
# cursor.execute(comando)
# con.commit()  # Para quando alteramos ou Editamos o Banco de Dados

# # Para armazenar as informações ou mudanças:
#resultado = cursor.fetchall()


# Read
comando_2 = 'SELECT * FROM Venda;'    # Não precisa especificar com 'DB_01.'  antes de 'venda'.
cursor.execute(comando_2)
resultado_f = cursor.fetchall()
print(resultado_f)


# UPDATE
# nvalor = 1999
# id = 5
# comando03 = f'UPDATE Vendas SET valor = "{nvalor}" where idvendas ="{id}";'
# cursor.execute(comando03)

# Delete
# id = 5
# nome = 'Neogeo_CD'
# comando_l = f'DELETE FROM Vendas WHERE valor = {2000}'
# cursor.execute(comando_l)
# con.commit()





#cursor.close()
con.close()


"""


"""
