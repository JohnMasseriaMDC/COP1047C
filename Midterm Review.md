---
marp: true
theme: gaia
paginate: true
style: |
  section {
    font-size: 28px;
  }
---

# 🐍 Introduction to Python
### COP 1047C

---

# 🎯 Learning Objectives

- Understand what Python is
- Use variables and expressions
- Identify data types
- Apply branching (if statements)
- Build loops

---

# 🧠 Warm-Up

### Think-Pair-Share

- What is a program?
- Where is Python used?

---

# 🐍 What is Python?

- High-level language
- Easy to read/write
- Used in:
  - AI
  - Web development
  - Data science
  - Automation

---

# 👋 First Python Program

```python
print("Hello, World!")
````

👉 What do you think this does?

---

# 🧠 Key Idea

* Programs = instructions
* Python runs line by line
* Syntax matters!

---

# 🔢 Variables

```python
age = 20
name = "Alex"
```

* Store data
* Created when assigned

---

# ⚙️ Expressions

```python
total = 5 + 3
price = 10 * 2
```

👉 Expressions = values + operators

---

# ⚠️ Important Rule

```python
x = 5
x = x + 1
```

👉 Right side evaluates first!

---

# 🧩 Data Types

| Type  | Example |
| ----- | ------- |
| int   | 5       |
| float | 3.14    |
| str   | "hello" |
| bool  | True    |

---

# 🔍 Checking Types

```python
type(5)
type("hi")
```

---

# ⚠️ Type Error Example

```python
"5" + 5
```

👉 Why does this fail?

---

# 🔀 Branching

```python
if x > 10:
    print("Big")
```

👉 What happens if false?

---

# 🔁 If / Else

```python
if x > 10:
    print("Big")
else:
    print("Small")
```

---

# 🔄 If / Elif / Else

```python
if x > 10:
    print("Big")
elif x == 10:
    print("Equal")
else:
    print("Small")
```

---

# 🧠 Key Concept

* Conditions → True/False
* Indentation matters!
* No braces `{}`

---

# 🔁 While Loop

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

---

# 🔁 For Loop

```python
for i in range(5):
    print(i)
```

---

# 🔍 range()

```python
range(5)      # 0–4
range(1, 6)   # 1–5
```

---

# ⚠️ Infinite Loop

```python
while True:
    print("Oops")
```

👉 What’s missing?

---

# 🧠 Quick Check #1

```python
x = 5
print(x + 2)
```

👉 What prints?

---

# 🧠 Quick Check #2

```python
type("10")
```

👉 What type?

---

# 🧠 Quick Check #3

```python
x = 3
if x > 5:
    print("A")
else:
    print("B")
```

---

# 🧠 Quick Check #4

```python
for i in range(3):
    print(i)
```

---

# 🧪 Mini Activity

👉 Write a program:

* Store your age
* Print "Adult" if ≥ 18

---

# 🧩 Practice Problem

```python
num = 7
```

👉 Print:

* "Even" or "Odd"

---

# 🧩 Loop Practice

👉 Print numbers from 1–10
👉 Only show multiples of 3

---

# 🧩 Stretch Challenge

```python
age = int(input("Enter age: "))
```

👉 Output:

* Child
* Teen
* Adult

---

# 🚨 Common Mistakes

* Using `=` instead of `==`
* Mixing strings and numbers
* Bad indentation
* Infinite loops

---

# 🎯 Exit Ticket

1. What is a variable?
2. `=` vs `==`?
3. Type of `3.0`?
4. What does this print?

```python
for i in range(2, 5):
    print(i)
```

---

# 🎉 Summary

* Python basics
* Variables & expressions
* Data types
* Branching
* Loops

👉 You can now write basic programs!

```
