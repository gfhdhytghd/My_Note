# 5. 函数类型 / Function Types

## 一次函数 / Linear Functions

### 定义 / Definition

A linear function is a function of the form $f(x) = ax + b$, where $a$ and $b$ are constants. Its graph is a straight line.
一次函数的形式为 $f(x) = ax + b$，其中 $a$ 和 $b$ 是常数。其图像是一条直线。

### 一般形式 / General Form

$$f(x) = ax + b$$

其中：
Where:
- $a$ 是斜率 / $a$ is the slope
- $b$ 是 $y$ 轴截距 / $b$ is the $y$-intercept
- $a \neq 0$（否则为常数函数）/ $a \neq 0$ (otherwise it's a constant function)

### 性质 / Properties

- **图像 / Graph:** 直线 / Straight line
- **定义域 / Domain:** $\mathbb{R}$ (所有实数 / all real numbers)
- **值域 / Range:** $\mathbb{R}$ (所有实数 / all real numbers)
- **单调性 / Monotonicity:** 
  - 当 $a > 0$ 时，函数递增 / When $a > 0$, function is increasing
  - 当 $a < 0$ 时，函数递减 / When $a < 0$, function is decreasing

### 例子 / Examples

- $f(x) = 2x + 1$ （斜率为2，$y$轴截距为1）
- $g(x) = -3x + 5$ （斜率为-3，$y$轴截距为5）
- $h(x) = x$ （斜率为1，过原点）

### 求解一次函数 / Solving Linear Functions

**根（零点）/ Root (Zero):**
令 $f(x) = 0$，即 $ax + b = 0$
Set $f(x) = 0$, i.e., $ax + b = 0$

解得：$x = -\frac{b}{a}$ (当 $a \neq 0$ 时)
Solution: $x = -\frac{b}{a}$ (when $a \neq 0$)

## 二次函数 / Quadratic Functions

### 定义 / Definition

A quadratic function is a function of the form $f(x) = ax^2 + bx + c$, where $a \neq 0$. Its graph is a parabola.
二次函数的形式为 $f(x) = ax^2 + bx + c$，其中 $a \neq 0$。其图像是抛物线。

### 一般形式 / General Form

$$f(x) = ax^2 + bx + c \quad (a \neq 0)$$

### 性质 / Properties

- **图像 / Graph:** 抛物线 / Parabola
- **定义域 / Domain:** $\mathbb{R}$ (所有实数 / all real numbers)
- **开口方向 / Opening Direction:**
  - 当 $a > 0$ 时，开口向上 / When $a > 0$, opens upward
  - 当 $a < 0$ 时，开口向下 / When $a < 0$, opens downward

### 顶点 / Vertex

**顶点坐标 / Vertex Coordinates:**
$$\left(-\frac{b}{2a}, f\left(-\frac{b}{2a}\right)\right)$$

**顶点是抛物线的最高点或最低点 / The vertex is the highest or lowest point of the parabola**

### 对称轴 / Axis of Symmetry

**对称轴方程 / Axis of Symmetry Equation:**
$$x = -\frac{b}{2a}$$

### 值域 / Range

- 当 $a > 0$ 时：$\left[f\left(-\frac{b}{2a}\right), +\infty\right)$
- 当 $a < 0$ 时：$\left(-\infty, f\left(-\frac{b}{2a}\right)\right]$

### 二次函数的不同形式 / Different Forms of Quadratic Functions

#### 1. 标准形式 / Standard Form
$$f(x) = ax^2 + bx + c$$

#### 2. 顶点形式 / Vertex Form
$$f(x) = a(x - h)^2 + k$$
其中 $(h, k)$ 是顶点坐标 / where $(h, k)$ is the vertex

#### 3. 因式分解形式 / Factored Form
$$f(x) = a(x - r_1)(x - r_2)$$
其中 $r_1, r_2$ 是函数的根 / where $r_1, r_2$ are the roots of the function

### 例子 / Examples

- $f(x) = x^2 - 4x + 3$
  - 顶点：$(2, -1)$ / Vertex: $(2, -1)$
  - 对称轴：$x = 2$ / Axis of symmetry: $x = 2$

- $g(x) = -2x^2 + 8x - 6$
  - 顶点：$(2, 2)$ / Vertex: $(2, 2)$
  - 对称轴：$x = 2$ / Axis of symmetry: $x = 2$

### 求解二次方程 / Solving Quadratic Equations

#### 二次公式 / Quadratic Formula
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

#### 判别式 / Discriminant
$$\Delta = b^2 - 4ac$$

- $\Delta > 0$：两个不同的实根 / Two distinct real roots
- $\Delta = 0$：一个重根 / One repeated root
- $\Delta < 0$：无实根 / No real roots

## 三次函数 / Cubic Functions

### 定义 / Definition

A cubic function is a function of the form $f(x) = ax^3 + bx^2 + cx + d$, where $a \neq 0$. Its graph can have one or two turning points.
三次函数的形式为 $f(x) = ax^3 + bx^2 + cx + d$，其中 $a \neq 0$。其图像可能有一个或两个拐点。

### 一般形式 / General Form

$$f(x) = ax^3 + bx^2 + cx + d \quad (a \neq 0)$$

### 性质 / Properties

- **图像 / Graph:** S 形曲线 / S-shaped curve
- **定义域 / Domain:** $\mathbb{R}$ (所有实数 / all real numbers)
- **值域 / Range:** $\mathbb{R}$ (所有实数 / all real numbers)
- **单调性 / Monotonicity:** 可能有局部最大值和最小值 / May have local maxima and minima

### 三次函数的行为 / Behavior of Cubic Functions

- 当 $a > 0$ 时：
  - $x \to -\infty$ 时，$f(x) \to -\infty$
  - $x \to +\infty$ 时，$f(x) \to +\infty$

- 当 $a < 0$ 时：
  - $x \to -\infty$ 时，$f(x) \to +\infty$
  - $x \to +\infty$ 时，$f(x) \to -\infty$

### 例子 / Examples

- $f(x) = x^3 - 3x^2 + 2$
- $g(x) = -x^3 + 6x^2 - 9x + 4$
- $h(x) = 2x^3 + x - 1$

### 拐点 / Inflection Points

三次函数可能有拐点，即曲线从凹向上变为凹向下（或相反）的点。
Cubic functions may have inflection points where the curve changes from concave up to concave down (or vice versa).

拐点的 $x$ 坐标可以通过求解 $f''(x) = 0$ 得到。
The $x$-coordinate of inflection points can be found by solving $f''(x) = 0$.

## 函数类型总结表 / Summary Table of Function Types

| 函数类型 / Function Type | 一般式 / General Form | 图像 / Graph | 定义域 / Domain | 值域特点 / Range Characteristics |
|------------------------|----------------------|---------------|-----------------|--------------------------------|
| 一次函数 / Linear | $ax + b$ | 直线 / Straight line | $\mathbb{R}$ | $\mathbb{R}$ |
| 二次函数 / Quadratic | $ax^2 + bx + c$ | 抛物线 / Parabola | $\mathbb{R}$ | 有最值 / Has extremum |
| 三次函数 / Cubic | $ax^3 + bx^2 + cx + d$ | S 形曲线 / S-shaped curve | $\mathbb{R}$ | $\mathbb{R}$ |

## 多项式函数的一般性质 / General Properties of Polynomial Functions

### 连续性 / Continuity
所有多项式函数在其定义域内都是连续的。
All polynomial functions are continuous on their domain.

### 可微性 / Differentiability
所有多项式函数在其定义域内都是可微的。
All polynomial functions are differentiable on their domain.

### 根的个数 / Number of Roots
$n$ 次多项式最多有 $n$ 个实根。
An $n$-th degree polynomial has at most $n$ real roots.

## 相关概念 / Related Concepts

- [[functions_basics|函数基础]] - 函数的基本概念和性质
- [[real_numbers|实数]] - 函数值的范围



[//begin]: # "Autogenerated link references for markdown compatibility"
[functions_basics|函数基础]: functions_basics.md "4. 函数基础 / Functions Basics"
[real_numbers|实数]: real_numbers.md "1. 实数 / Real Numbers"
[//end]: # "Autogenerated link references"
