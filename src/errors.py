def convert_to_integer(value):
    try:
        result = int(value)
        # print(f'Conversion successful! Result: {result}')
        return result
    except ValueError: # Addresses specific error class
        print('Conversion failed. Please enter a valid integer.')
    except ZeroDivisionError:
        print('Cannot divide by zero!')       
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
    else: # Only happens if no exceptions occurred
        print('Else invoked.')
    finally: # Happens no matter what
        print('Closing any open resources.')
            
# User input
spam = input('Enter a number to convert to integer: ') # input - prompts for user input in terminal
convert_to_integer(spam)