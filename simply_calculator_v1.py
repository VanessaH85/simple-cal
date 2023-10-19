#simple calculator application

#Create functions, based on the two numbers and the operation that the user has input
def addition(number_1,number_2): 
    a = number_1+number_2
    return a


def subtraction(number_1,number_2): 
    b = number_1-number_2
    return b


def multiplication(number_1,number_2): 
    c = number_1*number_2
    return c


def division(number_1,number_2): 
    d = number_1/number_2
    return d


#Request user choose to either enter two numbers and an operator or to read all of the equations from a new txt file
user_choice=input ('''Select one of the following Options below:
                    we - write an equation
                   
                    :\n ''').lower()

#If user chooses to enter two numbers and an operator, Display the answer to the equation. Every equation entered by the user is be written to a text file.

if user_choice =="we":       

    while True:
        try:
            number_1=int(input("Please enter your 1st number:\n"))
            break
        except Exception:
            print("Oops! That was not a valid number. Try again...")

    while True:
        try:
            number_2=int(input("Please enter your 2nd number:\n"))
            break
        except Exception:
            print("Oops! That was not a valid number. Try again...") 


    menu=input ('''Select one of the following Options below:
                + - addition
                - - subtraction
                x - multiplication
                / - division
                :\n ''').lower()
    
    
    if menu == "+":
        open_equation = open("equation.txt","a")
        sum_of_add=addition(number_1,number_2)
        print(sum_of_add)
        open_equation.write(str(number_1)+" + "+str(number_2)+" = "+str(sum_of_add)+"\n")
        open_equation.close()

    elif menu == "-":
        open_equation = open("equation.txt","a")
        sum_of_sub=subtraction(number_1,number_2)
        print(sum_of_sub)
        open_equation.write(str(number_1)+" - "+str(number_2)+" = "+str(sum_of_sub)+"\n")
        open_equation.close()

    elif menu == "x":
        open_equation = open("equation.txt","a")
        sum_of_mul=multiplication(number_1,number_2)
        print(sum_of_mul)
        open_equation.write(str(number_1)+" x "+str(number_2)+" = "+str(sum_of_mul)+"\n")
        open_equation.close()

    elif menu == "/":
        try:
            open_equation = open("equation.txt","a")
            sum_of_div=division(number_1,number_2)
            print(sum_of_div)
            open_equation.write(str(number_1)+" / "+str(number_2)+" = "+str(sum_of_div)+"\n")
            open_equation.close()    
        except ZeroDivisionError:
            open_equation = open("equation.txt","a") 
            sum_of_div=0
            print(sum_of_div)
            open_equation.write(str(number_1)+" / "+str(number_2)+" = "+str(sum_of_div)+"\n")
            open_equation.close()


