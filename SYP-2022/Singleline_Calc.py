from array import array
import re
viableInput = "[+-/*0-"+ str(max(1)) +"]"

op = ""
def main():
    equation = input("give me an equation: ")
    if re.search(viableInput, equation) == None:
        print("You need to give me + or minus")
        main()
    else:
        breakup_equation(equation);

#this breaks the euqation into an array with num1, op, and num2 respectivly
def breakup_equation(equation=str):
    num1 = ''
    num2 = ''
    op   = ''
    operations = "[+-/*]"
    equation_arr = re.findall(viableInput, equation.strip())
    curr_num = 1 #this is the current number that we're assigning
    for i in equation_arr:
        if(re.search(operations, i) == None):
            if curr_num == 1:
                num1 += i
            else:
                num2 += i
        else:
            curr_num += 1
            op = i
    values_to_int(num1, num2, op)


#makes num1 and num2 integers
def values_to_int(num1, num2, op):
    num1 = int(num1)
    num2 = int(num2)
    calc(num1, num2, op)

def add(num1, num2):
    return num1+num2
def subtract(num1, num2):
    return num1-num2
def multiply(num1, num2):
    return num1*num2
def divide(num1, num2):
    return num1/num2

def calc(num1, num2, op):
    num = 0
    if op == '*':
        num = multiply(num1, num2)
    elif op == '/':
        num = divide(num1, num2)
    elif op == '+':
        num = add(num1, num2)
    elif op == '-':
        num = subtract(num1, num2)
    print(num)



if __name__ == "__main__":
    main()