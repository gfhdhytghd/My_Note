# 电势、电势能与带电粒子运动 / Electric Potential, Energy, and Charged-Particle Motion

默认静电场、真空或可近似为真空的空气；无限平面与无限长圆柱模型忽略边缘效应。$E=\|\vec E\|$ 为大小，$E_r$ 为向外取正的径向分量，$k=1/(4\pi\epsilon_0)$。 / Assume electrostatics in vacuum or approximately vacuum-like air; infinite-sheet and infinite-cylinder models neglect edge effects. $E=\|\vec E\|$ is the magnitude, $E_r$ is the signed outward radial component, and $k=1/(4\pi\epsilon_0)$.

## 电势与电场方向 / Potential and Field Direction

电势差定义为单位试探电荷电势能的变化。电场力做功为 $W_E=q\int_i^f\vec E\cdot d\vec\ell$，结合 $\Delta U=-W_E$，得到： / Potential difference is the change in potential energy per unit test charge. Electric work is $W_E=q\int_i^f\vec E\cdot d\vec\ell$; using $\Delta U=-W_E$ gives:

$$\boxed{V_f-V_i=-\int_i^f\vec E\cdot d\vec\ell},\qquad dV=-\vec E\cdot d\vec\ell,\qquad\boxed{\vec E=-\nabla V}.$$

沿非零电场移动，点积为正，电势下降；逆电场移动，电势上升；沿等势面移动，电场不做功。电场垂直于等势面，这些结论与试探电荷的正负无关。 / Moving along a nonzero field gives a positive dot product and decreasing potential; moving against it increases potential. Motion along an equipotential involves no electric work. The field is perpendicular to equipotentials, independently of the sign of a test charge.

## 电势能与电荷正负 / Potential Energy and Charge Sign

电荷 $q$ 在外部电势 $V$ 中的电势能为 $U=qV$（需选定参考零点），其变化为： / A charge $q$ in an external potential $V$ has potential energy $U=qV$ for a chosen reference, with change:

$$\boxed{\Delta U=q\Delta V},\qquad\boxed{W_E=-q\Delta V}.$$

| 电荷 / Charge | 电势升高 $\Delta V>0$ / Potential rises | 电势降低 $\Delta V<0$ / Potential falls |
| --- | --- | --- |
| 正电荷，如质子 / Positive, e.g. proton | $\Delta U>0$ | $\Delta U<0$ |
| 负电荷，如电子 / Negative, e.g. electron | $\Delta U<0$ | $\Delta U>0$ |

因此在相同电势变化下，质子与电子的电势能变化符号相反。只受电场力、从静止释放时，正电荷起初沿电场加速，负电荷起初逆电场加速，两者的电势能都减小。 / Protons and electrons have opposite potential-energy changes for the same potential change. Released from rest under electric force alone, positive charges initially accelerate along the field and negative charges against it; both lose potential energy.

## 平行板电势差与击穿条件 / Plate Voltage and Breakdown

均匀电场中，沿电场方向取坐标 $x$，积分直接得到 $V(x)=V(0)-Ex$。相距 $d$ 的两块等势平行板满足： / In a uniform field, choose $x$ along the field. Integration gives $V(x)=V(0)-Ex$. Two equipotential parallel plates separated by $d$ satisfy:

$$\Delta V=-Ed\quad\text{(along the field)},\qquad\boxed{E=\frac{|\Delta V|}{d}}.$$

若固定电压并要求不超过给定击穿场强，条件为 $|\Delta V|/d\leq E_{\mathrm{breakdown}}$，所以临界间距是最小允许间距，而不是最大间距；若固定间距，则可求最大电压： / At fixed voltage, requiring the field not to exceed a specified breakdown threshold gives $|\Delta V|/d\leq E_{\mathrm{breakdown}}$. The threshold separation is a minimum, not a maximum; at fixed spacing, it instead gives a maximum voltage:

$$\boxed{d_{\min}=\frac{|\Delta V|}{E_{\mathrm{breakdown}}}},\qquad\boxed{|\Delta V|_{\max}=E_{\mathrm{breakdown}}d}.$$

这是把击穿场强视为给定常量的理想模型，实际使用通常需低于临界场强。计算时统一使用 SI 单位：$1\,\mathrm{mm}=10^{-3}\,\mathrm m$，$1\,\mathrm{V/m}=1\,\mathrm{N/C}$。 / This idealized model treats the breakdown threshold as a given constant; practical operation generally stays below it. Use consistent SI units: $1\,\mathrm{mm}=10^{-3}\,\mathrm m$ and $1\,\mathrm{V/m}=1\,\mathrm{N/C}$.

## 悬挂带电小球的受力平衡 / Equilibrium of a Suspended Charged Ball

设电场水平，小球质量为 $m$、电荷为 $q$，绳与竖直方向的偏角大小为 $\theta$。平衡时竖直方向张力抵消重力，水平方向张力抵消电场力： / Let the field be horizontal, the ball have mass $m$ and charge $q$, and the string make an angle of magnitude $\theta$ with the vertical. At equilibrium, tension balances gravity vertically and electric force horizontally:

$$T\cos\theta=mg,\qquad T\sin\theta=|q|E.$$

$$\tan\theta=\frac{|q|E}{mg}\quad\Longrightarrow\quad\boxed{E=\frac{mg\tan\theta}{|q|}}.$$

对正电荷可直接将分母写成 $q$；负电荷偏向电场反方向。若场来自单个均匀大薄电荷面，$|\sigma|=2\epsilon_0E$；若来自理想异号平行板的板间区域，$|\sigma|=\epsilon_0E$。面电荷的正负要根据电场方向与小球所在侧另行判断。 / For a positive charge, the denominator is simply $q$; a negative charge deflects opposite the field. A single uniform large thin sheet gives $|\sigma|=2\epsilon_0E$, whereas the gap of ideal oppositely charged plates gives $|\sigma|=\epsilon_0E$. Determine the sign of the surface charge separately from the field direction and the ball's location.

## 带电粒子经过电势差加速 / Charged-Particle Acceleration Through a Voltage

若只有静电力做功，机械能守恒 $K_i+U_i=K_f+U_f$；在非相对论速度下： / If only the electrostatic force does work, $K_i+U_i=K_f+U_f$. At nonrelativistic speeds:

$$\boxed{\Delta K=-q\Delta V},\qquad\frac12m(v_f^2-v_i^2)=-q\Delta V.$$

从静止出发要能加速到终点，必须满足 $q\Delta V<0$。在此前提下，$-q\Delta V=|q\Delta V|$，所以： / Acceleration from rest to the final point requires $q\Delta V<0$. Under this condition, $-q\Delta V=|q\Delta V|$, giving:

$$\boxed{\frac12mv^2=|q\Delta V|},\qquad\boxed{v=\sqrt{\frac{2|q\Delta V|}{m}}}.$$

不要先取绝对值而丢掉运动方向条件：质子从高电势向低电势加速，电子从低电势向高电势加速。若 $q\Delta V>0$，电场使粒子减速，粒子需要足够初动能才能到达终点。 / Do not use absolute values to hide the direction condition: protons accelerate toward lower potential, electrons toward higher potential. If $q\Delta V>0$, the field slows the particle, which needs sufficient initial kinetic energy to reach the endpoint.

两个粒子从静止经过相同大小的加速电压，且电荷大小相等，则动能相同、速度满足 $v\propto1/\sqrt m$。电子与质子的非相对论速度比为： / Two particles starting from rest through equal accelerating voltage magnitudes, with equal charge magnitudes, gain equal kinetic energies and have $v\propto1/\sqrt m$. The nonrelativistic electron-to-proton speed ratio is:

$$\boxed{\frac{v_e}{v_p}=\sqrt{\frac{m_p}{m_e}}\approx\sqrt{1836}\approx42.8}.$$

两者需沿各自的加速方向运动，并非以相同方向经过同一有符号电势差。上述速度公式要求所得 $v\ll c$；能量变化关系 $\Delta K=-q\Delta V$ 本身仍成立。 / Each particle must move in its own accelerating direction, not traverse the same signed potential difference in the same direction. These speed formulas require $v\ll c$; the energy relation $\Delta K=-q\Delta V$ itself remains valid.

## 速判规则与解题顺序 / Quick Rules and Problem-Solving Order

| 情形 / Situation | 速判公式 / Quick rule |
| --- | --- |
| 导体材料静电平衡 / Conducting material in equilibrium | $E=0$，导体等势 / Equipotential conductor |
| 单个均匀无限薄电荷面 / Single uniform infinite sheet | $E=|\sigma|/(2\epsilon_0)$ |
| 光滑导体表面紧邻外侧 / Immediately outside a smooth conductor | $E_\perp=\sigma/\epsilon_0$，保留方向符号 / Signed normal component |
| 等量异号理想平行板之间 / Between equal opposite ideal plates | $E=|\sigma|/\epsilon_0=|\Delta V|/d$ |
| 无限线电荷 / Infinite line | $E\propto1/r$ |
| 球对称电荷分布外部 / Exterior spherical field | $E\propto1/r^2$，总电荷非零时 / For nonzero net charge |
| 均匀绝缘球内部 / Uniform insulating sphere interior | $E\propto r$ |
| 沿电场方向 / Along the field | 电势降低 / Potential decreases |
| 电势能变化 / Potential-energy change | $\Delta U=q\Delta V$ |
| 静电力做功 / Electric work | $\Delta K=-q\Delta V$ |
| 从静止非相对论加速 / Nonrelativistic acceleration from rest | $\frac12mv^2=|q\Delta V|$，要求 $q\Delta V<0$ / Requires $q\Delta V<0$ |

1. **先判断几何对称性与材料：**球、柱还是平面？导体还是绝缘体？ / **Identify symmetry and material:** sphere, cylinder, or plane; conductor or insulator?
2. **选高斯面并分区：**空腔、金属、间隙和外部要分开处理。 / **Choose a Gaussian surface and split regions:** distinguish cavity, metal, gaps, and exterior.
3. **计算净包围电荷：**体电荷用体积，面电荷用面积，线电荷用长度；导体内 $E=0$ 可反推感应电荷。 / **Find net enclosed charge:** use volume, area, or length as appropriate; zero field in metal can determine induced charge.
4. **先求有符号分量，再按题意取大小：**向内的径向场为负，电场大小不能为负。 / **Find signed components before magnitudes:** inward radial fields are negative, but magnitudes are not.
5. **遇到电势或速度，转用积分与能量：**$\Delta V=-\int\vec E\cdot d\vec\ell$，$\Delta K=-q\Delta V$；最后检查单位与适用条件。 / **For potential or speed, use integration and energy:** $\Delta V=-\int\vec E\cdot d\vec\ell$, $\Delta K=-q\Delta V$; then check units and assumptions.

## 相关笔记 / Related Notes

- [[Physics/2.Electrostatics/gauss_law_and_conductors]] — 对称电场与导体 / Symmetric fields and conductors
- [[Math_Calculus/6.Multivariable_Calculus/traces_and_contour_maps]] — 等高线与等势线 / Contours and equipotentials

## 来源 / Sources

- [[Daily Notes/2026-09-16]] — 课堂记录 / Class notes

[//begin]: # "Autogenerated link references for markdown compatibility"
[//end]: # "Autogenerated link references"
