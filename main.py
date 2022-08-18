
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
        token = text[ip].split(', ')
        ftoken = token[0].replace('\n', '')
        match ftoken:
            case "REG":
                registers.append('0')
            case "SET":
                registers[(int)(token[1])] = token[2].replace("\"", "")
            case "OUT":
                print(registers[(int)(token[1])])
            case "EXT":
                break
            case other:
                print("Unknown operation! : " + token[0])
        if ip < len(text):
            ip += 1
        else:
            return


if __name__ == "__main__":
    main()
    input("Press enter to continue...")
