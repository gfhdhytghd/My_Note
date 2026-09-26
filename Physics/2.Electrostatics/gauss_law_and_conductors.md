# 高斯定律、对称电场与导体 / Gauss’s Law, Symmetric Fields, and Conductors

## 物理量与符号定义 / Physical Quantities and Symbols

以下按“符号—定义—SI 单位”查阅；电荷和电荷密度保留正负号，下标 $i,f$ 表示初态、末态，$\Delta$ 表示末值减初值。 / Read each entry as symbol, definition, and SI unit; charges and charge densities retain their signs, subscripts $i,f$ mean initial and final, and $\Delta$ means final minus initial.

| 符号 / Symbol | 定义与含义 / Definition and meaning | SI 单位 / SI unit |
| --- | --- | --- |
| $q,Q$ | 电荷量：物体所带电荷的代数值，可正可负；具体所指由题目确定。 / Electric charge: the signed charge of an object; its role depends on context. | $\mathrm C$ |
| $\vec F$ | 电场力：电荷在外电场中受到的力，$\vec F=q\vec E$。 / Electric force on a charge in an external field, $\vec F=q\vec E$. | $\mathrm N$ |
| $\vec E,E$ | 电场为单位试探电荷所受的电场力，$\vec E=\vec F/q$（试探电荷不扰动原场）；$E=\|\vec E\|\geq0$ 是大小。 / Electric field is force per unit test charge that does not disturb the source field; $E$ is its nonnegative magnitude. | $\mathrm{N/C}=\mathrm{V/m}$ |
| $E_r,E_x,E_\perp$ | 电场沿径向、$x$ 轴、表面法向的有符号分量；$E_r=\vec E\cdot\hat r$，$E_\perp=\vec E\cdot\hat n$。 / Signed radial, $x$, and surface-normal field components. | $\mathrm{N/C}$ |
| $\epsilon_0,k$ | $\epsilon_0$ 为真空介电常数，约 $8.85\times10^{-12}\,\mathrm{C^2/(N\,m^2)}$；$k=1/(4\pi\epsilon_0)$ 为库仑常数，约 $8.99\times10^9\,\mathrm{N\,m^2/C^2}$。 / Vacuum permittivity and Coulomb's constant, respectively. | 分别如左 / As given |
| $\lambda$ | 线电荷密度：单位长度上的电荷，$\lambda=dQ/d\ell$；均匀时 $\lambda=Q/L$。 / Linear charge density: charge per unit length; $Q/L$ when uniform. | $\mathrm{C/m}$ |
| $\sigma$ | 面电荷密度：单位面积上的电荷，$\sigma=dQ/dA$；均匀时 $\sigma=Q/A$。 / Surface charge density: charge per unit area; $Q/A$ when uniform. | $\mathrm{C/m^2}$ |
| $\rho,\rho_0$ | 体电荷密度：单位体积上的电荷，$\rho=dQ/d\mathcal V$；$\rho_0$ 表示均匀的常量密度。 / Volume charge density: charge per unit volume; $\rho_0$ denotes a uniform constant density. | $\mathrm{C/m^3}$ |
| $r,R$ | $r$ 为观察点到球心或轴线的距离；$R$ 为带电球或球壳的固定半径。 / $r$ is the observation distance from the center or axis; $R$ is the fixed sphere or shell radius. | $\mathrm m$ |
| $L,W,d,x$ | $L$ 为长度（如高斯柱面长度），$W$ 为矩形宽度，$d$ 为板间距，$x$ 为位置坐标。 / Length, rectangle width, plate separation, and position coordinate, respectively. | $\mathrm m$ |
| $A,\mathcal V$ | $A$ 为面积（如柱盒单个端面面积），$\mathcal V$ 为体积；用 $\mathcal V$ 区别于电势 $V$。 / Area, such as one pillbox face, and volume; $\mathcal V$ distinguishes volume from potential $V$. | $\mathrm{m^2},\mathrm{m^3}$ |
| $Q_{\mathrm{enc}}$ | 高斯面包围的净电荷，即面内所有电荷的代数和；$Q_{\mathrm{enc}}(r)$ 表示它随高斯面半径变化。 / Net charge enclosed by a Gaussian surface; $Q_{\mathrm{enc}}(r)$ emphasizes dependence on its radius. | $\mathrm C$ |
| $q$（空腔 / cavity） | 空腔内且不接触导体的物体所带的总电荷，不包含腔壁电荷。 / Total charge of objects inside the cavity without touching the conductor, excluding wall charge. | $\mathrm C$ |
| $Q_{\mathrm{inner}},Q_{\mathrm{outer}},Q_{\mathrm{cond}}$ | 分别为导体内表面、外表面、导体本身的净电荷；$Q_{\mathrm{cond}}=Q_{\mathrm{inner}}+Q_{\mathrm{outer}}$，不计空腔物体的 $q$。 / Net inner-surface, outer-surface, and conductor charges; the conductor total excludes the cavity object's $q$. | $\mathrm C$ |
| $Q_s$ | 指定壳或表面的总电荷：球壳题中是整层球壳电荷，圆柱题中是长度 $L$ 的指定侧面电荷。 / Total charge on the specified shell or surface: the entire spherical shell or a cylindrical surface segment of length $L$. | $\mathrm C$ |
| $\Phi_E$ | 电通量：电场穿过曲面的有符号积分，$\Phi_E=\int_S\vec E\cdot d\vec A$；闭合面用 $\oint$。 / Electric flux: the signed surface integral of the field; $\oint$ denotes a closed surface. | $\mathrm{N\,m^2/C}$ |
| $S,dA,d\vec A$ | $S$ 为积分曲面，$dA$ 为微小面积，$d\vec A=\hat n\,dA$ 为面积向量；闭合面的法向朝外。 / Integration surface, infinitesimal area, and vector area; closed-surface normals point outward. | $dA$: $\mathrm{m^2}$ |
| $\hat r,\hat n$ | 单位向量：$\hat r$ 径向向外，$\hat n$ 沿选定法向；导体边界处从金属指向相邻空间。 / Unit vectors in the outward radial and chosen normal directions; at a conductor boundary the normal points from metal into adjacent space. | 无量纲 / Dimensionless |
| $\theta$（通量 / flux） | 电场 $\vec E$ 与面积向量 $d\vec A$ 的夹角。 / Angle between the electric field and the vector area. | $\mathrm{rad}$ |
| $d\Omega$ | 带方向的微小立体角，$d\Omega=(\hat r\cdot\hat n)dA/r^2$，此处 $r$ 从点电荷量起。 / Oriented infinitesimal solid angle, with $r$ measured from the point charge. | $\mathrm{sr}$ |
| $r_a,r_b,r_c$ | 同轴模型中内棒半径、外管内半径、外管外半径，$r_a<r_b<r_c$。 / Inner-rod radius, tube inner radius, and tube outer radius. | $\mathrm m$ |
| $\lambda_a,\lambda_b,\lambda_c,\lambda_{\mathrm{tube}},\lambda_s$ | 分别为内棒、外管内表面、外管外表面、整根外管以及某指定表面的单位轴向长度电荷；$\lambda_{\mathrm{tube}}=\lambda_b+\lambda_c$。 / Charge per unit axial length of the rod, tube inner surface, tube outer surface, whole tube, and a specified surface, respectively. | $\mathrm{C/m}$ |
| $\sigma_a,\sigma_b,\sigma_c$ | 半径 $r_a,r_b,r_c$ 处各表面的面电荷密度；均匀时 $\sigma_j=\lambda_j/(2\pi r_j)$，$j=a,b,c$。 / Surface charge densities at the three radii; the stated relation assumes uniformity. | $\mathrm{C/m^2}$ |

默认静电场、真空或可近似为真空的空气；无限平面与无限长圆柱模型忽略边缘效应。$E=\|\vec E\|$ 为大小，$E_r$ 为向外取正的径向分量，$k=1/(4\pi\epsilon_0)$。 / Assume electrostatics in vacuum or approximately vacuum-like air; infinite-sheet and infinite-cylinder models neglect edge effects. $E=\|\vec E\|$ is the magnitude, $E_r$ is the signed outward radial component, and $k=1/(4\pi\epsilon_0)$.

## 高斯定律与高斯面的选择 / Gauss's Law and Gaussian Surfaces

电通量衡量电场穿过曲面的程度；闭合面的面积向量指向外侧。高斯定律中的电荷是高斯面内的净电荷： / Electric flux measures the field passing through a surface; area vectors on a closed surface point outward. The charge in Gauss's law is the net enclosed charge:

$$\Phi_E=\oint_S\vec E\cdot d\vec A=\oint_S E\cos\theta\,dA=\frac{Q_{\mathrm{enc}}}{\epsilon_0}.$$

从库仑定律理解：对点电荷 $q$，面元通量为 $d\Phi_E=kq\,d\Omega$，其中 $d\Omega$ 是带方向的立体角。若电荷在闭合面内，$\oint d\Omega=4\pi$，所以 $\Phi_E=4\pi kq=q/\epsilon_0$；若在面外，净立体角为零。对所有电荷叠加即得到高斯定律。 / From Coulomb's law, a point charge $q$ contributes $d\Phi_E=kq\,d\Omega$, where $d\Omega$ is the oriented solid angle. An enclosed charge gives $\oint d\Omega=4\pi$, hence $\Phi_E=4\pi kq=q/\epsilon_0$; an external charge gives zero net solid angle. Superposition gives Gauss's law for general charge distributions.

高斯定律普遍成立，但只有足够对称时，才能方便地将电场从积分中提出。面外电荷虽然不贡献净通量，仍可影响高斯面上各点的电场；$Q_{\mathrm{enc}}=0$ 只说明净通量为零，不能直接推出 $E=0$。 / Gauss's law is always valid, but extracting the field from the integral is convenient only with sufficient symmetry. External charges can affect the field on the surface even though they contribute zero net flux; $Q_{\mathrm{enc}}=0$ does not by itself imply $E=0$.

| 对称性 / Symmetry | 高斯面 / Gaussian surface | 通量化简 / Simplified flux |
| --- | --- | --- |
| 球对称 / Spherical | 同心球面 / Concentric sphere | $E_r4\pi r^2$ |
| 无限长圆柱对称 / Infinite cylindrical | 同轴圆柱面 / Coaxial cylinder | $E_r2\pi rL$；端盖通量为零 / Zero end-cap flux |
| 无限大平面对称 / Infinite planar | 跨过平面的薄柱盒 / Pillbox crossing the plane | 两端面贡献，侧面为零 / Two faces contribute; side contributes zero |

## 无限带电平面与两板叠加 / Infinite Sheets and Superposition

对均匀无限薄带电面，取两端面面积均为 $A$ 的对称柱盒。由对称性，电场垂直于平面，两侧大小相等。以 $\sigma>0$ 为例，两端通量均向外： / For a uniform infinite thin sheet, choose a symmetric pillbox whose two faces each have area $A$. Symmetry makes the field perpendicular to the sheet and equal in magnitude on both sides. For $\sigma>0$, both face fluxes are outward:

$$2EA=\frac{\sigma A}{\epsilon_0}\quad\Longrightarrow\quad\boxed{E=\frac{|\sigma|}{2\epsilon_0}}.$$

正面电荷产生远离平面的电场，负面电荷产生指向平面的电场。公式不含距离，因此在无限平面模型下，$0.1d$、$0.25d$ 不改变单个平面的场强；但必须先确定观察点位于哪一侧、两板之间还是外部。 / Positive sheets produce fields away from the sheet; negative sheets produce fields toward it. The magnitude is independent of distance, so distances such as $0.1d$ or $0.25d$ do not change a sheet's field in this model; the point's side and whether it lies between or outside the sheets still matter.

令左板位于 $x=0$，右板位于 $x=d$，$+x$ 向右。由 $\vec E_{\mathrm{net}}=\vec E_1+\vec E_2$，对于 $\sigma>0$： / Put the left sheet at $x=0$ and the right sheet at $x=d$, with $+x$ to the right. From $\vec E_{\mathrm{net}}=\vec E_1+\vec E_2$, for $\sigma>0$:

| 两板电荷密度 / Sheet densities | 左侧 $x<0$ / Left | 板间 $0<x<d$ / Between | 右侧 $x>d$ / Right |
| --- | --- | --- | --- |
| 左 $+\sigma$、右 $+\sigma$ / Both positive | $E_x=-\sigma/\epsilon_0$ | $E_x=0$ | $E_x=+\sigma/\epsilon_0$ |
| 左 $+\sigma$、右 $-\sigma$ / Opposite signs | $E_x=0$ | $E_x=+\sigma/\epsilon_0$ | $E_x=0$ |

例如异号板之间，两场都从正板指向负板，故 $E=\sigma/(2\epsilon_0)+\sigma/(2\epsilon_0)=\sigma/\epsilon_0$。完全抵消需要两板面电荷密度大小相等；有限板只在远离边缘的区域近似满足这些结果。 / Between opposite sheets, both fields point from the positive sheet to the negative sheet, giving $E=\sigma/(2\epsilon_0)+\sigma/(2\epsilon_0)=\sigma/\epsilon_0$. Complete cancellation requires equal density magnitudes; finite plates approximate these results only away from edges.

## 导体静电平衡 / Conductors in Electrostatic Equilibrium

若导体材料内部存在电场，自由电荷会受到 $\vec F=q\vec E$ 而重新分布；达到静电平衡时，内部总电场必须为零。再在金属内部取任意微小高斯面，可知材料内部没有净体电荷，多余电荷位于表面，包括可能存在的空腔内表面。 / A field inside conducting material would exert $\vec F=q\vec E$ on free charges and cause redistribution. At electrostatic equilibrium, the total interior field must vanish. Applying Gauss's law to small surfaces within the metal shows that there is no net bulk charge; excess charge resides on surfaces, including cavity surfaces when present.

$$\boxed{\vec E=\vec0\quad\text{inside conducting material}}.$$

由 $V_B-V_A=-\int_A^B\vec E\cdot d\vec\ell=0$，每个连通导体是等势体。表面切向电场也为零，否则电荷会沿表面移动。“金属材料内部”不等于“空腔内部”；空腔中有电荷时，空腔电场通常不为零。 / Since $V_B-V_A=-\int_A^B\vec E\cdot d\vec\ell=0$, each connected conductor is equipotential. The tangential field at its surface also vanishes, or charges would move along it. Conducting material and an empty cavity region are different: a cavity containing charge generally has a nonzero field.

## 导体空腔中的感应电荷 / Induced Charge on a Cavity

设空腔内电荷总量为 $q$，取完全位于金属内部且包围空腔的高斯面。由于该面处处 $E=0$，得到： / Let the total charge inside a cavity be $q$. Choose a Gaussian surface entirely within the metal and enclosing the cavity. Because $E=0$ everywhere on this surface:

$$0=\oint\vec E\cdot d\vec A=\frac{q+Q_{\mathrm{inner}}}{\epsilon_0}\quad\Longrightarrow\quad\boxed{Q_{\mathrm{inner}}=-q}.$$

若导体本身总电荷为 $Q_{\mathrm{cond}}$，电荷守恒进一步给出 $Q_{\mathrm{outer}}=Q_{\mathrm{cond}}+q$。例如 $q=-2.25\,\mathrm{pC}$，内表面为 $+2.25\,\mathrm{pC}$；若导体原本中性且孤立，外表面为 $-2.25\,\mathrm{pC}$。 / If the conductor's net charge is $Q_{\mathrm{cond}}$, charge conservation gives $Q_{\mathrm{outer}}=Q_{\mathrm{cond}}+q$. For $q=-2.25\,\mathrm{pC}$, the inner surface carries $+2.25\,\mathrm{pC}$; an initially neutral isolated conductor then has $-2.25\,\mathrm{pC}$ on its outer surface.

内表面总电荷为 $-q$ 不要求电荷位于中心；但均匀分布通常需要球形空腔与居中点电荷的对称性。接地导体可与大地交换电荷，因此不能预设其总电荷保持不变。 / The total inner charge is $-q$ even if the charge is off-center; uniformity generally requires a spherical cavity and a centered point charge. A grounded conductor can exchange charge with Earth, so its net charge need not remain fixed.

## 球对称电场：导体球与绝缘球 / Spherical Fields: Conductors and Insulators

球对称时，半径 $r$ 的同心高斯面上径向电场相同： / Under spherical symmetry, the radial field is constant over a concentric Gaussian sphere of radius $r$:

$$E_r4\pi r^2=\frac{Q_{\mathrm{enc}}(r)}{\epsilon_0}\quad\Longrightarrow\quad\boxed{E_r(r)=k\frac{Q_{\mathrm{enc}}(r)}{r^2}}.$$

**导体实心球：**半径为 $R$、总电荷为 $Q$ 的球形导体在无外场破坏对称性时，电荷均匀分布于表面，内部 $E=0$，外部等效为位于球心的点电荷。 / **Solid conducting sphere:** for a sphere of radius $R$ and charge $Q$, with no external field breaking symmetry, charge is uniform on the surface. The interior field is zero, and the exterior field equals that of a point charge at the center.

$$E_r(r)=\begin{cases}0,&r<R,\\kQ/r^2,&r>R.\end{cases}\qquad E(r>R)=k\frac{|Q|}{r^2}.$$

**均匀带电绝缘实心球：**电荷固定分布于整个体积，不能套用“导体内部场为零”。若体密度为 $\rho_0$，则： / **Uniformly charged insulating solid sphere:** charge occupies the volume, so the zero-field rule for conducting material does not apply. For uniform volume density $\rho_0$:

$$Q_{\mathrm{enc}}(r)=\begin{cases}\rho_0\frac43\pi r^3,&r<R,\\\rho_0\frac43\pi R^3=Q,&r>R.\end{cases}$$

$$\boxed{E_r(r)=\begin{cases}\dfrac{\rho_0r}{3\epsilon_0},&r<R,\\\dfrac{\rho_0R^3}{3\epsilon_0r^2},&r>R.\end{cases}}$$

球内大小随 $r$ 线性增加，球外按 $1/r^2$ 衰减；球心为零，$r=R$ 处两式连续，大小最大。若 $\rho_0<0$，$E_r<0$ 表示向内；求大小时用 $|\rho_0|$。 / The magnitude grows linearly inside and falls as $1/r^2$ outside. It is zero at the center, continuous at $r=R$, and maximal there. If $\rho_0<0$, the negative radial component points inward; use $|\rho_0|$ for the magnitude.

## 均匀薄球壳与中心电荷 / Uniform Thin Spherical Shells and Central Charges

半径为 $R$、总电荷为 $Q_s$ 的均匀薄球壳，壳内高斯面不包围电荷；结合球对称性得 $E_r4\pi r^2=0$，故壳内 $E=0$。壳外包围全部电荷： / For a uniform thin shell of radius $R$ and charge $Q_s$, an interior Gaussian sphere encloses no charge. Spherical symmetry then gives $E_r4\pi r^2=0$, so the interior field vanishes. Outside, all shell charge is enclosed:

$$E_r(r)=\begin{cases}0,&r<R,\\kQ_s/r^2,&r>R.\end{cases}$$

若在均匀绝缘薄球壳中心再放置点电荷 $q$，叠加后壳内 $E_r=kq/r^2$（$0<r<R$），壳外 $E_r=k(q+Q_s)/r^2$。若改为有厚度的导体球壳，则空腔、金属、外部必须分区：空腔中可有电场，金属内仍为零，外部在球对称条件下由总包围电荷决定。 / Adding a point charge $q$ at the center of a uniformly charged insulating shell gives $E_r=kq/r^2$ for $0<r<R$ and $E_r=k(q+Q_s)/r^2$ outside. For a conducting shell of finite thickness, distinguish cavity, metal, and exterior: the cavity may have a field, the metal has none, and the spherically symmetric exterior field depends on the total enclosed charge.

## 无限长线电荷 / Infinite Line Charge

对线密度为 $\lambda$ 的无限长直线电荷，取半径 $r$、长度 $L$ 的同轴高斯柱面。电场径向，端盖无通量，侧面电场大小处处相同： / For an infinite straight line of density $\lambda$, choose a coaxial Gaussian cylinder of radius $r$ and length $L$. The radial field gives zero end-cap flux and a constant field magnitude on the curved surface:

$$E_r\cdot(2\pi rL)=\frac{\lambda L}{\epsilon_0}\quad\Longrightarrow\quad\boxed{E_r=\frac{\lambda}{2\pi\epsilon_0r}},\qquad\boxed{E=\frac{|\lambda|}{2\pi\epsilon_0r}}.$$

正线电荷向外，负线电荷向内，大小按 $1/r$ 衰减。原因是通量穿过的圆柱侧面积随 $r$ 增长，而球面面积随 $r^2$ 增长。 / Positive line charge gives an outward field and negative line charge an inward field, with magnitude proportional to $1/r$. The cylindrical flux area grows as $r$, whereas a spherical area grows as $r^2$.

## 同轴圆柱导体的分区推导 / Piecewise Fields of Coaxial Conductors

设无限长内导体棒半径为 $r_a$，线电荷密度为 $\lambda_a$；外导体管内、外半径为 $r_b,r_c$，其中 $r_a<r_b<r_c$，管的净线电荷密度为 $\lambda_{\mathrm{tube}}$。外管内、外表面线密度分别为 $\lambda_b,\lambda_c$。 / Let an infinite inner conducting rod have radius $r_a$ and line density $\lambda_a$. An outer conducting tube has inner and outer radii $r_b,r_c$, with $r_a<r_b<r_c$, and net line density $\lambda_{\mathrm{tube}}$. Its inner and outer surfaces carry line densities $\lambda_b,\lambda_c$.

在外管金属中取高斯柱面，$E=0$ 要求 $\lambda_a+\lambda_b=0$。再由外管电荷守恒 $\lambda_b+\lambda_c=\lambda_{\mathrm{tube}}$： / A Gaussian cylinder in the tube's metal has $E=0$, requiring $\lambda_a+\lambda_b=0$. Charge conservation for the tube gives $\lambda_b+\lambda_c=\lambda_{\mathrm{tube}}$, hence:

$$\boxed{\lambda_b=-\lambda_a},\qquad\boxed{\lambda_c=\lambda_{\mathrm{tube}}+\lambda_a}.$$

每个非金属区域用 $E_r2\pi rL=Q_{\mathrm{enc}}/\epsilon_0$，可得完整分段式： / Applying $E_r2\pi rL=Q_{\mathrm{enc}}/\epsilon_0$ in each nonmetal region gives:

$$\boxed{E_r(r)=\begin{cases}0,&r<r_a,\\\dfrac{\lambda_a}{2\pi\epsilon_0r},&r_a<r<r_b,\\0,&r_b<r<r_c,\\\dfrac{\lambda_a+\lambda_{\mathrm{tube}}}{2\pi\epsilon_0r},&r>r_c.\end{cases}}$$

例如 $\lambda_a=-\lambda$、$\lambda>0$，间隙中 $E_r=-\lambda/(2\pi\epsilon_0r)$，负号表示向内。外部场不一定非零：若 $\lambda_{\mathrm{tube}}=-\lambda_a$，总包围电荷为零，外部场也为零。 / For $\lambda_a=-\lambda$ with $\lambda>0$, the gap field is $E_r=-\lambda/(2\pi\epsilon_0r)$, pointing inward. The exterior field need not be nonzero: if $\lambda_{\mathrm{tube}}=-\lambda_a$, the enclosed net charge and exterior field both vanish.

## 圆柱表面电荷密度 / Cylindrical Surface Charge Density

半径 $r$、长度 $L$ 的圆柱侧面积为 $2\pi rL$；若该表面的线电荷密度为 $\lambda_s$，电荷为 $Q_s=\lambda_sL$，因此： / A cylindrical surface of radius $r$ and length $L$ has area $2\pi rL$. If that surface carries line density $\lambda_s$, its charge is $Q_s=\lambda_sL$, so:

$$\boxed{\sigma=\frac{\lambda_s}{2\pi r}},\qquad\sigma_a=\frac{\lambda_a}{2\pi r_a},\quad\sigma_b=\frac{-\lambda_a}{2\pi r_b},\quad\sigma_c=\frac{\lambda_a+\lambda_{\mathrm{tube}}}{2\pi r_c}.$$

这里必须使用对应表面的线电荷密度；不能将整根外管的净线密度直接用于内表面。 / Use the line density of the particular surface, not the tube's net line density for its inner surface.

## 导体表面刚外侧的电场 / Field Immediately Outside a Conductor

用无穷薄柱盒跨过带电表面，并令 $\hat n$ 从导体材料指向外部空间。柱盒厚度趋零时侧面通量消失，高斯定律给出法向场的跳变： / Use an infinitesimal pillbox across a charged surface, with $\hat n$ pointing from the conducting material into the adjacent space. Side flux vanishes as its thickness tends to zero, and Gauss's law gives the normal-field jump:

$$(\vec E_{\mathrm{out}}-\vec E_{\mathrm{in}})\cdot\hat n=\frac{\sigma}{\epsilon_0}.$$

导体内部 $\vec E_{\mathrm{in}}=0$，表面切向场也为零，因此在光滑表面紧邻外侧： / Since $\vec E_{\mathrm{in}}=0$ and the tangential surface field vanishes, immediately outside a smooth conducting surface:

$$\boxed{\vec E_{\mathrm{out}}=\frac{\sigma}{\epsilon_0}\hat n},\qquad\boxed{\sigma=\epsilon_0E_\perp},\qquad E=\frac{|\sigma|}{\epsilon_0}.$$

单个孤立无限薄电荷面两侧都有场，通量为 $2EA$；导体边界内侧无场，通量只有 $E_\perp A$，这解释了因子 $2$ 的区别。对于空腔内表面，$\hat n$ 指向空腔，未必与从轴线或球心向外的 $\hat r$ 同向。 / An isolated infinite sheet has fields on both sides, giving flux $2EA$; a conductor boundary has no interior field, leaving only $E_\perp A$. This explains the factor of two. At a cavity wall, $\hat n$ points into the cavity and may oppose the radial direction $\hat r$.

## 电场图像的判断 / Reading Field Graphs

画图前先确认纵轴是非负的大小 $E$，还是可以为负的分量 $E_r$。分区求包围电荷，再判断零点、幂律、方向和表面跳变。 / Before plotting, distinguish a nonnegative magnitude $E$ from a signed component $E_r$. Determine enclosed charge region by region, then identify zeros, power laws, directions, and surface jumps.

| 区域 / Region | 图像特征 / Graph behavior |
| --- | --- |
| 均匀绝缘实心球内部 / Uniform insulating sphere interior | $E\propto r$，从零线性增长 / Linear growth from zero |
| 球对称分布外部 / Outside a spherical distribution | $E\propto1/r^2$，总电荷非零时 / For nonzero total charge |
| 无限线电荷或同轴间隙 / Infinite line or coaxial gap | $E\propto1/r$ |
| 导体材料内 / Conducting material | $E=0$ |
| 理想无限平面的一侧 / One side of an infinite sheet | $E$ 为常数 / Constant magnitude |

同轴导体常见顺序为 $0\to1/r\to0\to1/r$，最后一段是否为零及其符号由总线电荷决定。负内棒使间隙内的 $E_r$ 位于横轴下方。表面电荷允许法向场跳变；均匀绝缘球只有体电荷、无额外面电荷时，$r=R$ 处电场连续。 / A common coaxial pattern is $0\to1/r\to0\to1/r$, but the last segment's sign and whether it vanishes depend on the net line charge. A negative inner rod puts the gap's $E_r$ below the axis. Surface charge allows jumps in the normal field; a uniformly charged insulating sphere without an extra surface charge has a continuous field at $r=R$.

## 相关笔记 / Related Notes

- [[Physics/2.Electrostatics/electric_field_and_charge_density]] — 电场与电荷密度 / Fields and charge density
- [[Physics/2.Electrostatics/electric_potential_and_energy]] — 电势与能量应用 / Potential and energy applications

## 来源 / Sources

- [[Daily Notes/2026-09-16]] — 课堂记录 / Class notes

[//begin]: # "Autogenerated link references for markdown compatibility"
[//end]: # "Autogenerated link references"
