# AI Code Review Assignment (Python)

## Candidate
- Name: Raymond Munguti
- Approximate time spent: 

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- Wrong denominator: Divides total revenue from non-cancelled rders by total orders (including cancelled), producing incorrect average.
- Empty List: len(orders) = 0 triggers ZeroDivisionError
- All Cancelled Orders: Returns misleading 0.0 (total=0, count>0) instead of error or None.

### Edge cases & risks
- Empty orders list: Triggers ZeroDivisionError (division by len(orders) = 0).

- All cancelled orders: Returns misleading 0 (sums to total=0 but divides by non-zero total count).

- Missing keys: Raises KeyError when "status" or "amount" absent from order dicts.

- Non-numeric amounts: Causes TypeError during addition (total += order["amount"]).

- Negative amounts: Processes successfully but may violate business rules.

- Malformed orders: Fails with TypeError or AttributeError on non-dict items.

### Code quality / design issues
- Lacks type hints,docstring and input validation for orders list.
- Assumes dictionary structure without checks for missing "status" or "amount" keys.
- Variable count misleadingly includes cancelled orders instead of tracking only valid ones.
- Code uses an inefficient manual loop.


## 2) Proposed Fixes / Improvements
### Summary of changes
- Add error handling for missing keys and invalid data types
- Consistent return: Always 0.0 for empty/no-valid-orders
- Clear docstring: Precise args/returns/raises documentation
- Graceful skipping: Invalid orders skipped instead of raising errors
- Loop → Filtered collection: Manual loop replaced with cleaner validation + collection

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

- Empty list: Returns 0.0 (graceful handling)

- All cancelled: Returns 0.0 (no valid orders found)

- Mixed statuses: Correctly averages only non-cancelled orders

- Missing keys: Skips invalid orders silently (no crash)

- Invalid types: Non-numeric amounts and non-dict items skipped

- Single order: Works correctly for edge case of one valid order

- Boundary values: Handles zero, negative, and large amounts correctly

- Performance: Scales with varying list sizes (no intermediate list allocation)


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- Claims "dividing by the number of orders" but code divides by total count including cancelled, misstating the logic; says "correctly excludes cancelled orders" but only excludes from sum, not average properly.

### Rewritten explanation
- This function calculates the average order value by summing amounts from non-cancelled orders and dividing by the count of non-cancelled orders (not total orders). It returns 0 when there are no valid orders to average. The function validates that orders contain required fields and handles edge cases like empty input.

## 4) Final Judgment
- Decision: Reject
- Justification:Contains a critical logic error (wrong denominator) that produces incorrect results, plus multiple crash scenarios (empty list, missing keys). This would fail in production and produce wrong business metrics.
- Confidence & unknowns:High confidence in the bugs identified. Unknown: intended behavior for edge cases (should it return 0, None, or raise exception?).

---

# Task 2 — Count Valid Emails

##` 1) Code Review Findings
### Critical bugs
- 

### Edge cases & risks
- 

### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- 

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- 

### Edge cases & risks
- 

### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- 

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:
