conv_type = input("Choose conversion type: decimal to binary(b), binary to decimal(d) ")
#while not(conv_type=="b") or not(conv_type=="d"):
#    conv_type = input("Type not recognized, type in 'b' or 'd': ")
if conv_type=='b':
    binary = input("Type in binary number that you want converted ")
    binary = int(binary,2)
    print(binary)

if conv_type=='d':
    decimal = input("Type in decimal number that you want converted ")
    decimal = int(decimal)
    print(bin(decimal))