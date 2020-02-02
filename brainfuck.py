from __future__ import print_function
import sys, os

path = sys.argv[1]

if not os.path.exists(path):
    print("File not found")
    sys.exit()

fil = open(path, "r") #file
file = fil.read()
file = file.replace('\n', '')
fil.close()

tape = [0]
pointer = 0
fileptr = 0

while fileptr < len(file):

    if file[fileptr] == '+':
        tape[pointer] += 1
        if tape[pointer] > 255:
            tape[pointer] = 0

    elif file[fileptr] == '-':
        tape[pointer] -= 1
        if tape[pointer] < 0:
            tape[pointer] = 255

    elif file[fileptr] == '>':
        pointer += 1

    elif file[fileptr] == '<':
        if pointer <= 0:
            print("error: pointer must be bigger than 0")
            sys.exit()
        else:
            pointer -= 1

    elif file[fileptr] == '.':
        print(chr(tape[pointer]), end = '')

    elif file[fileptr] == ',':
        # tape[pointer] = ord(sys.stdin.read(1))
        input = raw_input("\nPlease enter a character: ")
        tape[pointer] = ord(input[0])

    elif file[fileptr] == '[':
        counter = 0
        if tape[pointer] == 0:
            for char in range(fileptr + 1, len(file)):
                if file[char] == '[':
                    counter += 1
                elif file[char] == ']':
                    if counter <= 0: # <= for if it miraculously skips 0
                        fileptr = char # no +1;happens automatically at the end
                        break
                    else: counter -= 1

    elif file[fileptr] == ']':
        counter = 0
        if not tape[pointer] == 0:
            for char in reversed(range(0, fileptr - 1)):
                if file[char] == ']':
                    counter += 1
                elif file[char] == '[':
                    if counter <= 0: # <= for if it miraculously skips 0
                        fileptr = char # no +1;happens automatically at the end
                        break
                    else: counter -= 1

    if pointer >= len(tape):
        tape.append(0)

    fileptr += 1

print("\n\n")
print("tape: ", tape)

print("Filename: " + path.split("/")[-1])
