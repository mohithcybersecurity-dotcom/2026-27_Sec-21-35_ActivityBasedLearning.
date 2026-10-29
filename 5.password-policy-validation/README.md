# Case Study 29: Password Policy Validation Engine

## 1. Problem Statement
Check passwords against a security policy covering length, character categories, repetition and prohibited words. For every password the program must say whether it is valid and, if not, explain each rule that failed.

## 2. Objectives
- Process strings character by character with loops.
- Use string methods `isupper()`, `islower()`, `isdigit()` and the `in` operator.
- Collect all failures in a list so that every broken rule is explained.
- Allow the user to test their own password.

## 3. Assumptions
- Length must be 8 to 20 characters.
- A valid password needs an uppercase letter, a lowercase letter, a digit and one special character from `!@#$%^&*`.
- Spaces are not allowed.
- The same character may not appear 3 or more times in a row.
- Prohibited text (ignoring case): password, 1234, qwerty, admin.

## 4. Algorithm
1. Store the policy, the sample passwords and optionally the user's password.
2. For each password create an empty `failed` list.
3. Check the length against the minimum and maximum.
4. Loop through the characters and count uppercase, lowercase, digits, specials and spaces.
5. Add a message to `failed` for each category that is missing (or for spaces that are present).
6. Check every position for three identical characters in a row.
7. Convert the password to lower case and check each prohibited word with `in`.
8. If `failed` is empty print VALID; otherwise print INVALID and every message.

## 5. Pseudocode
```text
START
  SET MIN_LENGTH, MAX_LENGTH, SPECIALS, PROHIBITED list
  passwords = sample list ; READ custom password ; add it if not empty
  FOR each pw in passwords
      failed = empty list
      IF length(pw) < MIN_LENGTH THEN add "too short"
      IF length(pw) > MAX_LENGTH THEN add "too long"
      upper = lower = digit = special = space = 0
      FOR each character ch in pw
          count its category
      IF upper = 0 THEN add "no uppercase" ... (same for lower, digit, special)
      IF space > 0 THEN add "contains space"
      FOR i = 0 to length-3
          IF pw[i] = pw[i+1] = pw[i+2] THEN repeated = true
      IF repeated THEN add "repeated characters"
      FOR each word in PROHIBITED
          IF word is inside lower-case pw THEN add "prohibited text"
      IF failed is empty THEN PRINT VALID
      ELSE PRINT INVALID and all messages
STOP
```


## 6. Source Code
The complete, commented program is in [`password_validator.py`](password_validator.py).

To run it:
```bash
python password_validator.py
```

## 7. Test Cases
| Test | Input / Scenario | Expected Result |
|------|------------------|-----------------|
| T1 | Secure@2026 | VALID |
| T2 | short1! | INVALID: too short; no uppercase |
| T3 | ALLUPPER123! | INVALID: no lowercase letter |
| T4 | NoDigits@here | INVALID: no digit |
| T5 | NoSpecial2026 | INVALID: no special character |
| T6 | My Pass@2026 | INVALID: contains a space |
| T7 | Baaa@2026x | INVALID: same character repeated 3 or more times |
| T8 | Admin@Pass99 | INVALID: contains prohibited text 'admin' |
| T9 | (custom) Zebra@2026Zebra@2026 | VALID (exactly 20 characters) |

## 8. Output
```text
Enter your own password to test (or press Enter to skip): 
'Secure@2026' -> VALID
'short1!' -> INVALID
      - Too short (minimum 8 characters)
      - No uppercase letter
'alllowercase1!' -> INVALID
      - No uppercase letter
      - Same character repeated 3 or more times in a row
'ALLUPPER123!' -> INVALID
      - No lowercase letter
'NoDigits@here' -> INVALID
      - No digit
'NoSpecial2026' -> INVALID
      - No special character from !@#$%^&*
'My Pass@2026' -> INVALID
      - Contains a space
'Baaa@2026x' -> INVALID
      - Same character repeated 3 or more times in a row
'Admin@Pass99' -> INVALID
      - Contains prohibited text 'admin'
```



## 9. Explanation Notes (for viva / demo)
- All failed rules are collected first and printed together, so the user sees every problem at once.
- `word in lowered` checks for a substring; lower-casing makes the check case-insensitive.
- The repeat check stops at `len(pw) - 2` so that `pw[i+2]` never goes out of range.

## 10. Conclusion
The validator accepts strong passwords and gives a precise explanation for each weak one, including passwords that break several rules at once. It reinforces string traversal and conditional logic. It can be extended with more rules such as checking for the user's name or for keyboard sequences.
