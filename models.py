# CRUD
# CREAR
def crear_persona(mysql, Tipodoc, Documento, Nombres, Apellidos, Nacimiento, Genero, Email,  # Siempre va mysql
                  Telefono, Direccion, es_alumno, es_acudiente, es_colaborador):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()  # Siempre va este
    # QUERY de Insert
    sQuery = '''INSERT INTO persona (TipoId, Identificacion, Nombres, Apellidos, FechaNacimiento, Genero,
      Correo, Telefono, Direccion, Es_Alumno, Es_Acudiente, Es_Colaborador) 
      VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    # print(sQuery)

    # Ejecucion de la Sentencia
    cur.execute(sQuery, (Tipodoc, Documento, Nombres, Apellidos, Nacimiento, Genero, Email,
                         Telefono, Direccion, es_alumno, es_acudiente, es_colaborador))
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()


def crear_usuario(mysql, Documento, Nom_usuario, Email, Telefono, Contraseña):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()
    # QUERY de Insert
    sQuery = '''INSERT INTO usuario (Usuario, Nom_usuario, Email, Telefono, Privilegio, Contraseña) 
      VALUES(%s, %s, %s, %s, %s, %s)'''
    # print(sQuery)

    # Ejecucion de la Sentencia
    cur.execute(sQuery, (Documento, Nom_usuario,
                Email, Telefono, '', Contraseña))
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()


def crear_categoria(mysql, IdCategoria, NombreCategoria):
    cur = mysql.connection.cursor()
    sQuery = '''INSERT INTO categoria (idCategoria, Nom_Categoria) 
      VALUES(%s, %s)'''

    # Ejecucion de la Sentencia
    cur.execute(sQuery, (IdCategoria, NombreCategoria))
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()

# READ


def validar_persona(mysql, Documento):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()
    sQuery = "SELECT Identificacion FROM persona WHERE Identificacion='{}'".format(
        Documento)
    cur.execute(sQuery)
    row = cur.fetchone()
    # Cerramos el cursor
    cur.close()

    return row


def validar_usuario(mysql, Documento):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()
    sQuery = "SELECT Usuario,Contraseña,Privilegio FROM bd_escuela.usuario WHERE Usuario='{}'".format(
        Documento)
    # print(sQuery)
    cur.execute(sQuery)
    row = cur.fetchone()
    # Cerramos el cursor
    cur.close()

    return row


def validar_categoria(mysql, IdCategoria):
    cur = mysql.connection.cursor()
    sQuery = "SELECT idCategoria, Nom_Categoria FROM bd.escuela.categoria WHERE idCategoria'{}'".format(
        IdCategoria)
    # print(sQuery)
    cur.execute(sQuery)
    row = cur.fetchone()
    # Cerramos el cursor
    cur.close()

    # Ejecucion de la Sentencia
    cur.execute(sQuery)
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()

# UPDATE


def actualizar(mysql, email, name):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()
    # QUERY de UPDATE
    # Ejecucion de la Sentencia
    cur.execute('''UPDATE usuarios SET name=%s WHERE email=%s ''', (name, email))
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()


def actualizar_persona(mysql, Tipodoc, Documento, Nombres, Apellidos, Nacimiento, Genero, Email,  # Siempre va mysql
                       Telefono, Direccion, es_alumno, es_acudiente, es_colaborador):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()  # Siempre va este
    # QUERY de Update
    sQuery = '''UPDATE persona SET TipoId = %s, Identificacion = %s, Nombres = %s, Apellidos = %s, FechaNacimiento = %s, Genero = %s,
      Correo = %s, Telefono = %s, Direccion = %s, Es_Alumno = %s, Es_Acudiente = %s, Es_Colaborador = %s WHERE Documento = %s''',
    (Tipodoc, Nombres, Apellidos, Nacimiento, Genero, Email,  # Siempre va mysql
     Telefono, Direccion, es_alumno, es_acudiente, es_colaborador, Documento)
    # print(sQuery)

    # UPDATE `productos`.`productos` SET `nombre` = 'fresa' WHERE (`codigo` = '1');
    # Ejecucion de la Sentencia
    cur.execute(sQuery, (Tipodoc, Nombres, Apellidos, Nacimiento, Genero, Email,
                         Telefono, Direccion, es_alumno, es_acudiente, es_colaborador, Documento))
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()


def actualizar_usuario(mysql, Documento, Nom_usuario, Email,  # Siempre va mysql
                       Telefono, Contraseña):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()  # Siempre va este
    # QUERY de Update
    sQuery = '''UPDATE usuario SET Usuario = %s, Nom_usuario = %s, Email = %s, Telefono = %s, Contraseña = %s
     WHERE Usuario = %s''',
    (Nom_usuario, Email, Telefono, Contraseña,  # Siempre va mysql
     Documento)
    # print(sQuery)

    # UPDATE `productos`.`productos` SET `nombre` = 'fresa' WHERE (`codigo` = '1');
    # Ejecucion de la Sentencia
    cur.execute(sQuery, (Nom_usuario, Email, Telefono, Contraseña,  # Siempre va mysql
                         Documento))
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()


def actualizar_categoria(mysql, IdCategoria, NombreCategoria):
    cur = mysql.connection.cursor()
    sQuery = '''UPDATE categoria SET idCategoria = %s, Nom_Categoria = %s WHERE idCategoria =%s''',
    (NombreCategoria, IdCategoria)
    # print(sQuery)
    cur.execute(sQuery(NombreCategoria, IdCategoria))
    mysql.connection.commit()

    # Cerramos el cursor
    cur.close()

# DELETE


def Eliminar(mysql, email):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()
    sQuery = "DELETE FROM usuarios WHERE email='{}'".format(email)
    print(sQuery)
    cur.execute(sQuery)
    row = cur.fetchone()
    # Cerramos el cursor
    cur.close()

    return row


def eliminar_persona(mysql, Documento):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()
    sQuery = "DELETE FROM persona WHERE Identificacion='{}'".format(Documento)
    # print(sQuery)
    cur.execute(sQuery)
    row = cur.fetchone()
    # Cerramos el cursor
    cur.close()

    return row


def eliminar_usuario(mysql, Documento):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()
    sQuery = "DELETE FROM usuario WHERE Usuario='{}'".format(Documento)
    # print(sQuery)
    cur.execute(sQuery)
    row = cur.fetchone()
    # Cerramos el cursor
    cur.close()

    return row


def eliminar_categoria(mysql, IdCategoria):
    # Cursor para la ejecución
    cur = mysql.connection.cursor()
    sQuery = "DELETE FROM categoria WHERE idCategoria='{}'".format(IdCategoria)
    # print(sQuery)
    cur.execute(sQuery)
    row = cur.fetchone()
    # Cerramos el cursor
    cur.close()

    return row
