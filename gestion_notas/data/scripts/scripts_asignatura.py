listado_asignaturas = '''
    SELECT id_asignatura,codigo_asig,nombre_asig,descripcion_asig
    FROM asignaturas
    WHERE habilitado = 1
'''