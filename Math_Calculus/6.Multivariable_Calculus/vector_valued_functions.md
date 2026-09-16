# 向量值函数与空间曲线 / Vector-Valued Functions and Space Curves

## 空间曲线的坐标平面投影 / Coordinate-Plane Projections of a Space Curve

三维空间中的向量值函数可以写成 $\vec{r}(t)=\langle x(t),y(t),z(t)\rangle$。当参数 $t$ 变化时，点 $P(t)$ 在空间中移动并描出一条空间曲线。 / A vector-valued function in three-dimensional space can be written as $\vec{r}(t)=\langle x(t),y(t),z(t)\rangle$. As the parameter $t$ changes, the point $P(t)$ moves through space and traces a space curve.

空间曲线在坐标平面上的投影，是通过忽略垂直于该平面的坐标得到的二维曲线： / A coordinate-plane projection of the space curve is obtained by dropping the coordinate perpendicular to that plane:

- 投影到 $xy$ 平面：$\langle x(t),y(t),0\rangle$，等价于观察 $x(t)$ 与 $y(t)$ 的关系。 / Onto the $xy$-plane: $\langle x(t),y(t),0\rangle$, showing the relationship between $x(t)$ and $y(t)$.
- 投影到 $xz$ 平面：$\langle x(t),0,z(t)\rangle$，等价于观察 $x(t)$ 与 $z(t)$ 的关系。 / Onto the $xz$-plane: $\langle x(t),0,z(t)\rangle$, showing the relationship between $x(t)$ and $z(t)$.
- 投影到 $yz$ 平面：$\langle 0,y(t),z(t)\rangle$，等价于观察 $y(t)$ 与 $z(t)$ 的关系。 / Onto the $yz$-plane: $\langle 0,y(t),z(t)\rangle$, showing the relationship between $y(t)$ and $z(t)$.

这些二维投影如同空间曲线在三个坐标平面上的“影子”，可以帮助判断曲线的整体形状、绕轴方式和坐标之间的关系。 / These two-dimensional projections act like the curve's “shadows” on the three coordinate planes, helping reveal its overall shape, how it winds around an axis, and the relationships among its coordinates.

![空间曲线及其在三个坐标平面上的投影 / Space curve and its projections onto the coordinate planes](../../attachments/2026-09-02_space_curve_projections.jpeg)

## 空间中圆的参数化 / Parametrizing Circles in Space

例题：参数化一个半径为 $5$、圆心为 $P=(1,-3,6)$ 的圆。关键是先根据圆所在平面确定哪个坐标保持不变，再让另外两个坐标分别用 $5\cos t$ 和 $5\sin t$ 绕圆心变化，其中 $0\leq t<2\pi$。 / Example: Parametrize a circle of radius $5$ centered at $P=(1,-3,6)$. First determine which coordinate remains constant from the plane containing the circle; then vary the other two coordinates around the center using $5\cos t$ and $5\sin t$, where $0\leq t<2\pi$.

- 圆所在平面平行于 $xy$ 平面时，$z=6$ 保持不变：$\vec{r}(t)=\langle1+5\cos t,-3+5\sin t,6\rangle$。 / If the circle lies in a plane parallel to the $xy$-plane, $z=6$ remains constant: $\vec{r}(t)=\langle1+5\cos t,-3+5\sin t,6\rangle$.
- 圆所在平面平行于 $yz$ 平面时，$x=1$ 保持不变：$\vec{r}(t)=\langle1,-3+5\cos t,6+5\sin t\rangle$。 / If the circle lies in a plane parallel to the $yz$-plane, $x=1$ remains constant: $\vec{r}(t)=\langle1,-3+5\cos t,6+5\sin t\rangle$.

检验方法：从参数方程消去 $t$ 后，两种情形分别满足 $(x-1)^2+(y+3)^2=25$、$z=6$，以及 $(y+3)^2+(z-6)^2=25$、$x=1$。 / Check: eliminating $t$ gives $(x-1)^2+(y+3)^2=25$ with $z=6$ in the first case, and $(y+3)^2+(z-6)^2=25$ with $x=1$ in the second.

![平行于坐标平面的空间圆参数化例题 / Example of parametrizing circles parallel to coordinate planes](../../attachments/2026-09-02_circle_parametrization_example.jpeg)

## 向量值函数的求导法则 / Differentiation Rules for Vector-Valued Functions

单变量微积分的求导法则可直接推广到向量值函数；若 $\vec r(t)$、$\vec r_1(t)$ 与 $\vec r_2(t)$ 均可导，则向量的导数逐分量计算。 / The differentiation rules of single-variable calculus carry over to vector-valued functions; if $\vec r(t)$, $\vec r_1(t)$, and $\vec r_2(t)$ are differentiable, differentiate componentwise.

- **和法则 / Sum rule：** $\frac{d}{dt}[\vec r_1(t)+\vec r_2(t)]=\vec r_1'(t)+\vec r_2'(t)$。 / $\frac{d}{dt}[\vec r_1(t)+\vec r_2(t)]=\vec r_1'(t)+\vec r_2'(t)$.
- **常数倍法则 / Constant multiple rule：** 对任意常数 $c$，$\frac{d}{dt}[c\vec r(t)]=c\vec r'(t)$。 / For any constant $c$, $\frac{d}{dt}[c\vec r(t)]=c\vec r'(t)$.
- **标量乘积法则 / Scalar product rule：** 若 $f(t)$ 为标量函数，则 $\frac{d}{dt}[f(t)\vec r(t)]=f'(t)\vec r(t)+f(t)\vec r'(t)$。 / If $f(t)$ is scalar-valued, then $\frac{d}{dt}[f(t)\vec r(t)]=f'(t)\vec r(t)+f(t)\vec r'(t)$.
- **链式法则 / Chain rule：** 若 $g(t)$ 为标量函数，则 $\frac{d}{dt}\vec r(g(t))=\vec r'(g(t))g'(t)$。 / If $g(t)$ is scalar-valued, then $\frac{d}{dt}\vec r(g(t))=\vec r'(g(t))g'(t)$.

例：设 $\vec r(t)=\langle e^{4t},\sin t,t^3\rangle$，$g(t)=5t-1$。因为 $g(t)$ 是标量函数，向量值函数的乘积法则为 $\frac{d}{dt}[g(t)\vec r(t)]=g'(t)\vec r(t)+g(t)\vec r'(t)$。 / Example: Let $\vec r(t)=\langle e^{4t},\sin t,t^3\rangle$ and $g(t)=5t-1$. Since $g(t)$ is scalar-valued, the product rule is $\frac{d}{dt}[g(t)\vec r(t)]=g'(t)\vec r(t)+g(t)\vec r'(t)$.

这里 $g'(t)=5$，$\vec r'(t)=\langle4e^{4t},\cos t,3t^2\rangle$，代入乘积法则可得： / Here $g'(t)=5$ and $\vec r'(t)=\langle4e^{4t},\cos t,3t^2\rangle$; substituting into the product rule gives:

$$
\frac{d}{dt}[g(t)\vec r(t)]
=5\langle e^{4t},\sin t,t^3\rangle+(5t-1)\langle4e^{4t},\cos t,3t^2\rangle
=\left\langle(20t+1)e^{4t},\;5\sin t+(5t-1)\cos t,\;t^2(20t-3)\right\rangle.
$$

## 空间曲线的切线 / Tangent Line to a Space Curve

若空间曲线为 $\vec r(t)$，且 $\vec r'(t_0)\neq\vec0$，则它在 $t=t_0$ 对应点 $\vec r(t_0)$ 处的切线为 $\vec L(s)=\vec r(t_0)+s\vec r'(t_0)$，其中 $s$ 是切线的参数。 / If a space curve is $\vec r(t)$ and $\vec r'(t_0)\neq\vec0$, then its tangent line at the point $\vec r(t_0)$ is $\vec L(s)=\vec r(t_0)+s\vec r'(t_0)$, where $s$ parametrizes the line.

也可用原参数附近的线性近似写成 $\vec r(t)\approx\vec r(t_0)+(t-t_0)\vec r'(t_0)$。注意切线方向由一阶导数 $\vec r'(t_0)$ 给出；二阶导数 $\vec r''(t_0)$ 描述速度变化，与曲线的弯曲有关。 / Equivalently, the local linear approximation is $\vec r(t)\approx\vec r(t_0)+(t-t_0)\vec r'(t_0)$. The tangent direction comes from the first derivative $\vec r'(t_0)$; the second derivative $\vec r''(t_0)$ describes change in velocity and is related to curvature.

例：半径为 $1$ 的圆向右无滑动滚动时，轮缘上一点的轨迹为摆线 $\vec r(t)=\langle t-\sin t,1-\cos t\rangle$（$t\geq0$）。其切向量为 $\vec r'(t)=\langle1-\cos t,\sin t\rangle$。 / Example: When a circle of radius $1$ rolls to the right without slipping, a point on its rim traces the cycloid $\vec r(t)=\langle t-\sin t,1-\cos t\rangle$ ($t\geq0$). Its tangent vector is $\vec r'(t)=\langle1-\cos t,\sin t\rangle$.

当 $\sin t=0$ 且 $1-\cos t\ne0$ 时切线水平，因此 $t=(2k+1)\pi$（$k=0,1,2,\ldots$），对应点为 $\bigl((2k+1)\pi,2\bigr)$。当 $\vec r'(t)=\vec0$ 时，$t=2k\pi$，对应摆线的尖点；此时不能用切向量直接定义切线。 / The tangent is horizontal when $\sin t=0$ and $1-\cos t\ne0$, so $t=(2k+1)\pi$ ($k=0,1,2,\ldots$), at points $\bigl((2k+1)\pi,2\bigr)$. When $\vec r'(t)=\vec0$, $t=2k\pi$, giving cycloid cusps; the tangent vector does not directly define a tangent there.

## 向量值函数的积分 / Vector-Valued Integration

向量值函数的定积分可由黎曼和定义，也等价于逐分量积分。若 $\vec r(t)=\langle x(t),y(t),z(t)\rangle$，则

$$
\int_a^b\vec r(t)\,dt
=\left\langle\int_a^b x(t)\,dt,\int_a^b y(t)\,dt,\int_a^b z(t)\,dt\right\rangle.
$$

只要每个分量 $x(t)$、$y(t)$ 与 $z(t)$ 都可积，该向量积分便存在。 / A definite integral of a vector-valued function can be defined by Riemann sums and equivalently computed componentwise. If $\vec r(t)=\langle x(t),y(t),z(t)\rangle$, its integral exists whenever all three components are integrable.

向量值积分与标量积分一样满足线性性：对常数 $c$， / Vector-valued integrals obey the same linearity rules as scalar-valued integrals:

$$
\int c\vec r(t)\,dt=c\int\vec r(t)\,dt,\qquad
\int[\vec r_1(t)+\vec r_2(t)]\,dt=\int\vec r_1(t)\,dt+\int\vec r_2(t)\,dt.
$$

对位置向量的微分积分会恢复位置向量：$\displaystyle\int d\vec r=\vec r+\vec C$。因为 $d\vec r=\vec r'(t),dt$，所以 $\displaystyle\int\vec r'(t),dt=\vec r(t)+\vec C$，其中 $\vec C$ 是常向量。 / Integrating the differential of a position vector recovers the position vector: $\displaystyle\int d\vec r=\vec r+\vec C$. Since $d\vec r=\vec r'(t),dt$, $\displaystyle\int\vec r'(t),dt=\vec r(t)+\vec C$, where $\vec C$ is a constant vector.

相应的定积分形式为 $\displaystyle\int_a^b\vec r'(t),dt=\vec r(b)-\vec r(a)$。 / The corresponding definite-integral form is $\displaystyle\int_a^b\vec r'(t),dt=\vec r(b)-\vec r(a)$.

## 相关笔记 / Related Notes

- [[Math_Calculus/6.Multivariable_Calculus/lines_planes_and_distances]] — 直线与切线 / Lines and tangent lines
- [[Math_Calculus/6.Multivariable_Calculus/velocity_and_acceleration]] — 运动与曲率 / Motion and curvature

## 来源 / Sources

- [[Daily Notes/2026-09-02]] — 课堂记录 / Class notes
- [[Daily Notes/2026-09-03]] — 课堂记录 / Class notes

[//begin]: # "Autogenerated link references for markdown compatibility"
[//end]: # "Autogenerated link references"
