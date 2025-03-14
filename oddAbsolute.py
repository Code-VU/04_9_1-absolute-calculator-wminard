def calculateAbsolute():
    
    # This first line is provided for you
    try:
        in_num  = int(input("Enter a number: "))
    except:
        print('invalid input')
        return
    
    if in_num > 21:
        print('Result: ' + str((in_num-21)*2))
    else:
        print('Result: ' + str(21-in_num))
    # end assignment

## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()
