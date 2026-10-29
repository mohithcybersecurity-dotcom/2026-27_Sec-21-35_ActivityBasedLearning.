# Case Study 35: Text Compression Using Character Runs (Run-Length Encoding)

## 1. Problem Statement
Compress a string by replacing every run of identical consecutive characters with the character followed by the run length (for example `aaabbc` becomes `a3b2c1`). The program must compare the original and encoded lengths and say when encoding is not beneficial.

## 2. Objectives
- Traverse a string with indexes and compare neighbouring characters.
- Build a new string using concatenation.
- Compare lengths and make a decision.
- Handle special cases: empty input, single characters, strings with no repeats.

## 3. Assumptions
- The input text contains no digits (digits would make decoding ambiguous).
- Upper-case and lower-case letters are different characters.
- The program repeats until the user types `exit`.
- Encoding is beneficial only if the encoded string is strictly shorter.

## 4. Algorithm
1. Read a string; stop if it is `exit`; reject empty strings and strings containing digits.
2. Set `encoded = ""` and `count = 1`.
3. For i from 1 to length-1: if `text[i]` equals `text[i-1]` add 1 to count; otherwise append `text[i-1]` and count to `encoded` and reset count to 1.
4. After the loop append the last character and its count.
5. Compare lengths and print whether compression is beneficial.

## 5. Pseudocode
```text
START
  REPEAT
      READ text
      IF text = "exit" THEN STOP
      IF text is empty THEN print message ; CONTINUE
      IF text has a digit THEN print message ; CONTINUE
      encoded = "" ; count = 1
      FOR i = 1 to length(text) - 1
          IF text[i] = text[i-1] THEN count = count + 1
          ELSE
              encoded = encoded + text[i-1] + count
              count = 1
      encoded = encoded + last character + count
      PRINT original, encoded, lengths
      IF length(encoded) < length(text) THEN PRINT "beneficial"
      ELSE PRINT "NOT beneficial"
  UNTIL user types exit
STOP
```


## 6. Source Code
The complete, commented program is in [`run_length_encoding.py`](run_length_encoding.py).

To run it:
```bash
python run_length_encoding.py
```

## 7. Test Cases
| Test | Input / Scenario | Expected Result |
|------|------------------|-----------------|
| T1 | aaabbc | a3b2c1 (6 vs 6): NOT beneficial |
| T2 | abcd | a1b1c1d1 (4 vs 8): NOT beneficial |
| T3 | zzzzzzzz | z8 (8 vs 2): beneficial, 6 characters saved |
| T4 | A | A1 (1 vs 2): NOT beneficial |
| T5 | ab12 | Digits are not allowed message |
| T6 | (just press Enter) | Empty input message |
| T7 | exit | Program ends |

## 8. Output
```text
Run-Length Encoding (type 'exit' to stop)

Enter a string to compress: aaabbc
Original string : aaabbc (length 6 )
Encoded string  : a3b2c1 (length 6 )
Encoding is NOT beneficial. Keep the original string.

Enter a string to compress: abcd
Original string : abcd (length 4 )
Encoded string  : a1b1c1d1 (length 8 )
Encoding is NOT beneficial. Keep the original string.

Enter a string to compress: zzzzzzzz
Original string : zzzzzzzz (length 8 )
Encoded string  : z8 (length 2 )
Compression is beneficial. Characters saved: 6

Enter a string to compress: ab12
Digits are not allowed in the input. Try again.

Enter a string to compress: exit
```



## 9. Explanation Notes (for viva / demo)
- A run ends when the current character differs from the previous one; that is when we write the previous character and its count.
- The last run is written after the loop because the loop never sees a 'next different' character.
- Run-length encoding works best on data with long repeated sections.

## 10. Conclusion
The program correctly encodes repeated characters and honestly reports when the 'compressed' string is no shorter, as in `abcd` and `aaabbc`. It is a good example of how a simple loop can implement a real data-compression idea.
