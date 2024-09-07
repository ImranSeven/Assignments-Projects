// PART A TASK 1

public abstract class Taxi implements Delivery {

    // Declaring class constants
    public static final String SEDAN = "Sedan";
    public static final String SUV = "SUV";
    public static final String VAN = "Van";
    public static final int MAX_REGO_LEN = 6;
    public static final int MAX_SEDAN_CAPACITY = 4;
    public static final int MAX_SUV_CAPACITY = 6;
    public static final int MAX_VAN_CAPACITY = 8;
    public static final boolean STATUS_UNAVAILABLE = false;
    public static final boolean STATUS_AVAILABLE = true;


// instances variables (Part A Task 1)

    // Declare all instance variable
    private String vehicle;
    private String regoNumber;
    private int passengerCapacity;
    private boolean status; // false=unavailable, true = available


// constructor (Part A Task 1)

    /* The constructor accept vehicle, regoNumber ,passengerCapacity and
    availabilityStatus instance variable as a parameter. */
    public Taxi(String vehicle, String regoNumber, int passengerCapacity, boolean availabilityStatus) {
        this.vehicle = vehicle;
        this.regoNumber = regoNumber;
        this.passengerCapacity = passengerCapacity;
        this.status = availabilityStatus;
    }


// getter | accessor (Part A Task 2)

    // getter for vehicle instance variable
    public String getVehicle() {
        return vehicle;
    }

    // getter for regoNumber instance variable
    public String getRegoNumber() {
        return regoNumber;
    }

    // getter for passengerCapacity instance variable
    public int getPassengerCapacity() {
        return passengerCapacity;
    }

    // getter for status instance variable
    public boolean isStatus() {
        return status;
    }


// setter | mutator (Part A Task 3 & 4)

    /* The setter/mutator method for vehicle instance variable accepts a parameter where the values can only be from one
     of the defined three categories of vehicle which are Sedan, SUV or Van.
     The method should return a boolean to indicate the success or failure of the mutation. */
    public boolean setVehicle(String vehicle) {
        boolean isValid = true;
        this.vehicle = vehicle;
        // Sets the corresponding values for "regoNumber", "passengerCapacity", and "status" instance variables
        switch (vehicle) {
            case SEDAN:
                regoNumber = "BAH932";
                passengerCapacity = MAX_SEDAN_CAPACITY;
                status = STATUS_AVAILABLE;
                break;
            case SUV:
                regoNumber = "WWV345";
                passengerCapacity = MAX_SUV_CAPACITY;
                status = STATUS_AVAILABLE;
                break;
            case VAN:
                regoNumber = "WVR777";
                passengerCapacity = MAX_VAN_CAPACITY;
                status = STATUS_UNAVAILABLE;
                break;
            // if the vehicle is an invalid type
            default:
                System.out.println("Invalid vehicle type: " + vehicle); // print an error message
                isValid = false;
        }
        return isValid;
    }

    // Setter for regoNumber instance variable
    public void setRegoNumber(String regoNumber) {  // Check if the length of the regoNumber is valid
        if (regoNumber.length() == MAX_REGO_LEN) {
            this.regoNumber = regoNumber;
        } else {
            System.out.println("Error: Invalid registration number provided."); // Print an error message
        }
    }

    // Setter for passengerCapacity instance variable
    public void setPassengerCapacity(int passengerCapacity) {
        if (this.vehicle.equals(Taxi.SEDAN) && passengerCapacity >= 1 && passengerCapacity <= MAX_SEDAN_CAPACITY) {
            this.passengerCapacity = passengerCapacity;
        } else if (this.vehicle.equals(Taxi.SUV) && passengerCapacity >= 1 && passengerCapacity <= MAX_SUV_CAPACITY) {
            this.passengerCapacity = passengerCapacity;
        } else if (this.vehicle.equals(Taxi.VAN) && passengerCapacity >= 1 && passengerCapacity <= MAX_VAN_CAPACITY) {
            this.passengerCapacity = passengerCapacity;
        } else {
            System.out.println("Error: Invalid passenger capacity number provied.");    // print an error message
        }
    }

    // Setter for status instance variable
    public void setStatus(boolean status) {
        this.status = status;
    }


// other method ((Part A Task 5)

    @Override
    public String toString() {
        return "Vehicle: " + vehicle +
                "\nRegistration Number: " + regoNumber +
                "\nPassenger Capacity: " + passengerCapacity +
                "\nAvailability Status: " + status;
    }
}
