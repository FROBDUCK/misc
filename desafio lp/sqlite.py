import sqlite3

conn = sqlite3.connect("todo-app.db")

cursor = conn.cursor()

#conn.execute("CREATE TABLE ponto (titulo_da_coleta text, ponto_da_coleta text, data integer, nome,descrição text, status text)")
    
conn.execute("INSERT into ponto ('aaaaaaaa','Ponto',1,'victor','do lado da casa de fulano' ,'ativo')")

cursor.execute("DELETE from ponto (titulo_da_coleta text, ponto_da_coleta text, data integer, nome,descrição text, status text)")

conn.commit()
conn.close()


cursor.execute("SELECT * FROM ponto")
print(cursor.fetchall())