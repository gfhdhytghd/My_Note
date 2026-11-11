# 极坐标、柱坐标与球坐标积分 / Integrals in Polar, Cylindrical, and Spherical Coordinates

> 材料时间 / Material dates：2026-10-29 至 2026-11-02 的学习对话整理，不是课堂原始记录。入口见 [[Courses/2026_fall/recent_learning_review]]。  
> Organized from study conversations dated 2026-10-29 to 2026-11-02; this is not an original class transcript.

## 问题与直觉 / Problem and Intuition

圆盘、圆柱、球这类区域在直角坐标下要写 $\pm\sqrt{1-x^2}$ 这样的上下限，积分很难做。换成“半径 + 角度”描述后，区域常常变成简单的矩形范围。

Disks, cylinders, and balls need bounds such as $\pm\sqrt{1-x^2}$ in rectangular coordinates. Describing them by radius and angle often turns the region into a simple box of bounds.

但新坐标下的小块不再是 $dx\times dy$ 的正方形。极坐标的小块是一段弯曲的“扇环”：径向边长 $dr$，弧向边长 $r\,d\theta$，所以面积是 $r\,dr\,d\theta$。多出来的 $r$ 就是 Jacobian；离原点越远，同样的 $d\theta$ 扫过的弧越长。

The small pieces are no longer $dx\times dy$ squares. A polar piece is a curved sector of an annulus with radial side $dr$ and arc side $r\,d\theta$, so its area is $r\,dr\,d\theta$. The extra $r$ is the Jacobian: the same $d\theta$ sweeps a longer arc farther from the origin.

## 三套坐标与体积元 / The Three Systems and Their Elements

| 坐标 / System | 变换 / Transformation | 面积或体积元 / Element | 常用范围 / Typical ranges |
| --- | --- | --- | --- |
| 极坐标 / Polar | $x=r\cos\theta,\ y=r\sin\theta$ | $dA=r\,dr\,d\theta$ | $r\ge0$，$0\le\theta\le2\pi$ |
| 柱坐标 / Cylindrical | 极坐标 + $z=z$ / polar plus $z=z$ | $dV=r\,dz\,dr\,d\theta$ | 同上，$z$ 由上下曲面给出 / $z$ from bounding surfaces |
| 球坐标 / Spherical | $x=\rho\sin\phi\cos\theta,\ y=\rho\sin\phi\sin\theta,\ z=\rho\cos\phi$ | $dV=\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$ | $\rho\ge0$，$0\le\phi\le\pi$，$0\le\theta\le2\pi$ |

- 这里 $\phi$ 从正 $z$ 轴量起；有的教材把角度符号对调，使用前先确认约定。  
  Here $\phi$ is measured from the positive $z$-axis; some books swap the angle symbols, so check the convention first.
- 球坐标的小块三边长为 $d\rho$、$\rho\,d\phi$、$\rho\sin\phi\,d\theta$，乘起来得到 $\rho^2\sin\phi$。  
  A spherical piece has edges $d\rho$, $\rho\,d\phi$, and $\rho\sin\phi\,d\theta$, whose product gives $\rho^2\sin\phi$.
- 常用恒等式：$x^2+y^2=r^2$，$x^2+y^2+z^2=\rho^2$。  
  Useful identities: $x^2+y^2=r^2$ and $x^2+y^2+z^2=\rho^2$.

这些都是一般换元公式的特例，推导见 [[Math_Calculus/6.Multivariable_Calculus/change_of_variables_jacobian]]。

All three are special cases of the general change-of-variables formula; see the linked Jacobian note.

## 设限步骤 / Setting Up the Bounds

1. 先画或想象区域，找出对称轴。  
   Sketch the region and find its symmetry axis.
2. 把边界方程代入新坐标，解出半径变量的上下限。  
   Substitute the boundary equations and solve for the radial bounds.
3. 由“半径上限必须非负”或图形范围定出角度上下限。  
   Use nonnegativity of the radial bound or the picture to fix the angular bounds.
4. 被积函数换元后，再乘上 $r$ 或 $\rho^2\sin\phi$。  
   Convert the integrand, then multiply by $r$ or $\rho^2\sin\phi$.

**柱坐标设限示例**：$\int_{-1}^{1}\int_{-\sqrt{1-x^2}}^{\sqrt{1-x^2}}\int_0^4 f\,dz\,dy\,dx$ 的 $y$ 范围给出单位圆盘，$z$ 从 $0$ 到 $4$，因此区域是半径 $1$、高 $4$ 的圆柱：

**Cylindrical setup:** The $y$ bounds describe the unit disk and $z$ runs from $0$ to $4$, so the region is a cylinder of radius $1$ and height $4$:

$$\int_0^{2\pi}\int_0^1\int_0^4 f(r\cos\theta,r\sin\theta,z)\,r\,dz\,dr\,d\theta.$$

**极坐标示例**：双纽线 $r^2=\sin2\theta$ 在第一象限的一瓣上求 $\iint_D x\sqrt{x^2+y^2}\,dA$。只有 $\sin2\theta\ge0$ 时曲线才存在，第一象限对应 $0\le\theta\le\frac\pi2$，$0\le r\le\sqrt{\sin2\theta}$。被积式变为 $(r\cos\theta)(r)(r)=r^3\cos\theta$：

**Polar example:** On the first-quadrant loop of $r^2=\sin2\theta$, evaluate $\iint_D x\sqrt{x^2+y^2}\,dA$. The curve exists only where $\sin2\theta\ge0$; the first-quadrant loop uses $0\le\theta\le\frac\pi2$ and $0\le r\le\sqrt{\sin2\theta}$. The integrand becomes $r^3\cos\theta$:

$$\int_0^{\pi/2}\int_0^{\sqrt{\sin2\theta}}r^3\cos\theta\,dr\,d\theta=\frac14\int_0^{\pi/2}\sin^22\theta\cos\theta\,d\theta=\int_0^1(u^2-u^4)\,du=\frac2{15},$$

其中用了 $\sin^22\theta=4\sin^2\theta\cos^2\theta$ 和 $u=\sin\theta$。

using $\sin^22\theta=4\sin^2\theta\cos^2\theta$ and $u=\sin\theta$.

## 完整例题：球心不在原点的球 / Worked Example: A Ball Not Centered at the Origin

**题目**：$W=\{x^2+y^2+z^2\le2z\}$，求 $\iiint_W\sqrt{x^2+y^2+z^2}\,dV$。

**Problem:** For $W=\{x^2+y^2+z^2\le2z\}$, evaluate $\iiint_W\sqrt{x^2+y^2+z^2}\,dV$.

**识别区域**：配方得 $x^2+y^2+(z-1)^2\le1$，这是球心 $(0,0,1)$、半径 $1$ 的球，最低点恰好在原点。

**Identify the region:** Completing the square gives $x^2+y^2+(z-1)^2\le1$, a ball of radius $1$ centered at $(0,0,1)$ whose lowest point is the origin.

**设限**：代入 $\rho^2\le2\rho\cos\phi$，因 $\rho\ge0$ 得 $0\le\rho\le2\cos\phi$。上限非负要求 $\cos\phi\ge0$，即 $0\le\phi\le\frac\pi2$；绕 $z$ 轴对称，$0\le\theta\le2\pi$。

**Bounds:** Substituting gives $\rho^2\le2\rho\cos\phi$, so $0\le\rho\le2\cos\phi$. A nonnegative upper bound needs $\cos\phi\ge0$, so $0\le\phi\le\frac\pi2$; symmetry about the $z$-axis gives $0\le\theta\le2\pi$.

**计算 / Evaluate**：被积函数是 $\rho$，乘以 $\rho^2\sin\phi$ 得 $\rho^3\sin\phi$。

The integrand is $\rho$; multiplying by $\rho^2\sin\phi$ gives $\rho^3\sin\phi$.

$$I=\int_0^{2\pi}\int_0^{\pi/2}\int_0^{2\cos\phi}\rho^3\sin\phi\,d\rho\,d\phi\,d\theta=\int_0^{2\pi}\int_0^{\pi/2}4\cos^4\phi\sin\phi\,d\phi\,d\theta=2\pi\cdot\frac45=\frac{8\pi}5.$$

中间一步令 $u=\cos\phi$，$\int_0^{\pi/2}4\cos^4\phi\sin\phi\,d\phi=4\int_0^1u^4\,du=\frac45$。

The middle step uses $u=\cos\phi$, giving $4\int_0^1u^4\,du=\frac45$.

## 易错点 / Common Mistakes

- 漏乘 $r$ 或 $\rho^2\sin\phi$：这是最常见的错误，结果会差一个“面积缩放”。  
  Forgetting $r$ or $\rho^2\sin\phi$, which loses the area or volume scale factor.
- 球心不在原点时仍写 $0\le\rho\le1$：$\rho$ 是到原点的距离，不是到球心的距离。  
  Writing $0\le\rho\le1$ for an off-center ball: $\rho$ measures distance to the origin, not to the center.
- 双纽线、玫瑰线这类曲线只在部分角度存在，角度范围要由 $r^2\ge0$ 或 $r\ge0$ 决定。  
  Curves such as lemniscates and roses exist only for some angles; use $r^2\ge0$ or $r\ge0$ to set the angular range.

## 关联笔记 / Related Notes

- [[Math_Calculus/6.Multivariable_Calculus/multiple_integrals_center_of_mass]] — 累次积分与质心 / Iterated integrals and center of mass
- [[Math_Calculus/6.Multivariable_Calculus/change_of_variables_jacobian]] — 为什么会多出 $r$ 与 $\rho^2\sin\phi$ / Why $r$ and $\rho^2\sin\phi$ appear
- [[Math_Calculus/6.Multivariable_Calculus/quadric_surfaces]] — 识别球、圆柱、锥面 / Recognizing spheres, cylinders, and cones

## 来源 / Sources

- ChatGPT 对话 / ChatGPT conversation：[柱坐标变换 integrals](https://chatgpt.com/c/6ae4cc4d-b9a0-8333-a94b-d742070f16e9) — 圆柱设限与偏心球 $\frac{8\pi}5$ / Cylinder setup and the off-center ball.
- ChatGPT 对话 / ChatGPT conversation：[Calculate Paraboloid Volume](https://chatgpt.com/c/6ae3ed1c-993c-8325-811c-ddd552847d15) — 双纽线一瓣的 $\frac2{15}$ / The lemniscate-loop integral.
- 双纽线题的图只在截图中；本页只使用对话正文给出的“第一象限一瓣”。 / The lemniscate figure was only in a screenshot; this page uses only the stated first-quadrant loop.

[//begin]: # "Autogenerated link references for markdown compatibility"
[//end]: # "Autogenerated link references"
