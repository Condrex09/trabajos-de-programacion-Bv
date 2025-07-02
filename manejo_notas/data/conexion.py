import mysql.connector

conexion =  mysql.connector.connect(
    host ="127.0.0.1",
    port =3306,
    user ="root",
    database ="gestion_notas"
)

cursor = conexion.cursor()

cursor.execute('SELECT * FROM DOCENTES')
resultado = cursos.fetchall()
print(resultado)