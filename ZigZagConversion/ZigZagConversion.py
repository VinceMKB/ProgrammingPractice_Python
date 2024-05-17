def convert(s, rows):
    if rows <= 1:
        return s

    new_string = [''] * rows  # Initialize a list of empty strings
    j = 0
    direction = -1

    for i in range(len(s)):
        if j == rows - 1 or j == 0:
            direction *= -1
        new_string[j] += s[i]
        if direction == 1:
            j += 1
        else:
            j -= 1

    answer = ''.join(new_string)  # Concatenate all strings in the list
    return answer

# Test the function
s = "PAYPALISHIRING"
expected_output = "PAHNAPLSIIGYIR"
num_rows = 3

output = convert(s, num_rows)
print("This is the output string:", output)
print("ZigZagConversion")
