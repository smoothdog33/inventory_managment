/*
For first 50 units $ 0.50/unit
For next 100 units $ 0.75/unit
For next 100 units $ 1.20/unit
For unit above 250 $ 1.50/unit
An additional surcharge of 20% is added to the bill.
 */

import java.util.Scanner;
public class ElectricityBill {
    public static void main(String[] args) {
        int units;
        double bill = 0;



        // get units from scanner and calculate bill
        Scanner sc = new Scanner(System.in);
        units = sc.nextInt();

// WRITE YOUR CODE HERE
        if(units < 50 ){
            System.out.printf("up");
        }
        System.out.println("The electricity bill is $%.2f\n", bill);
    }
}
