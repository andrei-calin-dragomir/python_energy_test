import random
from pyJoules.energy_meter import measure_energy
from pyJoules.handler.csv_handler import CSVHandler

csv_handler = CSVHandler('result_G21.csv')

class ArrayEntry:
    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value
    
    def set(self, value):
        self.value = value

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

if __name__ == "__main__":
    for _ in range(10):
        # Generate a random array of 100,000 integers
        array = [ArrayEntry(value) for value in [random.randint(0, 100000) for _ in range(100000)]]

        bubbleSort_G21(array)
        print('Finished: G21 BubbleSort')

        csv_handler.save_data()