import random
import numpy as np
from pyJoules.energy_meter import measure_energy
from pyJoules.handler.csv_handler import CSVHandler

csv_handler = CSVHandler('result_numpy.csv')

@measure_energy(handler=csv_handler)
def bubbleSort_numPy(array_input, *args):
    """
    An optimized Bubble Sort implementation that performs the full sorting process on a NumPy array instead of a native Python array
    without early exits or any additional optimizations.
    """
    array = np.array(array_input)
    size = len(array)
    for _ in range(size):
        for j in range(size - 1):
            # yield array, j, j+1, -1, -1  # Yield the current state before comparing
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

if __name__ == "__main__":
    for _ in range(10):
        # Generate a random array of 100,000 integers
        random_array = [random.randint(0, 100000) for _ in range(100000)]

        bubbleSort_numPy(random_array)
        print('Finished: Numpy BubbleSort')

        csv_handler.save_data()