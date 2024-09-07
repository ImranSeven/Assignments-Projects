import java.util.ArrayList;

public class TaxiClassDriver {
    public static void main(String[] args) {

        System.out.println( "Instantiation of subclasses object:\n");

        // Code Part B Task 9 ( first 3 dot points) here

        // Instantiate subclass instances for TaxiMart and TaxiFood
        TaxiMart taximart = new TaxiMart(471, 300);
        TaxiFood taxifood = new TaxiFood("Fried rice", new ArrayList<String>(), 0.0);

        // Invoke appropriate methods to add respective items to their own arraylist.
        taximart.addGroceriesItem("Vegetables", 15);
        taximart.addGroceriesItem("Meat", 35.5);

        taxifood.addFoodOrder("Burger", 20.0);
        taxifood.addFoodOrder("Noodle", 15.0);

        // Print the information of the subclass instances respectively.
        System.out.println(taximart);
        System.out.println();
        System.out.println();
        System.out.println(taxifood);
        System.out.println();

        System.out.println( "Taxi delivery processed polymorphically:\n" );

        // Code Part B Task 9 ( last 2 dot points) here

        // Instantiate an array of class instances to demonstrate polymorphism (Rule 1 and Rule 3).
        Delivery[] deliveries = new Delivery[2];
        deliveries[0] = taximart;
        deliveries[1] = taxifood;

        // Print the information by invoke the sendDelivery() method to demonstrate it has been processed polymorphically.
        for (Delivery d : deliveries) {
            String result = d.sendDelivery();
            System.out.println(result);
            System.out.println();
        }
    }
}
