#Complete the function to return how many hrs and min are displayed on the 24th digital clock.
def digital_clock(n):
    horas = n%3600
    return horas

#Invoke the function with any interger (seconds after midnight)
print(digital_clock(150))
