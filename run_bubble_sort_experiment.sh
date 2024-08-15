#!/bin/bash

# Run the Python scripts in sequence

# echo "Running BubbleSort Before Optimization"
# python bubblesort_before.py

# echo "Running BubbleSort External"
# python bubblesort_external.py

# echo "Running BubbleSort G3"
# python bubblesort_G3.py

# echo "Running BubbleSort G15"
# python bubblesort_G15.py

echo "Running BubbleSort G21"
python bubblesort_G21.py

echo "Running BubbleSort NumPy"
python bubblesort_NumPy.py

echo "All scripts have been executed."
