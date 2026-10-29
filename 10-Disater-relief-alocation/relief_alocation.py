
# Case Study 94: Disaster Relief Supply Allocation
# Policy: areas are served in priority order (1 = most urgent).
#         Areas with the same priority are served in the order listed.
#         Each area gets as much of its need as the remaining stock allows.
# Syllabus used: lists, nested lists, tuples, tuple unpacking, loops, conditions

items = ["Food packets", "Water bottles", "Medical kits", "Blankets"]
stock = [1000, 1500, 200, 400]            # available quantity of each item

# Each area is a tuple: (name, priority, [needs of each item])
areas = [
    ("Village A", 2, [300, 500, 60, 100]),
    ("Town B",    1, [400, 600, 80, 150]),
    ("Village C", 3, [250, 300, 50, 120]),
    ("Camp D",    1, [200, 500, 70, 100]),
]

# ---------- Step 1: sort areas by priority (insertion sort, stable) ----------
for i in range(1, len(areas)):
    current = areas[i]
    j = i - 1
    while j >= 0 and areas[j][1] > current[1]:
        areas[j + 1] = areas[j]
        j = j - 1
    areas[j + 1] = current

# ---------- Step 2: allocate supplies ----------
print("ALLOCATION (in priority order)")
print("-" * 60)
total_unmet = [0, 0, 0, 0]

for area in areas:
    name, priority, needs = area                  # tuple unpacking
    print(f"{name} (priority {priority})")
    for k in range(len(items)):
        if stock[k] >= needs[k]:
            given = needs[k]
        else:
            given = stock[k]                      # give whatever is left
        stock[k] = stock[k] - given
        unmet = needs[k] - given
        total_unmet[k] = total_unmet[k] + unmet
        status = "fully met" if unmet == 0 else "SHORT by " + str(unmet)
        print(f"   {items[k]:<14} need {needs[k]:>4}  given {given:>4}  {status}")

# ---------- Step 3: summary ----------
print()
print("SUMMARY")
print("-" * 60)
for k in range(len(items)):
    print(f"{items[k]:<14} remaining stock: {stock[k]:>4}   total unmet demand: {total_unmet[k]:>4}")
