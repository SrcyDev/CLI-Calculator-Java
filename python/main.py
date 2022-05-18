##########START##########

#####IMPORT START#####

import math

#####IMPORT END#######

#####METHOD START#####
def main():
 x = int(input("Enter first number :-"))
      
 print("Enter your choice as follows:")
 print("1: Addition")
 print("2: Subtraction")
 print("3: Multiplication")
 print("4: Division")
 print("5: Modulus / Remainder")
 print("6: Exponent / Power")
         
 choice = int(input("Enter choice now : "))

 y = int(input("Enter second number :-"))

 # switch case
 if (choice == 1):
    print("The sum is:")
    print(x + y)
 elif(choice == 2):
    print("The difference is:")
    print(x - y)
 elif(choice == 3):
    print("The product is:")
    print(x * y)
 elif(choice==4):
    print("The divident is:")
    print(x / y)
 elif(choice==5):
    print("The modulus is:")
    print(x % y)
 elif(choice==6):
    print("The exponent is:")
    z = math.pow(x,y)
    print(z)
 else:
    print("Invalid try again.")
    main()

#####METHOD END#####    

main()

#####METHOD 2 START#####

def ask():
 print("Do you want to continue ? (y = 1/ n = 2)")  
 a = int(input())
 if(a == 1):
        print("Okay ! Continuing...")
        main()
 if (a == 2):
        print("Exiting...")
 else:
        print("Error. Please try again (This could be a bug, please check the input)")

#####METHOD 2 END#####

ask()

##########END##########
