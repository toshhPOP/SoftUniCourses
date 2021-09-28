MORSE_CODE_DICT = {'.-': 'A', '-...': 'B',
                   '-.-.': 'C', '-..': 'D', '.': 'E',
                   '..-.': 'F', '--.': 'G', '....': 'H',
                   '..': 'I', '.---': 'J', '-.-': 'K',
                   '.-..': 'L', '--': 'M', '-.': 'N',
                   '---': 'O', '.--.': 'P', '--.-': 'Q',
                   '.-.': 'R', '...': 'S', '-': 'T',
                   '..-': 'U', '...-': 'V', '.--': 'W',
                   '-..-': 'X', '-.--': 'Y', '--..': 'Z'}
code = input().split()
for a in range(len(code)):
    if code[a] != " ":
        if code[a] == "|":
            code[a] = " "
        else:
            code[a] = MORSE_CODE_DICT[code[a]]
print("".join(code))
