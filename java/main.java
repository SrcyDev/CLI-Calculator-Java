// Creating a simple calculator

// This is my first java program, hoping you will like it !
 
// importing necessary utilities

import java.util.Scanner;

//creating class

public class main
{
  public static void main(String args[])
    {
    method();
    method2();
    }

    static void method()
    {
    
    // creating input
    
    Scanner input1 = new Scanner(System.in);
    Scanner input2 = new Scanner(System.in);
    Scanner input3 = new Scanner(System.in);
    
    System.out.println("Enter first number :-"); 
    int x = input1.nextInt();
    
    /*
     * if(!input1.hasNextInt()) {
		   System.out.println(input1.nextInt()+" is not a valid Integer");
		   System.out.println("Please try again");
		   method();
		}
    
    if(!input2.hasNextInt()) {
		   System.out.println(input2.nextInt()+" is not a valid choice");
		   System.out.println("Please try again");
		   method();
		   
		}
		
    if(!input3.hasNextInt()) {
		   System.out.println(input3.nextInt()+" is not a valid Integer");
		   System.out.println("Please try again");
		   method();
		}
		
     */
    
    // Above code is being tested and is buggy, probably going to be removed 
    
    System.out.println("Enter your choice as follows:");
    System.out.println("1: Addition");
    System.out.println("2: Subtraction");
    System.out.println("3: Multiplication");
    System.out.println("4: Division");
    System.out.println("5: Modulus / Remainder");
    System.out.println("6: Exponent / Power");
    int choice = input2.nextInt();
    
    System.out.println("Enter second Number :-");
    int y = input3.nextInt();
    
    
    // switch case
    
    switch(choice)
    {
    case 1:
        System.out.println("The sum is " + (x + y));
        break ;
        
    case 2:
        System.out.println("The difference is " + (x - y));
        break ;
    
    case 3:
        System.out.println("The product is " + (x * y));
        break ;
        
    case 4:
        System.out.println("The divident is " + (x / y));
        break ;
        
    case 5:
        System.out.println("The modulus is " + (x % y));
        break ;
        
    case 6:
        double z = Math.pow(x,y);
        System.out.println("The exponent is " + z);
        break ;
        
    default:
        System.out.println("Invalid try again.");
        method();
        break ;

    }
  }
  
  static void method2()
   {
    // asking the user if he/she wants to continue
    
    Scanner ask = new Scanner(System.in);
    System.out.println("Do you want to continue ? (y = 1/n = 2)");
    int input = ask.nextInt();
    
    // Looping
    
    if(input == 1){
       System.out.println("Okay! Continuing... ");
    }else if (input == 2){
       System.out.println("Exiting...");
    }else{
       System.out.println("Invalid Choice");
    }
   
    while (input == 1){
        method();
        method2();
        break ;
    } 
   }
}   
