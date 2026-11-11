# 梁的剪力与弯矩：为什么要分段 / Beam Shear and Bending Moment: Why We Use Segments

> 材料时间 / Material dates：2026-10-29 至 2026-11-02 的学习对话整理，不是课堂原始记录。入口见 [[Courses/2026_fall/recent_learning_review]]。  
> Organized from study conversations dated 2026-10-29 to 2026-11-02; this is not an original class transcript.

## 问题与直觉 / Problem and Intuition

梁内部哪一处最危险？外力只作用在少数位置，但梁内每个截面都在传力。做法是：在距左端 $x$ 处假想地把梁切开，取一侧画自由体图。切口上必须有一个竖向内力 $V$（剪力）和一个内力偶 $M$（弯矩），这一段才能平衡。

Where is a beam most at risk? External loads act at a few places, but every section transmits force. Imagine cutting the beam at distance $x$ and drawing one side's free-body diagram; the cut must carry a vertical internal force $V$ (shear) and an internal couple $M$ (bending moment) for that piece to balance.

## 为什么要分段 / Why Segments Are Needed

切口左侧包含哪些载荷，取决于 $x$ 在哪里。只要 $x$ 越过一个集中力、集中力偶、支座，或分布载荷的起点和终点，自由体图里的载荷就变了，$V(x)$、$M(x)$ 的表达式也随之改变。所以每两个“载荷变化点”之间写一套方程。

Which loads lie left of the cut depends on $x$. Whenever $x$ passes a concentrated force, a concentrated couple, a support, or the start or end of a distributed load, the free-body diagram changes, and so do $V(x)$ and $M(x)$. Write one set of equations between each pair of load-change points.

## 符号约定与关系 / Sign Convention and Relations

常用约定：对左段的右切面，$V$ 向下为正，$M$ 逆时针为正（梁下侧受拉，“下凸”为正）。不同教材约定可能不同，同一题内必须保持一致。

A common convention: on the right face of the left piece, $V$ is positive downward and $M$ positive counterclockwise, which corresponds to sagging. Textbooks may differ; stay consistent within a problem.

在这一约定下，取分布载荷 $w(x)$ 向下为正：

With this convention and downward distributed load $w(x)$:

$$\frac{dV}{dx}=-w(x),\qquad\frac{dM}{dx}=V(x).$$

- 集中力处 $V$ 跳变，跳变量等于该力。  
  $V$ jumps at a concentrated force by the force's magnitude.
- 集中力偶处 $M$ 跳变。  
  $M$ jumps at a concentrated couple.
- $V=0$ 处常是一段内 $M$ 的极值候选点。  
  Points where $V=0$ are candidates for extreme $M$ within a segment.

**均布载荷的合力**：强度 $w$、作用长度 $x$ 时，合力为 $wx$，作用在这段载荷的中点，距切口 $x/2$。非均布载荷用“载荷图面积 = 合力、面积形心 = 作用点”。

**Resultant of a uniform load:** intensity $w$ over length $x$ has resultant $wx$ at its midpoint, $x/2$ from the cut. For non-uniform loads, the resultant is the area of the load diagram, acting at its centroid.

## 完整例题：第一段 $0<x<6$ / Worked Example: Segment $0<x<6$

对话中的梁：A 端支座反力 $A_y=30\ \text{kip}$ 向上，支座反力矩 $216\ \text{kip}\cdot\text{ft}$ 逆时针，从 A 起作用 $w=2\ \text{kip/ft}$ 的均布载荷，$x=6\ \text{ft}$ 处有 $10\ \text{kip}$ 集中力。梁的其余几何与载荷在截图中，未包含在材料里；下面只写第一段。

The conversation's beam has an upward reaction $A_y=30\ \text{kip}$ and a counterclockwise reaction moment of $216\ \text{kip}\cdot\text{ft}$ at A, a uniform load $w=2\ \text{kip/ft}$ starting at A, and a $10\ \text{kip}$ point load at $x=6\ \text{ft}$. The rest of the geometry was in a screenshot that was not included, so only the first segment is written here.

**为什么在 $x=6$ 分段**：越过 $x=6$ 后，切口左侧多了 $10\ \text{kip}$ 集中力，方程必然改变。

**Why split at $x=6$:** past $x=6$, the free-body diagram gains the $10\ \text{kip}$ load, so the equations must change.

**剪力**：左段竖向受力为 $30$ 向上、$2x$ 向下、$V$ 向下：

**Shear:** the left piece has $30$ up, $2x$ down, and $V$ down:

$$\sum F_y=30-2x-V=0\ \Rightarrow\ V(x)=30-2x\ \ \text{kip}.$$

**弯矩**：对切口取矩，逆时针为正。反力矩 $+216$；$30\ \text{kip}$ 在切口左侧 $x$ 处向上，产生顺时针矩 $-30x$；均布载荷合力 $2x$ 在 $x/2$ 处向下，产生逆时针矩 $+2x\cdot\frac x2=+x^2$；内弯矩 $+M$：

**Moment:** sum moments about the cut, counterclockwise positive:

$$216-30x+x^2+M=0\ \Rightarrow\ M(x)=-216+30x-x^2\ \ \text{kip}\cdot\text{ft}.$$

**检验**：$\frac{dM}{dx}=30-2x=V$，$\frac{dV}{dx}=-2=-w$，与微分关系一致。代值：$M(0)=-216$（与支座反力矩大小一致），$M(4)=-112\ \text{kip}\cdot\text{ft}$，$V(6^-)=18\ \text{kip}$，$M(6^-)=-72\ \text{kip}\cdot\text{ft}$。负号表示实际弯矩方向与假设正方向相反（上侧受拉）。

**Check:** both differential relations hold. Values: $M(0)=-216$, $M(4)=-112\ \text{kip}\cdot\text{ft}$, $V(6^-)=18\ \text{kip}$, and $M(6^-)=-72\ \text{kip}\cdot\text{ft}$. A negative value means the actual moment opposes the assumed positive sense (hogging).

第二段需要 $10\ \text{kip}$ 力的方向和梁的其余载荷，材料中没有，因此不写。

The second segment needs the direction of the $10\ \text{kip}$ load and the remaining loads, which are not in the material, so it is omitted.

## 易错点 / Common Mistakes

- 均布载荷的力臂写成 $x$：合力作用在载荷段中点，力臂是 $x/2$。  
  Using $x$ as the lever arm of a uniform load; the resultant acts at the midpoint, $x/2$ away.
- 忘记把支座反力矩写进取矩方程。  
  Leaving the support reaction moment out of the moment equation.
- 区间端点写成 $\le$ 并在集中力处取值：$V$ 在集中力处有跳变，要分别写 $V(6^-)$ 和 $V(6^+)$。  
  Evaluating $V$ exactly at a point load; $V$ jumps there, so use one-sided values.
- kip·ft 直接代入以 in 计的截面公式：先乘 12 换成 kip·in。  
  Using kip·ft with section properties in inches; multiply by 12 first.

## 关联笔记 / Related Notes

- [[Physics/3.Mechanics_of_Materials/README]] — 本章学习顺序 / Study order for this chapter
- [[Courses/2026_fall/emch_210/exam2_review]] — 自由体图、力矩与组合形心 / Free-body diagrams, moments, and composite centroids
- [[Physics/3.Mechanics_of_Materials/engineering_units_us_customary]] — kip·ft 与 kip·in / kip·ft and kip·in
- [[Math_Calculus/6.Multivariable_Calculus/multiple_integrals_center_of_mass]] — 分布载荷合力与形心的积分形式 / The integral view of resultants and centroids

## 来源 / Sources

- ChatGPT 对话 / ChatGPT conversation：[解释梁内力分段](https://chatgpt.com/c/6ae6b4a4-72a8-8330-b2d1-ee4f562985c9) — $0<x<6$ 段的 $V(x)$、$M(x)$ 推导 / Derivation of $V(x)$ and $M(x)$ on $0<x<6$.

[//begin]: # "Autogenerated link references for markdown compatibility"
[//end]: # "Autogenerated link references"
