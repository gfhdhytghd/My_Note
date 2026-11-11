# 二重积分换元与 Jacobian / Change of Variables and the Jacobian

> 材料时间 / Material dates：2026-10-29 至 2026-11-02 的学习对话整理，不是课堂原始记录。入口见 [[Courses/2026_fall/recent_learning_review]]。  
> Organized from study conversations dated 2026-10-29 to 2026-11-02; this is not an original class transcript.

## 问题与直觉 / Problem and Intuition

有些区域是斜放的菱形或平行四边形，在 $x,y$ 下要拆成几块；但如果换一组“沿着边走”的新坐标 $u,v$，区域就变成矩形。换元的代价是：$uv$ 平面里的一个小矩形，映射到 $xy$ 平面后会被拉伸、剪切，面积不再是 $du\,dv$。

Some regions, such as tilted rhombi or parallelograms, must be split into pieces in $x,y$. New coordinates $u,v$ aligned with the edges turn the region into a rectangle. The cost is that a small $u v$ rectangle is stretched and sheared by the map, so its image no longer has area $du\,dv$.

**J 是什么**：Jacobian $J$ 就是这个局部面积放大倍数。它是偏导矩阵的行列式；对线性映射来说，它就是 [[Math_Linear-Algebra/determinant_laplace_properties]] 中“$|\det A|$ 是面积缩放倍数”的那个行列式，只是现在每一点可以不同。

**What $J$ is:** The Jacobian $J$ is the local area scale factor. It is the determinant of the matrix of partial derivatives; for a linear map it is exactly the determinant whose absolute value scales area, as in the linked determinant note, except that it may now vary from point to point.

注意：力学里圆轴扭转的 $J$ 是极惯性矩，和这里的 Jacobian 只是同一个字母，含义完全不同，见 [[Physics/3.Mechanics_of_Materials/torsion_circular_shafts]]。

Note: in shaft torsion, $J$ denotes the polar moment of inertia. It shares the letter with the Jacobian but means something entirely different.

## 定义与公式 / Definition and Formula

设 $x=x(u,v)$，$y=y(u,v)$：

Let $x=x(u,v)$ and $y=y(u,v)$:

$$J=\frac{\partial(x,y)}{\partial(u,v)}=\begin{vmatrix}x_u&x_v\\y_u&y_v\end{vmatrix},\qquad\iint_R f(x,y)\,dx\,dy=\iint_S f\big(x(u,v),y(u,v)\big)\,|J|\,du\,dv.$$

**条件 / Conditions**

- 映射把 $S$ 一一对应到 $R$（边界上可以例外）。  
  The map is one-to-one from $S$ onto $R$, except possibly on the boundary.
- $x(u,v)$、$y(u,v)$ 有连续偏导，且 $S$ 内部 $J\ne0$。  
  The component functions have continuous partial derivatives and $J\ne0$ inside $S$.
- 公式里用 $|J|$：负号只表示取向翻转，面积不能为负。  
  Use $|J|$: a negative sign only records an orientation flip, and area cannot be negative.

**简短推导 / Short derivation**：$uv$ 平面中以 $du$、$dv$ 为边的小矩形，映射后近似为以 $\mathbf r_u\,du$ 和 $\mathbf r_v\,dv$ 为边的平行四边形，其中 $\mathbf r_u=\langle x_u,y_u\rangle$，$\mathbf r_v=\langle x_v,y_v\rangle$。平行四边形面积是两边向量行列式的绝对值，即 $|J|\,du\,dv$。

A small $du$ by $dv$ rectangle maps approximately to the parallelogram spanned by $\mathbf r_u\,du$ and $\mathbf r_v\,dv$. Its area is the absolute value of the determinant of these edge vectors, namely $|J|\,du\,dv$.

**极坐标检验 / Polar check**：$x=r\cos\theta$，$y=r\sin\theta$ 时，$J=\begin{vmatrix}\cos\theta&-r\sin\theta\\\sin\theta&r\cos\theta\end{vmatrix}=r$，正好是 [[Math_Calculus/6.Multivariable_Calculus/polar_cylindrical_spherical_integrals]] 中的 $r$。

For polar coordinates the determinant equals $r$, which is the factor used in the polar-integral note.

**反向 Jacobian / Inverse Jacobian**：若只方便写出 $u(x,y)$、$v(x,y)$，可用 $\frac{\partial(x,y)}{\partial(u,v)}=1\Big/\frac{\partial(u,v)}{\partial(x,y)}$。

If only $u(x,y)$ and $v(x,y)$ are convenient, use the reciprocal of the inverse Jacobian.

## 例 1：线性变换的面积放大 / Example 1: Area Scaling of a Linear Map

$G(u,v)=(3u-5v,\ 2u+v)$。偏导矩阵是常数，

For $G(u,v)=(3u-5v,\ 2u+v)$, the derivative matrix is constant:

$$J=\begin{vmatrix}3&-5\\2&1\end{vmatrix}=3+10=13.$$

三角形 $T$ 的顶点 $(0,1)$、$(0,5)$、$(4,0)$ 分别映到 $(-5,1)$、$(-25,5)$、$(12,8)$；线性映射把直线映成直线，所以像仍是三角形。$T$ 的面积为 $\frac12\cdot4\cdot4=8$，像的面积为 $13\times8=104$，用鞋带公式直接算像的顶点也得 $104$。

The vertices map to $(-5,1)$, $(-25,5)$, and $(12,8)$; lines map to lines, so the image is still a triangle. $T$ has area $8$, so the image has area $13\times8=104$, which the shoelace formula on the image vertices confirms.

对话在该题 (c) 小题处截断；上面的面积换算只是用 $J$ 做的验证，不代表原题 (c) 的要求。

The conversation was cut off at part (c); the area computation above is only a check using $J$ and does not claim to be the original part (c).

## 例 2（完整）：菱形区域 / Example 2 (Complete): A Rhombus Region

**题目**：$R$ 是顶点为 $(\pi,0)$、$(2\pi,\pi)$、$(\pi,2\pi)$、$(0,\pi)$ 的菱形，映射 $\Phi(u,v)=\left(\frac{u+v}2,\frac{u-v}2\right)$，求 $\iint_R\big((x-y)\sin(x+y)\big)^2\,dx\,dy$。

**Problem:** $R$ is the rhombus with the four vertices above, and $\Phi(u,v)=\left(\frac{u+v}2,\frac{u-v}2\right)$. Evaluate the integral.

**新变量**：两式相加减得 $u=x+y$，$v=x-y$，被积函数变为 $v^2\sin^2u$。

**New variables:** Adding and subtracting gives $u=x+y$ and $v=x-y$, so the integrand becomes $v^2\sin^2u$.

**新区域**：四个顶点变为 $(\pi,\pi)$、$(3\pi,\pi)$、$(3\pi,-\pi)$、$(\pi,-\pi)$，即矩形 $\pi\le u\le3\pi$，$-\pi\le v\le\pi$。

**New region:** The vertices become a rectangle with $\pi\le u\le3\pi$ and $-\pi\le v\le\pi$.

**Jacobian**：$J=\begin{vmatrix}\frac12&\frac12\\\frac12&-\frac12\end{vmatrix}=-\frac12$，取 $|J|=\frac12$。用反向检验：$\frac{\partial(u,v)}{\partial(x,y)}=\begin{vmatrix}1&1\\1&-1\end{vmatrix}=-2$，倒数的绝对值也是 $\frac12$。

The determinant is $-\frac12$, so $|J|=\frac12$; the inverse Jacobian $-2$ gives the same absolute value.

**计算 / Evaluate**

$$I=\frac12\int_\pi^{3\pi}\sin^2u\,du\int_{-\pi}^{\pi}v^2\,dv=\frac12\cdot\pi\cdot\frac{2\pi^3}{3}=\frac{\pi^4}{3}.$$

这里 $\sin^2u$ 在长度 $2\pi$ 的区间上积分为 $\pi$，$\int_{-\pi}^{\pi}v^2\,dv=\frac{2\pi^3}3$。原对话在这一步截断，以上结果由本页补算。

Over an interval of length $2\pi$, $\sin^2u$ integrates to $\pi$, and $\int_{-\pi}^{\pi}v^2\,dv=\frac{2\pi^3}3$. The conversation stopped at this step; the final value was computed for this note.

## 易错点 / Common Mistakes

- 忘记取绝对值，得到负面积或负积分。  
  Forgetting the absolute value, which produces a negative area factor.
- 把 $\frac{\partial(u,v)}{\partial(x,y)}$ 当成 $\frac{\partial(x,y)}{\partial(u,v)}$ 直接乘上去：两者互为倒数。  
  Using $\frac{\partial(u,v)}{\partial(x,y)}$ in place of $\frac{\partial(x,y)}{\partial(u,v)}$; they are reciprocals.
- 只换被积函数、不换区域：区域边界也必须用新变量重写，最好逐个变换顶点或边界线。  
  Changing the integrand but not the region; rewrite every boundary, for example by mapping vertices or edges.

## 关联笔记 / Related Notes

- [[Math_Calculus/6.Multivariable_Calculus/polar_cylindrical_spherical_integrals]] — 最常用的三种换元 / The three most common substitutions
- [[Math_Calculus/6.Multivariable_Calculus/multiple_integrals_center_of_mass]] — 累次积分基础 / Iterated-integral basics
- [[Math_Linear-Algebra/determinant_laplace_properties]] — 行列式的面积缩放意义 / Determinants as area scale factors
- [[Math_Linear-Algebra/linear_transformations_standard_matrix]] — 线性变换与标准矩阵 / Linear maps and standard matrices

## 来源 / Sources

- ChatGPT 对话 / ChatGPT conversation：[Calculate Paraboloid Volume](https://chatgpt.com/c/6ae3ed1c-993c-8325-811c-ddd552847d15) — 菱形换元与 $G(u,v)$ 的 Jacobian；两题均在对话中截断 / The rhombus substitution and the Jacobian of $G(u,v)$; both were cut off in the conversation.
- 原题图形只在截图中；顶点与映射以对话正文为准。 / Figures were only in screenshots; vertices and maps follow the conversation text.

[//begin]: # "Autogenerated link references for markdown compatibility"
[//end]: # "Autogenerated link references"
