# Case Study 42: Student Marks Matrix Analysis
# Syllabus used: nested lists, loops, conditions, formatted output

subjects = ["Maths", "Physics", "Chem", "Python", "English"]
names = ["Anil", "Bhavna", "Charan", "Divya", "Eswar", "Fatima"]

# marks[row][column] -> row = student, column = subject
marks = [
    [78, 65, 72, 90, 68],
    [88, 92, 85, 95, 80],
    [45, 40, 52, 60, 55],
    [67, 70, 64, 82, 75],
    [55, 38, 42, 70, 60],
    [92, 85, 90, 98, 88],
]

LOW_AVERAGE = 66        # subject average below this is "low performance"
FAIL_MARK = 40          # a mark below this is a failure in that subject

rows = len(marks)
cols = len(subjects)

# ---------- Print the matrix with row-wise totals and averages ----------
print(f"{'Student':<9}", end="")
for s in subjects:
    print(f"{s:>9}", end="")
print(f"{'Total':>8}{'Average':>9}")
print("-" * 68)

totals = []
for r in range(rows):
    row_total = 0
    print(f"{names[r]:<9}", end="")
    for c in range(cols):
        print(f"{marks[r][c]:>9}", end="")
        row_total = row_total + marks[r][c]
    totals.append(row_total)
    print(f"{row_total:>8}{row_total / cols:>9.1f}")

# ---------- Column-wise statistics ----------
print("-" * 68)
col_averages = []
print(f"{'Average':<9}", end="")
for c in range(cols):
    col_total = 0
    for r in range(rows):
        col_total = col_total + marks[r][c]
    col_averages.append(col_total / rows)
    print(f"{col_total / rows:>9.1f}", end="")
print()

print(f"{'Highest':<9}", end="")
for c in range(cols):
    best = marks[0][c]
    for r in range(rows):
        if marks[r][c] > best:
            best = marks[r][c]
    print(f"{best:>9}", end="")
print()

# ---------- Top performers ----------
print()
top = 0
for r in range(rows):
    if totals[r] > totals[top]:
        top = r
print("Overall topper :", names[top], "with total", totals[top])

print("Subject toppers:")
for c in range(cols):
    best_row = 0
    for r in range(rows):
        if marks[r][c] > marks[best_row][c]:
            best_row = r
    print(f"  {subjects[c]:<8}: {names[best_row]} ({marks[best_row][c]})")

# ---------- Subjects with low average ----------
print()
print("Subjects with average below", LOW_AVERAGE, ":")
found = False
for c in range(cols):
    if col_averages[c] < LOW_AVERAGE:
        print(f"  {subjects[c]} (average {col_averages[c]:.1f})")
        found = True
if not found:
    print("  None")

# ---------- Students failing any subject ----------
print()
print("Students with a mark below", FAIL_MARK, ":")
found = False
for r in range(rows):
    for c in range(cols):
        if marks[r][c] < FAIL_MARK:
            print(f"  {names[r]} in {subjects[c]} ({marks[r][c]})")
            found = True
if not found:
    print("  None")
