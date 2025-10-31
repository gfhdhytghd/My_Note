# 反三角函数 / Inverse Trigonometric Functions

**概述 / Overview：**  
反三角函数用于求已知三角函数值对应的角度。由于三角函数具有周期性，需要限制定义域使其成为一一对应函数。  
Inverse trigonometric functions are used to find angles corresponding to given trigonometric values. Due to the periodic nature of trigonometric functions, we must restrict their domains to make them bijective.

---

<details>
<summary>反函数 / Inverse Functions（点击展开/Click to expand）</summary>

card![[inverse_functions]]

</details>

## 主要反三角函数 / Main Inverse Trigonometric Functions

### 1. 反正弦函数 / Arcsine Function

**记号 / Notation：** $\arcsin x$ 或 $\sin^{-1} x$

**定义 / Definition：**  
$y = \arcsin x$ 当且仅当 $x = \sin y$ 且 $y \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$  
$y = \arcsin x$ if and only if $x = \sin y$ and $y \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$

**性质 / Properties：**
- 定义域：$[-1, 1]$ / Domain: $[-1, 1]$
- 值域：$\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ / Range: $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$
- 奇函数：$\arcsin(-x) = -\arcsin x$ / Odd function: $\arcsin(-x) = -\arcsin x$

---

### 2. 反余弦函数 / Arccosine Function

**记号 / Notation：** $\arccos x$ 或 $\cos^{-1} x$

**定义 / Definition：**  
$y = \arccos x$ 当且仅当 $x = \cos y$ 且 $y \in [0, \pi]$  
$y = \arccos x$ if and only if $x = \cos y$ and $y \in [0, \pi]$

**性质 / Properties：**
- 定义域：$[-1, 1]$ / Domain: $[-1, 1]$
- 值域：$[0, \pi]$ / Range: $[0, \pi]$
- 恒等式：$\arccos x + \arcsin x = \frac{\pi}{2}$ / Identity: $\arccos x + \arcsin x = \frac{\pi}{2}$

---

### 3. 反正切函数 / Arctangent Function

**记号 / Notation：** $\arctan x$ 或 $\tan^{-1} x$

**定义 / Definition：**  
$y = \arctan x$ 当且仅当 $x = \tan y$ 且 $y \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$  
$y = \arctan x$ if and only if $x = \tan y$ and $y \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$

**性质 / Properties：**
- 定义域：$(-\infty, \infty)$ / Domain: $(-\infty, \infty)$
- 值域：$\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ / Range: $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$
- 奇函数：$\arctan(-x) = -\arctan x$ / Odd function: $\arctan(-x) = -\arctan x$
- 水平渐近线：$y = \pm\frac{\pi}{2}$ / Horizontal asymptotes: $y = \pm\frac{\pi}{2}$

---

## 常用值 / Common Values

### 反正弦和反余弦的常用值 / Common Values for Arcsine and Arccosine

| $x$ | $\arcsin x$ | $\arccos x$ |
|:---:|:-----------:|:-----------:|
| $-1$ | $-\frac{\pi}{2}$ ($-90°$) | $\pi$ ($180°$) |
| $-\frac{\sqrt{3}}{2}$ | $-\frac{\pi}{3}$ ($-60°$) | $\frac{5\pi}{6}$ ($150°$) |
| $-\frac{\sqrt{2}}{2}$ | $-\frac{\pi}{4}$ ($-45°$) | $\frac{3\pi}{4}$ ($135°$) |
| $-\frac{1}{2}$ | $-\frac{\pi}{6}$ ($-30°$) | $\frac{2\pi}{3}$ ($120°$) |
| $0$ | $0$ ($0°$) | $\frac{\pi}{2}$ ($90°$) |
| $\frac{1}{2}$ | $\frac{\pi}{6}$ ($30°$) | $\frac{\pi}{3}$ ($60°$) |
| $\frac{\sqrt{2}}{2}$ | $\frac{\pi}{4}$ ($45°$) | $\frac{\pi}{4}$ ($45°$) |
| $\frac{\sqrt{3}}{2}$ | $\frac{\pi}{3}$ ($60°$) | $\frac{\pi}{6}$ ($30°$) |
| $1$ | $\frac{\pi}{2}$ ($90°$) | $0$ ($0°$) |

### 反正切的常用值 / Common Values for Arctangent

| $x$ | $\arctan x$ | 度数 / Degrees |
|:---:|:-----------:|:--------------:|
| $-\sqrt{3}$ | $-\frac{\pi}{3}$ | $-60°$ |
| $-1$ | $-\frac{\pi}{4}$ | $-45°$ |
| $-\frac{1}{\sqrt{3}}$ | $-\frac{\pi}{6}$ | $-30°$ |
| $0$ | $0$ | $0°$ |
| $\frac{1}{\sqrt{3}}$ | $\frac{\pi}{6}$ | $30°$ |
| $1$ | $\frac{\pi}{4}$ | $45°$ |
| $\sqrt{3}$ | $\frac{\pi}{3}$ | $60°$ |

---

## 其他反三角函数 / Other Inverse Trigonometric Functions

### 4. 反余切函数 / Arccotangent Function
**记号 / Notation：** $\operatorname{arccot} x$ 或 $\cot^{-1} x$  
**定义域 / Domain：** $(-\infty, \infty)$  
**值域 / Range：** $(0, \pi)$

### 5. 反正割函数 / Arcsecant Function
**记号 / Notation：** $\operatorname{arcsec} x$ 或 $\sec^{-1} x$  
**定义域 / Domain：** $(-\infty, -1] \cup [1, \infty)$  
**值域 / Range：** $[0, \pi] \setminus \{\frac{\pi}{2}\}$

### 6. 反余割函数 / Arccosecant Function
**记号 / Notation：** $\operatorname{arccsc} x$ 或 $\csc^{-1} x$  
**定义域 / Domain：** $(-\infty, -1] \cup [1, \infty)$  
**值域 / Range：** $[-\frac{\pi}{2}, \frac{\pi}{2}] \setminus \{0\}$

---

## 重要恒等式 / Important Identities

**基本恒等式 / Fundamental Identities：**
- $\sin(\arcsin x) = x$，当 $x \in [-1, 1]$ / $\sin(\arcsin x) = x$ for $x \in [-1, 1]$
- $\cos(\arccos x) = x$，当 $x \in [-1, 1]$ / $\cos(\arccos x) = x$ for $x \in [-1, 1]$
- $\tan(\arctan x) = x$，当 $x \in \mathbb{R}$ / $\tan(\arctan x) = x$ for $x \in \mathbb{R}$

**复合恒等式 / Composition Identities：**
- $\arcsin x + \arccos x = \frac{\pi}{2}$ / $\arcsin x + \arccos x = \frac{\pi}{2}$
- $\arctan x + \operatorname{arccot} x = \frac{\pi}{2}$ / $\arctan x + \operatorname{arccot} x = \frac{\pi}{2}$

---

## 应用示例 / Application Examples

**例1 / Example 1：**  
求 $\arcsin\left(\frac{1}{2}\right)$ 的值。  
Find the value of $\arcsin\left(\frac{1}{2}\right)$.

**解 / Solution：**  
因为 $\sin\frac{\pi}{6} = \frac{1}{2}$ 且 $\frac{\pi}{6} \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$，所以 $\arcsin\left(\frac{1}{2}\right) = \frac{\pi}{6}$。  
Since $\sin\frac{\pi}{6} = \frac{1}{2}$ and $\frac{\pi}{6} \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$, we have $\arcsin\left(\frac{1}{2}\right) = \frac{\pi}{6}$.

**例2 / Example 2：**  
简化 $\sin(\arccos x)$。  
Simplify $\sin(\arccos x)$.

**解 / Solution：**  
设 $\theta = \arccos x$，则 $\cos\theta = x$ 且 $\theta \in [0, \pi]$。  
Let $\theta = \arccos x$, then $\cos\theta = x$ and $\theta \in [0, \pi]$.

由恒等式 $\sin^2\theta + \cos^2\theta = 1$，得到：  
From the identity $\sin^2\theta + \cos^2\theta = 1$, we get:

$\sin\theta = \pm\sqrt{1 - \cos^2\theta} = \pm\sqrt{1 - x^2}$

因为 $\theta \in [0, \pi]$，所以 $\sin\theta \geq 0$，因此：  
Since $\theta \in [0, \pi]$, we have $\sin\theta \geq 0$, therefore:

$\sin(\arccos x) = \sqrt{1 - x^2}$

---

## 重要术语对照 / Key Terms

- 反三角函数：Inverse trigonometric functions
- 反正弦：Arcsine
- 反余弦：Arccosine  
- 反正切：Arctangent
- 反余切：Arccotangent
- 反正割：Arcsecant
- 反余割：Arccosecant
- 主值：Principal value
- 定义域限制：Domain restriction
- 周期性：Periodicity

**相关笔记 / Related Notes：** 来源于 [[2025-08-29]]，另见 [[trigonometric_functions]] 和 [[inverse_functions]]


[//begin]: # "Autogenerated link references for markdown compatibility"
[inverse_functions]: inverse_functions.md "反函数 / Inverse Functions"
[trigonometric_functions]: trigonometric_functions.md "三角函数 / Trigonometric Functions"
[//end]: # "Autogenerated link references"
