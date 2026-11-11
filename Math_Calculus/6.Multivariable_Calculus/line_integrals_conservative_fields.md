# 线积分、保守场与势函数 / Line Integrals, Conservative Fields, and Potential Functions

> 材料时间 / Material dates：2026-10-29 至 2026-11-02 的学习对话整理，不是课堂原始记录。入口见 [[Courses/2026_fall/recent_learning_review]]。  
> Organized from study conversations dated 2026-10-29 to 2026-11-02; this is not an original class transcript.

## 问题与直觉 / Problem and Intuition

推着购物车沿一条弯路走，空间中每一点都有一个力。每走一小段 $d\mathbf r$，只有力沿运动方向的分量真正做功：同向为正，垂直为零，反向为负。把整条路上的小贡献加起来，就是向量线积分。

Push a cart along a curved path through a force field. On each small step $d\mathbf r$, only the component of force along the motion does work: positive when aligned, zero when perpendicular, negative when opposed. Adding these contributions gives the vector line integral.

普通定积分累加“有符号面积”；向量线积分累加“沿路径的切向贡献”。

An ordinary definite integral adds signed area; a vector line integral adds tangential contributions along a path.

## 场与势 / Fields and Potentials

- **标量场**：每个位置对应一个数，例如温度 $T(x,y,z)$ 或海拔 $f(x,y)$。  
  **Scalar field:** a number at each point, such as temperature or altitude.
- **向量场**：每个位置对应一个箭头，例如风速 $\mathbf F(x,y,z)=\langle P,Q,R\rangle$。场是“整片空间的箭头”，不是单独一个向量。  
  **Vector field:** an arrow at each point, such as wind velocity. A field is the whole collection of arrows, not one vector.
- **梯度**把标量场变成向量场：$\nabla f$ 指向 $f$ 增长最快的方向，长度是最大增长率，详见 [[Math_Calculus/6.Multivariable_Calculus/limits_partials_and_gradient]]。  
  **The gradient** turns a scalar field into a vector field pointing toward fastest increase; see the linked gradient note.
- **势函数**：若存在标量函数 $f$ 使 $\mathbf F=\nabla f$，则 $f$ 是 $\mathbf F$ 的势函数，$\mathbf F$ 称为保守场。势函数可以理解为向量场的“多元原函数”。  
  **Potential function:** if $\mathbf F=\nabla f$ for some scalar $f$, then $f$ is a potential and $\mathbf F$ is conservative. A potential is a multivariable antiderivative of the field.

例：$f=x^2+y^2$ 像一个碗，$\nabla f=\langle2x,2y\rangle$ 处处指向远离原点的“上坡”方向。旋转场 $\langle-y,x\rangle$ 绕原点打转，在整个平面上找不到势函数。

Example: $f=x^2+y^2$ is a bowl and $\nabla f=\langle2x,2y\rangle$ points uphill away from the origin. The rotating field $\langle-y,x\rangle$ circles the origin and has no potential on the whole plane.

## 两种线积分 / Two Kinds of Line Integrals

设 $C$ 由 $\mathbf r(t)$，$a\le t\le b$ 参数化：

Let $C$ be parametrized by $\mathbf r(t)$ for $a\le t\le b$:

$$\int_C f\,ds=\int_a^b f(\mathbf r(t))\,\|\mathbf r'(t)\|\,dt,\qquad\int_C\mathbf F\cdot d\mathbf r=\int_a^b\mathbf F(\mathbf r(t))\cdot\mathbf r'(t)\,dt.$$

- 标量线积分 $\int_C f\,ds$ 累加标量，例如铁丝线密度为 $f$ 时的质量；与走向无关。  
  The scalar line integral adds a scalar, such as the mass of a wire with linear density $f$; it does not depend on direction.
- 向量线积分 $\int_C\mathbf F\cdot d\mathbf r$ 累加切向分量，例如功；反向走时变号。  
  The vector line integral adds tangential components, such as work; reversing the direction flips its sign.

## 线积分基本定理 / Fundamental Theorem for Line Integrals

**结论**：若 $C$ 分段光滑，从 $P$ 到 $Q$，且 $\nabla f$ 在包含 $C$ 的开集上连续，则

**Result:** If $C$ is piecewise smooth from $P$ to $Q$ and $\nabla f$ is continuous on an open set containing $C$, then

$$\int_C\nabla f\cdot d\mathbf r=f(Q)-f(P).$$

**为什么**：由路径链式法则，$\frac{d}{dt}f(\mathbf r(t))=\nabla f(\mathbf r(t))\cdot\mathbf r'(t)$。所以被积式正好是 $f$ 沿路径的变化率，再用单变量微积分基本定理，中间的升降全部抵消，只剩终点减起点。

**Why:** By the chain rule along a path, the integrand is the rate of change of $f$ along the curve. The single-variable fundamental theorem then cancels every intermediate rise and fall, leaving the end value minus the start value.

几何上，在山上从 $P$ 走到 $Q$，不论绕多远，海拔变化只取决于两端高度。推论：在保守场中，线积分与路径无关；闭合路径积分 $\oint_C\mathbf F\cdot d\mathbf r=0$。在连通开区域上，“保守”、“路径无关”和“任意闭路积分为零”三者等价。

Geometrically, the altitude change from $P$ to $Q$ depends only on the endpoints. Consequently, line integrals of conservative fields are path-independent and vanish around closed loops. On a connected open region, being conservative, path independence, and zero circulation around every closed loop are equivalent.

## 怎样判断保守场 / Testing for a Conservative Field

二维 $\mathbf F=\langle P,Q\rangle$：若 $\mathbf F=\nabla f$，则 $P=f_x$，$Q=f_y$，由 Clairaut 定理 $f_{xy}=f_{yx}$ 得必要条件

In 2-D, if $\mathbf F=\nabla f$, then Clairaut's theorem gives the necessary condition

$$\frac{\partial P}{\partial y}=\frac{\partial Q}{\partial x}.$$

- 不相等 → 一定不是保守场。例：$\langle-y,x\rangle$ 有 $P_y=-1\ne1=Q_x$，绕单位圆一周积分为 $2\pi\ne0$。  
  If they differ, the field is not conservative. For $\langle-y,x\rangle$, $P_y=-1\ne1=Q_x$, and its circulation around the unit circle is $2\pi$.
- 相等 → 还要求区域**单连通**（没有洞）且偏导连续，才能保证是保守场。反例：$\mathbf F=\left\langle\frac{-y}{x^2+y^2},\frac{x}{x^2+y^2}\right\rangle$ 在去掉原点的平面上满足 $P_y=Q_x$，但绕单位圆积分仍为 $2\pi$。  
  If they agree, the region must also be simply connected with continuous partials. The field above satisfies $P_y=Q_x$ on the punctured plane, yet its circulation around the unit circle is still $2\pi$.
- 三维 $\langle P,Q,R\rangle$：在单连通区域上检查 $P_y=Q_x$，$P_z=R_x$，$Q_z=R_y$（即 $\nabla\times\mathbf F=\mathbf0$）。  
  In 3-D on a simply connected region, check all three cross-partial equalities, which is the condition $\nabla\times\mathbf F=\mathbf0$.

## 求势函数：为什么“积分常数”是函数 / Finding a Potential: Why the Constant Is a Function

对 $f_x$ 关于 $x$ 积分时，其他变量被当作常数。任何只含 $y,z$ 的函数 $g(y,z)$ 对 $x$ 求偏导都是 $0$，所以“关于 $x$ 的原函数”只能确定到相差一个 $g(y,z)$。这就是写 $C(y,z)$ 而不是普通常数 $C$ 的原因。后续用 $f_y$、$f_z$ 一步步把这个函数确定下来，最后只剩一个真正的常数 $K$，它在 $f(Q)-f(P)$ 中抵消。

When integrating $f_x$ with respect to $x$, the other variables are held constant. Any function $g(y,z)$ has zero $x$-partial, so the $x$-antiderivative is determined only up to such a function. That is why the constant is written $C(y,z)$. The conditions on $f_y$ and $f_z$ then pin it down until only a true constant $K$ remains, which cancels in $f(Q)-f(P)$.

## 完整例题 / Worked Example

**题目**：$\mathbf F(x,y,z)=\langle2xy+z,\ x^2,\ x\rangle$，$C$ 是从 $P=(1,-1,2)$ 到 $Q=(2,2,3)$ 的任意分段光滑路径，求 $\int_C\mathbf F\cdot d\mathbf r$。

**Problem:** For the field above and any piecewise smooth path from $P=(1,-1,2)$ to $Q=(2,2,3)$, evaluate the line integral.

1. **检查**：$P_y=2x=Q_x$，$P_z=1=R_x$，$Q_z=0=R_y$，且 $\mathbf F$ 在 $\mathbb R^3$ 上光滑，所以保守。  
   **Check:** all three cross-partial pairs agree and the field is smooth on $\mathbb R^3$, so it is conservative.
2. **对 $x$ 积分**：$f=\int(2xy+z)\,dx=x^2y+xz+C(y,z)$。  
   **Integrate in $x$:** this gives $x^2y+xz+C(y,z)$.
3. **用 $f_y=x^2$**：$x^2+C_y=x^2$，故 $C_y=0$，$C(y,z)=D(z)$。  
   **Use $f_y=x^2$:** $C_y=0$, so $C$ depends only on $z$.
4. **用 $f_z=x$**：$x+D'(z)=x$，故 $D$ 为常数，取 $0$。势函数 $f=x^2y+xz$。  
   **Use $f_z=x$:** $D$ is constant; take it to be $0$, giving $f=x^2y+xz$.
5. **代端点**：$f(2,2,3)=8+6=14$，$f(1,-1,2)=-1+2=1$，所以积分为 $14-1=13$。  
   **Evaluate:** $f(Q)=14$ and $f(P)=1$, so the integral is $13$.

**路径无关检验**：取直线 $\mathbf r(t)=\langle1+t,-1+3t,2+t\rangle$ 或曲线 $\langle1+t,-1+3t^2,2+t^3\rangle$（$0\le t\le1$）直接参数化计算，结果都是 $13$。

**Path-independence check:** Direct parametrized computation along the straight line or the curve above, for $0\le t\le1$, also gives $13$.

## 数学势与物理势能的负号 / Sign Conventions: Mathematical Potential vs Physical Potential Energy

| 约定 / Convention | 关系 / Relation | 力做的功 / Work by the field |
| --- | --- | --- |
| 数学 / Mathematics | $\mathbf F=\nabla f$ | $\int_C\mathbf F\cdot d\mathbf r=f(Q)-f(P)$ |
| 物理 / Physics | $\mathbf F=-\nabla U$ | $W=-\Delta U=U(P)-U(Q)$ |

物理选负号是为了让“力做正功时势能减少”，减少的势能转化为动能，能量守恒写成 $K+U=\text{常数}$。例如地表附近重力 $\mathbf F=\langle0,0,-mg\rangle$，势能 $U=mgz$：物体下落时重力做正功，$U$ 减少。数学势 $f=-mgz$ 描述的是同一个场，只差一个符号。电学中 $\vec E=-\nabla V$ 采用同一约定，见 [[Physics/2.Electrostatics/electric_potential_and_energy]]。

Physics uses the minus sign so that positive work by the force lowers potential energy, which turns into kinetic energy and keeps $K+U$ constant. Near Earth, gravity is $\langle0,0,-mg\rangle$ with $U=mgz$: a falling object receives positive work and $U$ decreases. The mathematical potential $f=-mgz$ describes the same field with the opposite sign. Electrostatics uses the same convention, $\vec E=-\nabla V$.

## 易错点 / Common Mistakes

- 偏积分时写普通常数 $+C$：会丢掉依赖其他变量的项。  
  Writing a plain $+C$ during partial integration, which loses terms in the other variables.
- 只验证 $P_y=Q_x$ 就断定保守，却忽略区域有洞。  
  Concluding the field is conservative from $P_y=Q_x$ alone while ignoring holes in the domain.
- 把“求势函数”（得到函数 $f$）和“求线积分”（得到数值 $f(Q)-f(P)$）混为一谈。  
  Confusing finding the potential, which gives a function, with evaluating the line integral, which gives a number.
- 用物理势能代入数学公式时漏掉负号。  
  Dropping the minus sign when using a physical potential energy in the mathematical formula.

## 关联笔记 / Related Notes

- [[Math_Calculus/6.Multivariable_Calculus/limits_partials_and_gradient]] — 梯度、路径链式法则与 Clairaut 定理 / Gradients, the path chain rule, and Clairaut's theorem
- [[Math_Calculus/6.Multivariable_Calculus/vector_valued_functions]] — 路径的参数化 / Parametrizing paths
- [[Physics/1.Vectors/vectors_and_scalars]] — 点积与做功 / Dot products and work
- [[Physics/2.Electrostatics/electric_potential_and_energy]] — 电势与 $\vec E=-\nabla V$ / Electric potential and $\vec E=-\nabla V$

## 来源 / Sources

- ChatGPT 对话 / ChatGPT conversation：[解释保守向量场](https://chatgpt.com/c/6ae8cbf3-a308-8326-9993-d0925995bdb1) — 线积分直觉、保守场定义、场与势、板书例题 $13$ / Line-integral intuition, conservative fields, fields and potentials, and the board example.
- 板书照片未包含在整理材料中；例题数据以对话正文为准。 / The board photo was not included; example data follow the conversation text.

[//begin]: # "Autogenerated link references for markdown compatibility"
[//end]: # "Autogenerated link references"
