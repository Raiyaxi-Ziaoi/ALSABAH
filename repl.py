
def main():  # Main function
    stack = []  # Stack
    registers = []  # Registers
    while True:  # Loop
        text = input("$> ")
        token = text.split(', ')  # Tokens split by ", "
        ftoken = token[0].replace('\n', '')  # Clean first token
        match ftoken:  # Match cleaned token
            case "REG":  # Create empty register
                registers.append('0')
            case "SET":  # Set register to value
                registers[(int)(token[1])] = token[2].replace("\"", "")
            case "OUT":  # Output contentes of register
                print(registers[(int)(token[1])])
            case "PSH":  # Push value to stack
                stack.append(token[1])
            case "ADD":  # Adds last two stack values
                result = (int)(stack[-1]) + (int)(stack[-2])
                stack.pop(-1)
                stack.pop(-1)
                stack.append(result)
            case "SUB":  # Subtracts last two stack values
                result = (int)(stack[-1]) - (int)(stack[-2])
                stack.pop(-1)
                stack.pop(-1)
                stack.append(result)
            case "MUL":  # Multiplies last two stack values
                result = (int)(stack[-1]) * (int)(stack[-2])
                stack.pop(-1)
                stack.pop(-1)
                stack.append(result)
            case "DIV":  # Divides last two stack values
                result = (int)(stack[-1]) / (int)(stack[-2])
                stack.pop(-1)
                stack.pop(-1)
                stack.append(result)
            case "MOD":  # Modulo operation on last two stack values
                result = (int)(stack[-1]) % (int)(stack[-2])
                stack.pop(-1)
                stack.pop(-1)
                stack.append(result)
            case "STS":  # Set register from stack
                registers[(int)(token[1])] = stack[-1]
                stack.pop(-1)
            case "INP":  # Takes input and stores in register
                registers[(int)(token[1])] = input()
            case "EXT":  # Exit
                break
            case other:
                print("Unknown operation! : " + token[0])


if __name__ == "__main__":
    main()
    input("Press enter to continue...")  # Catch to stop exit
