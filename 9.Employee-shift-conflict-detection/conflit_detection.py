# Case Study 48: Tuple-Based Employee Shift Conflict Detection
# Syllabus used: tuples, tuple unpacking, lists, strings (slicing), loops

# Each shift is a tuple: (employee, day, start time, end time)
shifts = [
    ("E101", "Mon", "09:00", "17:00"),
    ("E102", "Mon", "10:00", "14:00"),
    ("E101", "Mon", "16:00", "20:00"),
    ("E103", "Tue", "08:00", "12:00"),
    ("E103", "Tue", "12:00", "16:00"),
    ("E102", "Tue", "13:00", "18:00"),
    ("E102", "Tue", "17:30", "21:00"),
    ("E101", "Wed", "09:00", "13:00"),
    ("E104", "Wed", "18:00", "09:00"),
]

# ---------- Step 1: validate shifts and convert times to minutes ----------
valid = []      # (employee, day, start minutes, end minutes, start text, end text)
print("VALIDATION")
for shift in shifts:
    emp, day, start, end = shift                    # tuple unpacking
    # "HH:MM" -> minutes after midnight, using string slicing
    start_min = int(start[0:2]) * 60 + int(start[3:5])
    end_min = int(end[0:2]) * 60 + int(end[3:5])
    if end_min <= start_min:
        print(f"  Invalid shift ignored: {emp} {day} {start}-{end} (end must be after start)")
    else:
        valid.append((emp, day, start_min, end_min, start, end))

# ---------- Step 2: compare every pair of shifts ----------
print()
print("CONFLICT CHECK")
conflict_count = 0
conflicting_employees = []

for i in range(len(valid)):
    for j in range(i + 1, len(valid)):
        emp1, day1, s1, e1, st1, en1 = valid[i]
        emp2, day2, s2, e2, st2, en2 = valid[j]
        # same employee, same day, and the time ranges overlap
        if emp1 == emp2 and day1 == day2 and s1 < e2 and s2 < e1:
            conflict_count = conflict_count + 1
            print(f"  CONFLICT: {emp1} on {day1}: {st1}-{en1} overlaps {st2}-{en2}")
            if emp1 not in conflicting_employees:
                conflicting_employees.append(emp1)

# ---------- Step 3: summary ----------
print()
print("SUMMARY")
print("  Shifts read          :", len(shifts))
print("  Valid shifts         :", len(valid))
print("  Conflicts found      :", conflict_count)
if len(conflicting_employees) == 0:
    print("  Employees in conflict: None")
else:
    print("  Employees in conflict:", ", ".join(conflicting_employees))
