# Case Study 27: Advanced Numeric Pattern Generator (Hollow Diamond)

## 1. Problem Statement
Generate a hollow, symmetric numeric diamond pattern whose size is entered by the user. Each row shows its row number at the left and right edges, with spaces inside. The program must reject invalid sizes and keep the pattern perfectly aligned.

## 2. Objectives
- Use loops and string multiplication to build aligned patterns.
- Validate user input with a `while` loop, `isdigit()` and range checks.
- Build a list of row numbers and print the diamond from it.
- Understand how leading spaces and inner gaps are calculated.

## 3. Assumptions
- The size n is a whole number between 2 and 9 (so every row number is a single digit and the pattern stays aligned).
- Size n means n rows in the upper half; total rows = 2n - 1.
- Negative numbers, decimals, letters and empty input are invalid.

## 4. Algorithm
1. Repeat: read the size as text.
2. If the text is not made of digits, print an error and ask again.
3. Convert to an integer; if it is below 2 or above 9, print an error and ask again; otherwise stop asking.
4. Create a list `rows` containing 1..n followed by n-1..1.
5. For each row number i: start the line with (n - i) spaces and the digit i.
6. If i > 1, append (2i - 3) spaces and the digit i again.
7. Print the line.

## 5. Pseudocode
```text
START
  REPEAT
      READ text
      IF text is not all digits THEN PRINT error ; CONTINUE
      n = integer(text)
      IF n < 2 OR n > 9 THEN PRINT error ; CONTINUE
  UNTIL input is valid
  rows = empty list
  FOR i = 1 to n : add i to rows
  FOR i = n-1 down to 1 : add i to rows
  FOR each i in rows
      line = (n - i) spaces + i
      IF i > 1 THEN line = line + (2*i - 3) spaces + i
      PRINT line
STOP
```



## 6. Source Code
The complete, commented program is in [`hollow_diamond.py`](hollow_diamond.py).

To run it:
```bash
python hollow_diamond.py
```

## 7. Test Cases
| Test | Input / Scenario | Expected Result |
|------|------------------|-----------------|
| T1 | 4 | 7 rows: 1 / 2 2 / 3 3 / 4 4 / 3 3 / 2 2 / 1 (hollow diamond) |
| T2 | 5 | 9 rows, widest row `5       5` |
| T3 | 2 | 3 rows: 1 / 2 2 / 1 |
| T4 | abc | Invalid input message, asks again |
| T5 | 1 | Invalid size message (below 2) |
| T6 | 12 | Invalid size message (above 9) |
| T7 | -3 | Invalid input message (contains '-') |

## 8. Output
```text
Enter the diamond size (whole number from 2 to 9): abc
Invalid input: please enter a whole number (no letters, signs or decimals).
Enter the diamond size (whole number from 2 to 9): 12
Invalid size: it must be between 2 and 9.
Enter the diamond size (whole number from 2 to 9): 4

   1
  2 2
 3   3
4     4
 3   3
  2 2
   1
```



## 9. Explanation Notes (for viva / demo)
- Left spaces = n - i moves the number towards the centre; the gap between the two numbers is 2i - 3.
- `isdigit()` returns False for negative signs, decimals and letters.
- `range(n-1, 0, -1)` counts downwards for the bottom half.

## 10. Conclusion
The program prints a correctly aligned hollow numeric diamond for every valid size and politely rejects invalid input until a valid value is entered. It shows how nested logic, string repetition and validation loops work together. The same approach can be used for other patterns such as hollow triangles and hourglasses.
