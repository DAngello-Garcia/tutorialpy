 def divide(num1,num2):
     if num2 !=0:
         return num1/num2
     else:
         raise Exception('El núme')

def multiply(num1, num2):
    try:
        return num1/num2
    except:
        print("Error")
        return "h"


print(multiply(3,0))
