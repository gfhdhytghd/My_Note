# 轴向应力、变形与热膨胀 / Axial Stress, Deformation, and Thermal Expansion

> 材料时间 / Material dates：2026-10-29 至 2026-11-02 的学习对话整理，不是课堂原始记录。入口见 [[Courses/2026_fall/recent_learning_review]]。  
> Organized from study conversations dated 2026-10-29 to 2026-11-02; this is not an original class transcript.

## 问题与直觉 / Problem and Intuition

两根柱子承受同样的 16 kip 压力，粗柱和细柱“吃力”的程度不同。比较材料是否安全，要看单位面积上的力，而不是总力。柱子受力后还会缩短；加热又会让它伸长。多根柱子一起顶住刚性块时，这两种变形必须协调。

Two posts under the same 16 kip load are not equally stressed if their areas differ. Safety depends on force per unit area, not total force. Loaded posts shorten, heated posts lengthen, and posts sharing a rigid cap must deform compatibly.

## 符号是什么 / What the Symbols Mean

| 符号 / Symbol | 含义 / Meaning | 常用单位 / Units |
| --- | --- | --- |
| $\sigma$ | 正应力：轴向力除以截面积，$\sigma=P/A$ / Normal stress | ksi, MPa |
| $\varepsilon$ | 正应变：长度变化比例，$\varepsilon=\delta/L$，无量纲 / Normal strain, dimensionless | in/in |
| $E$ | 杨氏模量：材料抵抗拉压变形的能力，越大越难变形 / Young's modulus | ksi, GPa |
| $\delta$ | 长度变化量 / Change in length | in, mm |
| $\alpha$ | 线膨胀系数：升温 $1^\circ$ 时自由伸长占原长的比例 / Coefficient of linear thermal expansion | $1/^\circ\mathrm F$, $1/^\circ\mathrm C$ |

小写 $\sigma$ 表示应力；大写 $\Sigma$ 在 $\sum F_y=0$ 中表示求和。线性代数笔记中用 $\Sigma$ 命名应力张量矩阵，那是矩阵的名字，见 [[Math_Linear-Algebra/eigenvalues_eigenvectors_eigenspaces]]。下标表示材料或构件，例如 $\sigma_s$ 是钢（steel），$\alpha_b$ 是黄铜（brass）。

Lowercase $\sigma$ is stress; uppercase $\Sigma$ in $\sum F_y=0$ means summation. The linear-algebra note uses $\Sigma$ as the name of a stress-tensor matrix. Subscripts name the material or member, for example $\sigma_s$ for steel and $\alpha_b$ for brass.

**例**：$16\ \text{kip}$ 压在 $8\ \text{in}^2$ 截面上，$\sigma=16/8=2\ \text{ksi}$（压应力），即平均每平方英寸承受 $2\ \text{kip}$。

**Example:** $16\ \text{kip}$ on $8\ \text{in}^2$ gives a compressive stress of $2\ \text{ksi}$.

## 关键公式与条件 / Key Formulas and Conditions

由胡克定律 $\sigma=E\varepsilon$ 和 $\varepsilon=\delta/L$：

From Hooke's law and the definition of strain:

$$\delta=\varepsilon L=\frac{\sigma L}{E}=\frac{PL}{AE},\qquad\delta_T=\alpha\,\Delta T\,L.$$

- 应力除以 $E$ 得到变形比例，再乘原长得到实际变形。  
  Stress divided by $E$ gives the strain; multiplying by length gives the deformation.
- 适用条件：线弹性范围；均质、等截面；轴力通过截面形心；离加载点和截面突变处足够远。  
  Conditions: linear elastic range, homogeneous prismatic member, load through the centroid, and locations away from load points and abrupt changes.
- 多段杆：$\delta=\sum\frac{P_iL_i}{A_iE_i}$，每段用自己的内力。  
  For segmented bars, sum $P_iL_i/(A_iE_i)$ using each segment's internal force.
- 自由热膨胀不产生应力；只有膨胀被约束时才产生热应力。  
  Free thermal expansion causes no stress; thermal stress appears only when expansion is restrained.

## 超静定问题的三步 / Three Steps for Statically Indeterminate Members

平衡方程不够时，还要用变形协调：

When equilibrium alone is not enough, add compatibility:

1. **平衡**：由自由体图写 $\sum F=0$。  
   **Equilibrium:** write $\sum F=0$ from the free-body diagram.
2. **协调**：根据几何约束写变形关系，例如刚性块不倾斜时各柱缩短量相等。  
   **Compatibility:** write the geometric constraint, such as equal shortening under a level rigid cap.
3. **力—变形关系**：把 $\delta=\frac{PL}{AE}\pm\alpha\Delta TL$ 代入协调方程。  
   **Force–deformation:** substitute $\delta=\frac{PL}{AE}\pm\alpha\Delta TL$ into the compatibility equation.

## 完整例题（自拟数据）/ Worked Example (Assumed Data)

对话中的题目是两根钢柱 A、B 与一根黄铜柱 C 支撑刚性块，黄铜柱升温。原题的载荷、截面和长度在截图中，未包含在材料里；下面用自拟数据演示同一方法。

The conversation's problem had steel posts A and B and a heated brass post C under a rigid cap. Its loads, areas, and lengths were in a screenshot that was not included, so the data below are assumed to demonstrate the method.

**条件**：总载荷 $P=60\ \text{kip}$ 对称作用；两根钢柱各 $A_s=2\ \text{in}^2$，$E_s=29000\ \text{ksi}$；黄铜柱 $A_b=3\ \text{in}^2$，$E_b=15000\ \text{ksi}$，$\alpha_b=9.80\times10^{-6}/^\circ\mathrm F$；三柱原长均为 $L=10\ \text{in}$；只有黄铜柱升温 $\Delta T=20^\circ\mathrm F$。

**Given:** $P=60\ \text{kip}$ applied symmetrically; each steel post has $A_s=2\ \text{in}^2$ and $E_s=29000\ \text{ksi}$; the brass post has $A_b=3\ \text{in}^2$, $E_b=15000\ \text{ksi}$, and $\alpha_b=9.80\times10^{-6}/^\circ\mathrm F$; all posts have $L=10\ \text{in}$; only the brass post warms by $20^\circ\mathrm F$.

**平衡 / Equilibrium**：$2F_s+F_b=60$。

**协调 / Compatibility**（缩短量取正）：钢柱只受压缩短；黄铜柱的净缩短量 = 受压缩短 − 热伸长。

Taking shortening as positive, steel shortens from load only, while brass shortens from load minus its thermal expansion:

$$\frac{F_sL}{A_sE_s}=\frac{F_bL}{A_bE_b}-\alpha_b\Delta T\,L.$$

$L$ 两边约去。代入数值并与平衡方程联立，得 $F_s\approx18.44\ \text{kip}$，$F_b\approx23.12\ \text{kip}$。

$L$ cancels. Solving with equilibrium gives $F_s\approx18.44\ \text{kip}$ and $F_b\approx23.12\ \text{kip}$.

**应力与变形 / Stresses and deformation**：$\sigma_s=\frac{18.44}{2}\approx9.22\ \text{ksi}$，$\sigma_b=\frac{23.12}{3}\approx7.71\ \text{ksi}$（均为压应力）；共同缩短量 $\delta=\frac{18.44(10)}{2(29000)}\approx0.00318\ \text{in}$。

Both stresses are compressive; the common shortening is about $0.00318\ \text{in}$.

**解读**：不升温时同一组数据给出 $F_s\approx21.61\ \text{kip}$，$F_b\approx16.77\ \text{kip}$。黄铜受热“想变长”，却被刚性块压住，于是它分担了更多载荷。

**Interpretation:** Without heating, the same data give $F_s\approx21.61\ \text{kip}$ and $F_b\approx16.77\ \text{kip}$. The heated brass tries to lengthen, is held by the cap, and therefore carries more load.

## 易错点 / Common Mistakes

- 把 $\alpha\Delta TL$ 的符号写反：先约定“缩短为正”或“伸长为正”，再逐项判断。  
  Reversing the sign of $\alpha\Delta TL$; fix whether shortening or lengthening is positive, then check each term.
- 混用 $\alpha_b$ 的下标：$b$ 指 brass（材料），不一定是图中的 B 柱。  
  Misreading $\alpha_b$: $b$ means brass, not necessarily post B.
- 单位不统一：$E$ 用 ksi 时力用 kip、面积用 in²。  
  Mixing units: with $E$ in ksi, use kip and in².

## 关联笔记 / Related Notes

- [[Physics/3.Mechanics_of_Materials/README]] — 本章学习顺序 / Study order for this chapter
- [[Physics/3.Mechanics_of_Materials/engineering_units_us_customary]] — kip、ksi 换算 / kip and ksi conversions
- [[Physics/3.Mechanics_of_Materials/torsion_circular_shafts]] — 扭转中的剪应力 / Shear stress in torsion
- [[Courses/2026_fall/emch_210/exam2_review]] — 自由体图与平衡方程 / Free-body diagrams and equilibrium
- [[Math_Linear-Algebra/eigenvalues_eigenvectors_eigenspaces]] — 应力张量与主应力 / Stress tensors and principal stresses

## 来源 / Sources

- ChatGPT 对话 / ChatGPT conversation：[解释10ksi来源](https://chatgpt.com/c/6ae69794-e770-832b-9901-f88a921d3aad) — $\sigma$ 的含义、$\sigma L/E$、$\alpha_b$ 与三柱协调方程 / Meaning of $\sigma$, $\sigma L/E$, $\alpha_b$, and the three-post compatibility equation.
- 对话标题中的“10 ksi”在可用正文中没有出现推导；本页不复述该数值来源。 / The “10 ksi” in the title has no derivation in the available text, so this page does not reconstruct it.

[//begin]: # "Autogenerated link references for markdown compatibility"
[//end]: # "Autogenerated link references"
