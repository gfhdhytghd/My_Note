# 多元函数的极限、偏导与梯度 / Multivariable Limits, Partial Derivatives, and Gradients

## 等值集与多元函数图像 / Level Sets and Graphs of Multivariable Functions

二元函数 $z=f(x,y)$ 的图像是三维曲面；固定函数值 $f(x,y)=c$ 得到等高线。三元函数 $w=f(x,y,z)$ 的完整图像位于四维空间，通常改用等值面 $f(x,y,z)=c$ 表示其空间分布。 / The graph of a two-variable function $z=f(x,y)$ is a surface in three dimensions, and fixing $f(x,y)=c$ gives a level curve. The full graph of a three-variable function $w=f(x,y,z)$ lies in four dimensions, so level surfaces $f(x,y,z)=c$ are usually used to represent its spatial distribution.

在相邻等高线的函数值之差相同时，等高线越密，单位距离内的函数值变化通常越快。梯度进一步给出局部最陡上升的精确方向与速率。 / When adjacent contours differ by equal function-value increments, closer contours usually indicate a faster change per unit distance. The gradient gives the exact local direction and rate of steepest increase.

典型等值面如下；更完整的曲面分类见 [[Math_Calculus/6.Multivariable_Calculus/quadric_surfaces]]。 / Typical level surfaces are listed below; see the linked note for a fuller classification of quadric surfaces.

| 等值面 / Level surface | $c>0$ | $c=0$ | $c<0$ |
| --- | --- | --- | --- |
| $x^2+y^2+z^2=c$ | 半径 $\sqrt c$ 的球面 / Sphere of radius $\sqrt c$ | 原点 / Origin | 空集 / Empty set |
| $x^2+y^2-z^2=c$ | 单叶双曲面 / One-sheet hyperboloid | 双圆锥面 / Double cone | 双叶双曲面 / Two-sheet hyperboloid |

## 多元函数的极限 / Limits of Multivariable Functions

对 $f:D\subseteq\mathbb R^n\to\mathbb R$，若 $\mathbf a$ 是 $D$ 的聚点，则 $\lim_{\mathbf x\to\mathbf a}f(\mathbf x)=L$ 表示当定义域内的点 $\mathbf x$ 从任意方向趋近 $\mathbf a$ 时，函数值都趋近同一个 $L$。严格地说： / For $f:D\subseteq\mathbb R^n\to\mathbb R$, where $\mathbf a$ is an accumulation point of $D$, $\lim_{\mathbf x\to\mathbf a}f(\mathbf x)=L$ means that $f(\mathbf x)$ approaches the same value $L$ as domain points $\mathbf x$ approach $\mathbf a$ from every direction. Formally:

$$
\forall\varepsilon>0,\ \exists\delta>0:\quad
0<\|\mathbf x-\mathbf a\|<\delta
\Longrightarrow
|f(\mathbf x)-L|<\varepsilon.
$$

- **直接代入 / Direct substitution：**若函数由连续函数通过和、积、复合与非零分母的商组成，通常可直接代入。 / A function built from continuous functions by sums, products, compositions, and quotients with nonzero denominators can usually be evaluated by substitution.
- **路径检验 / Path test：**找到两条路径产生不同极限即可证明极限不存在；若若干路径结果相同，甚至所有直线路径都相同，仍不足以证明极限存在。 / Two paths producing different limits prove nonexistence; agreement along several paths, or even all straight-line paths, does not prove existence.
- **夹逼法 / Squeeze theorem：**若 $|f(\mathbf x)|\leq g(\mathbf x)$ 且 $g(\mathbf x)\to0$，则 $f(\mathbf x)\to0$。 / If $|f(\mathbf x)|\leq g(\mathbf x)$ and $g(\mathbf x)\to0$, then $f(\mathbf x)\to0$.

例如 $f(x,y)=(x^2-y^2)/(x^2+y^2)$：沿 $y=0$ 有 $f=1$，沿 $x=0$ 有 $f=-1$，所以原点处的极限不存在。 / For $f(x,y)=(x^2-y^2)/(x^2+y^2)$, the path $y=0$ gives $f=1$, while $x=0$ gives $f=-1$, so the limit at the origin does not exist.

## 连续性 / Continuity

函数在 $\mathbf a$ 处连续，当且仅当 $f(\mathbf a)$ 有定义、极限存在，并且 $\lim_{\mathbf x\to\mathbf a}f(\mathbf x)=f(\mathbf a)$。极限只考察目标点附近的函数值，不要求目标点本身有定义；连续性则把极限值与函数值连接起来。 / A function is continuous at $\mathbf a$ exactly when $f(\mathbf a)$ is defined, the limit exists, and $\lim_{\mathbf x\to\mathbf a}f(\mathbf x)=f(\mathbf a)$. A limit concerns values near the target point and does not require the function to be defined there; continuity connects the limiting value to the actual function value.

## 一阶偏导数 / First-Order Partial Derivatives

求某个变量的偏导时，只让该变量变化，把其他变量视为常数；普通的乘积、商与链式法则仍然适用。 / To take a partial derivative with respect to one variable, vary only that variable and treat all others as constants; the ordinary product, quotient, and chain rules still apply.

$$
f_x=\frac{\partial f}{\partial x},\qquad
f_y=\frac{\partial f}{\partial y},\qquad
f_z=\frac{\partial f}{\partial z}.
$$

例如，若 $f(x,y,z)=x^2y+ye^{xz}+z^3$，则： / For example, if $f(x,y,z)=x^2y+ye^{xz}+z^3$, then:

$$
f_x=2xy+yze^{xz},\qquad
f_y=x^2+e^{xz},\qquad
f_z=xye^{xz}+3z^2.
$$

## 高阶与混合偏导 / Higher-Order and Mixed Partial Derivatives

二阶偏导是连续求两次偏导。下标按从左到右的操作顺序读取，而分数记号的分母按从右到左读取： / A second-order partial derivative is obtained by differentiating twice. Read subscripts from left to right, but read the denominator in fractional notation from right to left:

$$
f_{xy}=(f_x)_y=\frac{\partial^2f}{\partial y\partial x}.
$$

若相关混合偏导在目标区域内连续，Clairaut 定理允许交换求导顺序：$f_{xy}=f_{yx}$。计算高阶混合偏导时，可以先选会让某些项直接变为零的变量，再交换求导顺序，从而减少不必要的计算。 / If the relevant mixed partials are continuous in the region, Clairaut's theorem permits $f_{xy}=f_{yx}$. For higher-order mixed partials, first differentiate with respect to variables that eliminate terms, then exchange the order to avoid unnecessary work.

## 梯度与方向导数 / Gradient and Directional Derivatives

梯度由各个一阶偏导组成： / The gradient consists of the first-order partial derivatives:

$$
\nabla f=\langle f_x,f_y\rangle
\quad\text{或}\quad
\nabla f=\langle f_x,f_y,f_z\rangle.
$$

在点 $P$ 画梯度向量时，把箭头起点放在 $P$，按 $\nabla f(P)$ 的分量决定方向。梯度垂直于经过 $P$ 的等高线或等值面，并指向函数值增长最快的方向；其长度 $\|\nabla f(P)\|$ 是最大增长率。 / To draw the gradient at $P$, place the arrow's tail at $P$ and use the components of $\nabla f(P)$ for its direction. The gradient is perpendicular to the level curve or surface through $P$, points in the direction of steepest increase, and has magnitude $\|\nabla f(P)\|$, the maximum rate of increase.

若 $\mathbf u$ 是单位向量，则沿 $\mathbf u$ 的方向导数为： / If $\mathbf u$ is a unit vector, the directional derivative along $\mathbf u$ is:

$$
D_{\mathbf u}f(P)=\nabla f(P)\cdot\mathbf u.
$$

- $D_{\mathbf u}f>0$：沿该方向函数增大。 / The function increases in that direction.
- $D_{\mathbf u}f<0$：沿该方向函数减小。 / The function decreases in that direction.
- $D_{\mathbf u}f=0$：该方向与梯度垂直，通常沿等值集的切向。 / The direction is perpendicular to the gradient and is typically tangent to the level set.
- 若 $\nabla f(P)=\mathbf0$，则所有单位方向的一阶方向导数都为零，但不能仅凭这一点判断极值。 / If $\nabla f(P)=\mathbf0$, every first-order directional derivative is zero, but this alone does not determine whether an extremum occurs.

## 路径链式法则 / Chain Rule Along a Path

若标量函数 $f$ 沿可微路径 $\mathbf r(t)$ 变化，则复合函数的变化率为： / If a scalar function $f$ is evaluated along a differentiable path $\mathbf r(t)$, the rate of change of the composite function is:

$$
\boxed{\frac{d}{dt}f(\mathbf r(t))=\nabla f(\mathbf r(t))\cdot\mathbf r'(t)}.
$$

二维分量形式为： / In two-dimensional component form:

$$
\frac{d}{dt}f(x(t),y(t))
=f_x(x(t),y(t))x'(t)+f_y(x(t),y(t))y'(t).
$$

这里 $\mathbf r'(t)$ 是路径的速度向量，点积同时考虑函数在各坐标方向的敏感度与实际运动方向。若速度为 $q=\|\mathbf r'(t)\|>0$，单位切向量为 $\mathbf T=\mathbf r'(t)/q$，则 $\frac{d}{dt}f(\mathbf r(t))=qD_{\mathbf T}f$。 / Here $\mathbf r'(t)$ is the path velocity. The dot product combines the function's sensitivity in each coordinate direction with the actual direction of motion. If the speed is $q=\|\mathbf r'(t)\|>0$, the unit tangent is $\mathbf T=\mathbf r'(t)/q$, so $\frac{d}{dt}f(\mathbf r(t))=qD_{\mathbf T}f$.

## 线性近似与全微分 / Linear Approximation and the Total Differential

若 $f$ 在点 $(a,b,c)$ 附近可微，则： / If $f$ is differentiable near $(a,b,c)$, then:

$$
f(a+\Delta x,b+\Delta y,c+\Delta z)
\approx f(a,b,c)+f_x\Delta x+f_y\Delta y+f_z\Delta z.
$$

相应的全微分为 $df=f_x\,dx+f_y\,dy+f_z\,dz$。各偏导存在并不自动保证函数可微；可微性要求这个线性表达式能统一控制所有方向的一阶误差。 / The corresponding total differential is $df=f_x\,dx+f_y\,dy+f_z\,dz$. The existence of all partial derivatives does not by itself guarantee differentiability; differentiability requires this linear expression to control the first-order error in every direction.

## 偏微分方程示例 / Example of a Partial Differential Equation

偏微分方程包含未知的多元函数及其偏导数。例如一维热方程 $u_t=ku_{xx}$（$k>0$），其中 $u(x,t)$ 表示位置 $x$、时间 $t$ 的温度，$k$ 是热扩散率；具体解还需要初始条件和边界条件。 / A partial differential equation contains an unknown multivariable function and its partial derivatives. For example, the one-dimensional heat equation is $u_t=ku_{xx}$ ($k>0$), where $u(x,t)$ is the temperature at position $x$ and time $t$, and $k$ is the thermal diffusivity; a specific solution also requires initial and boundary conditions.

## 快速检查 / Quick Check

1. 求偏导前，先圈出当前求导变量，其余变量全部视为常数。 / Before differentiating, identify the active variable and treat every other variable as constant.
2. 判断极限不存在时找不同路径；证明极限存在时控制整个邻域。 / Use different paths to disprove a limit; control the entire neighborhood to prove one.
3. 方向导数中的方向向量必须先单位化。 / Normalize the direction vector before using it in a directional derivative.
4. 路径变化率使用 $\nabla f(\mathbf r(t))\cdot\mathbf r'(t)$，不要遗漏路径速度。 / For change along a path, use $\nabla f(\mathbf r(t))\cdot\mathbf r'(t)$ and do not omit the path velocity.

## 相关笔记 / Related Notes

- [[Math_Calculus/6.Multivariable_Calculus/traces_and_contour_maps]] — 截线、等高线与等高线图 / Traces, level curves, and contour maps
- [[Math_Calculus/6.Multivariable_Calculus/quadric_surfaces]] — 二次曲面与等值面示例 / Quadric surfaces and level-surface examples
- [[Math_Calculus/6.Multivariable_Calculus/vector_valued_functions]] — 向量值函数与路径 / Vector-valued functions and paths
- [[Math_Calculus/2.Limit/limits]] — 单变量极限基础 / Single-variable limit basics

## 来源 / Sources

- [[Daily Notes/2026-09-03]] — 三元函数极限、偏导与梯度 / Limits, partial derivatives, and gradients
- [[Daily Notes/2026-09-18]] — 等值面、多元极限与连续性 / Level surfaces, multivariable limits, and continuity
- [[Daily Notes/2026-09-21]] — 高阶偏导、Clairaut 定理与热方程 / Higher-order partials, Clairaut's theorem, and the heat equation
- [[Daily Notes/2026-09-23]] — 梯度绘图与路径链式法则 / Drawing gradients and the path chain rule

[//begin]: # "Autogenerated link references for markdown compatibility"
[//end]: # "Autogenerated link references"
