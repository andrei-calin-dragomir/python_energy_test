from pyJoules.energy_meter import measure_energy
from pyJoules.handler.csv_handler import CSVHandler
import random

csv_handler = CSVHandler('result_external.csv')

@measure_energy(handler=csv_handler)
def bubbleSort_external(array, *args):
    """
    Bubble Sort is a simple comparison-based sorting algorithm that 
    repeatedly compares adjacent elements in a list and swaps them 
    if they are in the wrong order until the list is sorted.
    
    Time complexity: O(n^2), where n is the number of elements in the list.
    """
    size = len(array)
    for i in range(size):
        swapped = False
        for j in range(size - i - 1):
            # yield array, j, j+1, -1, -1 # Yield the current state before comparing
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break

if __name__ == "__main__":

    for _ in range(10):
        # Generate a random array of 10,000 integers
        random_array = [random.randint(0, 100000) for _ in range(100000)]

        bubbleSort_external(random_array)
        print('Finished: Baseline BubbleSort')

        csv_handler.save_data()