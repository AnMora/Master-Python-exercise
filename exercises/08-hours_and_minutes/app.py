#Complete the function to calculate how many hours and minutes are passed since midnight.
def hours_minutes(secs):
    # horas = int(secs/3600)
    # minutos=int(secs/60)
    # return horas, minutos

    return int(secs/3600), int(secs/60)
    
#Invoke the funtion and pass any interger as its argument.
print(hours_minutes(3900))