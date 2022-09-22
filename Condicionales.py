#Condiciolales if elief else
#Nos permiten evaluar expresiones booleanas que de cumplirse realizan
#Una accion y en caso de que no entonces realizan otra

#Evaluar si una persona es mayor de edad
#Nos diga  es bebe, niño, joven, adulto, adulto mayor, y el genero

#genre = input("Ingresa tu genero: ")
#age = int(input('Ingresa tu edad actual: '))
#if age < 2:
#    print("Eres un bebe"+ " y eres: " + genre)
#elif age < 12:
#    print("Eres in niño"+ " y eres: " + genre)
#elif age < 18:
#    print("Eres un joven " + " y eres: " + genre)
#elif age < 50:
#    print("Eres un adulto" + " y eres: " + genre)
#else:
 #   print("Eres muy mayor"+ " y eres: " + genre)

    
 # Profesor   
genre = input("Ingresa tu genero (H/M): ")
age = int(input('Ingresa tu edad actual: '))
mujer = ""
if genre == "M":
   mujer = "a" 

if age < 2:
    print(f"Eres un{mujer} bebe")
elif age < 12:
    print(f"Eres un{mujer} niño")
elif age < 18:
    print(f"Eres un{mujer} joven")
elif age < 50:
    print(f"Eres un{mujer} adulto")
else:
    print(f"Eres{mujer} muy mayor")
