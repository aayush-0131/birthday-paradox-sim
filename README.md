# Birthday Paradox Simulator

## Overview

This project is a Python-based simulation of the classic "Birthday Paradox". The paradox states that in a group of people, the probability of at least two individuals sharing a birthday is much higher than one might intuitively expect.

This script runs Monte Carlo simulations to empirically determine the minimum number of people required in a group to have a greater than 50% probability that at least two of them share a birthday. For simplicity, the simulation assumes a non-leap year (365 days).

## How It Works

1.  **`has_duplicate_birthday(num_people)`**: This function simulates a single "room" with `num_people`. It generates a random integer between 1 and 365 for each person. Using a `set` for efficient lookup, it checks if a duplicate birthday is generated.
2.  **`run_simulation(num_people, num_simulations)`**: To find the probability for a given group size, this function calls `has_duplicate_birthday` thousands of times (default is 10,000) and calculates the ratio of successful outcomes (shared birthdays) to the total number of simulations.
3.  **`find_min_people_for_50_percent()`**: This is the main driver function. It starts with a group of 2 people and iteratively increases the group size, running simulations for each size until the calculated probability exceeds 0.5 (50%).

## How to Run

1.  Ensure you have Python 3 installed.
2.  Clone the repository or download the `simulator.py` file.
3.  Open your terminal and navigate to the project directory.
4.  Run the script:
    ```bash
    python simulator.py
    ```

## Expected Output

The script will print the probability for each group size until it crosses the 50% threshold, at which point it will display the final result.