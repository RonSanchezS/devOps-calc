# functions
def sumar(x, y):
   return x + y
 
def restar(x, y):
   return x - y
 
def multiplicar(x, y):
   return x * y

def dividir(x, y):
   return x / y
 
# MENU
print("Seleccionar operacion:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
 
choice = input("Ingrese operacion(1, 2, 3 o 4):")
num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))
 
if choice == '1':
   print(num1,"+",num2,"=", sumar(num1,num2))
 
elif choice == '2':
   print(num1,"-",num2,"=", restar(num1,num2))
 
elif choice == '3':
    print (num1,"*",num2,"=", multiplicar(num1,num2))
 
elif choice == '4':
    print (num1,"/",num2,"=", dividir(num1,num2))
    
else:
   print("******* Dato invalido! **********")