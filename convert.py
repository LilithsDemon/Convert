def convertDtoB(denary):
    found = False
    count = 0
    while found == False:
        if(denary >= 2**count):
            count = count + 1
        else:
            found = True
    binary_value = ""
    for i in range(count):
        if(denary >= 2**(count-(i+1))):
            binary_value = binary_value + "1"
            denary = denary - (2**(count-(i+1)))
        else:
            binary_value = binary_value + "0"
    return binary_value

def convertBtoD(binary):
    denary = 0
    for i in range(len(binary)):
        if (binary[i] == "1"):
            denary = denary + (2**(len(binary)-(i + 1)))
    return denary


if __name__ == "__main__":
    denary_input = input("What value would you like to input: ")
    val = convertDtoB(int(denary_input))
    print (val)
