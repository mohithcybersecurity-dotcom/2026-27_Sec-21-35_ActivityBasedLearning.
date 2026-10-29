# Case Study 13: ATM Transaction Sequence Simulation

## 1. Problem Statement
Simulate an ATM account. A sequence of deposit and withdrawal requests is processed one by one. The program must maintain the balance, enforce withdrawal limits, reject invalid transactions with a reason, and print a transaction summary.

## 2. Objectives
- Process a list of transaction tuples using a loop and tuple unpacking.
- Validate each transaction with nested conditional statements.
- Maintain a running balance and daily withdrawal total.
- Produce a clear summary of accepted and rejected transactions.

## 3. Assumptions
- Opening balance = Rs. 10,000.
- Maximum single withdrawal = Rs. 5,000; maximum total withdrawals in a day = Rs. 10,000.
- A minimum balance of Rs. 500 must remain after any withdrawal.
- Withdrawals must be multiples of Rs. 100.
- Transaction type is 'D' (deposit) or 'W' (withdrawal); anything else is invalid.
- All transactions happen on the same day.

## 4. Algorithm
1. Set the opening balance and limits; store the transactions as `(type, amount)` tuples.
2. For each transaction, unpack `kind` and `amount` and set `reason = ""`.
3. Reject if the type is not D/W or the amount is not positive.
4. For withdrawals also check: multiple of 100, per-transaction limit, daily limit, minimum balance.
5. If no reason was found, update the balance (add for D, subtract for W) and the counters.
6. Otherwise store the rejected transaction with its reason.
7. After the loop, print totals, closing balance and the list of rejected transactions.

## 5. Pseudocode
```text
START
  balance = 10000 ; withdrawn_today = 0 ; accepted = 0
  FOR each (kind, amount) in transactions
      reason = ""
      IF kind is not D and not W THEN reason = "Invalid type"
      ELSE IF amount <= 0 THEN reason = "Amount must be positive"
      ELSE IF kind is W THEN
          IF amount mod 100 != 0 THEN reason = "Not multiple of 100"
          ELSE IF amount > PER_TXN_LIMIT THEN reason = "Per-transaction limit"
          ELSE IF withdrawn_today + amount > DAILY_LIMIT THEN reason = "Daily limit"
          ELSE IF balance - amount < MIN_BALANCE THEN reason = "Minimum balance"
      IF reason is empty THEN
          update balance, counters ; PRINT ACCEPTED
      ELSE
          store in rejected list ; PRINT REJECTED with reason
  PRINT summary and rejected list
STOP
```


## 6. Source Code
The complete, commented program is in [`atm_simulation.py`](atm_simulation.py).

To run it:
```bash
python atm_simulation.py
```

## 7. Test Cases
| Test | Input / Scenario | Expected Result |
|------|------------------|-----------------|
| T1 | D 3000 on balance 10000 | ACCEPTED, balance 13000 |
| T2 | W 2000 | ACCEPTED, balance 11000 |
| T3 | W 6000 | REJECTED: Exceeds per-transaction limit |
| T4 | W 1550 | REJECTED: Amount must be a multiple of 100 |
| T5 | D -500 | REJECTED: Amount must be positive |
| T6 | X 100 | REJECTED: Invalid transaction type |
| T7 | W 5000 after Rs. 9,500 already withdrawn | REJECTED: Exceeds daily withdrawal limit |
| T8 | Whole sequence | Accepted 5, Rejected 5, closing balance Rs. 6000 |

## 8. Output
```text
Opening balance: Rs. 10000
-------------------------------------------------------
#1  D   3000  ACCEPTED  balance = 13000
#2  W   2000  ACCEPTED  balance = 11000
#3  W   6000  REJECTED  (Exceeds per-transaction limit)
#4  W   1550  REJECTED  (Amount must be a multiple of 100)
#5  D   -500  REJECTED  (Amount must be positive)
#6  X    100  REJECTED  (Invalid transaction type)
#7  W   4000  ACCEPTED  balance = 7000
#8  W   3500  ACCEPTED  balance = 3500
#9  D   2500  ACCEPTED  balance = 6000
#10 W   5000  REJECTED  (Exceeds daily withdrawal limit)

TRANSACTION SUMMARY
-------------------------------------------------------
Total transactions : 10
Accepted           : 5
Rejected           : 5
Total deposited    : Rs. 5500
Total withdrawn    : Rs. 9500
Closing balance    : Rs. 6000

Rejected transactions:
  #3: W 6000 -> Exceeds per-transaction limit
  #4: W 1550 -> Amount must be a multiple of 100
  #5: D -500 -> Amount must be positive
  #6: X 100 -> Invalid transaction type
  #10: W 5000 -> Exceeds daily withdrawal limit
```



## 9. Explanation Notes (for viva / demo)
- `elif` is used so that only the first problem found is reported.
- `amount % 100 != 0` checks whether the amount is a multiple of 100.
- The `rejected` list stores tuples so they can be unpacked later in the summary.

## 10. Conclusion
The simulation processed all ten transactions correctly: five were accepted and five were rejected with the right reason, ending at Rs. 6000. It demonstrates validation logic, running totals and tuple unpacking. In a real ATM the same logic would be connected to a database and a card/PIN module.
