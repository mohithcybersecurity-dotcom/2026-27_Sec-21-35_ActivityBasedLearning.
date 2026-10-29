# Case Study 48: Tuple-Based Employee Shift Conflict Detection

## 1. Problem Statement
Employee shifts are stored as tuples (employee, day, start, end). The program must find shifts of the same employee on the same day that overlap in time, ignore invalid shifts, and report the employees whose schedules conflict.

## 2. Objectives
- Represent records as tuples and unpack them.
- Convert time strings such as `09:30` into minutes using string slicing.
- Compare every pair of records with nested loops.
- Use the interval-overlap rule: `start1 < end2 and start2 < end1`.

## 3. Assumptions
- Times are written as `HH:MM` in 24-hour format.
- A shift must end after it starts and must stay within one day (overnight shifts are treated as invalid).
- Shifts that only touch (one ends exactly when the next begins) are NOT a conflict.
- Only shifts of the same employee on the same day can conflict.

## 4. Algorithm
1. Store the shifts as tuples.
2. For each shift, unpack it and convert start and end to minutes: `hours * 60 + minutes`.
3. If end <= start, print an invalid-shift message and skip it; otherwise store it in `valid`.
4. For every pair `i < j` in `valid`, check same employee, same day and overlap.
5. On a conflict print a message, increase the counter and remember the employee (once).
6. Print the summary.

## 5. Pseudocode
```text
START
  READ shifts (employee, day, start, end)
  valid = empty list
  FOR each shift
      start_min = hours(start) * 60 + minutes(start)
      end_min   = hours(end)   * 60 + minutes(end)
      IF end_min <= start_min THEN PRINT invalid
      ELSE add to valid
  conflicts = 0 ; conflicting_employees = empty list
  FOR i = 0 to n-1
      FOR j = i+1 to n-1
          IF same employee AND same day AND start_i < end_j AND start_j < end_i THEN
              conflicts = conflicts + 1
              PRINT conflict
              add employee to conflicting_employees if not present
  PRINT summary
STOP
```


## 6. Source Code
The complete, commented program is in [`shift_conflicts.py`](shift_conflicts.py).

To run it:
```bash
python shift_conflicts.py
```

## 7. Test Cases
| Test | Input / Scenario | Expected Result |
|------|------------------|-----------------|
| T1 | E101 Mon 09:00-17:00 and 16:00-20:00 | CONFLICT (overlap 16:00-17:00) |
| T2 | E102 Tue 13:00-18:00 and 17:30-21:00 | CONFLICT (overlap 17:30-18:00) |
| T3 | E103 Tue 08:00-12:00 and 12:00-16:00 | No conflict (shifts only touch) |
| T4 | E101 Mon 09:00-17:00 and E102 Mon 10:00-14:00 | No conflict (different employees) |
| T5 | E104 Wed 18:00-09:00 | Invalid shift ignored (end before start) |
| T6 | Whole data | 9 read, 8 valid, 2 conflicts, employees E101 and E102 |

## 8. Output
```text
VALIDATION
  Invalid shift ignored: E104 Wed 18:00-09:00 (end must be after start)

CONFLICT CHECK
  CONFLICT: E101 on Mon: 09:00-17:00 overlaps 16:00-20:00
  CONFLICT: E102 on Tue: 13:00-18:00 overlaps 17:30-21:00

SUMMARY
  Shifts read          : 9
  Valid shifts         : 8
  Conflicts found      : 2
  Employees in conflict: E101, E102
```



## 9. Explanation Notes (for viva / demo)
- `start[0:2]` gives the hour characters and `start[3:5]` gives the minute characters.
- Two intervals overlap when each starts before the other ends.
- The inner loop starts at `i + 1` so that each pair is checked only once.

## 10. Conclusion
The program converts times to minutes, detects both genuine overlaps, correctly ignores touching and different-employee shifts and rejects the invalid shift. The interval-overlap test is a reusable idea for timetables, room booking and meeting schedulers.
