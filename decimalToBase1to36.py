def deci236(num,base):
    try:
        num = int(num)
    except:
        return "Invalid Number"
    if type(num) != int or num < 0:
        return "Invalid Number"
    try:
        base = int(base)
    except:
        return "Invalid Base"
    if type(base) != int or base not in range(2,37):
        return "Invalid Base"

    decimalTo36Dict = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',16:'G',17:'H',18:'I',19:'J',20:'K',21:'L',22:'M',23:'N',24:'O',25:'P',26:'Q',27:'R',28:'S',29:'T',30:'U',31:'V',32:'W',33:'X',34:'Y',35:'Z'}
    numToConvert = num
    powersOfbase = [1]
    while powersOfbase[-1] <= numToConvert: # Creates a List of relevant powers of the base plus one extra
        powersOfbase.append(powersOfbase[-1] * base)
        
    powersOfbase = powersOfbase[:-1][::-1] # Removes the extra element and reverses the list
    remainder = 0
    baseNumber = ""
    for num in powersOfbase: # Iterates through all the powers of the base found prviously and computes the value in the new base
        remainder = numToConvert % num
        baseNumber = baseNumber + decimalTo36Dict[numToConvert//num]
        numToConvert = remainder
    return baseNumber

print("Welcome to the Base Conversion Machine")
while True:
    print("----------------------------------------------------------------------------")
    num = input("Enter the positive integer that you want to convert: ")
    base = input("Enter the base you want to convert to (2-36): ")
    print(f"The number {num} in base {base} is: {deci236(num,base)}")