
# 🎯 Branching in Python

### COP 1047C – Introduction to Python Programming

### Sections 4.1 – 4.7

---

# 🧠 What Is a Branch?

A **branch** executes only when a condition is `True`.

```python
if user_age > 65:
    discount = 20
```

### 💡 Real-World Analogy

Restaurant host logic:

* If party == 1 → Counter
* If party == 2 → Small table
* Else → Large table

Programming is decision-making.

---

# 🔹 Basic `if` Statement

## Syntax

```python
if condition:
    # indented block
```

### ⚠️ Important

* Condition evaluates to `True` or `False`
* Use `==` for equality (NOT `=`)
* Indentation defines the branch

### Example

```python
num_years = 50

if num_years == 50:
    print("Golden anniversary!")
```

---

# 🔁 If–Else Structure

Exactly **ONE branch executes**

```python
if age < 25:
    insurance_price = 4800
else:
    insurance_price = 2200
```

### 🔎 Rule

* If condition is `True` → first block runs
* Otherwise → else runs
* Never both
* Never neither

---

# 🌲 Multi-Branch (`if`–`elif`–`else`)

Used when detecting **specific values**

```python
if num_sales == 0:
    bonus = 0
elif num_sales == 1:
    bonus = 2
elif num_sales == 2:
    bonus = 5
else:
    bonus = 10
```

### 🧠 Execution Order

* Checked top → bottom
* First `True` branch executes
* Only ONE branch runs

---

# 📊 Relational Operators

| Operator | Meaning               |
| -------- | --------------------- |
| `<`      | Less than             |
| `>`      | Greater than          |
| `<=`     | Less than or equal    |
| `>=`     | Greater than or equal |
| `==`     | Equal                 |
| `!=`     | Not equal             |

⚠️ `=<` and `<>` are NOT valid in Python.

---

# 📈 Detecting Ranges (Implicit Method)

Sequential `elif` creates implicit ranges.

```python
if age < 16:
    print("Too young")
elif age < 25:
    print("16-24")
elif age < 40:
    print("25-39")
else:
    print("40+")
```

### Why this works

If we reach:

```python
elif age < 25:
```

We already know:

* age ≥ 16
* age < 25

So range is **16–24**

---

# 🔗 Logical Operators

| Operator | Meaning           |
| -------- | ----------------- |
| `and`    | Both must be True |
| `or`     | At least one True |
| `not`    | Reverses value    |

### Example

```python
if age >= 18 and age <= 65:
```

Or using chaining:

```python
if 18 <= age <= 65:
```

---

# 🕳 Ranges with Gaps

Example: Child OR Senior discount

```python
if age <= 12:
    price = 11
elif age >= 65:
    price = 12
else:
    price = 14
```

### Explicit version

```python
if (age <= 12) or (age >= 65):
```

---

# ⚠️ Multiple DISTINCT `if` Statements

Very different from `if`–`elif`

Each `if` is independent.

```python
num_boxes = 0
num_apples = 9

if num_apples < 20:
    num_boxes = 3

if num_apples < 10:
    num_boxes = num_boxes - 1
```

### 🧠 Key Difference

| Structure   | How many execute? |
| ----------- | ----------------- |
| if–elif     | Only ONE          |
| separate if | Possibly MANY     |

This is **critical for 4.7**

---

# 🪆 Nested `if` Statements

An `if` inside another `if`.

```python
if sales_type == 2:
    if sales_bonus < 5:
        sales_bonus = 10
    else:
        sales_bonus += 2
else:
    sales_bonus += 1
```

Use nested logic when:

* A decision depends on a previous decision

---

# 🧪 Concept Check

What prints?

```python
num_items = 4

if num_items < 2:
    print("a")
elif num_items < 7:
    print("f")
else:
    print("g")

print("m")
```

### ✅ Answer

```
f
m
```

---

# ❌ Common Student Mistakes

* Using `=` instead of `==`
* Forgetting indentation
* Writing impossible ranges
* Using separate `if` when they meant `elif`
* Overlapping conditions

---

# 🏁 Big Takeaways

✔ Conditions evaluate to `True` / `False`
✔ Indentation defines blocks
✔ `if`–`elif` → only ONE executes
✔ Separate `if` statements → multiple may execute
✔ Logical operators combine conditions
✔ Ranges can be implicit or explicit

---
