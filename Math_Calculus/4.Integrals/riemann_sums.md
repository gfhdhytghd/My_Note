# 黎曼和与求和记号 / Riemann Sums and Summation Notation

## 1. 求和记号 / Summation Notation

求和符号$\sum$用于表示“连续加总”，常见形式为$\sum_{i=1}^n a_i$，或带权形式$\sum_{i=1}^n w_i a_i$。  
The summation symbol $\sum$ denotes repeated addition, e.g., $\sum_{i=1}^n a_i$ or weighted sums $\sum_{i=1}^n w_i a_i$.

读法与要点：下标给出索引范围（从$i=1$到$n$），上标给出终点；把每个$i$代入表达式后再相加。  
Key idea: the subscript sets the index range (from $i=1$ to $n$); substitute Huck Institutes of the Life Scienceseach $i$ into the expression and then add.

## 2. 区间划分 / Partitioning an Interval

将区间$[a,b]$等分为$n$份，步长为$\Delta x=(b-a)/n$。  
Split the interval $[a,b]$ into $n$ equal parts with width $\Delta x=(b-a)/n$.

## 3. 左/右/中点近似 / Left, Right, and Midpoint Approximations

用函数值乘以小区间宽度并求和，可近似曲线下的面积。  
Summing function values times the subinterval width approximates the area under a curve.

- 左端点近似：$L_n=\sum_{i=0}^{n-1} f(a+i\Delta x)\Delta x$。  
  Left endpoint: $L_n=\sum_{i=0}^{n-1} f(a+i\Delta x)\Delta x$.
- 右端点近似：$R_n=\sum_{i=1}^{n} f(a+i\Delta x)\Delta x$。  
  Right endpoint: $R_n=\sum_{i=1}^{n} f(a+i\Delta x)\Delta x$.
- 中点近似：$M_n=\sum_{i=0}^{n-1} f(a+(i+0.5)\Delta x)\Delta x$。  
  Midpoint: $M_n=\sum_{i=0}^{n-1} f(a+(i+0.5)\Delta x)\Delta x$.

当$n$增大、$\Delta x\to0$时，这类和与定积分$\int_a^b f(x)\,dx$建立联系。  
As $n$ increases and $\Delta x\to0$, these sums connect to the definite integral $\int_a^b f(x)\,dx$.

**来源 / Source**  
[[journal/2025-12-01]]


