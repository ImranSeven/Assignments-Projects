import java.util.ArrayList;

public class TaxiMart extends Taxi {

// Instance Variables ( Part A Task 2 )

    // Declare all instance variable
    private int bootSpace;
    private int grocerySize;
    private ArrayList<String> groceryList;
    private double totalCost;


// Constructor ( Part A Task 3 )

    /* Call the constructor of the superclass.
       The constructor accept bootSpace and grocerySize instance variable as a parameter. */
    public TaxiMart(int bootSpace, int grocerySize) {
        super(SEDAN, "BAH932", MAX_SEDAN_CAPACITY, STATUS_AVAILABLE);
        this.bootSpace = bootSpace;
        this.grocerySize = grocerySize;
        this.groceryList = new ArrayList<>();
        this.totalCost = 0.0;
    }


// Getter/Accessor ( Part A Task 4 )

    // Getter for bootSpace instance variable
    public int getBootSpace() {
        return bootSpace;
    }

    // Getter for grocerySize instance variable
    public int getGrocerySize() {
        return grocerySize;
    }

    // Getter for groceryList instance variable
    public ArrayList<String> getGroceryList() {
        return groceryList;
    }

    // Getter for totalCost instance variable
    public double getTotalCost() {
        return totalCost;
    }


// Setter/Mutator ( Part A Task 5 )

    // Setter for bootSpace instance variable
    public void setBootSpace(int bootSpace) {
        this.bootSpace = bootSpace;
    }

    // Setter for grocerySize instance variable
    public void setGrocerySize(int grocerySize) {
        this.grocerySize = grocerySize;
    }


// ( Part A Task 6 )
    public void addGroceriesItem(String itemName, double itemCost) {
        if (itemName != null) {
            // Check if groceryList has reached the maximum capacity
            if (groceryList.size() < 30) {
                groceryList.add(itemName);
                totalCost += itemCost;
//                System.out.println("Item '" + itemName + "' added to grocery list.");
            } else {
                System.out.println("Grocery list is full.");
            }
        }
    }


// ( Part A Task 7 )
    public String deliverGroceries() {

        // Calculate the delivery commission
        double deliveryCommission = totalCost * 0.1;
        // Calculate the total cost with commission
        totalCost += deliveryCommission;

        return "Delivered: " + groceryList +  // list out all grocery items in the ArrayList
                "\nDelivery completed! Total cost is: $" + totalCost;
    }


// ( Part A Task 8 )

    @Override
    public String toString() {
        return super.toString() +
                "\n" +
                "\nBootSpace: " + bootSpace + " litre" +
                "\nGrocery Size: " + grocerySize + " litre" +
                "\nGrocery List: " + groceryList +
                "\nTotal Cost: $" + totalCost;
    }


//  ( Part B Task 8 )
    @Override
    public String sendDelivery() {
        return this.deliverGroceries();
    }
}
