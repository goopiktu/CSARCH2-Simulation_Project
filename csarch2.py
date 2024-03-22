import re

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

def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0.0*2^0"
    
    sign = "-" if decimal_num < 0 else ""
    decimal_num = abs(decimal_num)
    
    integer_part = int(decimal_num)
    fractional_part = decimal_num - integer_part
    
    integer_binary = bin(integer_part).replace("0b", "")
    
    fractional_binary = ""
    while fractional_part != 0:
        fractional_part *= 2
        if fractional_part >= 1:
            fractional_binary += "1"
            fractional_part -= 1
        else:
            fractional_binary += "0"
    
    exponent = len(integer_binary) - 1
    
    binary_num = f"{sign}{integer_binary}.{fractional_binary}*2^{exponent}"
    return binary_num

def main(numbers, inputInBinary=True):
    result = {}
    
    if not inputInBinary:
        numbers = decimal_to_binary(float(numbers))
    
    split = re.split(r'(\.|\*|\^)', numbers)
    print("Split ", split)
    
    if (normalizated_form_check(split) == False):
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
    
    for key, value in result.items():
        print(f'{key}: {value}')

    return result

# Example usage
binary_input = "0.00111*2^5"
main(binary_input)

print("\n")

decimal_input = "3.875"
main(decimal_input, inputInBinary=False)