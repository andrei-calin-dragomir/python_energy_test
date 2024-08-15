import random
from pyJoules.energy_meter import measure_energy
from pyJoules.handler.csv_handler import CSVHandler

csv_handler = CSVHandler('result_G3.csv')

@measure_energy(handler=csv_handler)
def bubbleSort_G3(array, *args):
    """
    A loop-optimized variant of the Bubble Sort implementation.
    Loop optimization techniques that can be used in this case: loop unrolling, early termination
    """
    size = len(array)
    for i in range(size):
        swapped = False
        for j in range(0, size - i - 1, 4):
            # Unrolling by 4 steps
            if j < size - i - 1:
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    swapped = True
            if j + 1 < size - i - 1:
                if array[j + 1] > array[j + 2]:
                    array[j + 1], array[j + 2] = array[j + 2], array[j + 1]
                    swapped = True
            if j + 2 < size - i - 1:
                if array[j + 2] > array[j + 3]:
                    array[j + 2], array[j + 3] = array[j + 3], array[j + 2]
                    swapped = True
            if j + 3 < size - i - 1:
                if array[j + 3] > array[j + 4]:
                    array[j + 3], array[j + 4] = array[j + 4], array[j + 3]
                    swapped = True
        # Early termination
        if not swapped:
            break

if __name__ == "__main__":
    for _ in range(10):
        # Generate a random array of 100,000 integers
        random_array = [random.randint(0, 100000) for _ in range(100000)]

        bubbleSort_G3(random_array)
        print('Finished: G3 BubbleSort')

        csv_handler.save_data()