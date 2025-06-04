num = int(input("Enter a decimal number: "))

bin_num = bin(num)
oct_num = oct(num)
hex_num = hex(num)

print(f"Binary: {bin_num}\nOctal: {oct_num}\nHexadecimal: {hex_num}")
print("\n---\n")

# Defining manually
def dec_to_bin(n:int) -> str:

    if n == 0:

        return "0"

    result = []

    while n != 0:

        remainder = n % 2
        result.append(str(remainder))
        n //= 2

    result.reverse()
    return "".join(result)


def dec_to_oct(n:int) -> str:

    if n == 0:

        return "0"

    result = []

    while n != 0:

        remainder = n % 8
        result.append(str(remainder))
        n //= 8

    result.reverse()
    return "".join(result)


def dec_to_hex(n:int) -> str:

    if n == 0:

        return "0"

    result = []

    while n != 0:

        remainder = n % 16
        
        # Note: Try using a dict next time I look at this
        match remainder:

            case 10:

                result.append("A")

            case 11:

                result.append("B")

            case 12:

                result.append("C")

            case 13:

                result.append("D")

            case 14:

                result.append("E")

            case 15: 

                result.append("F")

            case _:

                result.append(str(remainder))

        n //= 16

    result.reverse()
    return "".join(result)
        

print(f"Binary: {dec_to_bin(num)}\nOctal: {dec_to_oct(num)}\nHexadecimal: {dec_to_hex(num)}")