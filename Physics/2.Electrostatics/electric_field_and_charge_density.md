# 电场与连续电荷分布 / Electric Fields and Continuous Charge Distributions

默认静电场、真空或可近似为真空的空气；无限平面与无限长圆柱模型忽略边缘效应。$E=\|\vec E\|$ 为大小，$E_r$ 为向外取正的径向分量，$k=1/(4\pi\epsilon_0)$。 / Assume electrostatics in vacuum or approximately vacuum-like air; infinite-sheet and infinite-cylinder models neglect edge effects. $E=\|\vec E\|$ is the magnitude, $E_r$ is the signed outward radial component, and $k=1/(4\pi\epsilon_0)$.

## 电场的定义 / Definition of the Electric Field

电场定义为单位试探电荷所受的力：$\vec{E}(x,y,z)=\frac{\vec{F}_{\text{on }q}(x,y,z)}{q}$，因此电荷在电场中受到的力为 $\vec{F}=q\vec{E}$。电场由源电荷决定，与用来测量它的试探电荷无关。 / The electric field is the force per unit test charge: $\vec{E}(x,y,z)=\frac{\vec{F}_{\text{on }q}(x,y,z)}{q}$, so a charge in the field experiences $\vec{F}=q\vec{E}$. The field is determined by source charges and is independent of the test charge used to measure it.

- 电场强度是电场的大小 $|\vec{E}|$。 / Electric field strength is the magnitude $|\vec{E}|$.
- 单位为牛顿每库仑（$\mathrm{N/C}$），等价于伏特每米（$\mathrm{V/m}$）。 / Its unit is newtons per coulomb ($\mathrm{N/C}$), equivalent to volts per meter ($\mathrm{V/m}$).
- 正试探电荷受力方向与 $\vec{E}$ 相同，负电荷受力方向与 $\vec{E}$ 相反。 / A positive test charge feels a force along $\vec{E}$, while a negative charge feels a force opposite to $\vec{E}$.

![电场定义课堂课件 / Lecture slide on the electric field definition](../../attachments/2026-09-01_electric_field_definition.jpeg)

## 电荷密度 / Charge Density

宏观物体即使只带有很小的总电荷，也包含大量微观带电粒子，因此通常把电荷看作连续分布。电荷密度描述单位长度、单位面积或单位体积内分布了多少电荷。 / Even a macroscopically small total charge consists of many microscopic charged particles, so charge is often modeled as a continuous distribution. Charge density describes the amount of charge distributed per unit length, area, or volume.

- **线电荷密度 / Linear charge density：**均匀分布时 $\lambda=\frac{Q}{L}$，单位为 $\mathrm{C/m}$；一般情况下 $dq=\lambda\,dl$。常见于细导线。 / For a uniform distribution, $\lambda=\frac{Q}{L}$ with units $\mathrm{C/m}$; in general, $dq=\lambda\,dl$. This is commonly used for thin wires.
- **面电荷密度 / Surface charge density：**均匀分布时 $\sigma=\frac{Q}{A}$，单位为 $\mathrm{C/m^2}$；一般情况下 $dq=\sigma\,dA$。常见于薄板或球壳。 / For a uniform distribution, $\sigma=\frac{Q}{A}$ with units $\mathrm{C/m^2}$; in general, $dq=\sigma\,dA$. This is commonly used for thin plates or spherical shells.
- **体电荷密度 / Volume charge density：**均匀分布时 $\rho=\frac{Q}{V}$，单位为 $\mathrm{C/m^3}$；一般情况下 $dq=\rho\,dV$。常见于带电绝缘体。 / For a uniform distribution, $\rho=\frac{Q}{V}$ with units $\mathrm{C/m^3}$; in general, $dq=\rho\,dV$. This is commonly used for charged insulators.

若电荷密度随位置变化，总电荷需要通过积分求得：$Q=\int\lambda\,dl$、$Q=\iint\sigma\,dA$ 或 $Q=\iiint\rho\,dV$。 / If the charge density varies with position, the total charge is found by integration: $Q=\int\lambda\,dl$, $Q=\iint\sigma\,dA$, or $Q=\iiint\rho\,dV$.

![线、面与体电荷密度课堂课件 / Lecture slide on linear, surface, and volume charge densities](../../attachments/2026-09-03_charge_density.jpeg)

## 线电荷与无限带电平面 / Line Charge and an Infinite Charged Plane

求线电荷产生的电场时，先画图并定义坐标、变量和距离，再利用对称性。对于关于观察点对称的线电荷微元，水平方向（如 $x$ 分量）的电场相互抵消，垂直方向分量相加，因此可将积分化为半段的两倍：$\vec E(P)=k\int_0^{L/2}\frac{2\lambda\,dx}{r^2}\,\cos\theta\,\hat{k}$。 / To find the field of a line charge, draw the geometry and define the axes, variables, and distance first, then exploit symmetry. For charge elements symmetric about the observation point, horizontal components (such as $x$ components) cancel while vertical components add, reducing the integral to twice one half: $\vec E(P)=k\int_0^{L/2}\frac{2\lambda\,dx}{r^2}\,\cos\theta\,\hat{k}$.

无限均匀带电平面的电场为
$\vec E=\frac{\sigma}{2\epsilon_0}\hat n$，其中 $\hat n$ 是垂直于平面的单位法向量；正电荷的电场指向远离平面的一侧。 / The field of an infinite uniformly charged plane is
$\vec E=\frac{\sigma}{2\epsilon_0}\hat n$, where $\hat n$ is a unit normal vector to the plane; for positive charge, the field points away from the plane.

例题：$20\times20\,\mathrm{cm}$ 金属电极带电 $Q=+80\,\mathrm{nC}$。由于测量点距电极 $2.0\,\mathrm{mm}$，远小于电极边长 $0.20\,\mathrm{m}$，可近似为无限平面。面电荷密度为
$\sigma=Q/A=80\times10^{-9}/(0.20)^2=2.0\times10^{-6}\,\mathrm{C/m^2}$，故
$E=\sigma/(2\epsilon_0)\approx1.1\times10^5\,\mathrm{N/C}$，方向沿平面法线向上。 / Example: A $20\times20\,\mathrm{cm}$ metal electrode carries $Q=+80\,\mathrm{nC}$. Because the observation point is $2.0\,\mathrm{mm}$ away—much less than the $0.20\,\mathrm{m}$ side length—we approximate it as an infinite plane. The surface density is $\sigma=Q/A=2.0\times10^{-6}\,\mathrm{C/m^2}$, giving $E=\sigma/(2\epsilon_0)\approx1.1\times10^5\,\mathrm{N/C}$, directed upward along the plane's normal.

例题模型说明：上述金属电极结果采用孤立、两侧环境对称的薄板近似，$Q/A$ 是两面的合计投影面密度，每一面的实际密度为 $Q/(2A)$。若题目给的是单个导体表面的密度，应使用 $E=|\sigma_{\mathrm{face}}|/\epsilon_0$；观察点还应远离板的边缘。 / Model clarification: the electrode example assumes an isolated thin plate with symmetric surroundings. Here $Q/A$ combines both faces per projected area, while each face has density $Q/(2A)$. For the density on a single conducting face, use $E=|\sigma_{\mathrm{face}}|/\epsilon_0$; the observation point must also be far from the edges.

![线电荷电场的对称性与积分 / Symmetry and integration for the field of a line charge](../../attachments/2026-09-03_line_charge_field.jpeg)

![无限带电平面电场例题 / Infinite charged-plane field example](../../attachments/2026-09-03_infinite_plane_example.jpeg)

## 面电荷密度 / Surface Charge Density

一般定义是 $\sigma=dQ/dA$，因此 $Q=\int\sigma\,dA$；均匀分布时才可写成 $\sigma=Q/A$。 / In general, $\sigma=dQ/dA$, so $Q=\int\sigma\,dA$; a uniform distribution allows $\sigma=Q/A$.

$$\boxed{\sigma_{\mathrm{rectangle}}=\frac{Q}{LW}},\qquad\boxed{\sigma_{\mathrm{sphere}}=\frac{Q}{4\pi R^2}}.$$

单位为 $\mathrm{C/m^2}$，符号与该表面的电荷一致。导体薄板若两面都带电，必须明确 $Q$ 是某一面的电荷还是整块板的总电荷；不能自动把总电荷除以单面面积。 / Units are $\mathrm{C/m^2}$, and the sign follows the charge on that surface. If both faces of a conducting plate carry charge, distinguish the charge on one face from the total plate charge before dividing by area.

## 开学主题记录 / Opening Class Topics

[[Daily Notes/2026-08-25]] 提到了电磁学基础、正负电荷与导体，未记录详细推导；电场定义与连续分布的详细来源见上。 / [[Daily Notes/2026-08-25]] mentions introductory electromagnetism, positive and negative charges, and conductors without detailed derivations; detailed sources for fields and continuous distributions are listed above.

## 相关笔记 / Related Notes

- [[Physics/2.Electrostatics/gauss_law_and_conductors]] — 高斯定律与导体 / Gauss’s law and conductors

## 来源 / Sources

- [[Daily Notes/2026-09-01]] — 课堂记录 / Class notes
- [[Daily Notes/2026-09-03]] — 课堂记录 / Class notes
- [[Daily Notes/2026-09-16]] — 课堂记录 / Class notes

[//begin]: # "Autogenerated link references for markdown compatibility"
[//end]: # "Autogenerated link references"
