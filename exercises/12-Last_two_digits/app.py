#Complete the function to print the last two digits of an interger greater than 9. 
def last_two_digits(num):

    numero = int(num)
    if numero > 9:
        return int(str(numero)[-2:])
    else:
        print("Ingrese un numero mayor a 9")

#Invoke the function with any interger greater than 9.
print(last_two_digits("1234"))
