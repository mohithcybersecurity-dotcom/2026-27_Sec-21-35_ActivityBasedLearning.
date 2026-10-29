# Case Study 37: Nested Loop Calendar Generator

## 1. Problem Statement
Print a formatted monthly calendar when the starting weekday and the number of days in the month are given. Dates must be aligned under the weekday names, weeks must break correctly after Sunday, and invalid inputs must be rejected.

## 2. Objectives
- Use loops with a column counter to arrange data in rows and columns.
- Format text using right alignment and string multiplication.
- Validate numeric input with `while` loops.
- Handle a partial first and last week.

## 3. Assumptions
- Weeks run from Monday (1) to Sunday (7).
- The month has 28 to 31 days (the user supplies the value, so leap years are the user's responsibility).
- Each calendar cell is 4 characters wide.

## 4. Algorithm
1. Read the month title, the starting weekday (1-7) and the number of days (28-31), repeating until the numbers are valid.
2. Print the centred title and the weekday header.
3. Create `line` with (start - 1) blank cells and set `column = start - 1`.
4. For each day from 1 to days: add the day number to `line` in a 4-wide cell and increase `column`.
5. When `column` becomes 7, print the line and reset `line` and `column`.
6. After the loop, print the last incomplete line if it is not empty.

## 5. Pseudocode
```text
START
  READ month_name
  REPEAT READ start UNTIL 1 <= start <= 7
  REPEAT READ days  UNTIL 28 <= days <= 31
  PRINT month_name centred
  PRINT weekday header (Mon ... Sun)
  line = (start - 1) blank cells
  column = start - 1
  FOR day = 1 to days
      line = line + day (width 4)
      column = column + 1
      IF column = 7 THEN
          PRINT line
          line = "" ; column = 0
  IF line is not empty THEN PRINT line
STOP
```


## 6. Source Code
The complete, commented program is in [`calendar_generator.py`](calendar_generator.py).

To run it:
```bash
python calendar_generator.py
```

## 7. Test Cases
| Test | Input / Scenario | Expected Result |
|------|------------------|-----------------|
| T1 | November 2026, weekday 7 (Sunday), 30 days | 1 appears under Sun; last row contains only 30 under Mon |
| T2 | February 2026, weekday 7, 28 days | Last row is 23 to 28 (ends on Saturday); no extra empty row |
| T3 | Weekday 0 | Invalid weekday message, asks again |
| T4 | Weekday 9 | Invalid weekday message, asks again |
| T5 | Days 40 | Invalid number of days message, asks again |
| T6 | Weekday 1 (Mon), 31 days | First row starts with 1 under Mon; 5 full weeks + partial week |

## 8. Output
```text
Enter month name and year (e.g. November 2026): November 2026
Enter starting weekday (1=Mon, 2=Tue, ... 7=Sun): 7
Enter number of days in the month (28 to 31): 30

       November 2026        
 Mon Tue Wed Thu Fri Sat Sun
----------------------------
                           1
   2   3   4   5   6   7   8
   9  10  11  12  13  14  15
  16  17  18  19  20  21  22
  23  24  25  26  27  28  29
  30
```



## 9. Explanation Notes (for viva / demo)
- `column` counts how many cells the current line has; 7 means the week is complete.
- `f"{day:>4}"` right-aligns the number in 4 characters so single and double digits line up.
- `"    " * (start - 1)` creates the empty cells before the first date.

## 10. Conclusion
The generator produces a neatly aligned calendar for any valid weekday/month-length combination and handles partial first and last weeks. It demonstrates formatted output and counter-controlled loops, the same technique used for tables, seating charts and timetables.
