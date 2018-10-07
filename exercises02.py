
# coding: utf-8

# # HM02

# 1. Escribe un programa que mencione cómo se encuentra el clima. El Usuario deberá ingresar la temperatura actual:
#     * Si `temperatura` es mayor o igual a 35, el programa deberá imprimir `"Hace mucho calor"`.
#     * Si `temperatura` es menor a -15, el programa deberá imprimir `"Hace mucho frío"`
#     * Si `temperatura` es mayor a 25 y menor a 35, el programa deberá imprimir `"Hace calor"` 
#     * Si `temperatura` es mayor o igual a -15 y menor a 12, el programa deberá imprimir `"Hace frío"`
#     * Si `temperatura` se encuentra entre 12 y 25 (inclusivo), el programa deberá imprimir `"El clima es templado"`
#  

# In[3]:


temperatura=int(input("¿Cuál es la temperatura actual?: "))

if temperatura >=35:
    print("Hace mucho calor.")
elif temperatura <= -15:
    print("Hace mucho frío.")
elif 25<temperatura<35:
    print("Hace calor.")
elif -15<=temperatura<12:
    print("Hace frío.")
elif 12<=temperatura<=25:
    print("El clima es templado.")


# 2. Usuario - Contraseña
# 
# **2.1**  
# Consierando el diccionario `user_pass`, crea un programa que pida un usuario y valide si este se encuentra dentro del diccionario. Si el usuario se encuentra dentro de `user_pass`, el programa deberá imprimir `"usuario registrado"`; de otra manera, el programa deberá imprimir `"usuario no registrado"`. **nota: los programas de usuario-contraseña son más complicados**
# ```python
# user_pass = {'usr503': '2vu2bo',
#  'usr085': 'geeaa',
#  'usr406': 'xqzbiy',
#  'usr182': 'jbngo0',
#  'usr168': 'qih6e',
#  'usr900': '6ynym',
#  'usr542': '7p6mnd',
#  'usr847': 'ruqq6y',
#  'usr629': '9qs9g5',
#  'usr418': 'f15lg'}
# ```
# Por ejemplo:
# ```
# Ingresa tu usuario: usr085
# Usuario Registrado
# ```

# In[10]:


user_pass = {'usr503': '2vu2bo',
 'usr085': 'geeaa',
 'usr406': 'xqzbiy',
 'usr182': 'jbngo0',
 'usr168': 'qih6e',
 'usr900': '6ynym',
 'usr542': '7p6mnd',
 'usr847': 'ruqq6y',
 'usr629': '9qs9g5',
 'usr418': 'f15lg'}
usuario=input("Ingresa tu usuario: ")
if usuario in user_pass:
    print("Usuario registrado.")
else:
    print("Usuario no registrado.")


# **2.2**  
# Modifica el programa anterior: si el usuario **no** ha sido registrado, el programa deberá preguntarle al usuario si se desea registrar, si el usuario ingresa `"s"`, el programa deberá preguntarle al usuario una contraseña y agregarlo a `user_pass`; si el usuario ingresa `"n"` el programa deberá imprimir `"El usuario no fue registrado"`; si el usuario ingresa cualquier otra secuencia, el programa deberá imprimir `"Opción no valida. Saliendo del programa"`  
# Por ejemplo:
# ```
# Ingresa tu usuario: usr1643
# Usuario no registrado. ¿Deseas inscribirte (s/n)? n
# Saliendo del programa...
# ```
# ```
# Ingresa tu usuario: usr1643
# Usuario no registrado. ¿Deseas inscribirte (s/n)? y
# Opción no valida. Saliendo del programa
# ```
# ```
# Ingresa tu usuario: usr1643
# Usuario no registrado. ¿Deseas inscribirte (s/n)? s
# Ingresa tu contraseña: grapple981
# ```
# Y el diccionario se vería modificado de la siguiente manera
# ```python
# {'usr503': '2vu2bo',
#      ...
#  'usr418': 'f15lg',
#  'usr1643': 'grapple981'}
# ```

# In[1]:


user_pass = {'usr503': '2vu2bo',
 'usr085': 'geeaa',
 'usr406': 'xqzbiy',
 'usr182': 'jbngo0',
 'usr168': 'qih6e',
 'usr900': '6ynym',
 'usr542': '7p6mnd',
 'usr847': 'ruqq6y',
 'usr629': '9qs9g5',
 'usr418': 'f15lg'}

usuario=input("Ingresa tu usuario: ")
if usuario in user_pass:
    usuario1=print("Usuario registrado.")  
else:
    print("Usuario no registrado.")
    registro=input("¿Desea registrarlo?(s/n): ")
    if registro=="s":
        contra=input("Introduzca su contraseña: ")
        user_pass[usuario]=contra
        print(user_pass)
    else:
        if registro=="n":
            print("Saliendo del programa...")
        else:
            print("Instrucción inválida.")
        


# **2.3**.  
# Modifica el programa anterior: Si el usuario ya se ha registrado, el programa deberá pedirle al usuario que ingrese su contraseña. Si la contraseña no es la correcta, el programa deberá imprimir `"Contraseña invalida"`; si lo es, el programa deberá darle la bienvenida al usuario.
# ```
# Ingresa tu usuario: usr085
# Ingresa tu contraseña: passw
# Contraseña invalida
# ```
# ```
# Ingresa tu usuario: usr085
# Ingresa tu contraseña: geeaa
# Bienvenido, usr085
# ```

# In[15]:


user_pass = {'usr503': '2vu2bo',
'usr085': 'geeaa',
'usr406': 'xqzbiy',
'usr182': 'jbngo0',
'usr168': 'qih6e',
'usr900': '6ynym',
'usr542': '7p6mnd',
'usr847': 'ruqq6y',
'usr629': '9qs9g5',
'usr418': 'f15lg'}

usuario=input("Ingresa tu usuario: ")
if usuario in user_pass:
   usuario_registrado=print("Usuario registrado.")
   contraseña=input("Introduzca su contraseña: ")
   if contraseña in user_pass[usuario]:
       print("Bienvenido,",usuario)
   else:
       print("Contraseña incorrecta.")
else:
   print("Usuario no registrado.")
   registro=input("¿Desea registrarlo?(s/n): ")
   if registro=="s":
       contra=input("Introduzca su contraseña: ")
       user_pass[usuario]=contra
       print(user_pass)
   else:
       if registro=="n":
           print("Saliendo del programa...")
       else:
           print("Instrucción inválida.")
       


# 3. ¿Qué sucede al correr el siguiente código? Explica.
# ```python
#     for x in 2:
#         print(x)
# ```
Te lanza un error porque el número dos no es un iterable. Un iterable tiene que tener un "rango" o elementos dentro de él. Puede ser un range(), una lista, etc.
# 4. Escribe un programa que cree el siguiente patrón:
# ```
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
# ```

# In[29]:


for k in range(1,2):
    print(k,end=" ")
print()
for a in range(1,3):
    print(a,end=" ")
print()
for t in range(1,4):
    print(t,end=" ")
print()
for l in range(1,5):
    print(l,end=" ")
print()
for q in range(1,6):
    print(q,end=" ")
print()


# 5. Escribe un programa para adivinar un número:  
# Considerando un número objetivo `target_num`, el programa le deberá pedir al usuario ingresar un número `input_num`. Si `input_num` > `target_num`, el programa deberá informarle al usuario que su número está por encima del número objetivo; de otra manera, si `input_num` < `target_num`, el programa deberá informarle al usuario que su número se encuentra por debajo del número objetivo. El programa se termina una vez que el usuario adivine el número objetivo, i.e., una vez que `input_num == target_num`.

# In[ ]:


target_num=20
print("¿Cuál es el número que tengo?")
while target_num:
    input_num=int(input("Escribe un número: "))
    if input_num > target_num:
        print("Demasiado alto.")
    elif input_num < target_num:
        print("Demasiado bajo.")
    elif input_num == target_num:
        print("Ganaste.")
        break


# 6. Considerando las listas `capitale` y `estados`, escribe un programa que escriba `"la capital de <estado> es <capital>"`; donde `<estado>` y `<capital>` representa cada elemento de las listas mencionadas.
# 
# ```
# capitales = ['Aguascalientes', 'Mexicali', 'La Paz', 'Campeche', 'Saltillo', 'Colima',
#              'Tuxtla Gutiérrez', 'Chihuahua', 'Ciudad de México', 'Durango', 'Guanajuato',
#              'Chilpancingo', 'Pachuca', 'Guadalajara', 'Toluca', 'Morelia', 'Cuernavaca', 
#              'Tepic', 'Monterrey', 'Oaxaca', 'Puebla', 'Querétaro', 'Chetumal', 'San Luis Potosí',
#              'Culiacán', 'Hermosillo', 'Villahermosa', 'Ciudad Victoria', 'Tlaxcala', 'Xalapa',
#              'Mérida', 'Zacatecas']
# estados = ['Aguascalientes', 'Baja California', 'Baja California Sur', 'Campeche', 'Coahuila',
#            'Colima', 'Chiapas', 'Chihuahua', 'Distrito Federal', 'Durango', 'Guanajuato',
#            'Guerrero', 'Hidalgo', 'Jalisco', 'México', 'Michoacán', 'Morelos', 'Nayarit',
#            'Nuevo León', 'Oaxaca', 'Puebla', 'Querétaro', 'Quintana Roo', 'San Luis Potosí',
#            'Sinaloa', 'Sonora', 'Tabasco', 'Tamaulipas', 'Tlaxcala', 'Veracruz', 'Yucatán', 'Zacatecas']
# ```

# In[9]:


capitales = ['Aguascalientes', 'Mexicali', 'La Paz', 'Campeche', 'Saltillo', 'Colima',
             'Tuxtla Gutiérrez', 'Chihuahua', 'Ciudad de México', 'Durango', 'Guanajuato',
             'Chilpancingo', 'Pachuca', 'Guadalajara', 'Toluca', 'Morelia', 'Cuernavaca', 
             'Tepic', 'Monterrey', 'Oaxaca', 'Puebla', 'Querétaro', 'Chetumal', 'San Luis Potosí',
             'Culiacán', 'Hermosillo', 'Villahermosa', 'Ciudad Victoria', 'Tlaxcala', 'Xalapa',
             'Mérida', 'Zacatecas']
estados = ['Aguascalientes', 'Baja California', 'Baja California Sur', 'Campeche', 'Coahuila',
           'Colima', 'Chiapas', 'Chihuahua', 'Distrito Federal', 'Durango', 'Guanajuato',
           'Guerrero', 'Hidalgo', 'Jalisco', 'México', 'Michoacán', 'Morelos', 'Nayarit',
           'Nuevo León', 'Oaxaca', 'Puebla', 'Querétaro', 'Quintana Roo', 'San Luis Potosí',
           'Sinaloa', 'Sonora', 'Tabasco', 'Tamaulipas', 'Tlaxcala', 'Veracruz', 'Yucatán', 'Zacatecas']
estado_capital={}
for capital, estado in zip(capitales, estados):
    print("La capital de",estado,"es",capital)


# 7. Escribe un programa que imprima la siguiente tabla de Multiplicación de 10x10.
# 
# ```
# 01|02 03 04 05 06 07 08 09 10 
# -----------------------------
# 02|04 06 08 10 12 14 16 18 20 
# 03|06 09 12 15 18 21 24 27 30 
# 04|08 12 16 20 24 28 32 36 40 
# 05|10 15 20 25 30 35 40 45 50 
# 06|12 18 24 30 36 42 48 54 60 
# 07|14 21 28 35 42 49 56 63 70 
# 08|16 24 32 40 48 56 64 72 80 
# 09|18 27 36 45 54 63 72 81 90 
# 10|20 30 40 50 60 70 80 90 100
# ```

# In[51]:


lista1=[1,2,3,4,5,6,7,8,9,10]
for x in lista1:
    if x==2:
        print("\n---------------------")
    for j in lista1:
        if j==1:
            print(" ")
        multi=print(x*j, end=" ")
        


# 8. [Project Euler Problem #1](https://projecteuler.net/problem=1)  
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# 
# Find the sum of all the multiples of 3 or 5 below 1000.

# In[4]:


sum=0
for i in range(1,1001):
    if i%3==0 or i%5==0:
        sum+=i
print(sum)


# 9. [Project Euler Problem #10](https://projecteuler.net/problem=10)  
# The sum of the primes below $10$ is $2 + 3 + 5 + 7 = 17$.
# 
# Find the sum of all the primes below two million ($2,000,000,000$).
# 
# Hint: considera la [Criba de Eratóstenes](https://es.wikipedia.org/wiki/Criba_de_Erat%C3%B3stenes)

# In[21]:


##Sólo me salen los números primos, no la suma ):
sum=0
for b in range(2,2000000001):
    for s in range(2,b):
        if b%s==0:
            break
    else:
        print(b)

