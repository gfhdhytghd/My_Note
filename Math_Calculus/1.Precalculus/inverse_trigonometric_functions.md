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

## 求导与“逆用”模板（含$a$参数） / Derivatives and “Reverse-Use” Templates (with parameter $a$)

这里的“逆用”指：把求导公式倒过来用来识别不定积分（看到某种结构，就立刻联想到某个反三角函数）。  
Here “reverse-use” means using derivative formulas backward to recognize an antiderivative (spot a pattern in an integrand and match it to an inverse trig function).

### A. 标准求导模板 / Standard derivative templates

- $\frac{d}{dx}\arcsin u=\frac{u'}{\sqrt{1-u^2}}$（要求$|u|\leq1$）  
  $\frac{d}{dx}\arcsin u=\frac{u'}{\sqrt{1-u^2}}$ (requires $|u|\leq1$)
- $\frac{d}{dx}\arccos u=-\frac{u'}{\sqrt{1-u^2}}$（要求$|u|\leq1$）  
  $\frac{d}{dx}\arccos u=-\frac{u'}{\sqrt{1-u^2}}$ (requires $|u|\leq1$)
- $\frac{d}{dx}\arctan u=\frac{u'}{1+u^2}$（$u\in\mathbb{R}$）  
  $\frac{d}{dx}\arctan u=\frac{u'}{1+u^2}$ ($u\in\mathbb{R}$)

### B. 把$1$替换为$a$：缩放版（最常用） / Replace $1$ by $a$: scaled versions (most common)

把“$1-u^2$ / $1+u^2$”变成“$a^2-u^2$ / $a^2+u^2$”的核心办法是：先把$u$除以$a$再套用标准模板（通常取$a>0$）。  
The key trick to turn “$1-u^2$ / $1+u^2$” into “$a^2-u^2$ / $a^2+u^2$” is to scale the inside by $a$ (typically assume $a>0$).

- $\frac{d}{dx}\arcsin\left(\frac{u}{a}\right)=\frac{u'}{\sqrt{a^2-u^2}}$（$a>0$且$|u|\leq a$）  
  $\frac{d}{dx}\arcsin\left(\frac{u}{a}\right)=\frac{u'}{\sqrt{a^2-u^2}}$ ($a>0$ and $|u|\leq a$)
- $\frac{d}{dx}\arccos\left(\frac{u}{a}\right)=-\frac{u'}{\sqrt{a^2-u^2}}$（$a>0$且$|u|\leq a$）  
  $\frac{d}{dx}\arccos\left(\frac{u}{a}\right)=-\frac{u'}{\sqrt{a^2-u^2}}$ ($a>0$ and $|u|\leq a$)
- $\frac{d}{dx}\arctan\left(\frac{u}{a}\right)=\frac{au'}{a^2+u^2}$（$a>0$）  
  $\frac{d}{dx}\arctan\left(\frac{u}{a}\right)=\frac{au'}{a^2+u^2}$ ($a>0$)
- 等价写法：$\frac{d}{dx}\arcsin(au)=\frac{au'}{\sqrt{1-a^2u^2}}$（常用于把$\sqrt{1-\cdots}$凑成平方）  
  Equivalent form: $\frac{d}{dx}\arcsin(au)=\frac{au'}{\sqrt{1-a^2u^2}}$ (often used to turn $\sqrt{1-\cdots}$ into a square)
- 等价写法：$\frac{d}{dx}\arctan(au)=\frac{au'}{1+a^2u^2}$（常用于把$1+$后面凑成平方）  
  Equivalent form: $\frac{d}{dx}\arctan(au)=\frac{au'}{1+a^2u^2}$ (often used to complete a square in $1+\cdots$)

### C. 直接“逆用”：常见不定积分识别 / Direct reverse-use: common indefinite integrals

- $\int\frac{u'}{\sqrt{a^2-u^2}}\,dx=\arcsin\left(\frac{u}{a}\right)+C$（$a>0$）  
  $\int\frac{u'}{\sqrt{a^2-u^2}}\,dx=\arcsin\left(\frac{u}{a}\right)+C$ ($a>0$)
- $\int\frac{u'}{a^2+u^2}\,dx=\frac{1}{a}\arctan\left(\frac{u}{a}\right)+C$（$a>0$）  
  $\int\frac{u'}{a^2+u^2}\,dx=\frac{1}{a}\arctan\left(\frac{u}{a}\right)+C$ ($a>0$)
- 等价写法：$\int\frac{u'}{1+a^2u^2}\,dx=\frac{1}{a}\arctan(au)+C$（$a>0$）  
  Equivalent form: $\int\frac{u'}{1+a^2u^2}\,dx=\frac{1}{a}\arctan(au)+C$ ($a>0$)
- $\int\frac{u'}{\sqrt{u^2-a^2}}\,dx=\ln\lvert u+\sqrt{u^2-a^2}\rvert+C$（更像反双曲$\operatorname{arcosh}$的结构）  
  $\int\frac{u'}{\sqrt{u^2-a^2}}\,dx=\ln\lvert u+\sqrt{u^2-a^2}\rvert+C$ (this pattern is closer to inverse hyperbolic $\operatorname{arcosh}$)

### D. 小例子（把$1$换成$a$） / Mini examples (replacing $1$ by $a$)

- $\int\frac{1}{\sqrt{9-x^2}}\,dx=\arcsin\left(\frac{x}{3}\right)+C$  
  $\int\frac{1}{\sqrt{9-x^2}}\,dx=\arcsin\left(\frac{x}{3}\right)+C$
- $\int\frac{1}{x^2+4}\,dx=\frac{1}{2}\arctan\left(\frac{x}{2}\right)+C$  
  $\int\frac{1}{x^2+4}\,dx=\frac{1}{2}\arctan\left(\frac{x}{2}\right)+C$
- $\int\frac{3}{9+(3x+1)^2}\,dx=\frac{1}{3}\arctan\left(\frac{3x+1}{3}\right)+C$  
  $\int\frac{3}{9+(3x+1)^2}\,dx=\frac{1}{3}\arctan\left(\frac{3x+1}{3}\right)+C$

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
[2025-08-29]: <../../Daily Notes/2025-08-29.md> "2025-08-29"
[trigonometric_functions]: trigonometric_functions.md "三角函数 / Trigonometric Functions"
[//end]: # "Autogenerated link references"
