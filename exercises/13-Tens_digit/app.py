#Complete the function to return the tens digit of a given interger
def tens_digit(num):
    numero = int(num)
    # if numero > 9:
    return int(str(numero)[-2:-1])
    # else:
    #     print("Ingrese un numero mayor a 9")

#Invoke the function with any interger.
print(tens_digit("1234"))