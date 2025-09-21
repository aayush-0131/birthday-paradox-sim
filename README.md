# Birthday Paradox Simulator

## 🎯 Objective

This project is a command-line tool that runs Monte Carlo simulations to explore the "Birthday Paradox". It can be used in two ways:

1.  **Find Crossover Point**: Automatically find the minimum number of people required in a group for the probability of a shared birthday to exceed 50%.
2.  **Calculate for Specific Group Size**: Calculate the probability of a shared birthday for a specific number of people that you provide.

The simulation assumes a non-leap year (365 days) for simplicity.

## 🛠️ How to Run

This script is run from the terminal. It's recommended to use a virtual environment.

### Prerequisites
- Python 3

### Installation

1.  Clone the repository and navigate into the project directory.
2.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```
3.  This project has no external dependencies, so no installation is needed. The `requirements.txt` file is intentionally empty.

### Execution & Examples

The script's behavior changes based on whether you provide the `--people` flag.

**1. Find the 50% Crossover Point (Default Mode)**

To run the original simulation that finds the minimum number of people, run the script without any arguments.

```bash
python simulator.py
```
**Expected Output:**
```
Starting Birthday Paradox Simulation...
========================================
Num People | Probability of Shared Birthday
========================================
2          | 0.0028
...
22         | 0.4755
23         | 0.5071
========================================

Result: With 23 people, the probability first exceeds 50%!
```

**2. Calculate Probability for a Specific Group Size**

To calculate the probability for a specific group, use the `-p` or `--people` flag.

* **Example for a group of 40 people:**
    ```bash
    python simulator.py --people 40
    ```
    **Expected Output:**
    ```
    Calculating probability for a group of 40 people...
    ========================================
    Result: The probability of a shared birthday is approximately 89.12%.
    ```

* **Example for a group of 60 people:**
    ```bash
    python simulator.py -p 60
    ```
    **Expected Output:**
    ```
    Calculating probability for a group of 60 people...
    ========================================
    Result: The probability of a shared birthday is approximately 99.41%.
    ```