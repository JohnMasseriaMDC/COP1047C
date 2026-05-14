---
marp: true
theme: gaia
paginate: true
size: 4:3
style: |
  section {
    font-size: 26px;
  }

  table {
    margin-left: auto;
    margin-right: auto;
  }
---

<!-- _class: lead -->

# 4.5  
# Detecting Ranges  
## Using Logical Operators

---

# Logical Operators

A logical operator evaluates expressions as:

- `True`
- `False`

Python logical operators:

- `and`
- `or`
- `not`

---

# Logical Operator Definitions

| Operator | Meaning |
|-----------|------------|
| `a and b` | True if BOTH operands are True |
| `a or b` | True if AT LEAST ONE operand is True |
| `not a` | Reverses the Boolean value |

---

# Example

Let:

```python
x = 7
y = 9
````

Evaluate:

```python
(x > 0) and (y < 10)
```

True AND True → **True**

---

# More Examples

| Expression            | Result |
| --------------------- | ------ |
| `(x > 0) and (y < 5)` | False  |
| `(x < 0) or (y > 5)`  | True   |
| `not (x < 0)`         | True   |
| `not (x > 0)`         | False  |

---

# Detecting a Range

We often use `and` to detect values inside a range.

Example:

```python
if (x > 10) and (x < 15):
```

This detects:

> 11, 12, 13, 14

---

# Why This Works

* `x > 10` → defines lower bound
* `x < 15` → defines upper bound
* `and` → ensures overlap

Both must be True.

---

# Detecting Outside a Range

Example:

```python
if (x < -5) or (x > 10):
```

This detects:

* Values below -5
* Values above 10

---

# Booleans in Python

Boolean values:

* `True`
* `False`

Example:

```python
my_bool = True
is_small = 4 < 3   # False
```

Expressions evaluate to Boolean values.

---

# Logical Operators in Practice

Given:

```python
age = 19
days = 7
user_char = "q"
```

| Expression                   | Result |
| ---------------------------- | ------ |
| `(age > 16) and (age < 25)`  | True   |
| `(age > 16) and (days > 10)` | False  |
| `(age > 16) or (days > 10)`  | True   |

---

# More Boolean Examples

| Expression               | Result |
| ------------------------ | ------ |
| `not (days > 10)`        | True   |
| `not (age > 16)`         | False  |
| `not (user_char == "q")` | False  |

---

<!-- _class: lead -->

# Writing Range Conditions

---

# Greater Than 30 and Less Than 90

```python
if (days_logged > 30) and (days_logged < 90):
```

---

# Between 0 and 100

```python
if (max_cars > 0) and (max_cars < 100):
```

---

# Between 10 and 20 (Inclusive)

```python
if (num_stores >= 10) and (num_stores <= 20):
```

---

# Less Than 15 OR Greater Than 79

```python
if (not_valid < 15) or (not_valid > 79):
```

---

# More Practice Expressions

Minimum 2, Maximum 5:

```python
if (num_dogs >= 2) and (num_dogs <= 5):
```

---

Wage > 10 and < 18:

```python
if (wage > 10) and (wage < 18):
```

---

3-digit positive integer:

```python
if (num >= 100) and (num <= 999):
```

---

<!-- _class: lead -->

# Example

# Cable TV Channels

---

Regular channels: 2–499
HD channels: 1002–1499

```python
if (user_channel >= 2) and (user_channel <= 499):
    channel_type = "s"
elif (user_channel >= 1002) and (user_channel <= 1499):
    channel_type = "h"
else:
    channel_type = "e"
```

---

# Concept Check

If `user_channel = 300`:

1. Does first condition evaluate True?
   → Yes

2. Does the `elif` get checked?
   → No

Why?

Because only one branch executes.

---

<!-- _class: lead -->

# Explicit vs Implicit Ranges

---

# Explicit Ranges

```python
elif (x >= 0) and (x <= 10):
```

Both bounds written clearly.

---

# Implicit Ranges

```python
elif x <= 10:
```

If previous branch was:

```python
if x < 0:
```

Then `x >= 0` is already implied.

---

# Why Implicit Works

If:

```python
if x < 0:
```

does NOT execute,

Then we already know:

> x >= 0

So next branch only needs:

```python
elif x <= 10:
```

Cleaner and simpler.

---

## Challenge

Original (incorrect):

```python
if (salary_input >= 49000) or (salary_input <= 88000):
```

Correct logic (outside range):

```python
if (salary_input < 49000) or (salary_input > 88000):
    print("Different tax bracket")
else:
    print("27% tax bracket")
```

---

# Section 4.5 Key Takeaways

* `and` → both must be True
* `or` → at least one True
* `not` → reverses Boolean
* Use `and` to detect ranges
* Use `or` to detect outside ranges
* Multi-branch statements allow implicit ranges

---

# End of Section 4.5

## Questions?


