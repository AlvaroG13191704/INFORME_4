import json
#import pymysql
import pymysql 
def conection():
    return pymysql.connect(host='localhost',
                            user='root',
                            password='secret',
                            db='informe_4')


def get_users():
    db = conection() # Hacemos la conexión
    users = [] # acá se almacena el resultado
    list_users = []
    with db.cursor() as cursor: # 
        cursor.execute('SELECT * FROM usuarios;') # hacemos el request
        users = cursor.fetchall() # retorna un objeto
        print(users)
    db.close()
    for user in users:
        nueva_lista = list(user)
        dic = {'id':nueva_lista[0],'nombre':nueva_lista[1],'edad':nueva_lista[2],'genero':nueva_lista[3],'tel':nueva_lista[4]}
        list_users.append(dic)
    print(list_users)
    return list_users

def create_user(id,nombre,edad,genero,tel):
    db = conection() # Hacemos la conexión
    with db.cursor() as cursor:
        cursor.execute("INSERT INTO usuarios(id,nombre,edad,genero,tel) VALUES(%s,%s,%s,%s,%s);",(id,nombre,edad,genero,tel)) # insertamos los datos
    db.commit() # hacemos el commit
    db.close() # cerramos
    print('Se ha agragado un nuevo usuario')

def edit_user(id,nombre,edad,genero,tel):
    db = conection() # Hacemos la conexión
    with db.cursor() as cursor:
        cursor.execute("UPDATE usuarios set  nombre = %s,edad = %s, genero = %s, tel = %s WHERE id = %s;",(nombre,edad,genero,tel,id)) # editamos
    db.commit() # hacemos el commit
    db.close() # cerramos

def delete_user(id):
    db = conection() # Hacemos la conexión
    with db.cursor() as cursor:
        cursor.execute("DELETE FROM usuarios WHERE id = %s;",(id)) # editamos
    db.commit() # hacemos el commit
    db.close() # cerramos

