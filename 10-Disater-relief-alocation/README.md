# Case Study 94: Disaster Relief Supply Allocation

## 1. Problem Statement
After a disaster, limited relief supplies must be distributed among affected areas. Each area has a priority and a requirement for each item. The program must serve areas in priority order, allocate as much as possible from the remaining stock, and report the remaining stock and the unmet demand.

## 2. Objectives
- Combine lists, nested lists and tuples in one program.
- Sort records by priority using a stable insertion sort.
- Allocate limited resources using a prescribed policy.
- Calculate shortages and remaining stock.

## 3. Assumptions
- Priority 1 is most urgent, 3 is least urgent.
- Areas with the same priority are served in the order in which they were listed.
- For each item an area receives either its full requirement or whatever stock is left.
- Four items are handled: food packets, water bottles, medical kits and blankets.
- Quantities are whole numbers.

## 4. Algorithm
1. Store item names, the stock list and the area tuples `(name, priority, needs)`.
2. Sort the areas by priority with insertion sort (a stable sort keeps the listed order for equal priority).
3. For each area (in sorted order) and for each item: if stock >= need, give the full need; otherwise give the remaining stock.
4. Reduce the stock, calculate the unmet quantity and add it to the item's total unmet demand.
5. Print the allocation for every area.
6. Print the remaining stock and total unmet demand of each item.

## 5. Pseudocode
```text
START
  READ items, stock list, areas (name, priority, needs)
  SORT areas by priority using insertion sort (stable)
  total_unmet = [0, 0, 0, 0]
  FOR each area in sorted order
      FOR each item k
          IF stock[k] >= needs[k] THEN given = needs[k]
          ELSE given = stock[k]
          stock[k] = stock[k] - given
          unmet = needs[k] - given
          total_unmet[k] = total_unmet[k] + unmet
          PRINT need, given, status
  FOR each item k
      PRINT stock[k] and total_unmet[k]
STOP
```

## 6. Source Code
The complete, commented program is in [`relief_allocation.py`](relief_allocation.py).

To run it:
```bash
python relief_allocation.py
```

## 7. Test Cases
| Test | Input / Scenario | Expected Result |
|------|------------------|-----------------|
| T1 | Priority order of areas | Town B, Camp D (both priority 1, listed order), Village A, Village C |
| T2 | Town B and Camp D | All four items fully met |
| T3 | Village A water: need 500, stock left 400 | Given 400, SHORT by 100 |
| T4 | Village A medical kits: need 60, stock left 50 | Given 50, SHORT by 10 |
| T5 | Village C food: need 250, stock left 100 | Given 100, SHORT by 150 |
| T6 | Summary | Remaining stock 0 for all items; unmet 150 food, 400 water, 60 medical, 70 blankets |

## 8. Output
```text
ALLOCATION (in priority order)
------------------------------------------------------------
Town B (priority 1)
   Food packets   need  400  given  400  fully met
   Water bottles  need  600  given  600  fully met
   Medical kits   need   80  given   80  fully met
   Blankets       need  150  given  150  fully met
Camp D (priority 1)
   Food packets   need  200  given  200  fully met
   Water bottles  need  500  given  500  fully met
   Medical kits   need   70  given   70  fully met
   Blankets       need  100  given  100  fully met
Village A (priority 2)
   Food packets   need  300  given  300  fully met
   Water bottles  need  500  given  400  SHORT by 100
   Medical kits   need   60  given   50  SHORT by 10
   Blankets       need  100  given  100  fully met
Village C (priority 3)
   Food packets   need  250  given  100  SHORT by 150
   Water bottles  need  300  given    0  SHORT by 300
   Medical kits   need   50  given    0  SHORT by 50
   Blankets       need  120  given   50  SHORT by 70

SUMMARY
------------------------------------------------------------
Food packets   remaining stock:    0   total unmet demand:  150
Water bottles  remaining stock:    0   total unmet demand:  400
Medical kits   remaining stock:    0   total unmet demand:   60
Blankets       remaining stock:    0   total unmet demand:   70
```



## 9. Explanation Notes (for viva / demo)
- Insertion sort uses `>` (not `>=`) so equal priorities keep their original order: that is what 'stable' means.
- `stock[k]` is updated inside the loop, so later areas see the reduced stock.
- The policy is 'serve in priority order': it is not an equal-share policy, so low-priority areas can get nothing.

## 10. Conclusion
The allocation respected the priority policy: the two urgent areas were fully served, Village A received a partial supply and Village C received the least. All stock was used and the unmet demand was reported exactly. The program shows how simple loops can support real planning decisions, and the policy could be changed to proportional sharing.
