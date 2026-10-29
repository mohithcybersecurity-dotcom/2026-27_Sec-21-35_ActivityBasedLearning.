# Case Study 2: Progressive Electricity Billing
# Syllabus used: lists, loops, conditions, operators, formatted output

# ---------- Tariff details ----------
FIXED_CHARGE = 50                 # Rs. added to every bill
slab_sizes = [100, 100, 100]      # first 100, next 100, next 100 units
slab_rates = [3.0, 4.5, 6.0]      # Rs. per unit in each slab
ABOVE_RATE = 8.0                  # Rs. per unit beyond 300 units
SURCHARGE_LIMIT = 400             # surcharge if units > 400
SURCHARGE_PERCENT = 10            # % of energy charge
REBATE_LIMIT = 100                # rebate if units <= 100
REBATE_PERCENT = 5                # % of energy charge
INCREASE_LIMIT = 30               # flag a bill rising by more than 30 %

# ---------- Consumption data ----------
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
units_list = [120, 135, 142, 230, 150, 160]

previous_bill = 0
highest_bill = 0
highest_month = ""

print(f"{'Month':<7}{'Units':>6}{'Energy':>10}{'Surchg':>9}{'Rebate':>8}{'Fixed':>7}{'Total':>10}  Change")
print("-" * 68)

for i in range(len(months)):
    month = months[i]
    units = units_list[i]

    # ----- slab-wise energy charge -----
    remaining = units
    energy = 0
    for k in range(3):
        if remaining > slab_sizes[k]:
            energy = energy + slab_sizes[k] * slab_rates[k]
            remaining = remaining - slab_sizes[k]
        else:
            energy = energy + remaining * slab_rates[k]
            remaining = 0
    if remaining > 0:                      # units beyond the 3 slabs
        energy = energy + remaining * ABOVE_RATE

    # ----- surcharge and rebate -----
    surcharge = 0
    rebate = 0
    if units > SURCHARGE_LIMIT:
        surcharge = energy * SURCHARGE_PERCENT / 100
    if units <= REBATE_LIMIT:
        rebate = energy * REBATE_PERCENT / 100

    total = energy + surcharge - rebate + FIXED_CHARGE

    # ----- compare with previous month -----
    if i == 0:
        remark = "-"
    else:
        change = (total - previous_bill) / previous_bill * 100
        if change > INCREASE_LIMIT:
            remark = f"+{change:.1f}%  UNUSUAL INCREASE"
        else:
            remark = f"{change:+.1f}%"

    print(f"{month:<7}{units:>6}{energy:>10.2f}{surcharge:>9.2f}{rebate:>8.2f}{FIXED_CHARGE:>7}{total:>10.2f}  {remark}")

    if total > highest_bill:
        highest_bill = total
        highest_month = month
    previous_bill = total

print("-" * 68)
print(f"Highest bill: Rs. {highest_bill:.2f} in {highest_month}")
