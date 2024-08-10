#include <stdio.h>

void bubbleSortStep(int array[], int size);

// Function to perform the inner loop of Bubble Sort
void bubbleSortStep(int array[], int size) {
    for (int j = 0; j < size - 1; j++) {
        // Compare and swap adjacent elements if they are out of order
        if (array[j] > array[j + 1]) {
            int temp = array[j];
            array[j] = array[j + 1];
            array[j + 1] = temp;
        }
    }
}

