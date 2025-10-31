# 函数的复合 / Composition of Functions

**定义 / Definition：**  
函数的复合是指将一个函数的输出作为另一个函数的输入，形成一个新的函数。  
The composition of functions means using the output of one function as the input of another, forming a new function.

设有两个函数 $f(x)$ 和 $g(x)$，则 $f$ 与 $g$ 的复合记作 $f(g(x))$ 或 $(f \circ g)(x)$，表示先对 $x$ 应用 $g$，再对结果应用 $f$。  
Given two functions $f(x)$ and $g(x)$, the composition is denoted as $f(g(x))$ or $(f \circ g)(x)$, which means applying $g$ to $x$ first, then applying $f$ to the result.

---

## 一般形式 / General Form

$$
(f \circ g)(x) = f(g(x))
$$

**注意：复合函数的顺序很重要，通常 $f(g(x)) \neq g(f(x))$。**  
Note: The order of composition matters; usually $f(g(x)) \neq g(f(x))$.

---

## 例子 / Examples

**例1 / Example 1：**
设 $f(x) = x^2 + 1$ 和 $g(x) = 2x - 3$

- $(f \circ g)(x) = f(g(x)) = f(2x - 3) = (2x - 3)^2 + 1 = 4x^2 - 12x + 10$
- $(g \circ f)(x) = g(f(x)) = g(x^2 + 1) = 2(x^2 + 1) - 3 = 2x^2 - 1$

可以看出 $(f \circ g)(x) \neq (g \circ f)(x)$

**例2 / Example 2：**
设 $f(x) = \sqrt{x}$ 和 $g(x) = x - 4$

- $(f \circ g)(x) = f(g(x)) = f(x - 4) = \sqrt{x - 4}$（定义域：$x \geq 4$）

---

## 定义域 / Domain

复合函数 $(f \circ g)(x)$ 的定义域是满足以下条件的 $x$ 值：
1. $x$ 在 $g$ 的定义域内
2. $g(x)$ 在 $f$ 的定义域内

The domain of $(f \circ g)(x)$ consists of all $x$ values such that:
1. $x$ is in the domain of $g$
2. $g(x)$ is in the domain of $f$

**相关笔记 / Related Notes：** 来源于 [[2025-08-29]]


