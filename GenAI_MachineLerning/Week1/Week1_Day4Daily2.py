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
# Step 1: convert to 2D list
matrix = [list(row) for row in MATRIX_STR.strip().split('\n')]

rows = len(matrix)
cols = len(matrix[0])

result = []

# Step 2–3: read column by column + keep only letters/spaces
for c in range(cols):
    for r in range(rows):
        char = matrix[r][c]
        
        if char.isalpha():
            result.append(char)
        else:
            result.append(' ')   # replace symbols with space

# Step 4: join and clean extra spaces
decoded = ''.join(result)

# collapse multiple spaces into single space
final_message = ' '.join(decoded.split())

print(final_message)
