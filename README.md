# 🐍 Loops in Python (for / while)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Learning-success)
![Repo Size](https://img.shields.io/github/repo-size/abjaiyad/Python-ConditionalStatements)
![License](https://img.shields.io/badge/License-MIT-green)

Welcome to this repository! 🎉 Here, I’ve documented my learning on **Loops in Python** — one of the most important concepts for performing repetitive tasks efficiently.

---

## 📑 Table of Contents
- [📖 Overview](#-overview)  
- [🛠 Syntax](#-syntax)  
- [💡 Examples](#-examples)  
- [📝 Practice Exercises](#-practice-exercises)  
- [📌 Key Takeaway](#-key-takeaway)  
- [👨‍💻 Author](#-author)  

---

## 📖 Overview
Loops in Python allow programs to **execute a block of code multiple times**. Python mainly provides two types of loops: 1. **for loop** – iterates over a sequence or a fixed number of times. 2. **while loop** – runs as long as a specified condition is `True`.

---

## 🛠 Syntax
### ✅ for loop
```python
for variable in sequence:
    # Executes for each item in sequence
````

### ✅ while loop

```python
while condition:
    # Executes as long as condition is True
```

---

## 💡 Examples

### ✅ for loop Example

```python
# Print numbers from 1 to 5
for i in range(1, 6):
    print(i)
```

**Output:**

```
1
2
3
4
5
```

### ✅ while loop Example

```python
# Print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1
```

**Output:**

```
1
2
3
4
5
```

### ✅ Loop Control Statements

* **break** → Exit the loop immediately
* **continue** → Skip the current iteration and continue
* **pass** → Placeholder, does nothing

**Example:**

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

**Output:**

```
1
2
4
5
```

---

## 📝 Practice Exercises

1. Print all even numbers from 1 to 20 using a for loop.
2. Print the multiplication table of a given number using a while loop.
3. Keep asking the user to enter a number until they type `0`.
4. Calculate the factorial of a number using a loop.
5. Take a list of numbers and print only the odd ones using a loop.

---

## 📌 Key Takeaway

Loops are essential for **repeating tasks efficiently**, reducing code repetition, and enabling dynamic program flow in Python.

---

## 👨‍💻 Author

**Amad Bin Jaiyad**
📌 BCA Student | Exploring the Cutting-Edge of Technology
🔗 [GitHub](https://github.com/abjaiyad) | [LinkedIn](https://www.linkedin.com/in/)
