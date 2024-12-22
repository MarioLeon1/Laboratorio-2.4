import random

def generate_random_number(min_value=1, max_value=100):
    """
    Generate a random number between min_value and max_value (inclusive)
    """
    return random.randint(min_value, max_value)

def generate_random_list(size=5, min_value=1, max_value=100):
    """
    Generate a list of random numbers
    """
    return [random.randint(min_value, max_value) for _ in range(size)]

if __name__ == "__main__":
    # Example usage
    print("Random number:", generate_random_number())
    print("Random number between 1 and 10:", generate_random_number(1, 10))
    print("List of 5 random numbers:", generate_random_list())
    print("List of 3 random numbers between 1 and 10:", generate_random_list(3, 1, 10))