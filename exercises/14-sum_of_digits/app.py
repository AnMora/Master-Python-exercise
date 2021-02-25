#Complete the function "digits_sum" so that it prints the sum of a three digit number.
def digits_sum(num):
    res = int(num%1000)
    centenas = int(res-(res%100))/100
    res2 = int(num%100)
    decenas = int(res2-(res2%10))/10
    unidades = int(res%10)
    return centenas + decenas + unidades


#Invoke the function with any three-digit-number
#You can try other three-digit numbers if you want
print(digits_sum(123))