from pyJoules.energy_meter import measure_energy
from pyJoules.handler.csv_handler import CSVHandler
import ctypes
import h5py
import numpy as np
import random
import os

csv_handler = CSVHandler('result.csv')

lib = ctypes.CDLL('./libbubble_sort_step.so')
lib.bubbleSortStep.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]

class ArrayEntry:
    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value
    
    def set(self, value):
        self.value = value

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

@measure_energy(handler=csv_handler)
def bubbleSort_before_optimization(array, *args):
    """
    A non-optimized Bubble Sort implementation that performs the full sorting process
    without early exits or any additional optimizations.
    """
    size = len(array)
    for _ in range(size):
        for j in range(size - 1):
            # yield array, j, j+1, -1, -1  # Yield the current state before comparing
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

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

@measure_energy(handler=csv_handler)
def bubbleSort_G21(array, *args):
    """
    An object array optimization of the Bubble Sort implementation.
    The python-native array passed to the function is replaced by an array of ArrayEntry objects
    """
    size = len(array)
    for _ in range(size):
        for j in range(size - 1):
            # yield array, j, j+1, -1, -1  # Yield the current state before comparing
            j_val = array[j].get()
            j_one_val = array[j + 1].get()
            if j_val > j_one_val:
                array[j].set(j_one_val)
                array[j + 1].set(j_val)

@measure_energy(handler=csv_handler)
def bubbleSort_G27(array, *args):
    """
    A non-optimized Bubble Sort implementation using an HDF5 file stored in RAM.
    """
    size = len(array)
    # Create an HDF5 file in memory with 'core' driver and 'backing_store=False' to ensure it stays in RAM
    with h5py.File('in_memory.h5', 'w', driver='core', backing_store=False) as h5file:
        # Create a dataset within the HDF5 file to store the array
        dset = h5file.create_dataset('array', data=array)

        # Perform Bubble Sort on the dataset
        for _ in range(size):
            for j in range(size - 1):
                if dset[j] > dset[j + 1]:
                    # Swap elements within the HDF5 dataset
                    dset[j], dset[j + 1] = dset[j + 1], dset[j]

        # Return the sorted array as a numpy array
        sorted_array = dset[:]

@measure_energy(handler=csv_handler)
def bubbleSort_numPy(array, *args):
    """
    An optimized Bubble Sort implementation that performs the full sorting process on a NumPy array instead of a native Python array
    without early exits or any additional optimizations.
    """
    size = len(array)
    for _ in range(size):
        for j in range(size - 1):
            # yield array, j, j+1, -1, -1  # Yield the current state before comparing
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

if __name__ == "__main__":

    for _ in range(10):
        # Generate a random array of 10,000 integers
        random_array = [random.randint(0, 100000) for _ in range(10000)]

        # ~~~~~~~~~~~~~~~~~~~~~ External BubbleSort ~~~~~~~~~~~~~~~~~~~~
        array = random_array[:]
        bubbleSort_external(array)
        print('Finished: External BubbleSort')

        # ~~~~~~~~~~~~~~~~~~~~~ Baseline BubbleSort ~~~~~~~~~~~~~~~~~~~~

        array = random_array[:]
        bubbleSort_before_optimization(array)
        print('Finished: Baseline BubbleSort')

        # ~~~~~~~~~~~~~~~~~~~~~ Test case G3  ~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        array = random_array[:]
        bubbleSort_G3(array)
        print('Finished: G3 BubbleSort')

        # ~~~~~~~~~~~~~~~~~~~~~ Test case G15 ~~~~~~~~~~~~~~~~~~~~~~~~~~
        array = np.array(random_array, dtype=np.int32)  # Convert the list to a numpy array because ctypes requires it
        bubbleSort_G15(array)
        print('Finished: G15 BubbleSort')

        # ~~~~~~~~~~~~~~~~~~~~~ Test case G21 ~~~~~~~~~~~~~~~~~~~~~~~~~~

        array = [ArrayEntry(value) for value in random_array]
        bubbleSort_G21(array)
        print('Finished: G21 BubbleSort')

        # ~~~~~~~~~~~~~~~~~~~~~ Test case G27 ~~~~~~~~~~~~~~~~~~~~~~~~~~

        array = random_array[:]
        bubbleSort_G27(array)
        os.remove('bubble_sort_example.h5')
        print('Finished: G27 BubbleSort')

        # ~~~~~~~~~~~~~~~~~~~~~ Test case NumPy ~~~~~~~~~~~~~~~~~~~~~~~~
        array = np.array(random_array)
        bubbleSort_numPy(array)
        print('Finished: NumPy BubbleSort')

    csv_handler.save_data()