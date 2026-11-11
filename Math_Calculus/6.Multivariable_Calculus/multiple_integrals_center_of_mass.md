# 多重积分与质心 / Multiple Integrals and Center of Mass

> 材料时间 / Material dates：2026-10-29 至 2026-11-02 的学习对话整理，不是课堂原始记录。入口见 [[Courses/2026_fall/recent_learning_review]]。  
> Organized from study conversations dated 2026-10-29 to 2026-11-02; this is not an original class transcript. See the linked review page for the overview.

## 问题与直觉 / Problem and Intuition

一块薄板的密度处处不同时，不能直接用“面积 × 密度”算质量。做法是把板切成无数小块：每一小块面积为 $dA$，密度近似为常数 $\delta(x,y)$，质量约为 $\delta\,dA$，再把所有小块加起来。二重积分就是这个“切小块—求和—取极限”的过程；三重积分把小块换成小体积 $dV$。

When a thin plate has variable density, mass is not simply area times density. Cut the plate into tiny pieces of area $dA$, treat the density $\delta(x,y)$ as constant on each piece, add the masses $\delta\,dA$, and take the limit. A double integral formalizes this; a triple integral uses volume pieces $dV$ instead.

质心问的是“这块板在哪一点能被一根针顶住保持平衡”。它是位置的加权平均，权重是质量，而不是面积。

The center of mass is the balance point of the plate. It is a mass-weighted average of position, not an area-weighted one.

## 定义与积分次序 / Definitions and Order of Integration

在 I 型区域 $R=\{a\le x\le b,\ g_1(x)\le y\le g_2(x)\}$ 上，若 $f$ 连续，二重积分可以写成累次积分：

On a type I region $R=\{a\le x\le b,\ g_1(x)\le y\le g_2(x)\}$ with continuous $f$, the double integral can be written as an iterated integral:

$$\iint_R f(x,y)\,dA=\int_a^b\int_{g_1(x)}^{g_2(x)}f(x,y)\,dy\,dx.$$

- 内层上下限可以含外层变量；最外层上下限必须是常数。  
  Inner bounds may depend on outer variables; the outermost bounds must be constants.
- 先对 $y$ 积分时，$x$ 当作常数；这和偏导时把其他变量当常数是同一个想法。  
  While integrating in $y$, treat $x$ as a constant, just as in partial differentiation.
- 三重积分同理：$\iiint_W f\,dV$ 写成三层累次积分，每层的上下限只能依赖更外层的变量。  
  Triple integrals work the same way: each layer's bounds may depend only on variables further outside.

## 质量、矩与质心公式 / Mass, Moments, and Center-of-Mass Formulas

$$M=\iint_R\delta\,dA,\qquad M_y=\iint_R x\,\delta\,dA,\qquad M_x=\iint_R y\,\delta\,dA,$$

$$\bar x=\frac{M_y}{M},\qquad\bar y=\frac{M_x}{M}.$$

为什么 $M_y$ 里乘的是 $x$？$M_y$ 是“关于 $y$ 轴的矩”，力臂是小块到 $y$ 轴的距离，而这个距离正是 $x$。所以 $M_y$ 给出 $\bar x$，$M_x$ 给出 $\bar y$，下标和结果坐标是“交叉”的。

Why does $M_y$ contain $x$? $M_y$ is the moment about the $y$-axis, and the lever arm to the $y$-axis is $x$. Hence $M_y$ gives $\bar x$ and $M_x$ gives $\bar y$; the subscripts cross over.

三维立体同理：$M=\iiint_W\delta\,dV$，$\bar x=\frac1M\iiint_W x\,\delta\,dV$，$\bar y$、$\bar z$ 类推。密度为常数时，质心退化为形心（centroid），与 [[Courses/2026_fall/emch_210/exam2_review]] 第 6 节的组合面积形心是同一概念的连续版本。

For solids, $M=\iiint_W\delta\,dV$ and $\bar x=\frac1M\iiint_W x\,\delta\,dV$, with $\bar y$ and $\bar z$ analogous. With constant density the center of mass reduces to the centroid; the composite-area centroid in the EMCH 210 review is the discrete version of the same idea.

## 完整例题：密度为 $x^2$ 的三角形薄板 / Worked Example: Triangle with Density $x^2$

**题目**：区域由 $y=6-x$、$x=0$、$y=0$ 围成，密度 $\delta(x,y)=x^2$，求质心。

**Problem:** The region is bounded by $y=6-x$, $x=0$, and $y=0$, with density $\delta(x,y)=x^2$. Find the center of mass.

**区域**：三角形顶点为 $(0,0)$、$(6,0)$、$(0,6)$，取 $0\le x\le6$，$0\le y\le6-x$。

**Region:** The triangle has vertices $(0,0)$, $(6,0)$, and $(0,6)$, so $0\le x\le6$ and $0\le y\le6-x$.

**质量 / Mass**

$$M=\int_0^6\int_0^{6-x}x^2\,dy\,dx=\int_0^6(6x^2-x^3)\,dx=\left[2x^3-\frac{x^4}{4}\right]_0^6=432-324=108.$$

**关于 $y$ 轴的矩 / Moment about the $y$-axis**

$$M_y=\int_0^6\int_0^{6-x}x^3\,dy\,dx=\int_0^6(6x^3-x^4)\,dx=\left[\frac32x^4-\frac{x^5}{5}\right]_0^6=1944-\frac{7776}{5}=\frac{1944}{5}.$$

**关于 $x$ 轴的矩 / Moment about the $x$-axis**

$$M_x=\int_0^6\int_0^{6-x}x^2y\,dy\,dx=\frac12\int_0^6x^2(6-x)^2\,dx=\frac12\left[12x^3-3x^4+\frac{x^5}{5}\right]_0^6=\frac{648}{5}.$$

**结果 / Result**

$$\bar x=\frac{1944/5}{108}=\frac{18}{5}=3.6,\qquad\bar y=\frac{648/5}{108}=\frac65=1.2.$$

**合理性检查**：均匀三角形的形心是 $(2,2)$。密度 $x^2$ 让右侧更重，所以 $\bar x$ 右移到 $3.6$；而右侧的三角形很“矮”，重的部分集中在 $y$ 较小处，所以 $\bar y$ 下降到 $1.2$。

**Sanity check:** A uniform triangle has centroid $(2,2)$. Density $x^2$ makes the right side heavier, moving $\bar x$ to $3.6$; the right side of the triangle is short, so the heavy material sits at small $y$ and $\bar y$ drops to $1.2$.

## 易错点 / Common Mistakes

- 把 $M_y$ 和 $M_x$ 对调：记住“关于哪条轴，就乘到那条轴的距离”。  
  Swapping $M_y$ and $M_x$: multiply by the distance to the axis named in the subscript.
- 质心公式漏掉密度：只有密度为常数时才能约掉 $\delta$。  
  Dropping the density: $\delta$ cancels only when it is constant.
- 最后一层积分漏掉系数。例如 $\int_0^1\int_0^1\int_0^{\sqrt{1-x^2}}xyz\,dy\,dx\,dz$：内层得 $\frac{xz(1-x^2)}2$，中层得 $\frac z8$，最外层 $\int_0^1\frac z8\,dz=\frac1{16}$；若忘记 $\int z\,dz=\frac{z^2}{2}$ 的 $\frac12$，会错得 $\frac18$。  
  Losing a factor in the last layer. For the integral above, the inner layer gives $\frac{xz(1-x^2)}2$, the middle gives $\frac z8$, and the outer gives $\frac1{16}$; forgetting the $\frac12$ from $\int z\,dz$ gives the wrong value $\frac18$.

## 关联笔记 / Related Notes

- [[Math_Calculus/6.Multivariable_Calculus/polar_cylindrical_spherical_integrals]] — 圆形区域改用极、柱、球坐标 / Polar, cylindrical, and spherical coordinates for round regions
- [[Math_Calculus/6.Multivariable_Calculus/change_of_variables_jacobian]] — 一般换元与 Jacobian / General change of variables and the Jacobian
- [[Courses/2026_fall/emch_210/exam2_review]] — 组合面积形心 / Composite-area centroids

## 来源 / Sources

- ChatGPT 对话 / ChatGPT conversation：[Calculate Paraboloid Volume](https://chatgpt.com/c/6ae3ed1c-993c-8325-811c-ddd552847d15) — 实际内容为质心、极坐标、换元与线性变换题，不是抛物面体积 / The content is center of mass, polar coordinates, and change of variables, not paraboloid volume.
- ChatGPT 对话 / ChatGPT conversation：[积分结果校正](https://chatgpt.com/c/6ae3fbc5-1894-832a-bbd6-439e745e3e26) — 三重积分最后一步的 $\frac1{16}$ / The final step of the $\frac1{16}$ triple integral.
- 原题截图未包含在整理材料中；题目条件以对话正文为准。 / Original screenshots were not included; problem data follow the conversation text.

[//begin]: # "Autogenerated link references for markdown compatibility"
[//end]: # "Autogenerated link references"
