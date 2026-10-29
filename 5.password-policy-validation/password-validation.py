# Case Study 29: Password Policy Validation Engine
# Syllabus used: strings, lists, loops, conditions

# ---------- Policy ----------
MIN_LENGTH = 8
MAX_LENGTH = 20
SPECIALS = "!@#$%^&*"
PROHIBITED = ["password", "1234", "qwerty", "admin"]

# ---------- Passwords to test ----------
passwords = [
    "Secure@2026",
    "short1!",
    "alllowercase1!",
    "ALLUPPER123!",
    "NoDigits@here",
    "NoSpecial2026",
    "My Pass@2026",
    "Baaa@2026x",
    "Admin@Pass99",
]

# let the user add one more password to test
custom = input("Enter your own password to test (or press Enter to skip): ")
if custom != "":
    passwords.append(custom)

for pw in passwords:
    failed = []     # explanation of every failed rule

    # Rule 1: length
    if len(pw) < MIN_LENGTH:
        failed.append("Too short (minimum " + str(MIN_LENGTH) + " characters)")
    if len(pw) > MAX_LENGTH:
        failed.append("Too long (maximum " + str(MAX_LENGTH) + " characters)")

    # Count character categories using a loop
    upper = 0
    lower = 0
    digit = 0
    special = 0
    space = 0
    for ch in pw:
        if ch.isupper():
            upper = upper + 1
        elif ch.islower():
            lower = lower + 1
        elif ch.isdigit():
            digit = digit + 1
        elif ch in SPECIALS:
            special = special + 1
        elif ch == " ":
            space = space + 1

    if upper == 0:
        failed.append("No uppercase letter")
    if lower == 0:
        failed.append("No lowercase letter")
    if digit == 0:
        failed.append("No digit")
    if special == 0:
        failed.append("No special character from " + SPECIALS)
    if space > 0:
        failed.append("Contains a space")

    # Rule: no character repeated 3 or more times in a row
    repeated = False
    for i in range(len(pw) - 2):
        if pw[i] == pw[i + 1] and pw[i + 1] == pw[i + 2]:
            repeated = True
    if repeated:
        failed.append("Same character repeated 3 or more times in a row")

    # Rule: prohibited words (ignoring upper/lower case)
    lowered = pw.lower()
    for word in PROHIBITED:
        if word in lowered:
            failed.append("Contains prohibited text '" + word + "'")

    # ----- report -----
    if len(failed) == 0:
        print(f"'{pw}' -> VALID")
    else:
        print(f"'{pw}' -> INVALID")
        for message in failed:
            print("      - " + message)

