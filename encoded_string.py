instr = input()
if any(c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/" for c in instr):
    print(-1)
else:
    binary_sequence = ''.join(format(ord(c), '08b') for c in instr)
    while len(binary_sequence) % 6 != 0:
        binary_sequence += '0'
    outstr = []
    for i in range(0, len(binary_sequence), 6):
        chunk = binary_sequence[i:i+6]
        decimal_value = int(chunk, 2)
        if decimal_value < 26:
            outstr.append(chr(ord('A') + decimal_value))
        elif decimal_value < 52:
            outstr.append(chr(ord('a') + decimal_value - 26))
        elif decimal_value < 62:
            outstr.append(chr(ord('0') + decimal_value - 52))
        elif decimal_value == 62:
            outstr.append('+')
        elif decimal_value == 63:
            outstr.append('/')
    print(''.join(outstr))
==========================================================

Consider a non-empty input string instr. Print the outstr which is the encoded value of instr as per the following rules:

• Input string can have alphabets, digits, '+' and '". Print-1 if instr contains any other characters

Starting from the leftmost character in instr, convert the ASCII value of each character into its 8-bit binary value and form a sequence of 8-bit binary values by joining them in their order of conversion

Divide the 8-bit sequence formed above into 6-bit binary chunks

Starting from the leftmost 6-bit chuck convert each 6-bit chunk to a decimal number and map the converted decimal number to a character as per the below character mapping and add them to outsr

• Character mapping->0-A, 1-B, 25-Z, 26-a 27-b..., 51

-z, 52-0,53-1,619, 62-+, 63-/

Append Os to the last chunk if it has less than 6 bits

Input Format:

Read the input string instr from the standard input stream.

Output Format:

Print the encoded string outstr or -1 accordingly to the standard output stresam.


Input Format

String with given values

Constraints

-

Output Format

As stated

Sample Input 0

ABC123+
Sample Output 0

QUJDMTIzKw
