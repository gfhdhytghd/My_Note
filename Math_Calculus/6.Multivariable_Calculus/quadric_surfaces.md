# 二次曲面与截痕 / Quadric Surfaces and Traces

## 二次曲面速查表 / Quadric Surface Identification

二次曲面由三变量的二次方程描述。以下速判适用于**已配方、坐标轴与主轴对齐且无交叉项**的标准式，表中 $a,b,c>0$。含 $xy,xz,yz$ 等交叉项时，可能需要旋转坐标。 / A quadric surface is described by a quadratic equation in three variables. These shortcuts apply to **completed-square standard forms with aligned axes and no mixed terms**, with $a,b,c>0$. Mixed terms such as $xy,xz,yz$ may require a coordinate rotation.

| 标准式 / Standard form | 曲面 / Surface | 识别与方向 / Identification and direction |
| --- | --- | --- |
| $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}+\dfrac{z^2}{c^2}=1$ | 椭球面 / Ellipsoid | 三个正平方项 / Three positive squared terms |
| $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}-\dfrac{z^2}{c^2}=1$ | 单叶双曲面 / Hyperboloid of one sheet | 两正一负，轴沿负项对应的 $z$ 方向 / Two positive, one negative; axis along the negative term's $z$ direction |
| $\dfrac{z^2}{c^2}-\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1$ | 双叶双曲面 / Hyperboloid of two sheets | 一正两负，沿正项对应的 $z$ 方向分成两片 / One positive, two negative; two sheets along the positive term's $z$ direction |
| $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}-\dfrac{z^2}{c^2}=0$ | 椭圆锥面 / Elliptic cone | 异号项对应轴向，沿 $\pm z$ 延伸 / The uniquely signed term identifies the axis; extends along $\pm z$ |
| $z=\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}$ | 椭圆抛物面 / Elliptic paraboloid | 两平方项同号，向 $+z$ 开口 / Squared terms have the same sign; opens toward $+z$ |
| $z=\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}$ | 双曲抛物面（马鞍面） / Hyperbolic paraboloid (saddle) | 两平方项异号 / Squared terms have opposite signs |
| $\dfrac{y^2}{b^2}+\dfrac{z^2}{c^2}=1$ | 椭圆柱面 / Elliptic cylinder | 缺 $x$，沿 $x$ 方向延伸 / Missing $x$; extends along $x$ |

**先把非零右端归一化为 $1$，再数正负号。**例如 $x^2+y^2-z^2=-1$ 应改成 $z^2-x^2-y^2=1$，所以是双叶双曲面。正平方项之和等于 $0$ 可能只有一个点，等于负数则无实点，不能直接判成椭球面。 / **Normalize a nonzero right-hand side to $1$ before counting signs.** For example, $x^2+y^2-z^2=-1$ becomes $z^2-x^2-y^2=1$, a two-sheet hyperboloid. A sum of positive squared terms equal to zero may give a single point; equal to a negative number, it has no real points, rather than an ellipsoid.

## 柱面：缺哪个变量就沿哪个方向延伸 / Cylinders: The Missing Variable Gives the Direction

方程不含某个变量，表示沿该坐标方向平移不改变解集；当剩下两个变量描述非退化曲线时，就得到相应柱面。缺变量本身也可能对应退化集合或空集，仍需检查截面。 / If an equation omits a variable, translation along that coordinate direction preserves its solution set. A nondegenerate curve in the remaining variables generates a cylinder. Missing variables can also occur in degenerate or empty sets, so inspect the cross-section.

| 方程 / Equation | 延伸方向 / Extension direction | 类型 / Type |
| --- | --- | --- |
| $x^2+2z^2=8$ | 平行 $y$ 轴 / Parallel to the $y$-axis | 椭圆柱面 / Elliptic cylinder |
| $z^2+2y^2=8$ | 平行 $x$ 轴 / Parallel to the $x$-axis | 椭圆柱面 / Elliptic cylinder |
| $x^2+2y^2=8$ | 平行 $z$ 轴 / Parallel to the $z$-axis | 椭圆柱面 / Elliptic cylinder |
| $9y^2+z^2=1$ | 平行 $x$ 轴 / Parallel to the $x$-axis | 截面为 $\dfrac{y^2}{1/9}+\dfrac{z^2}{1}=1$ / Elliptic section $\dfrac{y^2}{1/9}+\dfrac{z^2}{1}=1$ |

若垂直于延伸方向的截面是圆，则是圆柱面；例如 $y^2+z^2=1$。 / If the cross-section perpendicular to the extension direction is a circle, the surface is a circular cylinder; for example, $y^2+z^2=1$.

### 课堂补充：二次柱面的分类 / Class Supplement: Quadratic Cylinders

课堂投影片列出直圆柱面、椭圆柱面、双曲柱面和抛物柱面。按非退化圆锥曲线截面分类，通常分为椭圆、双曲和抛物三大类，圆柱面是椭圆柱面的特殊情况；因此投影片写“三类”但列出四项，可以按这个包含关系理解。 / The lecture slide lists right circular, elliptic, hyperbolic, and parabolic cylinders. Classification by nondegenerate conic cross-sections gives three main families: elliptic, hyperbolic, and parabolic, with circular cylinders as a special elliptic case. This inclusion explains how the slide's “three types” can be reconciled with its four listed entries.

下面统一取沿 $z$ 方向延伸的例子，其中 $r,a,b>0$，$A\ne0$。每个平面 $z=t$ 都截出相同的曲线，只是高度不同。 / The examples below all extend along $z$, with $r,a,b>0$ and $A\ne0$. Every plane $z=t$ cuts out the same curve at a different height.

| 类型 / Type | 标准式示例 / Example standard form | $z=t$ 的截面 / Cross-section at $z=t$ |
| --- | --- | --- |
| 直圆柱面 / Right circular cylinder | $x^2+y^2=r^2$ | 半径 $r$ 的圆 / Circle of radius $r$ |
| 椭圆柱面 / Elliptic cylinder | $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$ | 半轴为 $a,b$ 的椭圆；$a=b$ 时为圆 / Ellipse with semiaxes $a,b$; a circle when $a=b$ |
| 双曲柱面 / Hyperbolic cylinder | $\dfrac{y^2}{b^2}-\dfrac{x^2}{a^2}=1$ | 沿 $\pm y$ 开口的双曲线 / Hyperbola opening toward $\pm y$ |
| 抛物柱面 / Parabolic cylinder | $y=Ax^2$ | $A>0$ 向 $+y$、$A<0$ 向 $-y$ 开口的抛物线 / Parabola opening toward $+y$ if $A>0$, toward $-y$ if $A<0$ |

- **柱面不一定是圆筒：**将椭圆、双曲线或抛物线沿固定方向无限平移，都能生成柱面；双曲柱面由两个互不相连的部分组成。 / **A cylinder need not be a circular tube:** translating an ellipse, hyperbola, or parabola indefinitely along a fixed direction generates a cylinder; a hyperbolic cylinder has two disconnected components.
- **延伸方向与截面开口方向不同：**$y=Ax^2$ 缺少 $z$，所以柱面沿 $z$ 延伸；$\pm y$ 描述的是抛物线截面的开口方向。 / **Extension and cross-section opening are different directions:** $y=Ax^2$ omits $z$, so the cylinder extends along $z$; $\pm y$ describes the opening of its parabolic cross-section.
- **抛物柱面与抛物面：**$z=x^2$ 缺少 $y$，是沿 $y$ 延伸的抛物柱面；$z=x^2+y^2$ 是椭圆抛物面；$z=x^2-y^2$ 是双曲抛物面。 / **Parabolic cylinder versus paraboloids:** $z=x^2$ omits $y$ and is a parabolic cylinder extending along $y$; $z=x^2+y^2$ is an elliptic paraboloid; $z=x^2-y^2$ is a hyperbolic paraboloid.

## 抛物面与锥面例题 / Paraboloid and Cone Examples

**椭圆抛物面：**$z=x^2+49y^2$ 的顶点为 $(0,0,0)$，因为右侧非负，故 $z\ge0$，向 $+z$ 开口；$z=-x^2-49y^2$ 则向 $-z$ 开口。 / **Elliptic paraboloid:** $z=x^2+49y^2$ has vertex $(0,0,0)$. Its nonnegative right side implies $z\ge0$, so it opens toward $+z$; $z=-x^2-49y^2$ opens toward $-z$.

平移后的形式如下：$AB>0$ 时为椭圆抛物面，顶点为 $(h,j,k)$；$A,B>0$ 向 $+z$，$A,B<0$ 向 $-z$。类似地，$x=y^2+z^2$ 向 $+x$ 开口。 / In the translated form below, $AB>0$ gives an elliptic paraboloid with vertex $(h,j,k)$; positive $A,B$ give a $+z$ opening, negative $A,B$ a $-z$ opening. Similarly, $x=y^2+z^2$ opens toward $+x$.

$$z-k=A(x-h)^2+B(y-j)^2$$

**双曲抛物面：**$AB<0$ 时为马鞍面，没有椭圆抛物面那样单一的开口方向，$(h,j,k)$ 是鞍点。例如下面两式均为双曲抛物面。 / **Hyperbolic paraboloid:** $AB<0$ gives a saddle surface with saddle point $(h,j,k)$, rather than a single opening direction as in an elliptic paraboloid. Both equations below are examples.

$$z=\frac{y^2}{8}-\frac{x^2}{15},\qquad6z+x^2-y^2=0\ \Longleftrightarrow\ z=\frac{y^2}{6}-\frac{x^2}{6}$$

**椭圆锥面：**$z^2=x^2+49y^2$ 的三个变量都平方，移项后右侧为零；轴沿 $z$，顶点为 $(0,0,0)$，包含上、下两个锥叶。 / **Elliptic cone:** $z^2=x^2+49y^2$ has three squared variables and zero on the right after rearrangement. Its axis is along $z$, its vertex is $(0,0,0)$, and it has upper and lower nappes.

$$z=\pm\sqrt{x^2+49y^2}$$

关键对比：$z=x^2+y^2$ 是抛物面，$z^2=x^2+y^2$ 是锥面；看第三个变量是一次还是平方。 / Key contrast: $z=x^2+y^2$ is a paraboloid, whereas $z^2=x^2+y^2$ is a cone; check whether the third variable is linear or squared.

## 椭球面、配方与轴长 / Ellipsoids, Completing the Square, and Axis Lengths

椭球面的中心为 $(h,k,l)$，沿三个坐标方向的半轴为 $a,b,c>0$，完整轴长为 $2a,2b,2c$。 / An ellipsoid has center $(h,k,l)$, semiaxes $a,b,c>0$ along the coordinate directions, and full axis lengths $2a,2b,2c$.

$$\frac{(x-h)^2}{a^2}+\frac{(y-k)^2}{b^2}+\frac{(z-l)^2}{c^2}=1$$

配方时先提出平方项系数，再将一次项系数减半后平方： / To complete the square, first factor out the quadratic coefficient, then halve and square the linear coefficient inside:

$$x^2+2px=(x+p)^2-p^2$$

$$Ax^2+Bx=A\left(x+\frac{B}{2A}\right)^2-\frac{B^2}{4A},\qquad A\ne0$$

**例题：**将 $x^2+y^2+3z^2+16x=-63$ 化为标准式。 / **Example:** Convert $x^2+y^2+3z^2+16x=-63$ to standard form.

$$x^2+16x=(x+8)^2-64$$

$$(x+8)^2-64+y^2+3z^2=-63\quad\Longrightarrow\quad(x+8)^2+y^2+3z^2=1$$

$$\boxed{\frac{(x+8)^2}{1}+\frac{y^2}{1}+\frac{z^2}{1/3}=1}$$

- 类型与中心：椭球面，中心 $(-8,0,0)$。 / Type and center: ellipsoid centered at $(-8,0,0)$.
- 半轴：$a_x=1,a_y=1,a_z=1/\sqrt3$。 / Semiaxes: $a_x=1,a_y=1,a_z=1/\sqrt3$.
- 完整轴长：$2,2,2/\sqrt3$。分母是半轴的平方；例如分母为 $25$，半轴为 $5$，完整轴长为 $10$。 / Full axis lengths: $2,2,2/\sqrt3$. Each denominator is a squared semiaxis; a denominator of $25$ means a semiaxis of $5$ and full axis length of $10$.

## 坐标轴截距 / Coordinate-Axis Intercepts

求哪条轴的截点，就把另外两个变量设为零；答案最好写成三维坐标。 / To find intercepts on an axis, set the other two variables to zero; preferably give the answers as three-dimensional points.

| 目标 / Target | 条件 / Conditions | 对 $x^2+\dfrac{y^2}{144}+\dfrac{z^2}{144}=1$ 的结果 / Results for this ellipsoid |
| --- | --- | --- |
| $x$ 轴截点 / $x$-intercepts | $y=z=0$ | $(\pm1,0,0)$ |
| $y$ 轴截点 / $y$-intercepts | $x=z=0$ | $(0,\pm12,0)$ |
| $z$ 轴截点 / $z$-intercepts | $x=y=0$ | $(0,0,\pm12)$ |

平移后的半轴端点不一定在坐标轴上。例如上一节椭球面的 $x$ 轴截点为 $(-9,0,0),(-7,0,0)$，但没有 $y$ 或 $z$ 轴截点，因为令 $x=0$ 后左侧至少为 $64>1$。 / After translation, semiaxis endpoints need not lie on the coordinate axes. The previous ellipsoid has $x$-intercepts $(-9,0,0),(-7,0,0)$, but no $y$- or $z$-intercepts, because setting $x=0$ makes its left side at least $64>1$.

## 截痕与退化情形 / Traces and Degenerate Cases

截痕是曲面与平面的交集；坐标平面截痕是其中的特殊情形，也可取 $z=t$ 等平行平面。截痕不一定是一条曲线，还可能是一个点、直线、两条直线或空集。 / A trace is the intersection of a surface with a plane. Coordinate-plane traces are special cases; parallel planes such as $z=t$ are also useful. A trace need not be a curve: it may be a point, a line, two lines, or the empty set.

| 截痕 / Trace | 所在平面 / Plane | 代入 / Substitution |
| --- | --- | --- |
| $xy$-trace | $xy$ 平面 / $xy$-plane | $z=0$ |
| $xz$-trace | $xz$ 平面 / $xz$-plane | $y=0$ |
| $yz$-trace | $yz$ 平面 / $yz$-plane | $x=0$ |

**例题：**$z=x^2+49y^2$ 的截痕如下；写答案时保留截平面条件。 / **Example:** The traces of $z=x^2+49y^2$ are listed below; retain the cutting-plane condition in the answer.

| 平面 / Plane | 联立结果 / Intersection equations | 形状 / Shape |
| --- | --- | --- |
| $z=0$ | $x^2+49y^2=0,\ z=0$ | 只有原点 $(0,0,0)$ / Only the origin |
| $y=0$ | $z=x^2,\ y=0$ | 向 $+z$ 的抛物线 / Parabola opening toward $+z$ |
| $x=0$ | $z=49y^2,\ x=0$ | 向 $+z$ 的抛物线 / Parabola opening toward $+z$ |
| $z=t>0$ | $\dfrac{x^2}{t}+\dfrac{y^2}{t/49}=1,\ z=t$ | 椭圆，半轴为 $\sqrt t,\sqrt t/7$ / Ellipse with semiaxes $\sqrt t,\sqrt t/7$ |
| $z=t<0$ | $x^2+49y^2=t,\ z=t$ | 无实交点 / No real intersection |

在固定的 $xy$ 平面内，以下方程说明常见退化情况；在三维中必须同时注明 $z=0$，否则如 $x^2+y^2=0$ 描述的是整条 $z$ 轴。 / Within the fixed $xy$-plane, the following equations illustrate common degenerate cases. In three dimensions, include $z=0$; otherwise, for example, $x^2+y^2=0$ describes the entire $z$-axis.

| 平面内方程 / Equation within the plane | 结果 / Result |
| --- | --- |
| $x^2+y^2=0$ | 一个点 $(0,0,0)$ / One point |
| $x^2+y^2=-1$ | 空集，无截痕 / Empty set; no trace |
| $x^2-y^2=0$ | 两条相交直线 $y=\pm x,\ z=0$ / Two intersecting lines |

## 单叶、双叶与锥面比较 / One Sheet, Two Sheets, and Cones

以下通过水平截痕比较三种曲面；$a,b,c>0$。这些曲面的轴沿 $z$，但只有 $a=b$ 时才绕该轴旋转对称。 / Compare these surfaces through horizontal traces, with $a,b,c>0$. Their axes are along $z$, but they have rotational symmetry about that axis only when $a=b$.

| 曲面 / Surface | $z=t$ 时 / At $z=t$ | 判断 / Interpretation |
| --- | --- | --- |
| 单叶双曲面 / One-sheet hyperboloid | $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1+\dfrac{t^2}{c^2}$ | 每个高度都有椭圆，整体连通 / Ellipse at every height; connected surface |
| 椭圆锥面 / Elliptic cone | $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=\dfrac{t^2}{c^2}$ | $t=0$ 为锥顶，其余为椭圆 / Vertex at $t=0$; ellipses otherwise |
| 双叶双曲面 / Two-sheet hyperboloid | $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=\dfrac{t^2}{c^2}-1$ | $-c<t<c$ 无截痕；$t=\pm c$ 各一个顶点；外侧为椭圆 / No trace for $-c<t<c$; vertices at $t=\pm c$; ellipses beyond |

最容易混淆的三个方程： / Three easily confused equations:

$$\underbrace{x^2+y^2-z^2=0}_{\text{cone}},\qquad\underbrace{x^2+y^2-z^2=1}_{\text{one sheet}},\qquad\underbrace{z^2-x^2-y^2=1}_{\text{two sheets}}$$

## 特殊情况、中心与顶点 / Special Cases, Centers, and Vertices

- **球面是椭球面的特殊情况：**三个半轴都等于 $r>0$。 / **A sphere is a special ellipsoid:** all three semiaxes equal $r>0$.

$$(x-h)^2+(y-k)^2+(z-l)^2=r^2\quad\Longleftrightarrow\quad\frac{(x-h)^2}{r^2}+\frac{(y-k)^2}{r^2}+\frac{(z-l)^2}{r^2}=1$$

- **圆抛物面是椭圆抛物面的特殊情况：**$z=x^2+y^2$ 的正高度水平截面为圆，也称旋转抛物面；$z=x^2+49y^2$ 的对应截面为非圆椭圆。 / **A circular paraboloid is a special elliptic paraboloid:** $z=x^2+y^2$ has circular horizontal sections at positive heights and is also called a paraboloid of revolution; $z=x^2+49y^2$ has noncircular elliptical sections.
- **中心与顶点：**椭球面和双曲面用中心描述平移位置；椭圆抛物面用顶点，锥面用锥顶，双曲抛物面可用鞍点描述。双叶双曲面还各有一个顶点。 / **Centers and vertices:** centers describe translations of ellipsoids and hyperboloids; elliptic paraboloids have a vertex, cones have an apex, and hyperbolic paraboloids have a saddle point. A two-sheet hyperboloid also has one vertex on each sheet.
- **读平移坐标：**$(x-h)^2$ 对应坐标 $h$，所以 $(x+8)^2$ 对应 $-8$。例如 $z=(x-2)^2+(y+3)^2+5$ 的顶点是 $(2,-3,5)$。 / **Reading translations:** $(x-h)^2$ corresponds to coordinate $h$, so $(x+8)^2$ corresponds to $-8$. For example, $z=(x-2)^2+(y+3)^2+5$ has vertex $(2,-3,5)$.

## 考场解题顺序 / Exam Workflow

1. **整理与配方：**移项、分组、配方；非零常数右端归一化为 $1$。 / **Rearrange and complete squares:** collect terms, complete squares, and normalize a nonzero constant right-hand side to $1$.
2. **识别类型：**查缺失变量、一次变量、平方项数量及符号，同时排除空集或退化情况。 / **Identify the type:** inspect missing variables, linear variables, and the number and signs of squared terms; check for empty or degenerate cases.
3. **读几何信息：**找中心、顶点或鞍点，再找轴向；分母开平方才是半轴，乘 $2$ 才是完整轴长。 / **Read the geometry:** locate the center, vertex, or saddle point and identify axis directions; square-root denominators for semiaxes and double them for full axis lengths.
4. **求截痕与截点：**坐标平面设一个变量为零，坐标轴设另外两个为零；检查是否有实解。 / **Find traces and intercepts:** set one variable to zero for a coordinate plane and the other two for an axis; check for real solutions.
5. **复核易错点：**椭圆 $c^2=a^2-b^2$；$z$ 与 $z^2$ 区分抛物面和锥面；右端 $0$ 与 $1$ 区分锥面和双曲面。 / **Check common pitfalls:** ellipses use $c^2=a^2-b^2$; distinguish $z$ from $z^2$ for paraboloids versus cones, and right-hand sides $0$ versus $1$ for cones versus hyperboloids.

## 相关笔记 / Related Notes

- [[Math_Calculus/6.Multivariable_Calculus/conic_sections]] — 圆锥曲线基础 / Conic prerequisites
- [[Math_Calculus/6.Multivariable_Calculus/traces_and_contour_maps]] — 截线与等高线 / Traces and contours

## 来源 / Sources

- [[Daily Notes/2026-09-14]] — 课堂记录 / Class notes

[//begin]: # "Autogenerated link references for markdown compatibility"
[//end]: # "Autogenerated link references"
