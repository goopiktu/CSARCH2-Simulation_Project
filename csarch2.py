import re
#numbers = input("Enter number: ")

#print(f'{numbers}'.format(numbers=numbers))

numbers = "0.00111*2^5"

def sign(number):
    if number[0] == "-":
        return 1
    else:
        return 0

def exponent(exponent):
    e = exponent + 16383
    e = bin(e).replace("b","").replace("0","",1)
    return e


def fraction(fraction):
    frac = fraction.ljust(112, "0")
    return frac

#def base():

def normalizated_form_check(complete_form):
    
    if ((len(complete_form[0]) > 1 and complete_form[0][0] != "-") or (complete_form[0][0] == "-" and len(complete_form[0]) > 2 ) or complete_form[0].find("1") == -1):
        return False
    return True


def normalize_form(complete_form):
    
    if (complete_form[0].find("1") == -1): # if left side of the dot is only 0s
        first_one = complete_form[2].find("1")
        count = len(complete_form[2]) - first_one
        for i in range(count):
            first_char = complete_form[2][0]
            complete_form[2] = complete_form[2][1:]
            complete_form[6] = str(int(complete_form[6]) - 1)
            complete_form[0] = complete_form[0] + first_char
        complete_form[0] = complete_form[0][0] + complete_form[0][1:].lstrip("0") if complete_form[0][0] == "-" else complete_form[0].lstrip("0")


    else: #if there is 1 in the left side of the dot
        ind = complete_form[0].find("1") + 1
        count = len(complete_form[0]) - ind
        for i in range(count):
            last_char = complete_form[0][-1]
            complete_form[0] = complete_form[0][:-1]
            complete_form[2] = last_char + complete_form[2]
            complete_form[6] = str(int(complete_form[6]) + 1)
        
        complete_form[0] = complete_form[0][0] + complete_form[0][1:].lstrip("0") if complete_form[0][0] == "-" else complete_form[0].lstrip("0")
    return complete_form

    


def main(numbers, inputInBinary=True):
   
    result = {}
    split = re.split(r'(\.|\*|\^)', numbers)
    print("Split ", split)
    
    if (inputInBinary == True and normalizated_form_check(split) == False):
        print("Number is not in normalized form")
        normalize_form(split)
        print("Number after normalize: ", split)

    
    ex = exponent(int(split[-1]))
    frac = fraction(split[2])

    result["sign"] = sign(split[0])
    result["exponent"] = ex
    result["fraction"] = frac
    result["complete"] = f'{result["sign"]}{result["exponent"]}{result["fraction"]}'
    result["hex_complete"] = hex(int(result["complete"], 2))
    #enumerate result
    for key, value in result.items():
        print(f'{key}: {value}')

    return result



   


main(numbers)

