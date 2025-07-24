script_menu_principal = '''
SELECT menu_opcion,opcion_menu
FROM opciones_menu
WHERE tipo_menu = 3
AND habilitado = 1
ORDER BY id
'''