# Case Study 2: Progressive Electricity Billing

## 1. Problem Statement
A household electricity bill is calculated using progressive slabs (higher rates for higher consumption), a fixed charge, a surcharge for very high usage and a rebate for very low usage. The bills of several months must be compared and any unusually large increase must be flagged.

## 2. Objectives
- Implement slab-wise (progressive) charge calculation using loops.
- Apply a surcharge and a rebate using conditional statements.
- Compare each month's bill with the previous month and calculate the percentage change.
- Identify the month with the highest bill and flag unusual increases.

## 3. Assumptions
- Slabs: first 100 units at Rs. 3.00, next 100 at Rs. 4.50, next 100 at Rs. 6.00, above 300 at Rs. 8.00 per unit.
- Fixed charge = Rs. 50 per month.
- Surcharge = 10 % of energy charge if units > 400.
- Rebate = 5 % of energy charge if units <= 100.
- An increase of more than 30 % over the previous month is 'unusual'.
- Consumption data for six months is stored in a list.

## 4. Algorithm
1. Store tariff constants, month names and the units consumed in each month.
2. For each month, set `remaining = units` and `energy = 0`.
3. For each of the three slabs: if `remaining` is more than the slab size, charge the full slab and reduce `remaining`; otherwise charge `remaining` units and set it to 0.
4. Charge any leftover units at the above-300 rate.
5. Calculate surcharge (units > 400) and rebate (units <= 100).
6. Total = energy + surcharge - rebate + fixed charge.
7. From the second month onward, calculate percentage change from the previous bill and flag it if above 30 %.
8. Track the highest bill and print it at the end.

## 5. Pseudocode
```text
START
  SET slab sizes, slab rates, ABOVE_RATE, FIXED_CHARGE, limits
  READ months and units list
  previous_bill = 0 ; highest_bill = 0
  FOR each month
      remaining = units ; energy = 0
      FOR each of the 3 slabs
          IF remaining > slab size THEN
              energy = energy + slab size * slab rate
              remaining = remaining - slab size
          ELSE
              energy = energy + remaining * slab rate
              remaining = 0
      IF remaining > 0 THEN energy = energy + remaining * ABOVE_RATE
      IF units > 400 THEN surcharge = 10% of energy
      IF units <= 100 THEN rebate = 5% of energy
      total = energy + surcharge - rebate + FIXED_CHARGE
      IF not first month THEN
          change = (total - previous_bill) / previous_bill * 100
          IF change > 30 THEN flag UNUSUAL INCREASE
      IF total > highest_bill THEN update highest bill and month
      previous_bill = total
  PRINT highest bill
STOP
```



## 6. Source Code
The complete, commented program is in [`electricity_billing.py`](electricity_billing.py).

To run it:
```bash
python electricity_billing.py
```

## 7. Test Cases
| Test | Input / Scenario | Expected Result |
|------|------------------|-----------------|
| T1 | Units = 50 | Energy 150.00, rebate 7.50, total Rs. 192.50 |
| T2 | Units = 100 | Energy 300.00, rebate 15.00, total Rs. 335.00 |
| T3 | Units = 150 | Energy 525.00, no rebate, total Rs. 575.00 |
| T4 | Units = 250 | Energy 1050.00, total Rs. 1100.00 |
| T5 | Units = 450 | Energy 2550.00, surcharge 255.00, total Rs. 2855.00 |
| T6 | Default data: Mar 142 units, Apr 230 units | April bill 980.00 is +81.8 % : UNUSUAL INCREASE |
| T7 | Default data: May 150 units after April | -41.3 % (decrease, not flagged) |

## 8. Output
```text
Month   Units    Energy   Surchg  Rebate  Fixed     Total  Change
--------------------------------------------------------------------
Jan       120    390.00     0.00    0.00     50    440.00  -
Feb       135    457.50     0.00    0.00     50    507.50  +15.3%
Mar       142    489.00     0.00    0.00     50    539.00  +6.2%
Apr       230    930.00     0.00    0.00     50    980.00  +81.8%  UNUSUAL INCREASE
May       150    525.00     0.00    0.00     50    575.00  -41.3%
Jun       160    570.00     0.00    0.00     50    620.00  +7.8%
--------------------------------------------------------------------
Highest bill: Rs. 980.00 in Apr
```


## 9. Explanation Notes (for viva / demo)
- The loop runs once per slab and uses `remaining` to track units not yet charged.
- Percentage change = (new - old) / old x 100.
- The rebate and surcharge are calculated on the energy charge only, not on the fixed charge.

## 10. Conclusion
The program calculates progressive bills correctly for every slab boundary, applies the rebate and surcharge rules and detects the sudden jump in April. Hand calculation and program results agree for all test values. The same slab-loop idea can be reused for water tariffs, income tax and courier charges.
