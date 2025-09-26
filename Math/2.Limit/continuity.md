# 连续性 / Continuity

## 1. 连续性的定义 / Definition of Continuity

### 1.1 在一点处连续 / Continuity at a Point

**定义（中文）：**  
函数 $f(x)$ 在点 $a$ 处连续，当且仅当：
1. $f(a)$ 存在（即 $a$ 在 $f$ 的定义域内）
2. $\lim_{x \to a} f(x)$ 存在
3. $\lim_{x \to a} f(x) = f(a)$

**Definition (English):**  
A function $f(x)$ is continuous at point $a$ if and only if:
1. $f(a)$ exists (i.e., $a$ is in the domain of $f$)
2. $\lim_{x \to a} f(x)$ exists
3. $\lim_{x \to a} f(x) = f(a)$

### 1.2 数学表达 / Mathematical Expression

$$\lim_{x \to a} f(x) = f(a)$$

### 1.3 等价定义 / Equivalent Definition

使用 $\epsilon-\delta$ 语言：
Using $\epsilon-\delta$ language:

对于任意 $\epsilon > 0$，存在 $\delta > 0$，使得当 $|x - a| < \delta$ 时，有 $|f(x) - f(a)| < \epsilon$。  
For any $\epsilon > 0$, there exists $\delta > 0$ such that when $|x - a| < \delta$, we have $|f(x) - f(a)| < \epsilon$.

---

## 2. 在区间上连续 / Continuity on an Interval

### 2.1 开区间连续 / Continuity on Open Interval

**定义：** 函数 $f(x)$ 在开区间 $(a, b)$ 上连续，当且仅当 $f(x)$ 在 $(a, b)$ 内的每一点都连续。  
**Definition:** A function $f(x)$ is continuous on an open interval $(a, b)$ if and only if $f(x)$ is continuous at every point in $(a, b)$.

### 2.2 闭区间连续 / Continuity on Closed Interval

**定义：** 函数 $f(x)$ 在闭区间 $[a, b]$ 上连续，当且仅当：
1. $f(x)$ 在 $(a, b)$ 内连续
2. $\lim_{x \to a^+} f(x) = f(a)$（右连续）
3. $\lim_{x \to b^-} f(x) = f(b)$（左连续）

**Definition:** A function $f(x)$ is continuous on a closed interval $[a, b]$ if and only if:
1. $f(x)$ is continuous in $(a, b)$
2. $\lim_{x \to a^+} f(x) = f(a)$ (right continuous)
3. $\lim_{x \to b^-} f(x) = f(b)$ (left continuous)

---

## 3. 连续函数的性质 / Properties of Continuous Functions

### 3.1 基本运算 / Basic Operations

如果 $f(x)$ 和 $g(x)$ 都在点 $a$ 处连续，则：  
If $f(x)$ and $g(x)$ are both continuous at point $a$, then:

- $f(x) + g(x)$ 在 $a$ 处连续 / $f(x) + g(x)$ is continuous at $a$
- $f(x) - g(x)$ 在 $a$ 处连续 / $f(x) - g(x)$ is continuous at $a$
- $f(x) \cdot g(x)$ 在 $a$ 处连续 / $f(x) \cdot g(x)$ is continuous at $a$
- $\frac{f(x)}{g(x)}$ 在 $a$ 处连续（当 $g(a) \neq 0$ 时）/ $\frac{f(x)}{g(x)}$ is continuous at $a$ (when $g(a) \neq 0$)

### 3.2 复合函数连续性 / Continuity of Composite Functions

如果 $g(x)$ 在 $a$ 处连续，$f(u)$ 在 $g(a)$ 处连续，则复合函数 $f(g(x))$ 在 $a$ 处连续。  
If $g(x)$ is continuous at $a$ and $f(u)$ is continuous at $g(a)$, then the composite function $f(g(x))$ is continuous at $a$.

### 3.3 反函数连续性 / Continuity of Inverse Functions

如果 $f(x)$ 在区间 $I$ 上连续且严格单调，则其反函数 $f^{-1}(x)$ 在对应的区间上连续。  
If $f(x)$ is continuous and strictly monotonic on interval $I$, then its inverse function $f^{-1}(x)$ is continuous on the corresponding interval.

---

## 4. 连续函数的类型 / Types of Continuous Functions

### 4.1 基本连续函数 / Basic Continuous Functions

- **多项式函数 / Polynomial Functions：** $p(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_0$  
  在其定义域内连续 / Continuous on their domain
- **有理函数 / Rational Functions：** $\frac{p(x)}{q(x)}$  
  在分母不为零的点处连续 / Continuous where the denominator is not zero
- **三角函数 / Trigonometric Functions：** $\sin x$, $\cos x$, $\tan x$ 等  
  在各自定义域内连续 / Continuous on their respective domains
- **指数函数 / Exponential Functions：** $a^x$ ($a > 0, a \neq 1$)  
  在 $\mathbb{R}$ 上连续 / Continuous on $\mathbb{R}$
- **对数函数 / Logarithmic Functions：** $\log_a x$ ($a > 0, a \neq 1$)  
  在 $(0, \infty)$ 上连续 / Continuous on $(0, \infty)$

### 4.2 分段函数连续性 / Continuity of Piecewise Functions

对于分段函数，需要检查分段点的连续性。  
For piecewise functions, we need to check continuity at the break points.

**例子 / Example：**

$$f(x) = \begin{cases}
x^2 + 1 & \text{if } x \leq 0 \\
2x + 1 & \text{if } x > 0
\end{cases}$$

在 $x = 0$ 处的连续性检查：  
Continuity check at $x = 0$:

- $f(0) = 0^2 + 1 = 1$
- $\lim_{x \to 0^-} f(x) = \lim_{x \to 0^-} (x^2 + 1) = 1$
- $\lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} (2x + 1) = 1$

因此 $f(x)$ 在 $x = 0$ 处连续。  
Therefore $f(x)$ is continuous at $x = 0$.

---

## 5. 不连续的类型 / Types of Discontinuities

### 5.1 可去不连续 / Removable Discontinuity

**特征：** 极限存在但不等于函数值。  
**Characteristic:** The limit exists but is not equal to the function value.

$$\lim_{x \to a} f(x) \neq f(a) \quad \text{或} \quad f(a) \text{未定义}$$

**例子 / Example：**

$$f(x) = \begin{cases}
\frac{x^2 - 1}{x - 1} & \text{if } x \neq 1 \\
\text{未定义} & \text{if } x = 1
\end{cases}$$

### 5.2 跳跃不连续 / Jump Discontinuity

**特征：** 左右极限存在但不相等。  
**Characteristic:** Left and right limits exist but are not equal.

$$\lim_{x \to a^-} f(x) \neq \lim_{x \to a^+} f(x)$$

**例子 / Example：**

$$f(x) = \begin{cases}
x & \text{if } x \leq 0 \\
x + 1 & \text{if } x > 0
\end{cases}$$

### 5.3 无穷不连续 / Infinite Discontinuity

**特征：** 函数在某点趋向无穷大。  
**Characteristic:** The function approaches infinity at some point.

**例子 / Example：**

$$f(x) = \frac{1}{x} \quad \text{在} \quad x = 0 \quad \text{处}$$

### 5.4 振荡不连续 / Oscillating Discontinuity

**特征：** 函数在某点附近振荡且无极限。  
**Characteristic:** The function oscillates near a point without a limit.

**例子 / Example：**

$$f(x) = \sin\left(\frac{1}{x}\right) \quad \text{在} \quad x = 0 \quad \text{处}$$

---

## 6. 连续性的重要定理 / Important Theorems about Continuity

### 6.1 中间值定理 / Intermediate Value Theorem

如果 $f(x)$ 在 $[a, b]$ 上连续，且 $f(a) \neq f(b)$，则对于任意介于 $f(a)$ 和 $f(b)$ 之间的值 $L$，存在 $c \in (a, b)$ 使得 $f(c) = L$。  
If $f(x)$ is continuous on $[a, b]$ and $f(a) \neq f(b)$, then for any value $L$ between $f(a)$ and $f(b)$, there exists $c \in (a, b)$ such that $f(c) = L$.

### 6.2 极值定理 / Extreme Value Theorem

如果 $f(x)$ 在闭区间 $[a, b]$ 上连续，则 $f(x)$ 在 $[a, b]$ 上必有最大值和最小值。  
If $f(x)$ is continuous on a closed interval $[a, b]$, then $f(x)$ must have maximum and minimum values on $[a, b]$.

### 6.3 一致连续性定理 / Uniform Continuity Theorem

闭区间上的连续函数必一致连续。  
A continuous function on a closed interval is necessarily uniformly continuous.

---

## 7. 相关链接 / Related Links

- [[limits]] - 极限基本概念
- [[limit_theorems]] - 极限定理
- [[intermediate_value_theorem]] - 中间值定理
- [[squeeze_theorem_trigonometric]] - 夹逼定理应用
- [[derivatives_basics]] - 导数基础
- [[derivative_rules]] - 求导法则

---

## 标签 / Tags
#连续性 #极限 #微积分 #Continuity #Limits #Calculus

---

*创建日期: 2025年1月18日*  
*对应课程: MATH 140 第1-4周内容*

[//begin]: # "Autogenerated link references for markdown compatibility"
[limits]: limits.md "极限 / Limits"
[limit_theorems]: limit_theorems.md "极限定理 / Limit Theorems"
[intermediate_value_theorem]: intermediate_value_theorem.md "中间值定理 / Intermediate Value Theorem"
[squeeze_theorem_trigonometric]: squeeze_theorem_trigonometric.md "三角函数的夹逼定理 / Squeeze Theorem for Trigonometric Functions"
[//end]: # "Autogenerated link references"
