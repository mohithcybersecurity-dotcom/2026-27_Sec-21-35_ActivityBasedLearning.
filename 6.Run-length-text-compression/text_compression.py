# Case Study 35: Text Compression Using Character Runs
# Example: "aaabbc" -> "a3b2c1"
# Syllabus used: strings, loops, conditions, input

print("Run-Length Encoding (type 'exit' to stop)")

while True:
    text = input("\nEnter a string to compress: ")

    if text == "exit":
        break
    if text == "":
        print("Empty input. Please type something.")
        continue

    # digits would confuse the decoding, so they are not allowed
    has_digit = False
    for ch in text:
        if ch.isdigit():
            has_digit = True
    if has_digit:
        print("Digits are not allowed in the input. Try again.")
        continue

    # ----- build the encoded string -----
    encoded = ""
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count = count + 1                      # same character: extend run
        else:
            encoded = encoded + text[i - 1] + str(count)   # run ended
            count = 1
    encoded = encoded + text[len(text) - 1] + str(count)   # last run

    # ----- compare lengths -----
    print("Original string :", text, "(length", len(text), ")")
    print("Encoded string  :", encoded, "(length", len(encoded), ")")
    if len(encoded) < len(text):
        saved = len(text) - len(encoded)
        print("Compression is beneficial. Characters saved:", saved)
    else:
        print("Encoding is NOT beneficial. Keep the original string.")

