SCRIPT_EXPLANATION = 'Hello User,\n This script calculates the sum of all numbers from 0 up to, but not including, the ' 
'specified limit by you that are multiples of at least one of the numbers you provide'

# Helper function to get upper limit

def get_limit():
    print('Please enter an upper limit.')
    while True:
        try:
            limit = int(input('>'))
            return limit
        except ValueError:
            print('Please only enter numbers')


# Helper function to get numbers

def get_numbers():
    numbers = []
    print('How many numbers do you want to calculate?')
    while True:
        try:
            numbers_amount = int(input('>'))
            break
        except ValueError:
            print('Please only enter the amount of numbers you want to add')
    print('Please enter the numbers you want to calculate')
    while True:
        try:
            for i in range(0,numbers_amount):
                    number = int(input('>'))
                    numbers.append(number)
            return numbers
        except ValueError:
            print('Please only enter numbers')
            

# Main function to execute the calculation

def main(limit, numbers):
    total_sum = 0
    n = 0
    for i in range(0, limit):
        for number in numbers:
            if n % number == 0:
                total_sum = total_sum + n
                break
        n = n + 1
    return total_sum

print(SCRIPT_EXPLANATION)
limit = get_limit()
numbers = get_numbers()
total_sum = main(limit, numbers)
print(f'The sum of the multiples of your number is {total_sum}')