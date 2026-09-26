# 二元函数的截线与等高线图 / Traces and Contour Maps

课程：[[Courses/2026_fall/math_230/course_overview]]。二元函数 $z=f(x,y)$ 把定义域中的每个点 $(x,y)$ 对应到一个高度 $z$，其图像通常是三维空间中的曲面。截线和等高线图帮助我们通过二维曲线理解曲面的形状。 / Course: [[Courses/2026_fall/math_230/course_overview]]. A function $z=f(x,y)$ assigns a height $z$ to each point $(x,y)$ in its domain; its graph is typically a surface in three-dimensional space. Traces and contour maps help us understand this surface through two-dimensional curves.

## 截线：用平面切曲面 / Traces: Slicing a Surface with a Plane

截线（trace）是曲面与某个平面的交线。对于 $z=f(x,y)$，常见做法是固定 $x$、$y$ 或 $z$，再研究剩下两个变量的关系；所得交集也可能为空或退化为一个点。 / A trace is the intersection of a surface with a plane. For $z=f(x,y)$, we commonly fix $x$, $y$, or $z$ and examine the relationship between the other two variables; the intersection may also be empty or degenerate to a point.

| 固定变量 / Fixed variable | 截线方程 / Trace equation | 所在平面 / Containing plane |
| --- | --- | --- |
| $x=a$ | $z=f(a,y)$ | 平行于 $yz$ 平面的竖直平面 / Vertical plane parallel to the $yz$-plane |
| $y=b$ | $z=f(x,b)$ | 平行于 $xz$ 平面的竖直平面 / Vertical plane parallel to the $xz$-plane |
| $z=c$ | $f(x,y)=c$，且 $z=c$ / With $z=c$ | 平行于 $xy$ 平面的水平平面 / Horizontal plane parallel to the $xy$-plane |

求截线时，先把固定值代入函数，再判断得到的是直线、抛物线、圆还是其他曲线，并注明它位于哪个平面。特别地，$x=0$、$y=0$、$z=0$ 对应三个坐标平面中的截线。 / To find a trace, substitute the fixed value, identify the resulting line, parabola, circle, or other curve, and state its containing plane. In particular, $x=0$, $y=0$, and $z=0$ give traces in the three coordinate planes.

**例：抛物面 $z=x^2+y^2$。**固定 $x=a$ 得到 $z=a^2+y^2$，固定 $y=b$ 得到 $z=x^2+b^2$，都是开口向上的抛物线；固定 $z=c$ 得到 $x^2+y^2=c$。当 $c>0$ 时，水平截线是在高度 $z=c$ 处、半径为 $\sqrt c$ 的圆；$c=0$ 时只有原点；$c<0$ 时无交点。 / **Example: the paraboloid $z=x^2+y^2$.** Fixing $x=a$ gives $z=a^2+y^2$, and fixing $y=b$ gives $z=x^2+b^2$, both upward-opening parabolas. Fixing $z=c$ gives $x^2+y^2=c$: a circle of radius $\sqrt c$ at height $z=c$ for $c>0$, only the origin for $c=0$, and no intersection for $c<0$.

## 等高线与等高线图 / Level Curves and Contour Maps

等高线（level curve / contour）是在 $xy$ 平面内满足同一函数值的点集： / A level curve, or contour, is the set of points in the $xy$-plane having the same function value:

$$\boxed{f(x,y)=c}.$$

水平截线由三维点 $(x,y,c)$ 组成；将它投影到 $xy$ 平面，就得到对应的等高线。选取多个高度 $c_1,c_2,\ldots$，画出各条等高线并标注函数值，就得到等高线图（contour map）。图上的两个坐标轴是 $x,y$，高度由曲线标签表示。 / A horizontal trace consists of three-dimensional points $(x,y,c)$; projecting it onto the $xy$-plane gives the corresponding level curve. Drawing level curves for several heights $c_1,c_2,\ldots$ and labeling their function values produces a contour map. Its axes are $x$ and $y$; height is represented by the curve labels.

对 $f(x,y)=x^2+y^2$，取 $c=0,1,4,9$，得到原点以及半径为 $1,2,3$ 的同心圆，标签分别为 $0,1,4,9$。标签向外增大，说明曲面从中心向外升高。这里高度间隔不相等，因此不能只看这些圆的间距来比较陡峭程度。 / For $f(x,y)=x^2+y^2$, the levels $c=0,1,4,9$ give the origin and concentric circles of radii $1,2,3$, labeled $0,1,4,9$. Increasing labels outward show that the surface rises away from the center. These height intervals are unequal, so circle spacing alone cannot be used to compare steepness.

### 等高距 / Contour Interval

等高距（contour interval）是等高线图中相邻两个绘制层级的函数值之差的大小，通常取固定值。对于 $z=f(x,y)$，它表示高度 $z$ 的变化量，而不是纸面上两条曲线的水平距离。 / The contour interval is the magnitude of the difference in function value between consecutive plotted levels, usually chosen to be constant. For $z=f(x,y)$, it measures a change in height $z$, not the horizontal distance between curves on the map.

$$\boxed{\Delta c=|c_{i+1}-c_i|}.$$

例如等高线依次标为 $10,20,30,40$，则等高距为 $10$；若标签的单位为米，等高距就是 $10\,\mathrm m$。如果从标为 $10$ 的线到标为 $40$ 的线共跨过三个等高间隔，则 $\Delta c=(40-10)/3=10$，计算时要数间隔而不是线条。 / For contours labeled $10,20,30,40$, the contour interval is $10$; if the labels are in meters, it is $10\,\mathrm m$. Crossing three equal level intervals from the contour labeled $10$ to the one labeled $40$ gives $\Delta c=(40-10)/3=10$: count intervals, not lines.

对于 $f(x,y)=x^2+y^2$，选择 $c=1,2,3,4$ 时，等高距固定为 $1$，对应圆的半径却是 $1,\sqrt2,\sqrt3,2$。越往外圆与圆的水平间距越小，说明相同高度变化发生在更短的水平距离内，曲面更陡。前例中的 $c=0,1,4,9$ 则具有不等的层级差 $1,3,5$，没有统一的等高距。 / For $f(x,y)=x^2+y^2$, choosing $c=1,2,3,4$ gives a constant contour interval of $1$, but the circle radii are $1,\sqrt2,\sqrt3,2$. Their horizontal spacing decreases outward, meaning the same height change occurs over a shorter horizontal distance and the surface is steeper. The earlier levels $c=0,1,4,9$ have unequal differences $1,3,5$, so they do not have a single constant contour interval.

## 如何求等高线：以 $f(x,y)=2x^2+5y^2$ 为例 / Finding Level Curves: An Example

求等高线的基本步骤是：**令函数值等于常数 $c$，整理方程、判断形状，再在 $xy$ 平面作图并标注 $c$。**这里固定的是高度，$x,y$ 仍然可以变化，不需要先求导。 / To find level curves, **set the function equal to a constant $c$, rearrange and identify the curve, then draw it in the $xy$-plane and label it with $c$.** The height is fixed while $x,y$ remain variable; no differentiation is needed.

### 1. 固定高度并判断取值范围 / Fix the Height and Check Possible Levels

令 $z=c$，得到等高线方程。因为平方项均非负，函数的值域为 $[0,\infty)$。 / Set $z=c$ to obtain the level-curve equation. Both squared terms are nonnegative, so the range is $[0,\infty)$.

$$2x^2+5y^2=c.$$

- $c<0$：无实数解，等高线为空集。 / No real solutions; the level set is empty.
- $c=0$：必须有 $x=y=0$，等值集合只有原点。 / Both $x$ and $y$ must be zero; the level set is just the origin.
- $c>0$：得到以原点为中心的椭圆。 / The level curve is an ellipse centered at the origin.

### 2. 化为标准式并找半轴 / Rewrite in Standard Form and Find the Semiaxes

当 $c>0$ 时，两边除以 $c$，把系数改写成分母： / For $c>0$, divide both sides by $c$ and rewrite the coefficients as denominators:

$$\frac{2x^2}{c}+\frac{5y^2}{c}=1
\quad\Longrightarrow\quad
\boxed{\frac{x^2}{c/2}+\frac{y^2}{c/5}=1}.$$

与椭圆标准式 $x^2/a^2+y^2/b^2=1$ 比较，沿 $x$、$y$ 方向的半轴分别为： / Comparing with the ellipse form $x^2/a^2+y^2/b^2=1$, the semiaxes along $x$ and $y$ are:

$$a=\sqrt{\frac c2},\qquad b=\sqrt{\frac c5}.$$

由于 $c/2>c/5$，长轴沿 $x$ 方向。注意分母是半轴的平方；原式中 $y^2$ 的系数较大，反而说明同一高度下 $y$ 方向的半轴较短。 / Since $c/2>c/5$, the major axis lies along $x$. The denominators are squared semiaxes; the larger coefficient of $y^2$ in the original expression means a shorter semiaxis along $y$ at the same height.

### 3. 选几个高度并作图 / Choose Levels and Sketch

例如选 $c=0,10,20,30$，等高距为 $10$。每条椭圆先标出四个轴截点 $(\pm a,0)$、$(0,\pm b)$，再用光滑曲线连接，并在曲线上标注对应的 $c$。 / For example, choose $c=0,10,20,30$, giving a contour interval of $10$. For each ellipse, mark the four intercepts $(\pm a,0)$ and $(0,\pm b)$, join them smoothly, and label the curve with its value of $c$.

| 高度 / Level | 等高线方程 / Level-curve equation | $x$ 方向半轴 / Semiaxis along $x$ | $y$ 方向半轴 / Semiaxis along $y$ |
| --- | --- | --- | --- |
| $c=0$ | $2x^2+5y^2=0$ | 原点 / Origin | 原点 / Origin |
| $c=10$ | $x^2/5+y^2/2=1$ | $\sqrt5$ | $\sqrt2$ |
| $c=20$ | $x^2/10+y^2/4=1$ | $\sqrt{10}$ | $2$ |
| $c=30$ | $x^2/15+y^2/6=1$ | $\sqrt{15}$ | $\sqrt6$ |

以 $c=10$ 为例，四个轴截点为 $(\pm\sqrt5,0)$、$(0,\pm\sqrt2)$；另取点 $(\sqrt{5/2},1)$，代回原函数得到 $2(5/2)+5(1)^2=10$，也在这条等高线上。 / For $c=10$, the four intercepts are $(\pm\sqrt5,0)$ and $(0,\pm\sqrt2)$. The point $(\sqrt{5/2},1)$ also lies on this contour because $2(5/2)+5(1)^2=10$.

图上是一组沿 $x$ 方向较长的同心椭圆，标签向外增大；半轴随 $\sqrt c$ 增长。因此在等高距相同的情况下，沿任一固定射线向外看，相邻椭圆的间距越来越小。对应的三维曲面是开口向上的椭圆抛物面。 / The map consists of concentric ellipses elongated along $x$, with labels increasing outward. Their semiaxes grow as $\sqrt c$, so for equal contour intervals, successive ellipses become closer along any fixed outward ray. The corresponding 3D surface is an upward-opening elliptic paraboloid.

## 补充例题：$f(x,y)=x^2-3y^2$ / Additional Example

![函数 x²−3y² 的等高线图与三维马鞍面对照 / Contour map and saddle surface of x²−3y²](../../assets/images/saddle_level_curves.png)

左图将相同高度的点画在 $xy$ 平面上，右图展示它们在曲面上的实际高度；两图颜色一一对应。暖色表示正高度，冷色表示负高度，灰色虚线表示零高度。 / The left panel plots equal-height points in the $xy$-plane; the right panel shows their actual heights on the surface, with matching colors. Warm colors indicate positive levels, cool colors negative levels, and dashed gray lines the zero level.

令函数值等于常数 $c$，得到等高线方程 $x^2-3y^2=c$。函数值可以是任意实数，需要分别讨论 $c>0$、$c<0$ 和 $c=0$。 / Set the function equal to a constant $c$ to obtain the level-curve equation $x^2-3y^2=c$. The range is all real numbers, so consider $c>0$, $c<0$, and $c=0$ separately.

### 1. 正高度：左右开口 / Positive Levels: Opening Left and Right

当 $c>0$ 时，两边除以 $c$，得到以原点为中心、沿 $x$ 方向开口的双曲线： / For $c>0$, divide by $c$ to obtain a hyperbola centered at the origin and opening along $x$:

$$\boxed{\frac{x^2}{c}-\frac{y^2}{c/3}=1},\qquad a=\sqrt c,\quad b=\sqrt{\frac c3}.$$

顶点为 $(\pm\sqrt c,0)$，与 $y$ 轴无交点。例如 $c=3$ 时，$x^2/3-y^2=1$，顶点为 $(\pm\sqrt3,0)$。 / The vertices are $(\pm\sqrt c,0)$, with no $y$-axis intercepts. For example, $c=3$ gives $x^2/3-y^2=1$, whose vertices are $(\pm\sqrt3,0)$.

### 2. 负高度：上下开口 / Negative Levels: Opening Up and Down

当 $c<0$ 时，记 $d=-c>0$，先改写为 $3y^2-x^2=d$，再除以 $d$。正项变成 $y$ 项，因此双曲线沿 $y$ 方向开口： / For $c<0$, let $d=-c>0$. Rewrite as $3y^2-x^2=d$, then divide by $d$. The positive term is now the $y$ term, so the hyperbola opens along $y$:

$$\boxed{\frac{y^2}{d/3}-\frac{x^2}{d}=1},\qquad a=\sqrt{\frac d3},\quad b=\sqrt d.$$

顶点为 $(0,\pm\sqrt{d/3})$，与 $x$ 轴无交点。例如 $c=-3$ 时，$y^2-x^2/3=1$，顶点为 $(0,\pm1)$。 / The vertices are $(0,\pm\sqrt{d/3})$, with no $x$-axis intercepts. For example, $c=-3$ gives $y^2-x^2/3=1$, whose vertices are $(0,\pm1)$.

### 3. 零高度：两条相交直线 / Zero Level: Two Intersecting Lines

当 $c=0$ 时，直接因式分解，不能除以 $c$： / For $c=0$, factor directly; division by $c$ is not allowed:

$$x^2-3y^2=(x-\sqrt3y)(x+\sqrt3y)=0
\quad\Longrightarrow\quad\boxed{y=\pm\frac{x}{\sqrt3}}.$$

零等高线是这两条直线的并集。它们也恰好是所有非零高度双曲线的渐近线；两条线同属 $c=0$，所以在原点相交不违反不同高度等高线不能相交的规则。 / The zero-level set is the union of these two lines. They are also the asymptotes of every nonzero-level hyperbola. Both lines have level $c=0$, so their intersection at the origin does not violate the rule that different levels cannot intersect.

### 4. 选取高度并作图 / Choose Levels and Sketch

例如选 $c=-6,-3,0,3,6$，等高距为 $3$。先画直线 $y=\pm x/\sqrt3$，再标出各双曲线顶点，画出逐渐靠近渐近线的两个分支，并标注 $c$。 / For example, choose $c=-6,-3,0,3,6$, with contour interval $3$. First draw $y=\pm x/\sqrt3$, then mark each hyperbola's vertices, sketch its two branches approaching the asymptotes, and label it with $c$.

| 高度 / Level | 等高线方程 / Level-curve equation | 形状与顶点 / Shape and vertices |
| --- | --- | --- |
| $c=-6$ | $y^2/2-x^2/6=1$ | 上下开口，$(0,\pm\sqrt2)$ / Opens up and down |
| $c=-3$ | $y^2-x^2/3=1$ | 上下开口，$(0,\pm1)$ / Opens up and down |
| $c=0$ | $y=\pm x/\sqrt3$ | 两条相交直线 / Two intersecting lines |
| $c=3$ | $x^2/3-y^2=1$ | 左右开口，$(\pm\sqrt3,0)$ / Opens left and right |
| $c=6$ | $x^2/6-y^2/2=1$ | 左右开口，$(\pm\sqrt6,0)$ / Opens left and right |

三维曲面 $z=x^2-3y^2$ 是马鞍面：沿 $y=0$ 有 $z=x^2$，向上弯；沿 $x=0$ 有 $z=-3y^2$，向下弯。因此等高线在正、负高度的开口方向不同。 / The surface $z=x^2-3y^2$ is a saddle: along $y=0$, $z=x^2$ bends upward; along $x=0$, $z=-3y^2$ bends downward. Accordingly, positive and negative contours open in different directions.

## 如何读等高线图 / How to Read a Contour Map

- **沿一条等高线走，函数值不变：**从一条等高线移动到另一条时，看标签判断高度增加还是减少。 / **The function value stays constant along a contour:** when moving between contours, use their labels to determine whether height increases or decreases.
- **等高差条件下，线密通常表示坡陡：**若相邻线的 $\Delta c$ 相同，沿局部垂直于等高线的方向，较小的水平间距 $\Delta\ell$ 对应较大的平均高度变化率 $|\Delta c|/\Delta\ell$；线疏则较平缓。 / **For equal level intervals, closer contours generally indicate a steeper slope:** along the local direction perpendicular to contours, smaller horizontal spacing $\Delta\ell$ gives a larger average height-change rate $|\Delta c|/\Delta\ell$. Wider spacing indicates gentler slopes.
- **不同高度的等高线不能相交：**同一个 $(x,y)$ 不能同时满足 $f(x,y)=c_1$ 和 $f(x,y)=c_2$，其中 $c_1\ne c_2$；但同一高度的等值集合可以出现交叉分支。 / **Contours of different levels cannot intersect:** a single $(x,y)$ cannot have two distinct function values $c_1\ne c_2$. A level set at one value can, however, have crossing branches.
- **闭合曲线要结合标签判断：**向中心标签升高表示向内升高，标签降低表示向内降低；不能仅凭同心形状就断定是山峰还是低谷。 / **Read labels on closed contours:** increasing labels toward the center indicate rising terrain inward, while decreasing labels indicate falling terrain. Concentric shapes alone do not distinguish a peak from a depression.

## 对比例子：鞍面 / A Contrasting Example: A Saddle

对 $z=x^2-y^2$，在 $y=0$ 平面内的截线为 $z=x^2$，向上开口；在 $x=0$ 平面内的截线为 $z=-y^2$，向下开口。这说明沿两个不同方向看，曲面一个方向上升、另一个方向下降，形成鞍形。 / For $z=x^2-y^2$, the trace in $y=0$ is $z=x^2$, opening upward, whereas the trace in $x=0$ is $z=-y^2$, opening downward. The surface rises in one direction and falls in the other, producing a saddle.

等高线满足 $x^2-y^2=c$：$c>0$ 时双曲线沿 $x$ 方向开口，$c<0$ 时沿 $y$ 方向开口；$c=0$ 时退化为相交直线 $y=\pm x$。这两条直线属于同一个高度 $c=0$，因此不违反“不同高度等高线不相交”的规则。 / The contours satisfy $x^2-y^2=c$: hyperbolas open along the $x$ direction for $c>0$ and along the $y$ direction for $c<0$. At $c=0$, the level set becomes the intersecting lines $y=\pm x$. Both lines have the same level $c=0$, so this does not violate the rule that different levels cannot intersect.

与静电学的联系：若用 $V(x,y)$ 表示二维电势分布，$V(x,y)=c$ 就是等势线；电场 $\vec E=-\nabla V$ 在梯度非零处垂直于等势线，并指向电势降低的方向。 / Connection to electrostatics: if $V(x,y)$ describes a two-dimensional potential, $V(x,y)=c$ gives equipotential contours. Where the gradient is nonzero, $\vec E=-\nabla V$ is perpendicular to these contours and points toward decreasing potential.

## 相关笔记 / Related Notes

- [[Math_Calculus/6.Multivariable_Calculus/quadric_surfaces]] — 二次曲面 / Quadric surfaces
- [[Physics/2.Electrostatics/electric_potential_and_energy]] — 电势与等势线 / Potential and equipotentials

## 来源 / Sources

- [[Daily Notes/2026-09-16]] — 课堂记录 / Class notes

[//begin]: # "Autogenerated link references for markdown compatibility"
[//end]: # "Autogenerated link references"
