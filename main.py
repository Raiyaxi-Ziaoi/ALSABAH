
def main():
    text = []
    stack = []
    registers = []
    sp = 0
    ip = 0
    print("Please enter a filename: ")
    with open(input(), "r") as f:
        text = f.readlines()
    while True:
        token = text[ip].split(' ')
        ftoken = token[0].replace('\n', '')
        match ftoken:
            case "PSH":
                stack.append(token[1])
            case "ARG":
                registers.append(0)
            case "MRG":
                for x in range((int)(token[1])):
                    registers.append(0)
            case "PLL":
                stack.append(registers[(int)(token[1])])
            case "SET":
                registers[(int)(token[1])] = stack[(int)(token[2])]
            case "MOV":
                registers[(int)(token[1])] = registers[(int)(token[2])]
                registers[(int)(token[1])] = 0
            case "HLD":
                registers[(int)(token[1])] = token[2]
            case "POP":
                stack.pop(-1)
            case "ADD":
                result = (int)(stack[-1]) + (int)(stack[-2])
                stack.pop(-1)
                stack.pop(-1)
                stack.append(result)
            case "SUB":
                result = (int)(stack[-1]) - (int)(stack[-2])
                stack.pop(-1)
                stack.pop(-1)
                stack.append(result)
            case "MUL":
                result = (int)(stack[-1]) * (int)(stack[-2])
                stack.pop(-1)
                stack.pop(-1)
                stack.append(result)
            case "DIV":
                result = (int)(stack[-1]) / (int)(stack[-2])
                stack.pop(-1)
                stack.pop(-1)
                stack.append(result)
            case "LOG":
                print(stack[(int)(token[1])])
            case "CHP":
                print(chr((int)(stack[(int)(token[1])])), end="")
            case "RGP":
                print(chr((int)(registers[(int)(token[1])])), end="")
            case "HLT":
                print()
                break
            case "PSS":
                print("", end="")
            case "JMP":
                ip = (int)(token[1]) - 2
            case "IF?":
                if registers[(int)(token[1])] == 1:
                    ip = (int)(token[2]) - 2
            case "INC":
                registers[(int)(token[1])] += 1
            case "INP":
                registers[(int)(token[1])] = (int)(input())
            case other:
                print("Unknown operation! : " + token[0])
        if ip < len(text):
            ip += 1
        else:
            return


if __name__ == "__main__":
    main()
    input("Press enter to continue...")
