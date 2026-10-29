Case Study 27: Advanced Numeric Pattern Generator
# Hollow numeric diamond with input validation
# Syllabus used: input, strings, loops, nested loops, conditions

# ---------- Input with validation ----------
while True:
    text = input("Enter the diamond size (whole number from 2 to 9): ")
    if not text.isdigit():
        print("Invalid input: please enter a whole number (no letters, signs or decimals).")
        continue
    n = int(text)
    if n < 2 or n > 9:
        print("Invalid size: it must be between 2 and 9.")
        continue
    break

# ---------- Decide which number each row prints ----------
# Rows go 1,2,...,n then n-1,...,1
rows = []
for i in range(1, n + 1):
    rows.append(i)
for i in range(n - 1, 0, -1):
    rows.append(i)

# ---------- Print the pattern ----------
print()
for i in rows:
    line = " " * (n - i) + str(i)            # leading spaces + left number
    if i > 1:
        line = line + " " * (2 * i - 3) + str(i)   # hollow gap + right number
    print(line)

