#playing around with decimal and hexadecimal notations in python

def HexToDec (string):
    ret = 0
    hex = "0123456789ABCDEF"
    for i,d in enumerate(string) :
        value= hex.index(d) # 0 to 15
        power = (len(string) -(i+1)) #power of 16
        ret += (value*16**power)
    return ret


def DecToHex(dec):
    hex_str = ''
    hex_digits = ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F')
    rem = dec % 16

    while dec >= rem:
        remainder = dec % 16
        quotient = dec / 16
        if quotient == 0:
            hex_str += hex_digits[int(remainder)]
        else:
            hex_str += hex_digits[int(remainder)]
        dec = quotient
    if quotient > 0:
        hex_str += hex_digits[int(quotient)]
    return hex_str[::-1] # reverse the string

print(DecToHex(123422))
print('validation:', hex(123422))

print(HexToDec("1E21E"))



