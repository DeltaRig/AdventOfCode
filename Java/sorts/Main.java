public class Main {
    public static void main(String[] args) {
        // initilize sorts
        Sort sort = new Sort();

        // Example array to sort
        int[] array = { 64, 34, 25, 12, 22, 11, 90 };

        // Printing the original array
        System.out.println("Original array:");
        for (int num : array) {
            System.out.print(num + " ");
        }
        System.out.println();

        // Sorting the array using bubble sort
        sort.selectionSort(array);

        // Printing the sorted array
        System.out.println("Sorted array:");
        for (int num : array) {
            System.out.print(num + " ");
        }
    }

}
