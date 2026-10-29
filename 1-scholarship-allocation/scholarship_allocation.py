# Case Study 1: University Scholarship Allocation
# Syllabus used: lists, tuples, tuple unpacking, loops, conditions

# ---------- Policy (change these values to test other situations) ----------
MIN_AGGREGATE = 75      # minimum average marks (%)
MIN_SUBJECT = 50        # minimum marks needed in EVERY subject
MIN_ATTENDANCE = 75     # minimum attendance (%)
MAX_INCOME = 300000     # maximum yearly family income (Rs.)
QUOTA = 3               # number of scholarships available

# ---------- Applicant data ----------
# Each student is a tuple: (name, [subject marks], attendance %, family income)
students = [
    ("Asha",   [88, 92, 85, 90], 92, 250000),
    ("Bharat", [70, 80, 65, 75], 85, 180000),
    ("Chitra", [88, 92, 85, 90], 92, 200000),
    ("Deepak", [95, 35, 90, 92], 95, 150000),
    ("Esha",   [82, 78, 80, 84], 70, 120000),
    ("Farhan", [90, 85, 88, 86], 88, 450000),
    ("Gita",   [80, 82, 79, 81], 90, 280000),
]

# ---------- Step 1: Check eligibility ----------
eligible = []   # will store tuples: (name, aggregate, attendance, income)

print("ELIGIBILITY CHECK")
print("-" * 60)
for student in students:
    name, marks, attendance, income = student      # tuple unpacking

    # find total and lowest mark using a loop
    total = 0
    lowest = marks[0]
    for m in marks:
        total = total + m
        if m < lowest:
            lowest = m
    aggregate = total / len(marks)

    # collect every reason for rejection
    reasons = []
    if aggregate < MIN_AGGREGATE:
        reasons.append("aggregate below " + str(MIN_AGGREGATE))
    if lowest < MIN_SUBJECT:
        reasons.append("a subject below " + str(MIN_SUBJECT))
    if attendance < MIN_ATTENDANCE:
        reasons.append("attendance below " + str(MIN_ATTENDANCE))
    if income > MAX_INCOME:
        reasons.append("income above " + str(MAX_INCOME))

    if len(reasons) == 0:
        eligible.append((name, aggregate, attendance, income))
        print(f"{name:<8} -> ELIGIBLE (aggregate {aggregate:.2f})")
    else:
        print(f"{name:<8} -> NOT ELIGIBLE: " + "; ".join(reasons))

# ---------- Step 2: Rank eligible students (bubble sort) ----------
# Tie-break rules: 1) higher aggregate, 2) higher attendance,
#                  3) lower income, 4) name in alphabetical order
n = len(eligible)
for i in range(n - 1):
    for j in range(n - 1 - i):
        name1, agg1, att1, inc1 = eligible[j]
        name2, agg2, att2, inc2 = eligible[j + 1]
        key1 = (agg1, att1, -inc1)      # tuples compare item by item
        key2 = (agg2, att2, -inc2)
        swap = False
        if key1 < key2:
            swap = True
        elif key1 == key2 and name1 > name2:
            swap = True
        if swap:
            eligible[j], eligible[j + 1] = eligible[j + 1], eligible[j]

# ---------- Step 3: Display ranking and award scholarships ----------
print()
print("RANK LIST (quota = " + str(QUOTA) + ")")
print("-" * 60)
print(f"{'Rank':<6}{'Name':<10}{'Aggregate':<11}{'Attend.':<9}{'Income':<9}Result")
rank = 1
for entry in eligible:
    name, agg, att, inc = entry
    if rank <= QUOTA:
        result = "SCHOLARSHIP AWARDED"
    else:
        result = "Waiting list"
    print(f"{rank:<6}{name:<10}{agg:<11.2f}{att:<9}{inc:<9}{result}")
    rank = rank + 1

# ---------- Step 4: Report ties that were resolved ----------
for i in range(len(eligible) - 1):
    if eligible[i][1] == eligible[i + 1][1]:
        print()
        print("Tie on aggregate between " + eligible[i][0] + " and " +
              eligible[i + 1][0] + " resolved using attendance/income/name rules.")
