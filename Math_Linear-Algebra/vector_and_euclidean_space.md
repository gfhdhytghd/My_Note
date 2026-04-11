# 向量与欧几里得空间 / Vectors and Euclidean Spaces

## 向量与向量空间 / Vectors and Vector Spaces
向量（vector）可以被看作“可相加、可数乘”的对象；抽象地说，向量空间是一个集合$V$，配备加法$+$与数乘$\cdot$，满足封闭性与一组线性公理（交换、结合、零向量、逆元、分配律等）。  
A vector can be viewed as an object you can add and scale; abstractly, a vector space is a set $V$ with addition $+$ and scalar multiplication $\cdot$ satisfying closure and linear axioms (commutativity/associativity, zero, inverses, distributivity, etc.).

### 零向量$\mathbf{0}$的性质 / Properties of the Zero Vector $\mathbf{0}$
零向量（zero vector）是加法单位元：对任意$v\in V$，都有$v+\mathbf{0}=v$。  
The zero vector is the additive identity: for any $v\in V$, $v+\mathbf{0}=v$.

常用结论（在任意向量空间中都成立）：  
Common consequences (true in any vector space):

- 唯一性 / Uniqueness：若$z$满足对任意$v$都有$v+z=v$，则$z=\mathbf{0}$。  
  If $z$ satisfies $v+z=v$ for all $v$, then $z=\mathbf{0}$.
- 消去律的特例 / A cancellation special case：若$v+w=v$，则$w=\mathbf{0}$。  
  If $v+w=v$, then $w=\mathbf{0}$.
- 逆元关系 / Additive inverse：对任意$v$存在唯一$-v$使得$v+(-v)=\mathbf{0}$；若$v+w=\mathbf{0}$，则$w=-v$。  
  For any $v$ there is a unique $-v$ with $v+(-v)=\mathbf{0}$; if $v+w=\mathbf{0}$ then $w=-v$.
- 与数乘的相容性 / Compatibility with scalar multiplication：$0\cdot v=\mathbf{0}$且$a\cdot\mathbf{0}=\mathbf{0}$（对任意标量$a$）。  
  $0\cdot v=\mathbf{0}$ and $a\cdot\mathbf{0}=\mathbf{0}$ (for any scalar $a$).
- “零向量不携带方向”/ No direction：在欧氏空间里$\mathbf{0}\cdot x=0$对任意$x$成立，但$\mathbf{0}$与任何非零向量的夹角通常不定义（因为$\|\mathbf{0}\|=0$）。  
  In Euclidean spaces, $\mathbf{0}\cdot x=0$ for any $x$, but the angle between $\mathbf{0}$ and a nonzero vector is typically undefined (since $\|\mathbf{0}\|=0$).

线性组合与张成：给定向量$v_1,\dots,v_k\in V$，形如$a_1v_1+\cdots+a_kv_k$（$a_i\in\mathbb{R}$）的向量称为线性组合；所有线性组合的集合称为$\operatorname{span}\{v_1,\dots,v_k\}$。  
Linear combination & span: given $v_1,\dots,v_k\in V$, any $a_1v_1+\cdots+a_kv_k$ ($a_i\in\mathbb{R}$) is a linear combination; the set of all such combinations is $\operatorname{span}\{v_1,\dots,v_k\}$.

线性无关与基：若$a_1v_1+\cdots+a_kv_k=\mathbf{0}$只可能推出$a_1=\cdots=a_k=0$，则$\{v_1,\dots,v_k\}$线性无关；能张成整个$V$且线性无关的集合称为一组基（basis），基的向量个数称为维数（dimension）。  
Linear independence & basis: if $a_1v_1+\cdots+a_kv_k=\mathbf{0}$ implies $a_1=\cdots=a_k=0$, then $\{v_1,\dots,v_k\}$ is linearly independent; a spanning independent set is a basis, and its size is the dimension.

### 向量空间快速检查 / Quick Check for a Vector Space
课堂上常用的第一轮检查是：集合是否包含零向量、是否对加法封闭、是否对数乘封闭。  
A common first-pass classroom check is: does the set contain the zero vector, and is it closed under addition and scalar multiplication.

严格定义还包含交换律、结合律、分配律等公理；但在常见的矩阵空间、多项式空间、欧氏空间子集里，这些运算规则通常继承自母空间，所以做题时常先抓“零向量 + 两种封闭性”。  
The full definition also includes commutativity, associativity, and distributive laws; but for common matrix spaces, polynomial spaces, and subsets of Euclidean spaces, those rules are inherited from the ambient space, so the practical checklist is often “zero vector + two closure properties.”

### “非正交$n$个向量也能表示任意向量”/ Non-orthogonal $n$ vectors can still represent any vector
常见说法“$n$个非正交向量相加可得到任意向量”更准确地应表述为：在$\mathbb{R}^n$中，只要给定$n$个线性无关向量$v_1,\dots,v_n$（不要求正交），那么任意向量$x\in\mathbb{R}^n$都能写成它们的线性组合：  
The common statement “$n$ non-orthogonal vectors can be added to get any vector” is more precisely: in $\mathbb{R}^n$, if you have $n$ linearly independent vectors $v_1,\dots,v_n$ (not necessarily orthogonal), then any $x\in\mathbb{R}^n$ can be written as a linear combination:
$$
x=a_1v_1+\cdots+a_nv_n.
$$

并且系数$(a_1,\dots,a_n)$是唯一的（因为$\{v_1,\dots,v_n\}$构成一组基）。  
Moreover, the coefficients $(a_1,\dots,a_n)$ are unique (since $\{v_1,\dots,v_n\}$ forms a basis).

矩阵视角：把$v_1,\dots,v_n$作为列向量组成矩阵$A=[v_1\ \cdots\ v_n]$，则“能表示任意$x$且表示唯一”等价于$A$可逆（$\det A\neq0$），此时$a=A^{-1}x$。  
Matrix view: put $v_1,\dots,v_n$ as columns of $A=[v_1\ \cdots\ v_n]$; being able to represent any $x$ uniquely is equivalent to $A$ being invertible ($\det A\neq0$), and then $a=A^{-1}x$.

注意：这里的“和”为带系数的和（线性组合），不是简单的$v_1+\cdots+v_n$。  
Note: the “sum” here is a weighted sum (a linear combination), not the plain $v_1+\cdots+v_n$.

## $\mathbb{R}^n$与坐标 / $\mathbb{R}^n$ and Coordinates
最常用的例子是$V=\mathbb{R}^n$：向量写成列向量或有序$n$元组$x=(x_1,\dots,x_n)$，标准基为$e_1,\dots,e_n$，其中$e_i$在第$i$个分量为$1$其余为$0$。  
The most common example is $V=\mathbb{R}^n$: vectors are column vectors or ordered $n$-tuples $x=(x_1,\dots,x_n)$, with the standard basis $e_1,\dots,e_n$ where $e_i$ has a $1$ in component $i$ and $0$ elsewhere.

在给定基$B=\{b_1,\dots,b_n\}$下，任意向量都可写为$x=c_1b_1+\cdots+c_nb_n$；系数$(c_1,\dots,c_n)$就是$x$在该基下的坐标。  
With a basis $B=\{b_1,\dots,b_n\}$, any vector can be written as $x=c_1b_1+\cdots+c_nb_n$; the coefficients $(c_1,\dots,c_n)$ are the coordinates of $x$ in that basis.

### 基与维数的典型例子 / Standard Examples of Basis and Dimension
- $\mathbb{R}^3$的标准基是
  The standard basis of $\mathbb{R}^3$ is
  $$
  \left\{
  \begin{bmatrix}1\\0\\0\end{bmatrix},
  \begin{bmatrix}0\\1\\0\end{bmatrix},
  \begin{bmatrix}0\\0\\1\end{bmatrix}
  \right\},
  $$
  因此$\dim(\mathbb{R}^3)=3$。  
  so $\dim(\mathbb{R}^3)=3$.

- 矩阵空间$M_{2\times2}(\mathbb{R})$的一组自然基是四个矩阵单位
  A natural basis for $M_{2\times2}(\mathbb{R})$ is given by the four matrix units
  $$
  \left\{
  \begin{bmatrix}1&0\\0&0\end{bmatrix},
  \begin{bmatrix}0&1\\0&0\end{bmatrix},
  \begin{bmatrix}0&0\\1&0\end{bmatrix},
  \begin{bmatrix}0&0\\0&1\end{bmatrix}
  \right\},
  $$
  所以$\dim(M_{2\times2}(\mathbb{R}))=4$。  
  so $\dim(M_{2\times2}(\mathbb{R}))=4$.

- 多项式空间$P_2(\mathbb{R})=\{ax^2+bx+c\mid a,b,c\in\mathbb{R}\}$的一组标准基是$\{1,x,x^2\}$，因此维数为$3$。  
  A standard basis of $P_2(\mathbb{R})=\{ax^2+bx+c\mid a,b,c\in\mathbb{R}\}$ is $\{1,x,x^2\}$, so its dimension is $3$.

- 对称矩阵空间$\operatorname{Sym}_{n\times n}(\mathbb{R})=\{A\mid A^T=A\}$是$M_{n\times n}(\mathbb{R})$的子空间，其一组自然基可写为对角单位矩阵$E_{11},\dots,E_{nn}$与所有$E_{ij}+E_{ji}$（$i<j$）；因此
  The symmetric matrix space $\operatorname{Sym}_{n\times n}(\mathbb{R})=\{A\mid A^T=A\}$ is a subspace of $M_{n\times n}(\mathbb{R})$, with a natural basis given by diagonal units $E_{11},\dots,E_{nn}$ together with all $E_{ij}+E_{ji}$ for $i<j$; therefore
  $$
  \dim(\operatorname{Sym}_{n\times n}(\mathbb{R}))=\frac{n(n+1)}{2}.
  $$

### $\mathbb{R}^2$不是$\mathbb{R}^3$的子空间 / Why $\mathbb{R}^2$ Is Not a Subspace of $\mathbb{R}^3$
$\mathbb{R}^2$本身不是$\mathbb{R}^3$的子空间，因为子空间必须先是母空间的子集，而$\mathbb{R}^2$里的元素是$(x,y)$，$\mathbb{R}^3$里的元素是$(x,y,z)$，两者不是同一种对象。  
$\mathbb{R}^2$ itself is not a subspace of $\mathbb{R}^3$ because a subspace must first be a subset of the ambient space, and elements of $\mathbb{R}^2$ are pairs $(x,y)$ while elements of $\mathbb{R}^3$ are triples $(x,y,z)$.

不过，$\mathbb{R}^3$里确实存在与$\mathbb{R}^2$“同构”的平面子空间，例如
However, $\mathbb{R}^3$ does contain plane subspaces that are isomorphic to $\mathbb{R}^2$, for example
$$
W=\{(x,y,0)\mid x,y\in\mathbb{R}\}.
$$
这个集合包含零向量，且对加法与数乘都封闭，所以它才是$\mathbb{R}^3$里的真正子空间。  
This set contains the zero vector and is closed under addition and scalar multiplication, so it is a genuine subspace of $\mathbb{R}^3$.

## 内积、范数与距离 / Inner Product, Norm, and Distance
欧几里得空间（Euclidean space）常指带有“内积”（inner product）的实向量空间；在$\mathbb{R}^n$中最典型的内积是点积：$x\cdot y=\sum_{i=1}^n x_iy_i$。  
A Euclidean space often means a real vector space equipped with an inner product; in $\mathbb{R}^n$ the standard one is the dot product $x\cdot y=\sum_{i=1}^n x_iy_i$.

内积给出几何量：范数（length）$\|x\|=\sqrt{x\cdot x}$，距离$d(x,y)=\|x-y\|$，以及夹角$\theta$满足$\cos\theta=\frac{x\cdot y}{\|x\|\|y\|}$（当$x,y\neq\mathbf{0}$）。  
The inner product induces geometric quantities: norm (length) $\|x\|=\sqrt{x\cdot x}$, distance $d(x,y)=\|x-y\|$, and angle $\theta$ via $\cos\theta=\frac{x\cdot y}{\|x\|\|y\|}$ (when $x,y\neq\mathbf{0}$).

## 正交、投影与分解 / Orthogonality, Projection, and Decomposition
若$x\cdot y=0$，则称$x$与$y$正交（orthogonal）；若再满足$\|x\|=\|y\|=1$，则称为规范正交（orthonormal）。  
If $x\cdot y=0$, then $x$ and $y$ are orthogonal; if also $\|x\|=\|y\|=1$, they are orthonormal.

投影：当$u\neq\mathbf{0}$时，$v$在$u$方向上的正交投影为$\operatorname{proj}_u(v)=\frac{v\cdot u}{u\cdot u}u$；于是$v$可分解为$v=\operatorname{proj}_u(v)+v_\perp$且$v_\perp\cdot u=0$。  
Projection: for $u\neq\mathbf{0}$, the orthogonal projection of $v$ onto $u$ is $\operatorname{proj}_u(v)=\frac{v\cdot u}{u\cdot u}u$; thus $v=\operatorname{proj}_u(v)+v_\perp$ with $v_\perp\cdot u=0$.

勾股关系：若$x\perp y$，则$\|x+y\|^2=\|x\|^2+\|y\|^2$（由展开$(x+y)\cdot(x+y)$即可）。  
Pythagorean relation: if $x\perp y$, then $\|x+y\|^2=\|x\|^2+\|y\|^2$ (expand $(x+y)\cdot(x+y)$).

## 常用不等式 / Useful Inequalities
柯西-施瓦茨不等式（Cauchy–Schwarz）：$|x\cdot y|\le\|x\|\|y\|$；三角不等式：$\|x+y\|\le\|x\|+\|y\|$。  
Cauchy–Schwarz: $|x\cdot y|\le\|x\|\|y\|$; triangle inequality: $\|x+y\|\le\|x\|+\|y\|$.

这些性质保证$\|x\|$确实像“长度”，$d(x,y)$确实像“距离”（满足非负、对称、三角不等式）。  
These properties ensure $\|x\|$ behaves like “length” and $d(x,y)$ behaves like a “distance” (nonnegative, symmetric, triangle inequality).

## 关联笔记 / Related Notes
- 物理里的向量直觉与点积/叉积：[[Physics/1.Vectors/vectors_and_scalars]]。  
  Physics intuition (dot/cross products): [[Physics/1.Vectors/vectors_and_scalars]].
- 基与维数：[[Math_Linear-Algebra/basis_and_dimension]]。  
  Basis and dimension: [[Math_Linear-Algebra/basis_and_dimension]].
- 换基与坐标变换：[[Math_Linear-Algebra/change_of_basis_coordinates]]。  
  Change of basis and coordinate conversion: [[Math_Linear-Algebra/change_of_basis_coordinates]].
- 线性方程组与向量表示：[[Math_Linear-Algebra/gauss_jordan_elimination]]。  
  Linear systems as vectors: [[Math_Linear-Algebra/gauss_jordan_elimination]].

## 来源 / Source
- 来源 / Source: [[journal/2026-01-28]]  
  Source journal: [[journal/2026-01-28]]
- 来源 / Source: [[journal/2026-03-16]]  
  Source journal: [[journal/2026-03-16]]
- 来源 / Source: [[journal/2026-03-18]]  
  Source journal: [[journal/2026-03-18]]

[//begin]: # "Autogenerated link references for markdown compatibility"
[//end]: # "Autogenerated link references"
