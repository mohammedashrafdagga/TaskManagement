import random
import string

# Generate Random Number Using A Code to Join a Task
def generate_code():
    return ''.join(random.choices(string.digits, k=6))
