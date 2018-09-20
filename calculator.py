import sys
def add(first_number,second_number):
    return first_number + second_number


def subtract(first_number,second_number):
    return first_number - second_number

def multiply(first_number,second_number):
    return first_number * second_number

def divide(first_number,second_number):
    return first_number /second_number

while True:
    try:
       first_number = int(input("Enter your first number :"))
       operand = input("Enter your operand :")
       second_number = int(input("Enter your second number :"))

       if operand == "+":
           result = add(first_number, second_number)
           print(result)
           break
       elif operand == "-":
           result = subtract(first_number, second_number)
           print(result)
           break

       elif operand == "*":
           result = multiply(first_number, second_number)
           print(result)
           break
       elif operand == "/":
           result = divide(first_number, second_number)
           print(result)
           break

       else:
           print ("input correct operand")

    except ValueError:
        print("input numbers only")
quit = input("please Enter q to exit.")
import sys
sys.exit(0)
