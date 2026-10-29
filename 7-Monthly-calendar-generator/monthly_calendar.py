
# Case Study 37: Nested Loop Calendar Generator
# Syllabus used: input, strings, loops, conditions, formatted output

# ---------- Input with validation ----------
month_name = input("Enter month name and year (e.g. November 2026): ")

while True:
    text = input("Enter starting weekday (1=Mon, 2=Tue, ... 7=Sun): ")
    if text.isdigit() and 1 <= int(text) <= 7:
        start = int(text)
        break
    print("Invalid weekday. Enter a number from 1 to 7.")

while True:
    text = input("Enter number of days in the month (28 to 31): ")
    if text.isdigit() and 28 <= int(text) <= 31:
        days = int(text)
        break
    print("Invalid number of days. Enter a value from 28 to 31.")

# ---------- Print the calendar ----------
print()
print(month_name.center(28))
week_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
header = ""
for d in week_days:
    header = header + f"{d:>4}"
print(header)
print("-" * 28)

line = "    " * (start - 1)      # blank cells before the 1st day
column = start - 1              # how many cells are filled in this week
for day in range(1, days + 1):
    line = line + f"{day:>4}"
    column = column + 1
    if column == 7:             # week is full: print and start a new line
        print(line)
        line = ""
        column = 0
if line != "":                  # print the last (partial) week
    print(line)
