# 空间直线、平面与距离 / Lines, Planes, and Distances

## 直线的参数方程 / Parametric Equations of a Line

直线的参数方程为： / The parametric equations of a line are:

$$x=x_0+at,\qquad y=y_0+bt,\qquad z=z_0+ct,\qquad t\in\mathbb R.$$

- 直线上的一点为 $P_0=(x_0,y_0,z_0)$。 / A point on the line is $P_0=(x_0,y_0,z_0)$.
- 方向向量为 $\vec v=\langle a,b,c\rangle$，且 $\vec v\ne\vec0$。 / The direction vector is $\vec v=\langle a,b,c\rangle$, with $\vec v\ne\vec0$.

## 平面的法向量 / Normal Vector of a Plane

平面 $Ax+By+Cz=D$ 的法向量可直接从系数读出： / A normal vector of the plane $Ax+By+Cz=D$ comes directly from its coefficients:

$$\boxed{\vec n=\langle A,B,C\rangle}$$

法向量垂直于平面内的所有方向，且 $A,B,C$ 不全为零。 / The normal vector is perpendicular to every direction in the plane, and $A,B,C$ cannot all be zero.

## 由一点和法向量写平面方程 / Plane Equation from a Point and a Normal

已知平面经过 $P_0=(x_0,y_0,z_0)$，法向量为 $\vec n=\langle A,B,C\rangle$，则平面方程为： / Given a point $P_0=(x_0,y_0,z_0)$ on the plane and a normal vector $\vec n=\langle A,B,C\rangle$, the plane equation is:

$$\boxed{A(x-x_0)+B(y-y_0)+C(z-z_0)=0}$$

展开后得到一般式 $Ax+By+Cz=D$，其中 $D=Ax_0+By_0+Cz_0$；法向量不必是单位向量。若已知三个不共线点 $P_0,P_1,P_2$，可取 $\vec{n}=\overrightarrow{P_0P_1}\times\overrightarrow{P_0P_2}$。 / Expanding gives the general form $Ax+By+Cz=D$, where $D=Ax_0+By_0+Cz_0$; the normal need not be a unit vector. Given three noncollinear points $P_0,P_1,P_2$, use $\vec{n}=\overrightarrow{P_0P_1}\times\overrightarrow{P_0P_2}$.

补充例题：过 $P_0=(1,-2,3)$、法向量为 $\langle2,1,-4\rangle$ 的平面满足 $2(x-1)+(y+2)-4(z-3)=0$，即 $2x+y-4z=-12$。 / Supplementary example: the plane through $P_0=(1,-2,3)$ with normal $\langle2,1,-4\rangle$ satisfies $2(x-1)+(y+2)-4(z-3)=0$, or $2x+y-4z=-12$.

## 两个平面的关系 / Relationships Between Two Planes

比较两个平面的非零法向量 $\vec n_1,\vec n_2$： / Compare the nonzero normal vectors $\vec n_1,\vec n_2$ of the two planes:

- **平行或重合 / Parallel or coincident：** $\vec n_1=k\vec n_2$，其中 $k\ne0$；再检查两个平面的常数项是否按相同比例变化，以区分平行与重合。 / If $\vec n_1=k\vec n_2$ for $k\ne0$, check whether the constant terms scale by the same factor to distinguish distinct parallel planes from coincident planes.
- **正交 / Perpendicular：** $\boxed{\vec n_1\cdot\vec n_2=0}$。 / The planes are perpendicular when their normal vectors have zero dot product.
- **既不平行也不正交 / Neither：** 法向量不成比例，且点积不为零。 / The normal vectors are not proportional and their dot product is nonzero.

## 坐标平面截线与坐标轴截点 / Coordinate Traces and Axis Intercepts

原记“设 x/y/z 为 0 后解方程”适用于求与**坐标平面或坐标轴**的交集。一般的面与面、线与面求交，需要联立它们各自的方程。 / The original shortcut “set x/y/z to zero and solve” applies to intersections with **coordinate planes or axes**. General surface–surface or line–plane intersections require solving their defining equations together.

| 目标 / Target | 代入条件 / Substitution |
| --- | --- |
| 与 $xy$ 平面的截线 / Trace in the $xy$-plane | $z=0$ |
| 与 $xz$ 平面的截线 / Trace in the $xz$-plane | $y=0$ |
| 与 $yz$ 平面的截线 / Trace in the $yz$-plane | $x=0$ |
| 与 $x$ 轴的交点 / $x$-axis intercept | $y=z=0$ |
| 与 $y$ 轴的交点 / $y$-axis intercept | $x=z=0$ |
| 与 $z$ 轴的交点 / $z$-axis intercept | $x=y=0$ |

例如，平面 $2x+3y+6z=6$ 与 $xy$ 平面的交线满足 $2x+3y=6,\ z=0$；它与三条坐标轴的交点分别为 $(3,0,0)$、$(0,2,0)$、$(0,0,1)$。**令一个坐标为零是在取坐标平面，令两个坐标为零是在取坐标轴。** / For example, the trace of $2x+3y+6z=6$ in the $xy$-plane satisfies $2x+3y=6,\ z=0$. Its three axis intercepts are $(3,0,0)$, $(0,2,0)$, and $(0,0,1)$. **Setting one coordinate to zero selects a coordinate plane; setting two to zero selects an axis.**

## 两个平面的交线 / Intersection of Two Planes

设两个平面的方程与非零法向量分别为： / Let the two planes and their nonzero normal vectors be:

$$\Pi_1:A_1x+B_1y+C_1z=D_1,\qquad\vec{n}_1=\langle A_1,B_1,C_1\rangle$$

$$\Pi_2:A_2x+B_2y+C_2z=D_2,\qquad\vec{n}_2=\langle A_2,B_2,C_2\rangle$$

若 $\vec{n}_1\times\vec{n}_2\ne\vec{0}$，两个平面相交于一条直线。交线方向同时垂直于两个法向量，因此可取方向向量 $\vec{d}=\vec{n}_1\times\vec{n}_2$。再联立方程找出一个公共点 $P_0$，即可写出交线： / If $\vec{n}_1\times\vec{n}_2\ne\vec{0}$, the planes intersect in a line. Its direction is perpendicular to both normals, so take $\vec{d}=\vec{n}_1\times\vec{n}_2$. Find a common point $P_0$ by solving the equations together, then write:

$$\vec{r}(t)=\vec{r}_0+t\vec{d},\qquad t\in\mathbb{R}$$

找公共点时可以尝试令一个坐标为零，但这个选择不一定有解；若无解，应换一个坐标或直接消元。若 $\vec{n}_1\times\vec{n}_2=\vec{0}$，两个平面平行或重合：方程左侧系数成比例且右侧常数也按同一比例变化时重合，否则平行且无交点。 / To find a common point, try setting one coordinate to zero, but that choice may yield no solution; then choose another coordinate or use elimination. If $\vec{n}_1\times\vec{n}_2=\vec{0}$, the planes are parallel or coincident: proportional left-hand coefficients and the same proportionality for the constants mean coincidence; otherwise the planes are distinct and parallel.

**例题：**求 $x+y+z=3$ 与 $x-y+z=1$ 的交线。相减得 $y=1$，代回得 $x+z=2$。令 $z=t$，得到以下参数式；方向向量 $\langle-1,0,1\rangle$ 与两法向量的叉积 $\langle2,0,-2\rangle$ 平行。 / **Example:** intersect $x+y+z=3$ and $x-y+z=1$. Subtraction gives $y=1$, then substitution gives $x+z=2$. Setting $z=t$ yields the parametrization below; its direction $\langle-1,0,1\rangle$ is parallel to the cross product $\langle2,0,-2\rangle$ of the normals.

$$\vec{r}(t)=\langle2,1,0\rangle+t\langle-1,0,1\rangle$$

## 直线与平面的交点 / Intersection of a Line and a Plane

把直线的参数式代入平面方程，先求参数 $t$，再代回直线求坐标。设直线方向 $\vec{d}\ne\vec{0}$，平面法向量 $\vec{n}=\langle A,B,C\rangle\ne\vec{0}$： / Substitute the line's parametrization into the plane equation, solve for $t$, then substitute back to obtain the coordinates. Assume a nonzero line direction $\vec{d}$ and a nonzero plane normal $\vec{n}=\langle A,B,C\rangle$:

$$\vec{r}(t)=\vec{r}_0+t\vec{d},\qquad\vec{n}\cdot\vec{r}=D$$

$$\vec{n}\cdot\vec{r}_0+t(\vec{n}\cdot\vec{d})=D$$

- 若 $\vec{n}\cdot\vec{d}\ne0$，有唯一交点，对应 $t=\dfrac{D-\vec{n}\cdot\vec{r}_0}{\vec{n}\cdot\vec{d}}$。 / If $\vec{n}\cdot\vec{d}\ne0$, there is exactly one intersection at $t=\dfrac{D-\vec{n}\cdot\vec{r}_0}{\vec{n}\cdot\vec{d}}$.
- 若 $\vec{n}\cdot\vec{d}=0$ 且 $\vec{n}\cdot\vec{r}_0\ne D$，直线与平面平行且无交点。 / If $\vec{n}\cdot\vec{d}=0$ and $\vec{n}\cdot\vec{r}_0\ne D$, the line is parallel to and disjoint from the plane.
- 若 $\vec{n}\cdot\vec{d}=0$ 且 $\vec{n}\cdot\vec{r}_0=D$，整条直线都在平面内。 / If $\vec{n}\cdot\vec{d}=0$ and $\vec{n}\cdot\vec{r}_0=D$, the entire line lies in the plane.

**例题：**直线 $\vec{r}(t)=\langle1,0,2\rangle+t\langle1,2,-1\rangle$ 与平面 $x+y+z=6$ 求交。代入得 $(1+t)+2t+(2-t)=6$，所以 $t=3/2$，交点为 $(5/2,3,1/2)$。 / **Example:** intersect $\vec{r}(t)=\langle1,0,2\rangle+t\langle1,2,-1\rangle$ with $x+y+z=6$. Substitution gives $(1+t)+2t+(2-t)=6$, so $t=3/2$ and the intersection is $(5/2,3,1/2)$.

## 点到直线的距离 / Distance from a Point to a Line

已知直线经过点 $A$，非零方向向量为 $\vec v$，点 $Q$ 到直线的距离为： / Given a line through $A$ with nonzero direction vector $\vec v$, the distance from $Q$ to the line is:

$$\boxed{d=\frac{\|\overrightarrow{AQ}\times\vec v\|}{\|\vec v\|}}$$

核心是叉积：平行四边形面积除以底边长度，得到高。 / The key is the cross product: divide the parallelogram's area by its base length to obtain its height.

## 点到平面的距离 / Distance from a Point to a Plane

点 $Q=(x_0,y_0,z_0)$ 到平面 $Ax+By+Cz=D$ 的距离为： / The distance from $Q=(x_0,y_0,z_0)$ to the plane $Ax+By+Cz=D$ is:

$$\boxed{d=\frac{|Ax_0+By_0+Cz_0-D|}{\sqrt{A^2+B^2+C^2}}}$$

## 相关笔记 / Related Notes

- [[Math_Linear-Algebra/vector_and_euclidean_space]] — 向量基础 / Vector basics

## 来源 / Sources

- [[Daily Notes/2026-09-08]] — 课堂记录 / Class notes
- [[Daily Notes/2026-09-10]] — 课堂记录 / Class notes
- [[Daily Notes/2026-09-11]] — 课堂记录 / Class notes

[//begin]: # "Autogenerated link references for markdown compatibility"
[//end]: # "Autogenerated link references"
