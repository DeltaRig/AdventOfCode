public class Sort {
    public static void bubbleSort(int[] intArray) {
        // On^2 Bubble sort algorithm implementation
        for (int lastUnsortedIndex = intArray.length - 1; lastUnsortedIndex > 0; lastUnsortedIndex--) {
            for (int i = 0; i < lastUnsortedIndex; i++) {
                // Comparing adjacent elements and swapping them if they are in the wrong order
                if (intArray[i] > intArray[i + 1]) {
                    swap(intArray, i, i + 1); // Call to swap function
                }
            }
        }
    }

    // On^2 Selection sort algorithm implementation
    public static void selectionSort(int[] intArray) {
        for (int lastUnsortedIndex = intArray.length - 1; lastUnsortedIndex > 0; lastUnsortedIndex--) {

            int largest = 0;

            for (int i = 1; i <= lastUnsortedIndex; i++) {
                if (intArray[i] > intArray[largest]) {
                    largest = i;
                }
            }

            swap(intArray, largest, lastUnsortedIndex);

        }
    }

    // O n^2 Insert sort algorithm
    public static void insertSort(int[] intArray) {
        for (int firstUnsortedIndex = 1; firstUnsortedIndex < intArray.length; firstUnsortedIndex++) {
            int newElement = intArray[firstUnsortedIndex];

            int i;

            for (i = firstUnsortedIndex; i > 0 && intArray[i - 1] > newElement; i--) {
                intArray[i] = intArray[i - 1];
            }

            intArray[i] = newElement;
        }

        for (int i = 0; i < intArray.length; i++) {
            System.out.println(intArray[i]);
        }
    }

    // shellSort
    public static void shellSort(int[] intArray) {
        for (int gap = intArray.length / 2; gap > 0; gap /= 2) {
            for (int i = gap; i < intArray.length; i++) {
                int temp = intArray[i];

                int j = i;

                while (j >= gap && intArray[j - gap] > temp) {
                    intArray[j] = intArray[j - gap];
                    j -= gap;
                }
                intArray[j] = temp;
            }
        }
    }

    // Method to swap two elements in an array
    static void swap(int[] array, int i, int j) {
        // If the indices are the same, no need to swap
        if (i == j) {
            return;
        }
        // Swapping the elements
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}
