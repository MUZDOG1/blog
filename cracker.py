import itertools
import string
import time

# Define characters to use in the password
CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
# Define all characters to use in the password
chars = string.printable

# Define the password to be cracked
PASSWORD = "password123"
password = "password123"

# Define the maximum password length to try
MAX_LENGTH = 10
max_length = 10

# Track the start time of the password cracking process
start_time = time.time()

# Try all possible combinations of characters up to MAX_LENGTH
for length in range(1, MAX_LENGTH + 1):
    for combination in itertools.product(CHARS, repeat=length):
# Try all possible combinations of characters up to max_length
for length in range(1, max_length + 1):
    for combination in itertools.product(chars, repeat=length):
        # Join the characters in the combination to form a password candidate
        candidate = "".join(combination)
        print(f"Trying password: {candidate}")
        print("Trying password:", candidate)
        # Check if the candidate matches the password
        if candidate == PASSWORD:
        if candidate == password:
            # Track the end time of the password cracking process
            end_time = time.time()
            print(f"Password found: {candidate}")
            print("Password found:", candidate)
            # Calculate the time taken to crack the password
            time_taken = end_time - start_time
            print(f"Time taken: {time_taken:.2f} seconds")
            print("Time taken:", time_taken, "seconds")
            # Terminate the password cracking process
            raise SystemExit