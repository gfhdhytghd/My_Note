# 7. 热力学基础 / Thermodynamics Basics

> 本笔记整理自 [[Daily Notes/2025-09-03|2025-09-03 日记]]

## 系统与周围 / System and Surroundings

### 系统 / System

系统是热力学研究中被选定的研究对象，可以是物质、能量或两者的组合。

A system is the selected object of study in thermodynamics, which can be matter, energy, or a combination of both.

### 周围 / Surroundings

周围是与系统相互作用的一切外部环境。

Surroundings are everything external to the system that interacts with it.

### 系统分类 / System Classification

1. **开放系统 / Open System**
   - 物质和能量都可以交换 / Both matter and energy can be exchanged
   - 例如：敞口烧杯 / Example: Open beaker

2. **封闭系统 / Closed System**
   - 只有能量可以交换 / Only energy can be exchanged
   - 例如：密封容器 / Example: Sealed container

3. **孤立系统 / Isolated System**
   - 物质和能量都不能交换 / Neither matter nor energy can be exchanged
   - 例如：理想保温瓶 / Example: Ideal thermos bottle

## 内能 / Internal Energy

### 定义 / Definition

内能是系统内所有微观粒子（原子、分子）的动能和势能的总和。

Internal energy is the sum of kinetic and potential energies of all microscopic particles (atoms, molecules) within the system.

$$U = U_{kinetic} + U_{potential}$$

### 内能变化 / Internal Energy Change

内能变化只取决于系统的初态和终态，与过程路径无关。

The change in internal energy depends only on the initial and final states of the system, not on the process path.

$$\Delta U = U_{final} - U_{initial}$$

### 影响因素 / Influencing Factors

1. **温度 / Temperature**
   - 温度升高，内能增加 / Higher temperature increases internal energy

2. **相变 / Phase Changes**
   - 熔化、汽化等过程改变内能 / Melting, vaporization change internal energy

3. **化学反应 / Chemical Reactions**
   - 化学键的形成和断裂改变内能 / Bond formation and breaking change internal energy

## 分子能量演化 / Molecular Energy Evolution

### 升温阶段 / Heating Within a Single Phase

- 在固态、液态或气态内部缓慢升温时，外界提供的热量主要转化为分子平动、转动与振动动能，平均动能与温度呈正比关系，例如理想气体有$\bar{E}_{k}=\frac{f}{2}k_BT$。  
  When heating within a single phase, supplied heat mainly boosts translational, rotational, and vibrational kinetic energies, with average kinetic energy scaling with temperature; for an ideal gas $\bar{E}_{k}=\frac{f}{2}k_BT$.
- 动能提升导致粒子运动更剧烈，也使分子间距的波动范围更大，但势能的平均值保持近似不变，因为作用力网络尚未发生宏观重组。  
  Rising kinetic energy makes molecular motion more vigorous and fluctuations in separation wider, yet the mean potential energy remains nearly unchanged because the intermolecular network has not reorganized.

### 相变平台 / Phase Transition Plateau

- 当加热曲线达到熔点或沸点一类相变平台时，体系温度几乎保持常数，新增热量用于克服分子间作用力以拉大平均间距，因此主要表现为势能增加。  
  Upon reaching melting or boiling plateaus, the temperature stays nearly constant and the added heat overcomes intermolecular forces to increase average separations, manifesting primarily as rising potential energy.
- 平台过程中分子动能分布几乎不变，潜热对应着势能垒的攀升；能量投入越多，越多分子离开原有势阱并进入新相。  
  Kinetic energy distribution hardly changes across the plateau; latent heat represents the climb over potential barriers, allowing more molecules to escape their original wells and populate the new phase.

### 能量图景 / Energy Landscape

- 升温区段倾斜、相变区段水平的“阶梯”式加热曲线可视为动能与势能交替主导的图示：斜段的斜率反映热容量，而水平段的长度对应潜热，与具体的[[intermolecular_forces]]强度密切相关。  
  The characteristic heating curve—slanted segments and horizontal plateaus—visualizes alternating dominance of kinetic and potential energy: ramp slopes reflect heat capacity whereas plateau lengths correspond to latent heat, tightly linked to the strength of [[intermolecular_forces]].

## 热传递 / Heat Transfer

### 定义 / Definition

热是系统与周围之间由于温度差而传递的能量。

Heat is energy transferred between system and surroundings due to temperature difference.

### 热传递方向 / Heat Transfer Direction

- **放热过程 / Exothermic Process**: $q < 0$ (系统向周围放热)
- **吸热过程 / Endothermic Process**: $q > 0$ (系统从周围吸热)

### 热传递方式 / Heat Transfer Methods

1. **传导 / Conduction**
   - 通过直接接触传递 / Transfer through direct contact

2. **对流 / Convection**
   - 通过流体运动传递 / Transfer through fluid motion

3. **辐射 / Radiation**
   - 通过电磁波传递 / Transfer through electromagnetic waves

## 功 / Work

### 定义 / Definition

功是系统与周围之间除热传递外的其他能量传递形式。

Work is energy transfer between system and surroundings other than heat transfer.

### 功的类型 / Types of Work

1. **体积功 / Volume Work**
   - 系统体积变化时做的功 / Work done when system volume changes
   - $w = -P_{external} \Delta V$

2. **电功 / Electrical Work**
   - 电流通过系统时做的功 / Work done when current passes through system

3. **表面功 / Surface Work**
   - 改变表面积时做的功 / Work done when changing surface area

### 功的符号约定 / Work Sign Convention

- **系统做功 / System does work**: $w < 0$ (系统失去能量)
- **对系统做功 / Work done on system**: $w > 0$ (系统获得能量)

## 热力学第一定律 / First Law of Thermodynamics

### 数学表达式 / Mathematical Expression

$$\Delta U = q + w$$

其中 / Where:
- $\Delta U$ = 内能变化 / Change in internal energy
- $q$ = 热传递 / Heat transfer
- $w$ = 功 / Work

### 物理意义 / Physical Meaning

能量既不能被创造也不能被消灭，只能从一种形式转换为另一种形式。

Energy cannot be created or destroyed, only converted from one form to another.

### 应用实例 / Application Examples

1. **恒容过程 / Constant Volume Process**
   - $\Delta V = 0$, 所以 $w = 0$
   - $\Delta U = q_V$ (恒容热)

2. **恒压过程 / Constant Pressure Process**
   - $w = -P\Delta V$
   - $\Delta U = q_P - P\Delta V$

## 焓 / Enthalpy

### 定义 / Definition

焓是内能与体积功的和，特别适用于恒压过程。

Enthalpy is the sum of internal energy and volume work, especially useful for constant pressure processes.

$$H = U + PV$$

### 焓变 / Enthalpy Change

$$\Delta H = \Delta U + P\Delta V$$

在恒压条件下 / Under constant pressure:
$$\Delta H = q_P$$

## 动态平衡 / Dynamic Equilibrium

> 本段整理自 [[journal/2025-10-29|2025-10-29 日记]]

### 核心定义 / Core Definition

- 在封闭体系中，正逆过程速率相等，宏观性质保持常数，但微观粒子持续交换。  
  In a closed system, forward and reverse process rates match so macroscopic observables stay constant while microscopic particles continue to exchange.
- 动态平衡满足热力学条件$\Delta G=0$且反应商等于平衡常数$Q=K$，表征体系能量最小化的稳定状态。  
  Dynamic equilibrium satisfies the thermodynamic condition $\Delta G=0$ with the reaction quotient equal to the equilibrium constant $Q=K$, indicating a stable, minimum-energy state.

### 化学反应中的动态平衡 / Dynamic Equilibrium in Chemical Reactions

- 可逆反应$\nu_A A + \nu_B B \rightleftharpoons \nu_C C + \nu_D D$在平衡时有$K=\frac{a_C^{\nu_C}a_D^{\nu_D}}{a_A^{\nu_A}a_B^{\nu_B}}$，任何对反应物或生成物活度的扰动都会通过速率调节恢复$Q=K$。  
  For a reversible reaction $\nu_A A + \nu_B B \rightleftharpoons \nu_C C + \nu_D D$, the equilibrium condition $K=\frac{a_C^{\nu_C}a_D^{\nu_D}}{a_A^{\nu_A}a_B^{\nu_B}}$ means any perturbation to reactant or product activities triggers rate adjustments that drive $Q$ back to $K$.
- 勒夏特列原理指出外界施加的浓度、压力或温度变化，会迫使体系沿着抵消扰动的方向移动以恢复动态平衡。  
  Le Châtelier's principle states that imposed changes in concentration, pressure, or temperature push the system along the direction that offsets the disturbance to reestablish dynamic equilibrium.
- 催化剂能同时降低正逆反应的活化能，从而更快到达平衡，但不会改变平衡组成，因为$K$仅受温度控制。  
  Catalysts lower activation energies for both forward and reverse paths, shortening the time needed to reach equilibrium without altering the equilibrium composition because $K$ depends only on temperature.

### 物态变化中的动态平衡 / Dynamic Equilibrium in Phase Changes

- 在密闭容器中，液体的蒸发速率与蒸气的冷凝速率相等时形成蒸发-冷凝平衡，此时蒸气压等于平衡蒸气压并随温度变化。  
  In a sealed vessel, vaporization-condensation equilibrium forms when evaporation and condensation rates match, yielding a saturated vapor pressure that varies with temperature.
- 固液共存时的熔化-凝固平衡类似，晶格不断吸收与释放粒子，宏观体积分数稳定，这与晶格能和[[intermolecular_forces]]强度紧密相关。  
  Melting-freezing equilibrium during solid-liquid coexistence works similarly: the lattice continuously absorbs and releases particles, keeping bulk fractions steady, tightly linked to lattice energy and [[intermolecular_forces]] strength.
- 相平衡可视作吉布斯相律$F=C-P+2$的特例，当自由度$F=0$时温度与压力固定，体系沿相图共存曲线运行。  
  Phase equilibria illustrate the Gibbs phase rule $F=C-P+2$; when the degrees of freedom $F=0$, temperature and pressure are fixed and the system follows a coexistence curve on the phase diagram.

### 微观图景与能量交流 / Microscopic Picture and Energy Exchange

- 动态平衡强调“动中有衡”，分子持续发生碰撞与转化，能量在正逆过程之间快速循环，但宏观变量如浓度、压强、相态比例保持恒定。  
  Dynamic equilibrium highlights the idea of "motion within balance": molecules keep colliding and converting, energy shuttles between forward and reverse steps, yet macroscopic variables such as concentration, pressure, and phase fractions remain constant.
- 掌握这一图景有助于解释速率与能量竞争、预测多步骤可逆反应以及理解[[gases_and_kmt|气体动理论]]中粒子逃逸与返回的统计互补性。  
  Understanding this picture clarifies the competition between kinetics and energetics, aids in predicting multi-step reversible reactions, and connects with the statistical reciprocity of particle escape and return in the [[gases_and_kmt|kinetic molecular theory]].

## 相关概念 / Related Concepts

- [[atom_basics|原子基础]] - 了解原子基本结构
- [[electron_attraction|电子间吸引力]] - 电子与原子核的相互作用
- [[mole_concept|摩尔概念]] - 原子数量的宏观表示

[//begin]: # "Autogenerated link references for markdown compatibility"
[Daily Notes/2025-09-03|2025-09-03 日记]: <../../Daily Notes/2025-09-03.md> "2025-09-03"
[intermolecular_forces]: ../6.Intermolecular_Forces/intermolecular_forces.md "分子间作用力（IMFs）/ Intermolecular Forces (Lecture 19, CHEM 110B)"
[journal/2025-10-29|2025-10-29 日记]: ../../journal/2025-10-29.md "2025-10-29"
[gases_and_kmt|气体动理论]: ../8.Gases/gases_and_kmt.md "气体与动理论 / Gases and Kinetic Molecular Theory"
[gases_and_kmt|kinetic molecular theory]: ../8.Gases/gases_and_kmt.md "气体与动理论 / Gases and Kinetic Molecular Theory"
[atom_basics|原子基础]: atom_basics.md "1. 原子基础 / Atomic Basics"
[electron_attraction|电子间吸引力]: electron_attraction.md "6. 电子间吸引力 / Electron Attraction"
[mole_concept|摩尔概念]: mole_concept.md "5. 摩尔概念 / The Concept of Mole"
[//end]: # "Autogenerated link references"
