# 求导与积分公式速查表 / Derivative & Integral Rules Cheat Sheet

本页把常用初等函数的求导与不定积分放在同一个表格里，便于快速查阅。  
This page collects common derivatives and indefinite integrals of elementary functions in one table for quick reference.

默认对$x$求导/积分，不定积分统一写成“$+C$”。  
Unless stated otherwise, differentiation/integration is with respect to $x$, and indefinite integrals include “$+C$”.

## 常见函数 / Common Functions

|原式|求导|积分|
|---|---|---|
|$c$|$0$|$cx+C$|
|$x$|$1$|$\frac{x^2}{2}+C$|
|$x^n$|$nx^{n-1}$|$\frac{x^{n+1}}{n+1}+C\,(n\neq-1)$|
|$\frac{1}{x}$|$-\frac{1}{x^2}$|$\ln\lvert x\rvert+C$|
|$\sqrt{x}=x^{1/2}$|$\frac{1}{2\sqrt{x}}$|$\frac{2}{3}x^{3/2}+C$|
|$\lvert x\rvert$|$\frac{x}{\lvert x\rvert}\,(x\neq0)$|$\frac{x\lvert x\rvert}{2}+C$|
|$e^x$|$e^x$|$e^x+C$|
|$a^x$|$a^x\ln a$|$\frac{a^x}{\ln a}+C\,(a>0,a\neq1)$|
|$\ln x$|$\frac{1}{x}$|$x\ln x-x+C\,(x>0)$|
|$\ln\lvert x\rvert$|$\frac{1}{x}\,(x\neq0)$|$x\ln\lvert x\rvert-x+C$|
|$\sin x$|$\cos x$|$-\cos x+C$|
|$\cos x$|$-\sin x$|$\sin x+C$|
|$\tan x$|$\sec^2x$|$-\ln\lvert\cos x\rvert+C$|
|$\cot x$|$-\csc^2x$|$\ln\lvert\sin x\rvert+C$|
|$\sec x$|$\sec x\tan x$|$\ln\lvert\sec x+\tan x\rvert+C$|
|$\csc x$|$-\csc x\cot x$|$\ln\lvert\csc x-\cot x\rvert+C$|
|$\sec^2x$|$2\sec^2x\tan x$|$\tan x+C$|
|$\csc^2x$|$-2\csc^2x\cot x$|$-\cot x+C$|
|$\sec x\tan x$|$\sec x\tan^2x+\sec^3x$|$\sec x+C$|
|$\csc x\cot x$|$-\csc x\cot^2x-\csc^3x$|$-\csc x+C$|
|$\arcsin x$|$\frac{1}{\sqrt{1-x^2}}$|$x\arcsin x+\sqrt{1-x^2}+C$|
|$\arccos x$|$-\frac{1}{\sqrt{1-x^2}}$|$x\arccos x-\sqrt{1-x^2}+C$|
|$\arctan x$|$\frac{1}{1+x^2}$|$x\arctan x-\frac{1}{2}\ln(1+x^2)+C$|
|$\frac{1}{\sqrt{1-x^2}}$|$\frac{x}{(1-x^2)^{3/2}}$|$\arcsin x+C$|
|$\frac{1}{1+x^2}$|$-\frac{2x}{(1+x^2)^2}$|$\arctan x+C$|
|$\sinh x$|$\cosh x$|$\cosh x+C$|
|$\cosh x$|$\sinh x$|$\sinh x+C$|
|$\tanh x$|$\operatorname{sech}^2x$|$\ln(\cosh x)+C$|
|$\operatorname{sech}^2x$|$-2\operatorname{sech}^2x\tanh x$|$\tanh x+C$|

## 法则与技巧 / Rules & Techniques

|原式|求导|积分|
|---|---|---|
|$u(x)+v(x)$|$u'(x)+v'(x)$|$\int(u+v)\,dx=\int u\,dx+\int v\,dx$|
|$k\cdot u(x)$|$k\cdot u'(x)$|$\int ku\,dx=k\int u\,dx$|
|$u(x)v(x)$|$u'v+uv'$|$\int u\,dv=uv-\int v\,du$|
|$\frac{u(x)}{v(x)}$|$\frac{u'v-uv'}{v^2}\,(v\neq0)$|（按具体$u,v$选择代换/分部/部分分式等）|
|$f(g(x))$|$f'(g(x))g'(x)$|$\int f(g(x))g'(x)\,dx=\int f(u)\,du\,(u=g(x))$|
|$\frac{u'(x)}{u(x)}$|$\frac{u''u-(u')^2}{u^2}\,(u\neq0)$|$\int\frac{u'}{u}\,dx=\ln\lvert u\rvert+C$|

另见常用积分诱导公式表：[[Math_Calculus/4.Integrals/reduction_formulas]]。  
See also the common integration reduction formulas: [[Math_Calculus/4.Integrals/reduction_formulas]].

## 三角恒等与变形 / Trig Identities & Transformations

本节汇总三角恒等式的常用形式（和差、倍角、半角、和差化积、积化和差等），用于化简与积分。  
This section summarizes the most-used trig identities (sum/difference, multiple-angle, half-angle, sum-to-product, product-to-sum, etc.) for simplification and integration.

### 和差公式 / Sum & Difference

|公式 / Identity|条件 / Conditions|
|---|---|
|$\sin(A\pm B)=\sin A\cos B\pm\cos A\sin B$|—|
|$\cos(A\pm B)=\cos A\cos B\mp\sin A\sin B$|—|
|$\tan(A\pm B)=\dfrac{\tan A\pm\tan B}{1\mp\tan A\tan B}$|分母$\ne0$ / denominator $\ne0$|

### 二倍角 / Double-Angle

|公式 / Identity|等价形式 / Equivalent forms|
|---|---|
|$\sin(2x)=2\sin x\cos x$|—|
|$\cos(2x)=\cos^2x-\sin^2x$|$=1-2\sin^2x=2\cos^2x-1$|
|$\tan(2x)=\dfrac{2\tan x}{1-\tan^2x}$|分母$\ne0$ / denominator $\ne0$|

### 三倍角 / Triple-Angle

|公式 / Identity|说明 / Notes|
|---|---|
|$\sin(3x)=3\sin x-4\sin^3x$|—|
|$\cos(3x)=4\cos^3x-3\cos x$|—|
|若$t=\tan x$，则$\tan(3x)=\dfrac{3t-t^3}{1-3t^2}$|分母$\ne0$ / denominator $\ne0$|

### 半角 / Half-Angle

为避免正负号混乱，常用平方形式；若需要$\sin\frac{x}{2},\cos\frac{x}{2}$本身，请按象限取符号。  
To avoid sign ambiguity, squared forms are used; if you need $\sin\frac{x}{2}$ or $\cos\frac{x}{2}$ themselves, choose signs by quadrant.

|公式 / Identity|条件 / Conditions|
|---|---|
|$\sin^2\frac{x}{2}=\dfrac{1-\cos x}{2}$|—|
|$\cos^2\frac{x}{2}=\dfrac{1+\cos x}{2}$|—|
|$\tan\frac{x}{2}=\dfrac{\sin x}{1+\cos x}=\dfrac{1-\cos x}{\sin x}$|分母$\ne0$ / denominator $\ne0$|

### 降幂（平方角）/ Power-Reduction (Square-Angle)

“平方角公式”常用于把$\sin^2x,\cos^2x$转成含$2x$的一次三角函数，从而配合积分或化简。  
Power-reduction identities rewrite $\sin^2x,\cos^2x$ into first powers of trig functions in $2x$, useful for integrals and simplification.

|公式 / Identity|等价形式 / Equivalent forms|
|---|---|
|$\sin^2x=\dfrac{1-\cos(2x)}{2}$|—|
|$\cos^2x=\dfrac{1+\cos(2x)}{2}$|—|
|$\sin x\cos x=\dfrac{1}{2}\sin(2x)$|—|

### 和差化积 / Sum-to-Product

|公式 / Identity|说明 / Notes|
|---|---|
|$\sin A+\sin B=2\sin\frac{A+B}{2}\cos\frac{A-B}{2}$|—|
|$\sin A-\sin B=2\cos\frac{A+B}{2}\sin\frac{A-B}{2}$|—|
|$\cos A+\cos B=2\cos\frac{A+B}{2}\cos\frac{A-B}{2}$|—|
|$\cos A-\cos B=-2\sin\frac{A+B}{2}\sin\frac{A-B}{2}$|—|

### 积化和差 / Product-to-Sum

|公式 / Identity|说明 / Notes|
|---|---|
|$\sin A\sin B=\dfrac{1}{2}\bigl(\cos(A-B)-\cos(A+B)\bigr)$|—|
|$\cos A\cos B=\dfrac{1}{2}\bigl(\cos(A-B)+\cos(A+B)\bigr)$|—|
|$\sin A\cos B=\dfrac{1}{2}\bigl(\sin(A+B)+\sin(A-B)\bigr)$|—|
|$\cos A\sin B=\dfrac{1}{2}\bigl(\sin(A+B)-\sin(A-B)\bigr)$|—|

### 辅助角 / Auxiliary Angle (Combine $a\sin x+b\cos x$)

当题目出现$a\sin x+b\cos x$时，常把它写成单一正弦/余弦，便于求极值、解方程或积分。  
When you see $a\sin x+b\cos x$, rewrite it as a single sine/cosine to simplify extrema, equations, or integrals.

令$R=\sqrt{a^2+b^2}$，取$\varphi$使得$\cos\varphi=\frac{a}{R}$、$\sin\varphi=\frac{b}{R}$，则：  
Let $R=\sqrt{a^2+b^2}$ and choose $\varphi$ such that $\cos\varphi=\frac{a}{R}$ and $\sin\varphi=\frac{b}{R}$, then:

$$
a\sin x+b\cos x=R\sin(x+\varphi)=R\cos(x-\varphi).
$$

### 万能代换 / Weierstrass Substitution

当积分是$\sin x,\cos x$的有理函数时，令$t=\tan\frac{x}{2}$常能把三角积分变成有理函数积分。  
For rational functions of $\sin x$ and $\cos x$, the substitution $t=\tan\frac{x}{2}$ often converts trig integrals into rational integrals.

$$
t=\tan\frac{x}{2},\quad
\sin x=\frac{2t}{1+t^2},\quad
\cos x=\frac{1-t^2}{1+t^2},\quad
dx=\frac{2}{1+t^2}\,dt.
$$

### 欧拉公式与棣莫弗 / Euler & De Moivre

用欧拉公式可以快速推导多倍角、积化和差等恒等式，并在求和题里尤其好用。  
Euler’s formula quickly derives multiple-angle and product-sum identities, and is especially handy for trigonometric sums.

$$
e^{ix}=\cos x+i\sin x,\quad
\cos x=\frac{e^{ix}+e^{-ix}}{2},\quad
\sin x=\frac{e^{ix}-e^{-ix}}{2i}.
$$

棣莫弗公式：  
De Moivre’s formula:

$$
(\cos x+i\sin x)^n=\cos(nx)+i\sin(nx).
$$

### 等差角求和 / Sums over Arithmetic Progressions

当角是$a,a+d,a+2d,\dots$时，$\sum\sin$与$\sum\cos$可以用封闭形式表达。  
For angles in arithmetic progression $a,a+d,a+2d,\dots$, $\sum\sin$ and $\sum\cos$ have closed forms.

$$
\sum_{k=0}^{n-1}\cos(a+kd)=\frac{\sin\frac{nd}{2}}{\sin\frac{d}{2}}\cos\Bigl(a+\frac{(n-1)d}{2}\Bigr),
$$

$$
\sum_{k=0}^{n-1}\sin(a+kd)=\frac{\sin\frac{nd}{2}}{\sin\frac{d}{2}}\sin\Bigl(a+\frac{(n-1)d}{2}\Bigr),
$$

其中$\sin\frac{d}{2}\ne0$。  
where $\sin\frac{d}{2}\ne0$.

## 常用积分诱导公式 / Common Integration Reduction Formulas

本节汇总最常见的一组“诱导公式/递推公式”，用于把高次幂积分化为低次幂积分。  
This section summarizes commonly used reduction (recurrence) formulas that reduce higher-power integrals to lower-power ones.

默认变量为$x$，不定积分统一写成“$+C$”。  
Unless stated otherwise, the variable is $x$, and indefinite integrals include “$+C$”.

### 三角函数幂 / Trig Power

|类型 / Type|定义 / Definition|诱导公式 / Reduction formula|条件 / Conditions|
|---|---|---|---|
|$\int\sin^n x\,dx$|$I_n=\int\sin^n x\,dx$|$I_n=-\frac{\sin^{n-1}x\cos x}{n}+\frac{n-1}{n}I_{n-2}$|$n\ge2$|
|$\int\cos^n x\,dx$|$J_n=\int\cos^n x\,dx$|$J_n=\frac{\cos^{n-1}x\sin x}{n}+\frac{n-1}{n}J_{n-2}$|$n\ge2$|
|$\int\tan^n x\,dx$|$T_n=\int\tan^n x\,dx$|$T_n=\frac{\tan^{n-1}x}{n-1}-T_{n-2}$|$n\ge2$|
|$\int\cot^n x\,dx$|$\operatorname{Cot}_n=\int\cot^n x\,dx$|$\operatorname{Cot}_n=-\frac{\cot^{n-1}x}{n-1}-\operatorname{Cot}_{n-2}$|$n\ge2$|
|$\int\sec^n x\,dx$|$\operatorname{Sec}_n=\int\sec^n x\,dx$|$\operatorname{Sec}_n=\frac{\sec^{n-2}x\tan x}{n-1}+\frac{n-2}{n-1}\operatorname{Sec}_{n-2}$|$n\ge2$|
|$\int\csc^n x\,dx$|$\operatorname{Csc}_n=\int\csc^n x\,dx$|$\operatorname{Csc}_n=-\frac{\csc^{n-2}x\cot x}{n-1}+\frac{n-2}{n-1}\operatorname{Csc}_{n-2}$|$n\ge2$|

### 多项式×指数/三角 / Polynomial × Exponential/Trig

|类型 / Type|定义 / Definition|诱导公式 / Reduction formula|条件 / Conditions|
|---|---|---|---|
|$\int x^n e^{ax}\,dx$|$E_n=\int x^n e^{ax}\,dx$|$E_n=\frac{x^n e^{ax}}{a}-\frac{n}{a}E_{n-1}$|$n\ge1,a\ne0$|
|$\int x^n\sin(ax)\,dx$|$S_n=\int x^n\sin(ax)\,dx$|$S_n=-\frac{x^n\cos(ax)}{a}+\frac{n}{a}C_{n-1}$|$n\ge1,a\ne0$|
|$\int x^n\cos(ax)\,dx$|$C_n=\int x^n\cos(ax)\,dx$|$C_n=\frac{x^n\sin(ax)}{a}-\frac{n}{a}S_{n-1}$|$n\ge1,a\ne0$|

### 对数幂 / Log-Power

|类型 / Type|定义 / Definition|诱导公式 / Reduction formula|条件 / Conditions|
|---|---|---|---|
|$\int(\ln x)^n\,dx$|$L_n=\int(\ln x)^n\,dx$|$L_n=x(\ln x)^n-nL_{n-1}$|$n\ge1,x>0$|

## $\int\sec^nx\tan^nx\,dx$ / Integrals of $\sec^nx\tan^nx$

### 定义与直觉 / Definition & Intuition
- 目标形式 / Target form：计算$\int\sec^nx\tan^nx\,dx$，其中$n\in\mathbb{N}$。  
  Compute $\int\sec^nx\tan^nx\,dx$ with $n\in\mathbb{N}$.
- 核心想法 / Core idea：利用$\tan^2x=\sec^2x-1$与$\sec^2x=1+\tan^2x$，配合“拆出一个导数因子”来做代换。  
  Use $\tan^2x=\sec^2x-1$ and $\sec^2x=1+\tan^2x$, plus “peel off a derivative factor” for substitution.

### 关键结论 / Key Results
- 恒等式 / Identities：$\tan^2x=\sec^2x-1$，$\sec^2x=1+\tan^2x$。  
  Identities: $\tan^2x=\sec^2x-1$, $\sec^2x=1+\tan^2x$.
- $n$为奇数 / $n$ odd：拆出一个$\sec x\tan x\,dx$，令$u=\sec x$，则$du=\sec x\tan x\,dx$；其余用$\tan^2x=\sec^2x-1$化为$u$的多项式：  
  If $n$ is odd, peel off $\sec x\tan x\,dx$, set $u=\sec x$, so $du=\sec x\tan x\,dx$; convert the rest using $\tan^2x=\sec^2x-1$ into a polynomial in $u$:
  $$
  \sec^{n-1}x\tan^{n-1}x=u^{n-1}(u^2-1)^{(n-1)/2}.
  $$
- $n$为偶数且$n\ge2$ / $n$ even and $n\ge2$：改写为$\tan^nx\sec^{n-2}x\sec^2x\,dx$，令$u=\tan x$，则$du=\sec^2x\,dx$；其余用$\sec^{n-2}x=(1+u^2)^{(n-2)/2}$。  
  If $n$ is even with $n\ge2$, rewrite as $\tan^nx\sec^{n-2}x\sec^2x\,dx$, set $u=\tan x$, so $du=\sec^2x\,dx$; use $\sec^{n-2}x=(1+u^2)^{(n-2)/2}$.
- 特例 / Special case（$n=1$）：$\int\sec x\tan x\,dx=\sec x+C$。  
  Special case ($n=1$): $\int\sec x\tan x\,dx=\sec x+C$.

### 例子 / Examples
- $n=2$：  
  $$
  \int\sec^2x\tan^2x\,dx=\int u^2\,du=\frac{\tan^3x}{3}+C,\quad(u=\tan x).
  $$
- $n=3$：  
  $$
  \int\sec^3x\tan^3x\,dx=\int u^2(u^2-1)\,du=\frac{u^5}{5}-\frac{u^3}{3}+C=\frac{\sec^5x}{5}-\frac{\sec^3x}{3}+C,\quad(u=\sec x).
  $$

## 来源 / Sources

- 三角恒等变形速查：[[Math_Calculus/1.Precalculus/trig_identities]]  
  Trig identities: [[Math_Calculus/1.Precalculus/trig_identities]]
- 常用积分诱导公式表：[[Math_Calculus/4.Integrals/reduction_formulas]]  
  Reduction formulas: [[Math_Calculus/4.Integrals/reduction_formulas]]
- $\int\sec^nx\tan^nx\,dx$：[[Math_Calculus/4.Integrals/sec_tan_power_integrals]]  
  $\int\sec^nx\tan^nx\,dx$: [[Math_Calculus/4.Integrals/sec_tan_power_integrals]]

## 矩阵乘矩阵 / Matrix-Matrix Multiplication

设$A\in\mathbb R^{m\times n}$，$B\in\mathbb R^{n\times p}$，则乘积$AB$有定义，且$AB\in\mathbb R^{m\times p}$。  
Let $A\in\mathbb R^{m\times n}$ and $B\in\mathbb R^{n\times p}$; then $AB$ is defined and $AB\in\mathbb R^{m\times p}$.

元素公式 / Entry formula：
$$
(AB)_{ij}=\sum_{k=1}^na_{ik}b_{kj}\quad(1\le i\le m,\;1\le j\le p).
$$

常见维度直接公式 / Direct formulas for common sizes：

1) $2\times2\cdot2\times2\to2\times2$
$$
\begin{bmatrix}
a_{11}&a_{12}\\
a_{21}&a_{22}
\end{bmatrix}
\begin{bmatrix}
b_{11}&b_{12}\\
b_{21}&b_{22}
\end{bmatrix}
=
\begin{bmatrix}
a_{11}b_{11}+a_{12}b_{21}&a_{11}b_{12}+a_{12}b_{22}\\
a_{21}b_{11}+a_{22}b_{21}&a_{21}b_{12}+a_{22}b_{22}
\end{bmatrix}.
$$

2) $2\times3\cdot3\times2\to2\times2$
$$
\begin{bmatrix}
a_{11}&a_{12}&a_{13}\\
a_{21}&a_{22}&a_{23}
\end{bmatrix}
\begin{bmatrix}
b_{11}&b_{12}\\
b_{21}&b_{22}\\
b_{31}&b_{32}
\end{bmatrix}
=
\begin{bmatrix}
a_{11}b_{11}+a_{12}b_{21}+a_{13}b_{31}&a_{11}b_{12}+a_{12}b_{22}+a_{13}b_{32}\\
a_{21}b_{11}+a_{22}b_{21}+a_{23}b_{31}&a_{21}b_{12}+a_{22}b_{22}+a_{23}b_{32}
\end{bmatrix}.
$$

3) $3\times2\cdot2\times3\to3\times3$
$$
\begin{bmatrix}
a_{11}&a_{12}\\
a_{21}&a_{22}\\
a_{31}&a_{32}
\end{bmatrix}
\begin{bmatrix}
b_{11}&b_{12}&b_{13}\\
b_{21}&b_{22}&b_{23}
\end{bmatrix}
=
\begin{bmatrix}
a_{11}b_{11}+a_{12}b_{21}&a_{11}b_{12}+a_{12}b_{22}&a_{11}b_{13}+a_{12}b_{23}\\
a_{21}b_{11}+a_{22}b_{21}&a_{21}b_{12}+a_{22}b_{22}&a_{21}b_{13}+a_{22}b_{23}\\
a_{31}b_{11}+a_{32}b_{21}&a_{31}b_{12}+a_{32}b_{22}&a_{31}b_{13}+a_{32}b_{23}
\end{bmatrix}.
$$

4) $3\times3\cdot3\times3\to3\times3$
$$
\begin{bmatrix}
a_{11}&a_{12}&a_{13}\\
a_{21}&a_{22}&a_{23}\\
a_{31}&a_{32}&a_{33}
\end{bmatrix}
\begin{bmatrix}
b_{11}&b_{12}&b_{13}\\
b_{21}&b_{22}&b_{23}\\
b_{31}&b_{32}&b_{33}
\end{bmatrix}
=
\begin{bmatrix}
c_{11}&c_{12}&c_{13}\\
c_{21}&c_{22}&c_{23}\\
c_{31}&c_{32}&c_{33}
\end{bmatrix},
$$
其中/where
$$
\begin{aligned}
c_{11}&=a_{11}b_{11}+a_{12}b_{21}+a_{13}b_{31},&c_{12}&=a_{11}b_{12}+a_{12}b_{22}+a_{13}b_{32},&c_{13}&=a_{11}b_{13}+a_{12}b_{23}+a_{13}b_{33},\\
c_{21}&=a_{21}b_{11}+a_{22}b_{21}+a_{23}b_{31},&c_{22}&=a_{21}b_{12}+a_{22}b_{22}+a_{23}b_{32},&c_{23}&=a_{21}b_{13}+a_{22}b_{23}+a_{23}b_{33},\\
c_{31}&=a_{31}b_{11}+a_{32}b_{21}+a_{33}b_{31},&c_{32}&=a_{31}b_{12}+a_{32}b_{22}+a_{33}b_{32},&c_{33}&=a_{31}b_{13}+a_{32}b_{23}+a_{33}b_{33}.
\end{aligned}
$$

推导（按列向量）/ Derivation (via columns)：  
将$B$写成$B=[\mathbf b_1,\dots,\mathbf b_p]$，则$AB=[A\mathbf b_1,\dots,A\mathbf b_p]$。  
Write $B$ as $B=[\mathbf b_1,\dots,\mathbf b_p]$, then $AB=[A\mathbf b_1,\dots,A\mathbf b_p]$.

对第$j$列，$\mathbf b_j=\sum_{k=1}^nb_{kj}\mathbf e_k$，所以  
For the $j$-th column, $\mathbf b_j=\sum_{k=1}^nb_{kj}\mathbf e_k$, so
$$
A\mathbf b_j=A\Bigl(\sum_{k=1}^nb_{kj}\mathbf e_k\Bigr)=\sum_{k=1}^nb_{kj}A\mathbf e_k=\sum_{k=1}^nb_{kj}\mathbf a_k.
$$
取第$i$个分量即得  
Taking the $i$-th component yields
$$
(AB)_{ij}=\sum_{k=1}^na_{ik}b_{kj}.
$$

连续变换顺序 / Order of successive transformations：若标准矩阵$B$先把$\mathbf x$变为$\mathbf y=B\mathbf x$，再由$A$把$\mathbf y$变为$\mathbf z=A\mathbf y$，则
Order rule: if matrix $B$ first maps $\mathbf x$ to $\mathbf y=B\mathbf x$, and then $A$ maps $\mathbf y$ to $\mathbf z=A\mathbf y$, then
$$
\mathbf z=A(B\mathbf x)=(AB)\mathbf x.
$$
因此复合变换$T_A\circ T_B$对应矩阵$AB$，并且“先变换的矩阵写在右边、后变换的写在左边”。  
So the composition $T_A\circ T_B$ corresponds to $AB$, and the matrix that acts first is on the right.

对应日记：[[journal/2026-02-16]]。  
Related daily note: [[journal/2026-02-16]].
