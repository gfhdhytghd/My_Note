# 三角函数的夹逼定理 / Squeeze Theorem for Trigonometric Functions

## 1. 三角函数的基本不等式 / Basic Trigonometric Inequalities

### 1.1 正弦函数的基本性质 / Basic Properties of Sine Function

**重要不等式 / Important Inequality：**  
对于任意实数 $x$，有：  
For any real number $x$, we have:

$$-1 \leq \sin x \leq 1$$

**几何意义 / Geometric Meaning：**  
正弦函数的值域为 $[-1, 1]$，因此 $\sin x$ 的绝对值不超过 $1$。  
The range of sine function is $[-1, 1]$, so the absolute value of $\sin x$ is at most $1$.

### 1.2 余弦函数的基本性质 / Basic Properties of Cosine Function

**重要不等式 / Important Inequality：**  
对于任意实数 $x$，有：  
For any real number $x$, we have:

$$-1 \leq \cos x \leq 1$$

---

## 2. 经典三角函数极限 / Classic Trigonometric Limits

### 2.1 $\lim_{x \to 0} \frac{\sin x}{x} = 1$

**这是微积分中最重要的极限之一 / This is one of the most important limits in calculus**

**证明方法 / Proof Method：** 使用夹逼定理  
**Proof Method:** Using the Squeeze Theorem

**步骤 / Steps：**

1. **建立不等式关系 / Establish Inequality Relationship：**

   在单位圆上，对于 $0 < x < \frac{\pi}{2}$：
   On the unit circle, for $0 < x < \frac{\pi}{2}$:

   $$\sin x < x < \tan x$$

   其中 $\tan x = \frac{\sin x}{\cos x}$  
   where $\tan x = \frac{\sin x}{\cos x}$

2. **变形得到夹逼条件 / Transform to Squeeze Condition：**

   从 $\sin x < x$ 得到：
   From $\sin x < x$, we get:
   
   $$\frac{\sin x}{x} < 1$$

   从 $x < \tan x = \frac{\sin x}{\cos x}$ 得到：
   From $x < \tan x = \frac{\sin x}{\cos x}$, we get:
   
   $$\cos x < \frac{\sin x}{x}$$

3. **应用夹逼定理 / Apply Squeeze Theorem：**

   当 $x \to 0^+$ 时：
   As $x \to 0^+$:

   $$\cos x \leq \frac{\sin x}{x} \leq 1$$

   且 $\lim_{x \to 0^+} \cos x = 1$，$\lim_{x \to 0^+} 1 = 1$  
   and $\lim_{x \to 0^+} \cos x = 1$, $\lim_{x \to 0^+} 1 = 1$

   因此：$\lim_{x \to 0^+} \frac{\sin x}{x} = 1$  
   Therefore: $\lim_{x \to 0^+} \frac{\sin x}{x} = 1$

4. **考虑负值 / Consider Negative Values：**

   对于 $x < 0$，设 $x = -t$（$t > 0$）：
   For $x < 0$, let $x = -t$ (where $t > 0$):

   $$\frac{\sin x}{x} = \frac{\sin(-t)}{-t} = \frac{-\sin t}{-t} = \frac{\sin t}{t}$$

   因此：$\lim_{x \to 0^-} \frac{\sin x}{x} = \lim_{t \to 0^+} \frac{\sin t}{t} = 1$  
   Therefore: $\lim_{x \to 0^-} \frac{\sin x}{x} = \lim_{t \to 0^+} \frac{\sin t}{t} = 1$

**结论 / Conclusion：**
$$\lim_{x \to 0} \frac{\sin x}{x} = 1$$

### 2.2 $\lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2}$

**证明方法 / Proof Method：** 使用三角恒等式和夹逼定理  
**Proof Method:** Using trigonometric identity and Squeeze Theorem

**步骤 / Steps：**

1. **使用三角恒等式 / Use Trigonometric Identity：**

   $$1 - \cos x = 2\sin^2\left(\frac{x}{2}\right)$$

2. **建立不等式 / Establish Inequality：**

   由于 $-1 \leq \sin\left(\frac{x}{2}\right) \leq 1$，有：
   Since $-1 \leq \sin\left(\frac{x}{2}\right) \leq 1$, we have:

   $$0 \leq \sin^2\left(\frac{x}{2}\right) \leq 1$$

3. **应用夹逼定理 / Apply Squeeze Theorem：**

   $$\frac{1 - \cos x}{x^2} = \frac{2\sin^2\left(\frac{x}{2}\right)}{x^2} = \frac{1}{2} \cdot \frac{\sin^2\left(\frac{x}{2}\right)}{\left(\frac{x}{2}\right)^2}$$

   设 $u = \frac{x}{2}$，当 $x \to 0$ 时 $u \to 0$：
   Let $u = \frac{x}{2}$, as $x \to 0$ we have $u \to 0$:

   $$\lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2} \cdot \lim_{u \to 0} \frac{\sin^2 u}{u^2} = \frac{1}{2} \cdot \left(\lim_{u \to 0} \frac{\sin u}{u}\right)^2 = \frac{1}{2} \cdot 1^2 = \frac{1}{2}$$

**结论 / Conclusion：**
$$\lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2}$$

---

## 3. 夹逼定理在三角函数中的其他应用 / Other Applications of Squeeze Theorem with Trigonometric Functions

### 3.1 $\lim_{x \to 0} x \sin\left(\frac{1}{x}\right) = 0$

**证明 / Proof：**

由于 $-1 \leq \sin\left(\frac{1}{x}\right) \leq 1$，有：
Since $-1 \leq \sin\left(\frac{1}{x}\right) \leq 1$, we have:

$$-|x| \leq x \sin\left(\frac{1}{x}\right) \leq |x|$$

当 $x \to 0$ 时：
As $x \to 0$:

$$\lim_{x \to 0} (-|x|) = 0 \quad \text{and} \quad \lim_{x \to 0} |x| = 0$$

因此，由夹逼定理：
Therefore, by the Squeeze Theorem:

$$\lim_{x \to 0} x \sin\left(\frac{1}{x}\right) = 0$$

### 3.2 $\lim_{x \to 0} \frac{\tan x}{x} = 1$

**证明 / Proof：**

$$\lim_{x \to 0} \frac{\tan x}{x} = \lim_{x \to 0} \frac{\sin x}{x \cos x} = \lim_{x \to 0} \frac{\sin x}{x} \cdot \frac{1}{\cos x} = 1 \cdot \frac{1}{1} = 1$$

### 3.3 $\lim_{x \to 0} \frac{\sin(ax)}{bx} = \frac{a}{b}$ （其中 $b \neq 0$）

**证明 / Proof：**

设 $u = ax$，当 $x \to 0$ 时 $u \to 0$：
Let $u = ax$, as $x \to 0$ we have $u \to 0$:

$$\lim_{x \to 0} \frac{\sin(ax)}{bx} = \lim_{x \to 0} \frac{a}{b} \cdot \frac{\sin(ax)}{ax} = \frac{a}{b} \cdot \lim_{u \to 0} \frac{\sin u}{u} = \frac{a}{b} \cdot 1 = \frac{a}{b}$$

---

## 4. 重要技巧和注意事项 / Important Techniques and Notes

### 4.1 三角函数极限计算的一般步骤 / General Steps for Trigonometric Limit Calculations

1. **识别类型 / Identify the Type：** 确定是否为 $\frac{0}{0}$ 型未定式  
   Determine if it's a $\frac{0}{0}$ indeterminate form

2. **寻找基本极限 / Find Basic Limits：** 利用 $\lim_{x \to 0} \frac{\sin x}{x} = 1$  
   Use $\lim_{x \to 0} \frac{\sin x}{x} = 1$

3. **变量替换 / Variable Substitution：** 将复杂表达式化为基本形式  
   Transform complex expressions to basic forms

4. **应用夹逼定理 / Apply Squeeze Theorem：** 当直接计算困难时  
   When direct calculation is difficult

### 4.2 常见错误 / Common Mistakes

- **忘记考虑定义域 / Forgetting Domain Considerations：** 某些三角函数在特定点无定义  
  Some trigonometric functions are undefined at certain points

- **角度单位混淆 / Angle Unit Confusion：** 注意弧度与角度的区别  
  Be careful about the difference between radians and degrees

- **夹逼条件不完整 / Incomplete Squeeze Conditions：** 确保不等式关系在所有相关点都成立  
  Ensure inequality relationships hold at all relevant points

---

## 5. 相关链接 / Related Links

- [[limit_theorems]] - 极限定理基础
- [[limits]] - 极限基本概念
- [[trigonometric_functions]] - 三角函数基础
- [[MATH_140_教学大纲总结]] - 课程大纲
- [[derivatives_basics]] - 导数基础
- [[derivative_rules]] - 求导法则

---

## 标签 / Tags
#夹逼定理 #三角函数 #极限 #微积分 #SqueezeTheorem #TrigonometricLimits

---

*创建日期: 2025年1月18日*  
*对应课程: MATH 140 第3-4周内容*

[//begin]: # "Autogenerated link references for markdown compatibility"
[limit_theorems]: limit_theorems.md "极限定理 / Limit Theorems"
[limits]: limits.md "极限 / Limits"
[trigonometric_functions]: ../1.Precalculus/trigonometric_functions.md "三角函数 / Trigonometric Functions"
[MATH_140_教学大纲总结]: ../MATH_140_%E6%95%99%E5%AD%A6%E5%A4%A7%E7%BA%B2%E6%80%BB%E7%BB%93.md "MATH 140 微积分与解析几何 I - 教学大纲总结"
[//end]: # "Autogenerated link references"
