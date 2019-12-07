import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

  
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        double meal_Cost = scan.nextDouble(); 
        int tipPercent = scan.nextInt(); 
        int taxPercent = scan.nextInt(); 
        scan.close();

        // Write your calculation code here.
        double tip = meal_Cost * tipPercent / 100;
        double tax = meal_Cost * taxPercent / 100;
		
        int totalCost = (int) Math.round(mealCost + tip + tax);

        System.out.println(totalCost);
    }
}