# Case Study 42: Student Marks Matrix Analysis

## 1. Problem Statement
The marks of several students in several subjects are stored as a matrix (nested list). The program must calculate row-wise totals and averages, column-wise averages and maxima, identify top performers and detect subjects with low average performance.

## 2. Objectives
- Represent a table of data as a nested list and access `marks[row][column]`.
- Use nested loops to traverse rows and columns.
- Calculate row-wise and column-wise statistics.
- Identify toppers, low-average subjects and failing marks.

## 3. Assumptions
- 6 students and 5 subjects; each mark is out of 100.
- A subject is 'low performing' if its class average is below 66.
- A mark below 40 is a failing mark.
- If two students tie for a topper, the one listed first is reported.

## 4. Algorithm
1. Store subject names, student names and the marks matrix.
2. Using nested loops, print each student's marks and calculate the row total and average.
3. Using nested loops with the loop order reversed (column outside, row inside), calculate the average and highest mark of every subject.
4. Find the student with the largest total (overall topper).
5. For every subject find the student with the highest mark.
6. Print subjects whose average is below 66.
7. Print every mark below 40 with the student's name and subject.

## 5. Pseudocode
```text
START
  READ subjects, names, marks (nested list)
  FOR each row r
      row_total = 0
      FOR each column c
          PRINT marks[r][c] ; row_total = row_total + marks[r][c]
      store row_total ; PRINT total and average
  FOR each column c
      col_total = 0 ; best = marks[0][c]
      FOR each row r
          col_total = col_total + marks[r][c]
          IF marks[r][c] > best THEN best = marks[r][c]
      PRINT average and best
  topper = row with largest total ; PRINT
  FOR each column : find row with highest mark ; PRINT subject topper
  FOR each column : IF average < LOW_AVERAGE THEN PRINT subject
  FOR each r, c : IF marks[r][c] < FAIL_MARK THEN PRINT student and subject
STOP
```


## 6. Source Code
The complete, commented program is in [`marks_matrix_analysis.py`](marks_matrix_analysis.py).

To run it:
```bash
python marks_matrix_analysis.py
```

## 7. Test Cases
| Test | Input / Scenario | Expected Result |
|------|------------------|-----------------|
| T1 | Fatima: 92,85,90,98,88 | Total 453, average 90.6, overall topper |
| T2 | Charan: 45,40,52,60,55 | Total 252, average 50.4 |
| T3 | Physics column | Average 65.0, highest 92 (Bhavna): flagged as low average |
| T4 | Python column | Average 82.5, highest 98 (Fatima) |
| T5 | Eswar Physics = 38 | Listed under marks below 40 |
| T6 | Maths column | Average 70.8: not flagged |

## 8. Output
```text
Student      Maths  Physics     Chem   Python  English   Total  Average
--------------------------------------------------------------------
Anil            78       65       72       90       68     373     74.6
Bhavna          88       92       85       95       80     440     88.0
Charan          45       40       52       60       55     252     50.4
Divya           67       70       64       82       75     358     71.6
Eswar           55       38       42       70       60     265     53.0
Fatima          92       85       90       98       88     453     90.6
--------------------------------------------------------------------
Average       70.8     65.0     67.5     82.5     71.0
Highest         92       92       90       98       88

Overall topper : Fatima with total 453
Subject toppers:
  Maths   : Fatima (92)
  Physics : Bhavna (92)
  Chem    : Fatima (90)
  Python  : Fatima (98)
  English : Fatima (88)

Subjects with average below 66 :
  Physics (average 65.0)

Students with a mark below 40 :
  Eswar in Physics (38)
```



## 9. Explanation Notes (for viva / demo)
- `marks[r][c]`: r chooses the student (row), c chooses the subject (column).
- For column statistics the outer loop is the column and the inner loop is the row.
- `end=""` in `print` keeps the cursor on the same line.

## 10. Conclusion
The program successfully analysed the 6 x 5 matrix: Fatima is the overall topper, Physics is the only low-average subject and Eswar's Physics mark is the only failing mark. It shows how nested lists and nested loops make table-style analysis straightforward.
