# 圆轴扭转与极惯性矩 / Torsion of Circular Shafts and the Polar Moment of Inertia

> 材料时间 / Material dates：2026-10-29 至 2026-11-02 的学习对话整理，不是课堂原始记录。入口见 [[Courses/2026_fall/recent_learning_review]]。  
> Organized from study conversations dated 2026-10-29 to 2026-11-02; this is not an original class transcript.

## 问题与直觉 / Problem and Intuition

一端固定、另一端拧一根圆钢棒：靠近轴心的材料几乎不动，越靠外的材料转过的弧长越大，剪切变形越大，剪应力也越大。所以离轴心越远的材料，对抵抗扭矩贡献越大。$J$ 就是把这种“离轴心远近”的几何贡献加起来得到的量。

Twist a round bar fixed at one end: material near the axis barely moves, while outer material travels a longer arc, so shear strain and shear stress grow outward. Material farther from the axis contributes more to resisting torque, and $J$ adds up that geometric contribution.

## J 是什么 / What $J$ Is

$$J=\int_A\rho^2\,dA.$$

把截面上每一小块面积 $dA$ 乘以它到圆心距离 $\rho$ 的平方，再全部加起来。距离平方让外圈材料权重更大。

Multiply each area element by the square of its distance to the center and add them up; squaring the distance weights outer material heavily.

**实心圆的推导**：把截面切成同心圆环，半径 $\rho$、宽 $d\rho$ 的圆环面积约为 $dA=2\pi\rho\,d\rho$，于是

**Solid circle:** Slice the section into thin rings of area $dA=2\pi\rho\,d\rho$:

$$J=\int_0^c\rho^2(2\pi\rho)\,d\rho=2\pi\cdot\frac{c^4}{4}=\frac{\pi c^4}{2}=\frac{\pi d^4}{32}.$$

其中 $c$ 是外半径，$d$ 是直径。空心圆轴：$J=\frac\pi2(c_o^4-c_i^4)$。$J$ 的单位是长度的四次方（$\text{m}^4$、$\text{in}^4$）。

Here $c$ is the outer radius and $d$ the diameter. For a hollow shaft, $J=\frac\pi2(c_o^4-c_i^4)$. $J$ has units of length to the fourth power.

这里的 $J$ 与多元微积分换元中的 Jacobian 同字母、不同含义，见 [[Math_Calculus/6.Multivariable_Calculus/change_of_variables_jacobian]]。不过 $J=\int\rho^2\,dA$ 本身正是用极坐标面积元 $\rho\,d\rho\,d\theta$ 算出来的。

This $J$ shares its letter with the Jacobian from change of variables but means something else; still, $J=\int\rho^2\,dA$ is itself computed with the polar area element.

## 关键公式 / Key Formulas

$$\tau=\frac{T\rho}{J},\qquad\tau_{\max}=\frac{Tc}{J},\qquad\phi=\frac{TL}{JG}.$$

| 符号 / Symbol | 含义 / Meaning |
| --- | --- |
| $T$ | 截面上的内部扭矩，由截面法求得 / Internal torque at the section |
| $\rho$ | 所求点到轴心的距离 / Distance from the axis to the point |
| $J$ | 整个截面的极惯性矩，用外半径 $c$ 计算 / Polar moment of the whole section |
| $G$ | 剪切模量 / Shear modulus |
| $\phi$ | 长度 $L$ 上的扭转角（rad）/ Angle of twist over length $L$ |

**为什么 $\tau\propto\rho$**：扭转时截面像刚性圆盘一样转动，剪应变 $\gamma=\rho\phi/L$ 随 $\rho$ 线性增长；线弹性下 $\tau=G\gamma$。再由 $T=\int_A\rho\,\tau\,dA$ 的平衡关系，就得到 $\tau=T\rho/J$。

**Why $\tau\propto\rho$:** Cross-sections rotate like rigid disks, so $\gamma=\rho\phi/L$ grows linearly with $\rho$, and $\tau=G\gamma$ in the linear elastic range. Equilibrium $T=\int_A\rho\,\tau\,dA$ then gives $\tau=T\rho/J$.

**适用条件**：圆形（实心或空心）截面、均质、线弹性、小变形，且离加载点和截面突变处足够远。非圆截面不能用这组公式。

**Conditions:** circular solid or hollow section, homogeneous, linear elastic, small deformation, and away from load points and abrupt changes. Non-circular sections need other formulas.

## 完整例题 / Worked Example

对话题目中轴的半径 $c=35\ \text{mm}$，A 点所在截面内部扭矩 $T_A=500\ \text{N}\cdot\text{m}$，A 点 $\rho_A=35\ \text{mm}$，B 点 $\rho_B=20\ \text{mm}$。B 点所在截面的扭矩没有出现在可用材料中，因此下面把两点都放在 $T=500\ \text{N}\cdot\text{m}$ 的同一截面上演示。

In the conversation's problem, $c=35\ \text{mm}$, $T_A=500\ \text{N}\cdot\text{m}$, $\rho_A=35\ \text{mm}$, and $\rho_B=20\ \text{mm}$. The torque at B's section is not in the available material, so both points are placed on one section with $T=500\ \text{N}\cdot\text{m}$ here.

$$J=\frac{\pi(0.035)^4}{2}\approx2.357\times10^{-6}\ \text{m}^4.$$

$$\tau(35\ \text{mm})=\frac{500(0.035)}{2.357\times10^{-6}}\approx7.42\ \text{MPa},\qquad\tau(20\ \text{mm})=\frac{500(0.020)}{2.357\times10^{-6}}\approx4.24\ \text{MPa}.$$

单位检查：$\frac{\text{N}\cdot\text{m}\cdot\text{m}}{\text{m}^4}=\text{N/m}^2=\text{Pa}$。两者之比 $7.42/4.24=35/20$，符合 $\tau\propto\rho$。

Unit check: the result is in pascals. The ratio $7.42/4.24$ equals $35/20$, consistent with $\tau\propto\rho$.

## 易错点 / Common Mistakes

- 用 $\rho$ 代替 $c$ 计算 $J$：$J$ 永远用整个截面的外半径，$\rho$ 只用在 $\tau=T\rho/J$ 的分子。  
  Using $\rho$ in place of $c$ when computing $J$; $J$ always uses the outer radius.
- 把直径当半径代入 $\frac{\pi c^4}{2}$，结果差 16 倍。  
  Substituting the diameter into $\frac{\pi c^4}{2}$, which is off by a factor of 16.
- mm 与 m 混用：$c^4$ 会把单位误差放大到 $10^{12}$ 倍。  
  Mixing mm and m; the fourth power magnifies the error by $10^{12}$.
- 不同轴段的内部扭矩不同：先用截面法求每段的 $T$。  
  Internal torque differs between shaft segments; find each segment's $T$ first.

## 关联笔记 / Related Notes

- [[Physics/3.Mechanics_of_Materials/README]] — 本章学习顺序 / Study order for this chapter
- [[Physics/3.Mechanics_of_Materials/axial_stress_strain_thermal]] — 正应力与胡克定律 / Normal stress and Hooke's law
- [[Physics/3.Mechanics_of_Materials/engineering_units_us_customary]] — 功率、hp 与 $P=T\omega$ / Power, hp, and $P=T\omega$
- [[Math_Calculus/6.Multivariable_Calculus/polar_cylindrical_spherical_integrals]] — 极坐标面积元 / The polar area element

## 来源 / Sources

- ChatGPT 对话 / ChatGPT conversation：[解释10ksi来源](https://chatgpt.com/c/6ae69794-e770-832b-9901-f88a921d3aad) — $J=\frac{\pi c^4}{2}$ 的含义、圆环推导与 $\tau=T\rho/J$；对话在计算 $\tau_A$ 时截断 / The meaning of $J$, the ring derivation, and $\tau=T\rho/J$; the conversation was cut off while computing $\tau_A$.
- 截图中的轴与载荷图未包含在材料中。 / The shaft figure in the screenshot was not included.

[//begin]: # "Autogenerated link references for markdown compatibility"
[//end]: # "Autogenerated link references"
