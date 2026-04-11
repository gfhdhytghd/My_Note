# 线性组合、张成与组分 / Linear Combinations, Span, and Components

## 线性组合 / Linear Combination
给定向量空间$V$（标量域为$\mathbb{F}$）中的向量$v_1,\dots,v_k$，形如
$$
a_1v_1+\cdots+a_kv_k\quad(a_i\in\mathbb{F})
$$
的向量称为它们的线性组合（linear combination）。  
Given vectors $v_1,\dots,v_k$ in a vector space $V$ over $\mathbb{F}$, any vector of the form $a_1v_1+\cdots+a_kv_k$ ($a_i\in\mathbb{F}$) is called a linear combination.

矩阵视角：把$v_1,\dots,v_k$作为列向量组成矩阵$A=[v_1\ \cdots\ v_k]$，则线性组合就是$Ax$，其中$x=(a_1,\dots,a_k)^\mathsf{T}$。  
Matrix view: put $v_1,\dots,v_k$ as columns of $A=[v_1\ \cdots\ v_k]$, then a linear combination is $Ax$ with $x=(a_1,\dots,a_k)^\mathsf{T}$.

### 现代“格式/记号”/ Modern Notation (Formatting)
把“多个向量+多个系数”的写法压缩成一次矩阵-向量乘法：把向量当作列拼成矩阵，把系数排成列向量。  
Compress “many vectors + many coefficients” into one matrix–vector product: stack vectors as columns in a matrix and stack coefficients into a column vector.

若$v_1,v_2,v_3\in\mathbb{R}^n$，系数为$c_1,c_2,c_3$，则
$$
[v_1\ v_2\ v_3]\begin{bmatrix}c_1\\c_2\\c_3\end{bmatrix}=c_1v_1+c_2v_2+c_3v_3.
$$
If $v_1,v_2,v_3\in\mathbb{R}^n$ with coefficients $c_1,c_2,c_3$, then $[v_1\ v_2\ v_3]\begin{bmatrix}c_1\\c_2\\c_3\end{bmatrix}=c_1v_1+c_2v_2+c_3v_3$.

一个对照例子（和课堂板书的“格式”一致）：令
$$
v_1=\begin{bmatrix}1\\2\end{bmatrix},\quad
v_2=\begin{bmatrix}2\\5\end{bmatrix},\quad
v_3=\begin{bmatrix}1\\-3\end{bmatrix},\quad
c=\begin{bmatrix}2\\5\\-4\end{bmatrix}.
$$
Then with $A=[v_1\ v_2\ v_3]$, we have
$$
Ac=\begin{bmatrix}1&2&1\\2&5&-3\end{bmatrix}\begin{bmatrix}2\\5\\-4\end{bmatrix}=2v_1+5v_2-4v_3.
$$

常见格式提醒：$[v_1\ v_2\ v_3]$表示“以这些向量为列的矩阵”，不是把它们做点积；系数写成列向量时，乘法$Ac$才维度匹配。  
Formatting reminder: $[v_1\ v_2\ v_3]$ means a matrix with these vectors as columns (not a dot product); writing coefficients as a column vector makes $Ac$ dimension-consistent.

## 张成与生成集 / Span and Generating Set
所有线性组合构成的集合称为张成（span）：
$$
\operatorname{span}\{v_1,\dots,v_k\}=\{a_1v_1+\cdots+a_kv_k:a_i\in\mathbb{F}\}.
$$
The set of all linear combinations is the span:
$\operatorname{span}\{v_1,\dots,v_k\}=\{a_1v_1+\cdots+a_kv_k:a_i\in\mathbb{F}\}$.

重要性质：$\operatorname{span}\{v_1,\dots,v_k\}$一定是$V$的一个线性子空间（对加法与数乘封闭），并且它是“包含这组向量的最小子空间”。  
Key property: $\operatorname{span}\{v_1,\dots,v_k\}$ is always a subspace of $V$ (closed under addition and scalar multiplication), and it is the smallest subspace containing those vectors.

若$\operatorname{span}\{v_1,\dots,v_k\}=V$，就说这组向量生成（span/generate）整个空间$V$，它们是$V$的一个生成集（generating set）。  
If $\operatorname{span}\{v_1,\dots,v_k\}=V$, then the vectors span/generate $V$ and form a generating set of $V$.

## 线性相关/无关与表示唯一性 / Dependence/Independence and Uniqueness
线性无关（linearly independent）的定义：若
$$
a_1v_1+\cdots+a_kv_k=\mathbf{0}
$$
只能推出$a_1=\cdots=a_k=0$，则$\{v_1,\dots,v_k\}$线性无关；否则线性相关（dependent）。  
Definition: $\{v_1,\dots,v_k\}$ is linearly independent if $a_1v_1+\cdots+a_kv_k=\mathbf{0}$ forces $a_1=\cdots=a_k=0$; otherwise it is dependent.

表示是否唯一：  
Uniqueness of representation:

- 若$v_1,\dots,v_k$线性无关，则在它们张成的子空间里，每个向量的系数表示是唯一的。  
  If $v_1,\dots,v_k$ are independent, then every vector in their span has a unique coefficient representation.
- 若线性相关，则表示通常不唯一（会出现“同一个向量有不同系数写法”）。  
  If they are dependent, representations are typically not unique (the same vector can be written with different coefficients).

小例子：在$\mathbb{R}^2$里取$v_1=(1,0)$、$v_2=(2,0)$，则$(2,0)=2v_1=1v_2$，系数不唯一，因为$\{v_1,v_2\}$线性相关。  
Quick example: in $\mathbb{R}^2$ with $v_1=(1,0)$ and $v_2=(2,0)$, we have $(2,0)=2v_1=1v_2$, so coefficients are not unique because $\{v_1,v_2\}$ is dependent.

## “组分/分量”的两种常见用法 / Two Common Meanings of “Components”
“线性组分”在笔记里常见有两种理解：一种是“相对于一组基的坐标分量”，另一种是“沿某个方向的投影分量”。  
In practice, “components” often means either coordinates in a basis or projection components along a direction.

### 1) 相对于基的坐标分量 / Coordinates in a Basis
给定$\mathbb{R}^n$的一组基$B=\{b_1,\dots,b_n\}$，任意向量$x$都能唯一写成
$$
x=c_1b_1+\cdots+c_nb_n,
$$
这里的$c_1,\dots,c_n$就是$x$在基$B$下的“组分/分量”（components），向量$c=(c_1,\dots,c_n)^\mathsf{T}$称为坐标向量$[x]_B$。  
Given a basis $B=\{b_1,\dots,b_n\}$ of $\mathbb{R}^n$, any vector $x$ can be uniquely written as $x=c_1b_1+\cdots+c_nb_n$; the scalars $c_1,\dots,c_n$ are the components of $x$ in basis $B$, and $c=(c_1,\dots,c_n)^\mathsf{T}$ is the coordinate vector $[x]_B$.

矩阵写法：令$B=[b_1\ \cdots\ b_n]$，则$x=Bc$，所以$c=B^{-1}x$（当$B$可逆，也就是$b_i$确实构成基）。  
Matrix form: with $B=[b_1\ \cdots\ b_n]$, we have $x=Bc$, so $c=B^{-1}x$ (when $B$ is invertible, i.e., the $b_i$ form a basis).

### 2) 沿方向的投影分量 / Projection Components Along a Direction
若$u$是单位向量（$\|u\|=1$），则$v$在$u$方向上的“标量分量”（scalar component）为$v\cdot u$，“向量分量”（vector component）为$(v\cdot u)u$。  
If $u$ is a unit vector ($\|u\|=1$), then the scalar component of $v$ along $u$ is $v\cdot u$, and the vector component is $(v\cdot u)u$.

若$u$不是单位向量，则正交投影为
$$
\operatorname{proj}_u(v)=\frac{v\cdot u}{u\cdot u}u.
$$
If $u$ is not unit length, the orthogonal projection is $\operatorname{proj}_u(v)=\frac{v\cdot u}{u\cdot u}u$.

## 线性方程组视角：求系数 / Linear Systems View: Solving for Coefficients
把$v_1,\dots,v_k$放成矩阵$A=[v_1\ \cdots\ v_k]$后，“向量$b$能否表示为它们的线性组合”就是问线性方程组$Ax=b$是否有解；“系数是否唯一”对应解是否唯一（是否存在自由变量）。  
With $A=[v_1\ \cdots\ v_k]$, the question “can $b$ be expressed as a linear combination of them?” becomes whether $Ax=b$ is solvable; “are the coefficients unique?” corresponds to whether the solution is unique (no free variables).

把这个过程用行变换做出来，就对应到高斯消元/高斯-约旦。  
Computing this via row operations corresponds to Gaussian / Gauss–Jordan elimination.

## 小例子 / Quick Examples
例1（坐标分量）：在$\mathbb{R}^2$取$b_1=(1,1)$、$b_2=(1,-1)$，则$(2,0)=1\cdot b_1+1\cdot b_2$，所以$[(2,0)]_B=(1,1)^\mathsf{T}$。  
Example 1 (coordinates): in $\mathbb{R}^2$ with $b_1=(1,1)$ and $b_2=(1,-1)$, we have $(2,0)=1\cdot b_1+1\cdot b_2$, so $[(2,0)]_B=(1,1)^\mathsf{T}$.

例2（投影分量）：$v=(2,1)$，$u=(1,0)$（单位向量），则$v$沿$u$的标量分量为$v\cdot u=2$，向量分量为$2u=(2,0)$。  
Example 2 (projection): with $v=(2,1)$ and $u=(1,0)$ (a unit vector), the scalar component is $v\cdot u=2$ and the vector component is $2u=(2,0)$.

## 关联笔记 / Related Notes
- 向量、内积、投影：[[Math_Linear-Algebra/vector_and_euclidean_space]]。  
  Vectors, inner products, projection: [[Math_Linear-Algebra/vector_and_euclidean_space]].
- 换基与坐标变换：[[Math_Linear-Algebra/change_of_basis_coordinates]]。  
  Change of basis and coordinate conversion: [[Math_Linear-Algebra/change_of_basis_coordinates]].
- 行变换求解$Ax=b$：[[Math_Linear-Algebra/gauss_jordan_elimination]]。  
  Row reduction for $Ax=b$: [[Math_Linear-Algebra/gauss_jordan_elimination]].

## 来源 / Source
- 来源 / Source: [[journal/2026-02-02]]  
  Source journal: [[journal/2026-02-02]]

[//begin]: # "Autogenerated link references for markdown compatibility"
[//end]: # "Autogenerated link references"
