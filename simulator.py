import random

def has_duplicate_birthday(num_people):
    """
    Simulates a room with a given number of people to check for shared birthdays.
    
    Args:
        num_people (int): The number of people in the room.
        
    Returns:
        bool: True if a shared birthday is found, False otherwise.
    """
    birthdays = set()
    for _ in range(num_people):
        # Generate a random day of the year (1-365, ignoring leap years for simplicity)
        birthday = random.randint(1, 365)
        if birthday in birthdays:
            return True # Found a duplicate
        birthdays.add(birthday)
    return False # No duplicates found

def run_simulation(num_people, num_simulations=10000):
    """
    Runs multiple simulations to find the probability of a shared birthday.
    
    Args:
        num_people (int): The number of people in each simulation.
        num_simulations (int): The number of times to run the simulation.
        
    Returns:
        float: The probability (0.0 to 1.0) of a shared birthday.
    """
    shared_birthday_count = 0
    for _ in range(num_simulations):
        if has_duplicate_birthday(num_people):
            shared_birthday_count += 1
    
    return shared_birthday_count / num_simulations

def find_min_people_for_50_percent():
    """
    Finds the minimum number of people required to have a >50% chance
    of a shared birthday.
    """
    print("Starting Birthday Paradox Simulation...")
    print("="*40)
    print("Num People | Probability of Shared Birthday")
    print("="*40)
    
    for num_people in range(2, 367):
        probability = run_simulation(num_people)
        print(f"{num_people:<10} | {probability:.4f}")
        
        if probability > 0.5:
            print("="*40)
            print(f"\nResult: With {num_people} people, the probability of a shared birthday first exceeds 50%!")
            print(f"The calculated probability is approximately {probability*100:.2f}%.")
            return

if __name__ == "__main__":
    find_min_people_for_50_percent()