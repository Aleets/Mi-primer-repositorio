import os


from email import message
from unittest import result


def sum(num1, num2):
  return num1 + num2


def rest(num1, num2):
  return num1 - num2

def multiplication(num1, num2):
  return num1 * num2

def divi(num1, num2):
  if num2 ==0:
    num2 = 1
  return num1 / num2

def return_values():
  num1 = int(input("Ingresa tu primer valor: "))
  num2 = int(input("Ingresa tu sugundo valor: "))
  return [num1, num2]

if __name__ == '__main__':
    message = f"Calculadora: \n Elige una opcion \n 1 - suma \n 2 - resta \n 3 - multiplicacion \n 4 - divición  \n 5 - salir \n"
    while True:
      opcion = int(input(message))
      if opcion ==1:
        numeros = return_values()
        result_sum = sum(numeros[0], numeros[1])
        print("El resultado de la suma es: ", result_sum)
      elif opcion ==2:
        numeros = return_values()
        result_rest = rest(numeros[0], numeros[1])
        print("El resultado de la resta es: ", result_rest)
      elif opcion ==3:
        numeros = return_values()
        result_multi = multiplication(numeros[0], numeros[1])
        print("El resultado de la multiplicacion es: ",result_multi)
      elif opcion == 4:
        numeros = return_values()
        result_div = divi(numeros[0], numeros[1])
        print("El resultado de la divicion es: ",result_div)
      elif opcion == 5:
        print("Bye!")
        break
      else:
        print("Opcion incorrecta!!!")




#if_name == 'main':
 #   print("Hola mundo!")