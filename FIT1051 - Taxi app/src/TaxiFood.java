import java.util.ArrayList;

public class TaxiFood extends Taxi {

// Instance Variables ( Part B Task 1 )

    // Declare all instance variable
    private String foodName;
    private ArrayList<String> foodList;
    private double totalCost;


// Constructor ( Part B Task 2 )

    /* Call the constructor of the superclass.
       The constructor accept foodName, foodList and totalCost instance variable as a parameter. */
    public TaxiFood(String foodName, ArrayList<String> foodList, double totalCost) {
        super(SUV, "WWW345", MAX_SUV_CAPACITY, STATUS_AVAILABLE);
        this.foodName = foodName;
        this.foodList = foodList;
        this.totalCost = totalCost;
    }


// Getter/Accessor ( Part B Task 3 )

    // Getter for foodName instance variable
    public String getFoodName() {
        return foodName;
    }

    // Getter for foodList instance variable
    public ArrayList<String> getFoodList() {
        return foodList;
    }

    // Getter for totalCost instance variable
    public double getTotalCost() {
        return totalCost;
    }


// setter/mutator ( Part B Task 4 )

    // Setter for foodName instance variable
    public void setFoodName(String foodName) {
        this.foodName = foodName;
    }

    // Setter for totalCost instance variable
    public void setTotalCost(double totalCost) {
        this.totalCost = totalCost;
    }


// ( Part B Task 5 )
    public void addFoodOrder(String foodName, double foodCost) {
        if (foodName != null) {
            // Check if food list has reached the maximum capacity
            if (foodList.size() < 30) {
                foodList.add(foodName);
                totalCost += foodCost;
//                System.out.println("Item '" + foodName + "' added to food list.");
            } else {
                System.out.println("Food list is full.");
            }
        }
    }


//  ( Part B Task 6 )
    public String deliverFood() {

        // Calculate the delivery commission
        double deliveryCommission = totalCost * 0.2;
        // Calculate the total cost with commission
        totalCost += deliveryCommission;

        return "Delivered: " + foodList +  // list out all food items in the ArrayList
           "\nDelivery completed! Total cost is: $" + totalCost;
    }


//  ( Part B Task 7 )

    @Override
    public String toString() {
        return super.toString() +
                "\n " +
                "\nFood Name: " + foodName +
                "\nFood List: " + foodList +
                "\nTotal Cost: $" + totalCost;
    }


//  ( Part B Task 8 )
    @Override
    public String sendDelivery() {
        return this.deliverFood();
    }
}
