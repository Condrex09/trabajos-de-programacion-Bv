#condicionales
#edad = 19
#edad = int(input("ingrese su edad: "))
#print("ingrese su edad: ")
#edad_str= (input())
#edad_int = int(edad_str)

#if edad_int >= 18:
    #print("usted es mayor de edad")
#else:
    #print("usted es menor de edad")   



#AB: El grupo de mayor poder adquisitivo, con un ingreso promedio por hogar de $7.177.530. 
#C1a: Clase media acomodada, con un ingreso promedio por hogar de $2.070.000. 
#C1b: Clase media emergente, con un ingreso promedio por hogar de $1.374.000. 
#C2: Clase media típica, con un ingreso promedio por hogar de $810.000. 
#C3: Clase media baja, con un ingreso promedio por hogar de $899.000. 
#D: Vulnerables, con un ingreso promedio por hogar de $562.000. 
#E: Pobres, con un ingreso promedio por hogar de $324.000.     



sueldo = int(input("ingrese su sueldo: "))
if sueldo >= 7177530:
    print("usted pertenence al grupo AB")
elif sueldo >= 2070000:
    print("usted pertenece al grupo C1a")
elif sueldo >= 1374000:
    print("usted pertenece al grupo C1b")
elif sueldo >= 810000:    
    print("usted pertenece al grupo C2")
elif sueldo >= 899000:
    print("usted pertenece al grupo C3")
elif sueldo >= 562000:
    print("usted pertenece al grupo D")
else:
    print("Usted pertenece al grupo E")
