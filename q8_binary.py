# QUESTION 8
def bin_to_dec():
    import random

    # Generate a random 4-digit number of 0s and 1s
    binary_num = ''.join(str(random.randint(0,1)) for _ in range(4))

    # Convert the binary number to base 10
    decimal_num = int(binary_num, 2)

    return decimal_num