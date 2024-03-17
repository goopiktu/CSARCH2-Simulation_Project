import re
#numbers = input("Enter number: ")

#print(f'{numbers}'.format(numbers=numbers))

numbers = "-1.00111*2^5"

def sign(sign):
    if(sign == "+"):
        return 0
    return 1


def exponent(exponent):
    e = exponent + 16383
    e = bin(e).replace("b","").replace("0","",1)
    return e


def fraction(fraction):
    frac = fraction.ljust(112, "0")
    return frac

#def base():


def main():
   

    split = re.split(r'(\.|\*|\^)', numbers)

    ex = exponent(int(split[-1]))
    frac = fraction(split[2])
    print("fraction:" + frac)
    print("exponent:" + ex)
    print(str(split))



main()

