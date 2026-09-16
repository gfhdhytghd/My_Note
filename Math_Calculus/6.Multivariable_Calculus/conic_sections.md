# 圆锥曲线 / Conic Sections

## 圆锥曲线的几何来源 / Geometry of Conic Sections

这里讨论的是**圆锥曲线（conic sections）**，包括圆、椭圆、抛物线、双曲线；“椭圆曲线（elliptic curve）”是另一个数学概念。以下讨论用平面截正圆双圆锥。 / This note covers **conic sections**: circles, ellipses, parabolas, and hyperbolas. An elliptic curve is a different mathematical concept. Here we consider plane sections of a right circular double cone.

当截平面**不经过锥顶**时，用 $\alpha$ 表示圆锥母线与轴的夹角，用 $\beta$ 表示截平面与轴的夹角： / When the cutting plane **does not pass through the vertex**, let $\alpha$ be the angle between a generator of the cone and its axis, and $\beta$ the angle between the cutting plane and the axis:

| 条件 / Condition | 截线 / Section |
| --- | --- |
| $\beta=90^\circ$ | 圆，截平面垂直于轴 / Circle; the plane is perpendicular to the axis |
| $\alpha<\beta<90^\circ$ | 椭圆，只截一个锥叶 / Ellipse; cuts one nappe |
| $\beta=\alpha$ | 抛物线，截平面平行于某条母线 / Parabola; the plane is parallel to a generator |
| $0\le\beta<\alpha$ | 双曲线，截两个锥叶 / Hyperbola; cuts both nappes |

若截平面**经过锥顶**，会出现退化情形：一个点、一条直线或两条相交直线。直线属于退化圆锥曲线。 / If the cutting plane **passes through the vertex**, the section degenerates to a point, a line, or two intersecting lines. A line is therefore a degenerate conic.

## 常用标准方程 / Standard Equations

以下 $x,y$ 是曲线所在平面内的直角坐标；标准式假设坐标轴与曲线的对称轴对齐。中心或顶点平移到 $(h,k)$ 时，用 $x-h,y-k$ 替代 $x,y$。 / Here $x,y$ are Cartesian coordinates within the plane of the curve; the standard forms assume axes aligned with its symmetry axes. Translating the center or vertex to $(h,k)$ replaces $x,y$ with $x-h,y-k$.

### 圆与椭圆 / Circle and Ellipse

圆心 $(h,k)$、半径 $R>0$ 的圆： / A circle with center $(h,k)$ and radius $R>0$:

$$(x-h)^2+(y-k)^2=R^2$$

规定 $a>b>0$，$a$ 是长半轴，$b$ 是短半轴，$c$ 是中心到焦点的距离。长轴长为 $2a$，短轴长为 $2b$；较大的分母决定长轴方向。 / Let $a>b>0$, with semimajor axis $a$, semiminor axis $b$, and center-to-focus distance $c$. The full axis lengths are $2a$ and $2b$; the larger denominator determines the major-axis direction.

| 项目 / Feature | 长轴水平 / Horizontal major axis | 长轴竖直 / Vertical major axis |
| --- | --- | --- |
| 标准式 / Standard form | $\dfrac{(x-h)^2}{a^2}+\dfrac{(y-k)^2}{b^2}=1$ | $\dfrac{(x-h)^2}{b^2}+\dfrac{(y-k)^2}{a^2}=1$ |
| 中心 / Center | $(h,k)$ | $(h,k)$ |
| 长轴顶点 / Major-axis vertices | $(h\pm a,k)$ | $(h,k\pm a)$ |
| 短轴端点 / Minor-axis endpoints | $(h,k\pm b)$ | $(h\pm b,k)$ |
| 焦点 / Foci | $(h\pm c,k)$ | $(h,k\pm c)$ |

**例题：**$\dfrac{x^2}{49}+\dfrac{y^2}{4}=1$ 的长轴沿 $x$ 方向，$a=7,b=2,c=3\sqrt5$。长、短轴长分别为 $14,4$；长轴顶点为 $(\pm7,0)$，短轴端点为 $(0,\pm2)$，焦点为 $(\pm3\sqrt5,0)$。 / **Example:** For $\dfrac{x^2}{49}+\dfrac{y^2}{4}=1$, the major axis is along $x$, and $a=7,b=2,c=3\sqrt5$. The full axis lengths are $14,4$; major-axis vertices are $(\pm7,0)$, minor-axis endpoints are $(0,\pm2)$, and foci are $(\pm3\sqrt5,0)$.

椭圆满足 $c^2=a^2-b^2$，曲线上任意点到两焦点的距离之和为 $2a$，离心率为 $e=c/a$；$a=b$ 时退化为圆的特殊情形，$e=0$。 / An ellipse satisfies $c^2=a^2-b^2$; distances to its two foci sum to $2a$, and eccentricity is $e=c/a$. The case $a=b$ is a circle, with $e=0$.

### 抛物线 / Parabola

抛物线上每一点到焦点与准线的距离相等。参数 $p\ne0$ 为带符号的量，顶点到焦点的距离为 $|p|$，离心率为 $e=1$。 / Every point on a parabola is equidistant from its focus and directrix. The parameter $p\ne0$ is signed; the vertex-to-focus distance is $|p|$, and eccentricity is $e=1$.

| 标准式 / Standard form | 顶点 / Vertex | 焦点 / Focus | 准线 / Directrix | 开口 / Opening |
| --- | --- | --- | --- | --- |
| $(x-h)^2=4p(y-k)$ | $(h,k)$ | $(h,k+p)$ | $y=k-p$ | $p>0$ 向上，$p<0$ 向下 / Up if $p>0$, down if $p<0$ |
| $(y-k)^2=4p(x-h)$ | $(h,k)$ | $(h+p,k)$ | $x=h-p$ | $p>0$ 向右，$p<0$ 向左 / Right if $p>0$, left if $p<0$ |

例如 $x^2=8y$ 中 $4p=8$，故 $p=2$，焦点为 $(0,2)$，准线为 $y=-2$；不要把 $8$ 直接当作焦距。 / For $x^2=8y$, we have $4p=8$, so $p=2$, the focus is $(0,2)$, and the directrix is $y=-2$; the coefficient $8$ is not the vertex-to-focus distance.

### 双曲线 / Hyperbola

左右开口的双曲线，其中 $a,b>0$： / A hyperbola opening left and right, with $a,b>0$:

$$\frac{(x-h)^2}{a^2}-\frac{(y-k)^2}{b^2}=1,\qquad c^2=a^2+b^2$$

- 中心 $(h,k)$；顶点 $(h\pm a,k)$；焦点 $(h\pm c,k)$；渐近线为 $y-k=\pm\dfrac{b}{a}(x-h)$。 / Center $(h,k)$; vertices $(h\pm a,k)$; foci $(h\pm c,k)$; asymptotes $y-k=\pm\dfrac{b}{a}(x-h)$.
- 曲线上任意点到两个焦点的距离之差的绝对值为 $2a$；离心率 $e=c/a>1$。双曲线不要求 $a>b$。 / The absolute difference of the distances to the two foci is $2a$; eccentricity is $e=c/a>1$. A hyperbola does not require $a>b$.

上下开口时，正项换成 $y$ 项；顶点为 $(h,k\pm a)$，焦点为 $(h,k\pm c)$： / For a hyperbola opening up and down, the $y$ term is positive; the vertices are $(h,k\pm a)$ and the foci are $(h,k\pm c)$:

$$\frac{(y-k)^2}{a^2}-\frac{(x-h)^2}{b^2}=1,\qquad y-k=\pm\frac{a}{b}(x-h)\quad\text{(asymptotes)}$$

## 配方与曲面截线例题 / Completing the Square and Surface Traces

**配方例题：**把 $4x^2+y^2-8x+4y-8=0$ 化成标准式。分别对 $x,y$ 配方，得到中心为 $(1,-2)$、长轴竖直的椭圆。 / **Completing the square:** rewrite $4x^2+y^2-8x+4y-8=0$ in standard form. Completing the square in $x,y$ gives an ellipse centered at $(1,-2)$ with a vertical major axis.

$$4(x-1)^2+(y+2)^2=16\quad\Longrightarrow\quad\frac{(x-1)^2}{4}+\frac{(y+2)^2}{16}=1$$

这里 $a=4,b=2,c=2\sqrt{3}$，焦点为 $(1,-2\pm2\sqrt{3})$。分母是半轴长度的**平方**，不是半轴长度。 / Here $a=4,b=2,c=2\sqrt{3}$, and the foci are $(1,-2\pm2\sqrt{3})$. The denominators are the **squares** of the semiaxis lengths, not the lengths themselves.

**曲面截线例题：**椭球面 $x^2/9+y^2/4+z^2=1$ 与平面 $z=k$ 联立得下式；这把前面的求交方法与圆锥曲线公式联系起来。 / **Surface trace example:** intersect the ellipsoid $x^2/9+y^2/4+z^2=1$ with $z=k$ to obtain the equation below, connecting intersection methods with conic formulas.

$$\frac{x^2}{9}+\frac{y^2}{4}=1-k^2,\qquad z=k$$

- $|k|<1$：截线为椭圆，两个半轴长分别为 $3\sqrt{1-k^2}$ 与 $2\sqrt{1-k^2}$。 / For $|k|<1$, the trace is an ellipse with semiaxis lengths $3\sqrt{1-k^2}$ and $2\sqrt{1-k^2}$.
- $|k|=1$：交集退化成一个点 $(0,0,k)$。 / For $|k|=1$, the intersection reduces to a point $(0,0,k)$.
- $|k|>1$：右侧为负，左侧非负，因此无实交点。 / For $|k|>1$, the right side is negative while the left side is nonnegative, so there is no real intersection.

## 快速自测 / Quick Self-Check

1. 求平面 $x+2y+3z=6$ 与 $xz$ 平面的交线。 / Find the trace of $x+2y+3z=6$ in the $xz$-plane.
2. 求 $x^2/9-y^2/16=1$ 的焦点和渐近线。 / Find the foci and asymptotes of $x^2/9-y^2/16=1$.
3. 求 $(y-1)^2=-8(x+2)$ 的顶点、焦点和准线。 / Find the vertex, focus, and directrix of $(y-1)^2=-8(x+2)$.

参考答案：① $y=0,\ x+3z=6$，可写为 $\vec{r}(t)=\langle6-3t,0,t\rangle$。② 焦点 $(\pm5,0)$，渐近线 $y=\pm4x/3$。③ $p=-2$，顶点 $(-2,1)$，焦点 $(-4,1)$，准线 $x=0$。 / Answers: ① $y=0,\ x+3z=6$, parametrized as $\vec{r}(t)=\langle6-3t,0,t\rangle$. ② Foci $(\pm5,0)$; asymptotes $y=\pm4x/3$. ③ $p=-2$; vertex $(-2,1)$; focus $(-4,1)$; directrix $x=0$.

## 相关笔记 / Related Notes

- [[Math_Calculus/6.Multivariable_Calculus/quadric_surfaces]] — 二次曲面 / Quadric surfaces

## 来源 / Sources

- [[Daily Notes/2026-09-11]] — 课堂记录 / Class notes
- [[Daily Notes/2026-09-14]] — 课堂记录 / Class notes

[//begin]: # "Autogenerated link references for markdown compatibility"
[//end]: # "Autogenerated link references"
