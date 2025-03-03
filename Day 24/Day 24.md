# Linear Regression from Scratch

## Key Points Discussed:

### Best fit line and its formula: 
```math
  y = mx + b
```
- Slope (`m`) and intercept (`b`) were discussed.

### **Mathematics in Linear Regression**:
- Importance of foundational and fundamental concepts before diving into algorithms.
- Discussion on manual coding examples in Python for linear regression.
- Examples included CGPA vs. Package data to predict outcomes.

### **Formulas and Calculations**:
- Explanation of how formulas are derived.
- Relation between slope and best fit line.
- Use of libraries like Scikit-learn in Python.

### **Types of Solutions**:
- **Closed-form Solution**: Direct method using Ordinary Least Squares (OLS).
  - Formula: 
  ```math
  y = mx + b
  ```
  - Calculation of `m` and `b` values directly.

- **Non-Closed Form Solution**: Iterative methods like Gradient Descent.
  - Preferred when dealing with high-dimensional data where direct formulas become complex.

### **Error Calculation**:
- Understanding distance and error in prediction points.
- Total distance or total error concept:

```math
  e = d1^2 + d2^2 + ... + dn^2
```

- Summation notation:

```math
  e = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
```

### **Practical Example**:
- Visualization of best fit line and nearest points.
- Error calculation between actual and predicted points.
- Use of mean values for x and y (e.g., mean of CGPA and mean of package).

### **Detailed Steps**:
1. Plotting data points and drawing the best fit line.
2. Identifying nearest points (d1 to d6).
3. Calculation of errors at each point.
4. Using squared errors to avoid positive/negative cancellation.
5. Deriving the formula for total error.

## **Understanding Linear Regression - Simple Explanation**

## **Step 1: What Are We Doing?**
Imagine you have **lots of toy cars** 🏎️, and you want to build a **ramp** (a straight slide) so that the cars roll down perfectly to a target.

But there's a problem! Some cars are missing the target because your ramp is not at the right angle. 😞

Your job is to **adjust the ramp** (change the slope and position) so that most cars land closest to the target. 🎯

This is what linear regression does! It tries to find the **best straight line** that matches all the points (cars).

---

## **Step 2: How Do We Know the Ramp is Wrong?**
For every car, we measure how far it lands from the target (like missing the hole in mini-golf ⛳).

```math
  \text{Error} = \text{actual landing} - \text{predicted landing}
```

If the error is **big**, we know our ramp needs fixing.  
If the error is **small**, our ramp is almost perfect!

We **square the errors** (so we don’t care about negative or positive errors).

```math
  \text{Total Error} = (y_1 - \hat{y}_1)^2 + (y_2 - \hat{y}_2)^2 + ...
```

Our goal is to **make this total error as small as possible**!

---

## **Step 3: How Do We Fix the Ramp?**
We need to **adjust the slope** (how steep the ramp is) and **adjust the height** (where it starts).

These are just **two numbers** in math:
- `m` (slope, controls steepness)
- `b` (intercept, controls height)

To fix the ramp, we need to figure out:  
👉 Should we **increase** or **decrease** the slope?  
👉 Should we **move the ramp up or down**?

To answer this, we use **differentiation** (a math trick that tells us how fast the error is changing).

---

## **Step 4: Using Differentiation to Find the Best Ramp**
Differentiation is like a **heat sensor** 🔥 that tells us if we're getting **closer** or **farther** from the best ramp.

- If we **increase the slope and the error goes up**, we should **decrease** it.
- If we **increase the slope and the error goes down**, we should **keep increasing** it.

Mathematically, we find **the slope of the error function** and update our values using **small steps** (like adjusting the ramp little by little).
