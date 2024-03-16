class EnumClassExample {
    // defining the enum inside the class
    public enum Weekdays {
        SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY
    }

    // main method
    public static void main(String[] args) {

        // loop throught the enum

        for (Weekdays w : Weekdays.values())
            System.out.println(w);
    }
}
