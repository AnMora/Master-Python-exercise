#Complete the function to return the tens digit and the ones digit of any interger.
def two_digits(digit):
    
    # mil = digit / 1000
    # tmp = digit % 1000

    # centenas = tmp / 100
    # tmp = tmp % 100

    # decenas = tmp / 10
    # unidades = tmp % 10

    res = int(digit%100)
    decenas = int(res-(res%10))/10
    unidades = int(res%10)

    return round(decenas, unidades)

#Invoke the function with any interger as its argument.
print(two_digits(79))
