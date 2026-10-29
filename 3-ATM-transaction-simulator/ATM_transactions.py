# Case Study 13: ATM Transaction Sequence Simulation
# Syllabus used: lists, tuples, tuple unpacking, loops, conditions

# ---------- Account rules ----------
opening_balance = 10000
PER_TXN_LIMIT = 5000       # maximum single withdrawal
DAILY_LIMIT = 10000        # maximum total withdrawals in a day
MIN_BALANCE = 500          # balance that must remain after withdrawal
NOTE_MULTIPLE = 100        # withdrawals must be multiples of 100

# ---------- Transactions ----------
# ("D" = deposit, "W" = withdrawal, amount)
transactions = [
    ("D", 3000), ("W", 2000), ("W", 6000), ("W", 1550), ("D", -500),
    ("X", 100),  ("W", 4000), ("W", 3500), ("D", 2500), ("W", 5000),
]

balance = opening_balance
withdrawn_today = 0
total_deposited = 0
accepted = 0
rejected = []          # list of (transaction number, type, amount, reason)

print(f"Opening balance: Rs. {balance}")
print("-" * 55)

number = 1
for txn in transactions:
    kind, amount = txn                      # tuple unpacking
    reason = ""                             # empty means "no problem"

    # ----- validation -----
    if kind != "D" and kind != "W":
        reason = "Invalid transaction type"
    elif amount <= 0:
        reason = "Amount must be positive"
    elif kind == "W":
        if amount % NOTE_MULTIPLE != 0:
            reason = "Amount must be a multiple of 100"
        elif amount > PER_TXN_LIMIT:
            reason = "Exceeds per-transaction limit"
        elif withdrawn_today + amount > DAILY_LIMIT:
            reason = "Exceeds daily withdrawal limit"
        elif balance - amount < MIN_BALANCE:
            reason = "Minimum balance would be violated"

    # ----- apply or reject -----
    if reason == "":
        if kind == "D":
            balance = balance + amount
            total_deposited = total_deposited + amount
        else:
            balance = balance - amount
            withdrawn_today = withdrawn_today + amount
        accepted = accepted + 1
        print(f"#{number:<2} {kind} {amount:>6}  ACCEPTED  balance = {balance}")
    else:
        rejected.append((number, kind, amount, reason))
        print(f"#{number:<2} {kind} {amount:>6}  REJECTED  ({reason})")
    number = number + 1

# ---------- Summary ----------
print()
print("TRANSACTION SUMMARY")
print("-" * 55)
print("Total transactions :", len(transactions))
print("Accepted           :", accepted)
print("Rejected           :", len(rejected))
print("Total deposited    : Rs.", total_deposited)
print("Total withdrawn    : Rs.", withdrawn_today)
print("Closing balance    : Rs.", balance)
if len(rejected) > 0:
    print()
    print("Rejected transactions:")
    for item in rejected:
        num, kind, amount, reason = item
        print(f"  #{num}: {kind} {amount} -> {reason}")
