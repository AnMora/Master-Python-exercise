#Complete the function to return:
#1) How many apples each single student will get.
#2) How many apples wil remain in the basket.
#Hint: You can resolve this exercise either importing the math module or without it 
def apple_sharing(n,k):
    var1 = round(k/n)
    var2 = (var1 * n)
    var3 = (k - var2)
    return var1, var3

#Print the two answer per the example output.
print(apple_sharing(6,50))