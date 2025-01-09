def checkforerror(input):
    inputlist = [char for char in input]  # Segments out each charcter in a list
    for item in inputlist:
        if item == '0' or item == '1':  # Makes sure it is only 0 or 1
            continue
        else:
            return False # If it is anything else it sends a false flag
    return True

def binarydecode(binary):
    binl = [char for char in binary]  # Splits binary into list
    binl.reverse()
    p = 0
    decimal = 0
    while p < len(binary):
        decimal = decimal + int(binl[p])*2**p # Adds the value of each digit moving from the first to last
        p+=1
    return decimal

def binaryencode(decimal):
    if decimal == 0:
        return '00000000'   # Handles the edge case of "0"
    num = 0        # Counter starts at 0
    decimal = int(decimal)  # Converts to something it can use
    output = [] # Creates an empty list for the output
    while 2**num <= decimal:  # Calculates the number of digits this number should be
        num+=1  
    num -=1    # Removes the last count so it gives an accurate number of how many digits the number should be
    while num != 0:
        if 2**num > decimal:
            output.append('0')  # If the power of 2 is more than the current decimal value this brings the power of 2 down by 1 and adds a 0 to indigate that digit should have a 0
            num -=1
        else:
            output.append('1')  # If the power of 2 is more than the current decimal value it subtracts it and adds a 1 to indicate that digit should be there
            decimal = decimal-(2**num)
            num -=1
    if decimal % 2 == 1:     # Adds the last digit on based on if it is odd or even
        output.append('1')
    else:
        output.append('0')
    while len(output) < 8:      # Makes sure the format is 8 digits
        output.insert(0,'0')
    return ''.join(output)  # Returns the joined list

def binary_calculator(bin1, bin2, operator):
    if checkforerror(bin1) == False:    # Runs the error checker on both of the inputs
        return 'Error'
    if checkforerror(bin2) == False:
        return 'Error'
    num1 = binarydecode(bin1)   # Uses the decode function so that it does the math in decimals rather than directly in binary
    num2 = binarydecode(bin2)
    if operator == '+':        # Does the function based on the operator type
        output =  (int(num1) + int(num2))
    if operator == '-':
        output = (int(num1) - int(num2))
    if operator == '*':
        output = (int(num1) * int(num2))
    if operator == '/':
        if int(num2) == 0: # Returns an error for dividing by zero
            return "NaN"
        output = int(int(num1) / int(num2))
    if output >= 0 and output < 256:
        return binaryencode(output)  # Makes sure its between 0 and 256
    else:
        return "Overflow"