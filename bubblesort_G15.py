import random
import numpy as np
import ctypes
from pyJoules.energy_meter import measure_energy
from pyJoules.handler.csv_handler import CSVHandler

csv_handler = CSVHandler('result_G15.csv')

lib = ctypes.CDLL('./libbubble_sort_step.so')
lib.bubbleSortStep.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]

@measure_energy(handler=csv_handler)
def bubbleSort_G15(array, *args):
    """
    A compiled language optimization of the Bubble Sort implementation.
    The body of the loop is written in C and used as a shared library
    """
    size = len(array)
    for _ in range(size):
        # Call the C function to perform the inner loop step
        lib.bubbleSortStep(array.ctypes.data_as(ctypes.POINTER(ctypes.c_int)), size)


if __name__ == "__main__":
    for _ in range(10):
        # Generate a random array of 100,000 integers
        array = np.array([random.randint(0, 100000) for _ in range(100000)], dtype=np.int32)  # Convert the list to a numpy array because ctypes requires it
        bubbleSort_G15(array)
        print('Finished: G15 BubbleSort')

        csv_handler.save_data()