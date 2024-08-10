# python_energy_test
Testing different energy consumptions of BubbleSort implementations in Python using PyJoular

# Run the test
## Without the venv (you will have to make sure that all required packages are already installed)
```bash
python bubble_sort_power.py
```

## With a poetry venv
Install the venv

```bash
poetry install
```
```bash
poetry shell
python bubble_sort_power.py
```

# Results
Results are saved in the `results.csv` file.
The results contain 10 evaluations of all function where each evaluation passes a different randomized array of integers to the functions.