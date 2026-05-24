import string

MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%
'''

# Convert to matrix
matrix = [list(row) for row in MATRIX_STR.strip().split('\n')]

sentence = ''

# Read column by column
for col in range(len(matrix[0])):
    for row in range(len(matrix)):

        char = matrix[row][col]

        # Keep only letters and spaces
        if char.isalpha() or char == ' ':
            sentence += char

print(sentence)