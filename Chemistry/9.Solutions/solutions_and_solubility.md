# 溶液与溶解度 / Solutions & Solubility

## 溶解度核心概念 / Core Solubility Concepts
- 溶解与析晶的动态平衡：当固体溶质与溶剂接触时，两过程并存；随溶质浓度升高，结晶速率提升直到与溶解速率相等，此时浓度即为该条件下的溶解度。  Dissolution and crystallization occur simultaneously; as solute concentration rises, crystallization accelerates until it matches dissolution, defining the solubility at those conditions.
- 溶解度定义：在特定条件下，一定量溶剂中所能溶解的最大溶质量（可用质量或物质的量衡量）。  Solubility is the maximum amount of solute (mass or moles) that dissolves in a given amount of solvent under specified conditions.
- 影响因素：溶质–溶剂与溶质–溶质的分子间作用力以及温度（对不同体系可增可减）；气体溶解度还受压强控制。  Determined by solute–solvent/solute–solute intermolecular forces and by temperature (direction depends on the system); gas solubility is also pressure dependent.
- 饱和度术语：  
  - 不饱和溶液：实际溶解量低于溶解度，如室温下 30 g NaCl/100 g 水全部溶解。  Unsaturated solutions hold less solute than solubility, e.g., 30 g NaCl per 100 g water at room temperature dissolves fully.  
  - 饱和溶液：已达最大溶解量，如 40 g NaCl 加入 100 g 水时仅约 36 g 溶解，其余析出。  Saturated solutions reach the maximal amount, e.g., only ≈36 g of 40 g NaCl dissolves in 100 g water.  
  - 过饱和溶液：暂时超出溶解度、极不稳定，可由升温溶解后降温制得，会随扰动析出多余溶质。  Supersaturated solutions temporarily exceed solubility (often by dissolving at high T then cooling) and shed excess solute upon disturbance.
- 关联与延伸：进一步理解依赖分子间作用力 [[Chemistry/6.Intermolecular_Forces/intermolecular_forces]] 与气体行为 [[Chemistry/8.Gases/gases_and_kmt]]。  Cross-check with intermolecular forces [[Chemistry/6.Intermolecular_Forces/intermolecular_forces]] and gas behavior [[Chemistry/8.Gases/gases_and_kmt]] for deeper context.

## 溶液组成与浓度指标 / Composition & Concentration Metrics
- 汇总常用指标：质量分数$w=\frac{m_\mathrm{solute}}{m_\mathrm{solution}}$、质量百分数$w\times100\%$、摩尔分数$x=\frac{n_\mathrm{solute}}{n_\mathrm{solution}}$、摩尔浓度$M=\frac{n_\mathrm{solute}}{V_\mathrm{solution}}$，以及 ppm/ppb/ppt 对应 $10^6/10^9/10^{12}$ 换算。  Common metrics include mass fraction $w$, weight percent $w\times100\%$, mole fraction $x$, molarity $M$, plus ppm/ppb/ppt scaling by $10^6/10^9/10^{12}$.
- 计算流程：先统一质量或物质的量，再参考 [[Chemistry/1.Atom_and_Mole/mass_percentage_calculations]] 与 [[Chemistry/1.Atom_and_Mole/mole_concept]] 的步骤逐一换算，能显著减少单位混乱。  Workflow: normalize masses or moles first, then follow the procedures in [[Chemistry/1.Atom_and_Mole/mass_percentage_calculations]] and [[Chemistry/1.Atom_and_Mole/mole_concept]] to avoid unit mix-ups.

## 溶解焓与溶剂化 / Dissolution Enthalpy & Solvation
- 溶解焓可分解为$\Delta H_1$（破坏溶质内部作用力）、$\Delta H_2$（破坏溶剂作用力）、$\Delta H_3$（形成溶质–溶剂作用），总焓变$\Delta H_\mathrm{soln}=\Delta H_1+\Delta H_2+\Delta H_3$。  The dissolution enthalpy splits into $\Delta H_1$ (break solute interactions), $\Delta H_2$ (break solvent interactions), and $\Delta H_3$ (form solute–solvent interactions), summing to $\Delta H_\mathrm{soln}$.
- 以 NaCl 为例：先克服晶格能，再松动水分子氢键，最后通过离子–偶极作用形成水合（溶剂化）壳层，这一过程由$\Delta H_3$和熵增共同驱动。  Example NaCl: overcome lattice energy, loosen water H-bonds, then build hydration shells via ion–dipole forces, with $\Delta H_3$ plus entropy gain driving dissolution.
- $\Delta H_\mathrm{soln}$ 可正可负：如 $\ce{CuSO4}$ 溶解放热而 $\ce{NH4NO3}$ 吸热，实验需监控温度并据此设计能量守恒步骤。  $\Delta H_\mathrm{soln}$ may be positive or negative: $\ce{CuSO4}$ dissolves exothermically whereas $\ce{NH4NO3}$ is endothermic, so monitor temperature and plan energy handling accordingly.
- 自发性判据：只要释放热量或带来足够熵增（混合、疏水效应等），吸热溶解也可自发；蛋白折叠中的疏水效应用同一逻辑，详见 [[Chemistry/7.Biological_Macromolecules/protein_structure_highlights]]。  Spontaneity requires either exothermicity or sufficient entropy gain (mixing, hydrophobic effects), so even endothermic dissolutions can proceed; protein folding leverages the same hydrophobic logic (see [[Chemistry/7.Biological_Macromolecules/protein_structure_highlights]]).

## 电解质与导电性 / Electrolytes & Conductivity
- 溶液能点亮灯泡取决于可自由迁移的离子；通电时阳离子指向阴极、阴离子指向阳极，从而形成电流。  Conductivity demands mobile ions: under potential, cations drift to the cathode and anions to the anode, completing the circuit.
- 电解质分类：强电解质完全离解、弱电解质部分离解、非电解质几乎不产生离子，只有离子浓度高的溶液才是良导体。  Electrolytes classify as strong (complete dissociation), weak (partial), and non-electrolytes (no ions); only high-ion solutions conduct well.
- 强酸速记：$\ce{HCl}$、$\ce{HBr}$、$\ce{HI}$、$\ce{HClO3}$、$\ce{HClO4}$、$\ce{H2SO4}$、$\ce{HNO3}$，在水中几乎完全生成 $\ce{H3O+}$ 与对应阴离子。  Strong acid roster—$\ce{HCl}$, $\ce{HBr}$, $\ce{HI}$, $\ce{HClO3}$, $\ce{HClO4}$, $\ce{H2SO4}$, $\ce{HNO3}$—fully produce $\ce{H3O+}$ and their anions in water.
- 强碱速记：$\ce{LiOH}$、$\ce{NaOH}$、$\ce{KOH}$、$\ce{RbOH}$、$\ce{CsOH}$、$\ce{Ca(OH)2}$、$\ce{Sr(OH)2}$、$\ce{Ba(OH)2}$，而 $\ce{NH3}$、$\ce{Mg(OH)2}$、胺类等仅弱产 $\ce{OH-}$。  Strong bases include $\ce{LiOH}$, $\ce{NaOH}$, $\ce{KOH}$, $\ce{RbOH}$, $\ce{CsOH}$, $\ce{Ca(OH)2}$, $\ce{Sr(OH)2}$, $\ce{Ba(OH)2}$, in contrast to weak bases like $\ce{NH3}$, $\ce{Mg(OH)2}$, and amines that barely yield $\ce{OH-}$.

## 浓度运算与稀释 / Concentration Operations & Dilution
- 先判别恒定量：转移操作保持浓度不变，而稀释保持溶质摩尔数不变并增大体积；这一思路能为任何题目迅速锁定方程。  Identify the invariant first: transfers keep concentration fixed, dilutions keep solute moles fixed while increasing volume; this mindset streamlines equation setup.
- 快速稀释公式 $M_1V_1=M_2V_2$ 适用于一步稀释；例：10.0 mL 的 2.25 M $\ce{Na3PO4}$ 稀释到 40.0 mL 得 $M_2=0.5625$ M，$\ce{Na+}$ 浓度为 $3\times0.5625=1.6875$ M。  The shortcut $M_1V_1=M_2V_2$ handles single-step dilutions; e.g., diluting 10.0 mL of 2.25 M $\ce{Na3PO4}$ to 40.0 mL yields $M_2=0.5625$ M and $[\ce{Na+}]=1.6875$ M.
- 多元强电解质需跟踪化学计量：1 M $\ce{CaCl2}$ 对应 1 M $\ce{Ca^{2+}}$ 与 2 M $\ce{Cl^{-}}$，总离子浓度 3 M，解题时务必平衡电荷与系数。  For multi-ionic solutes, map stoichiometry directly: 1 M $\ce{CaCl2}$ produces 1 M $\ce{Ca^{2+}}$ plus 2 M $\ce{Cl^{-}}$, totaling 3 M ions—always balance charges and coefficients.

## 亨利定律与气体溶解度 / Henry's Law & Gas Solubility
- 仅气体溶解度随外部压力显著变化，而液体与固体在常见范围内几乎不受影响。  Only dissolved gases respond strongly to pressure changes; liquids and solids are nearly pressure-independent.
- 亨利定律表述为 $C_g=kP_g$，其中 $C_g$ 为气体溶解度、$P_g$ 为气体分压、$k$ 为与溶剂间分子间作用力相关的常数。  Henry's law uses $C_g=kP_g$ where $k$ captures IMF strength between the gas and solvent.
- 强氢键或偶极作用的气体拥有更大的 $k$ 值，因此在相同分压下溶解更多；图像上体现为更陡的斜率。  Gases forming stronger IMFs with water have larger $k$ and steeper solubility–pressure slopes, so more dissolves at the same partial pressure.
- 碳酸饮料装瓶时在 1.5–2.0 atm 的 $\ce{CO2}$ 分压下达到高溶解度；开盖后分压骤降至近 0 atm，溶解度降低导致气泡逸出。  Soda stays saturated under 1.5–2.0 atm $\ce{CO2}$ headspace; opening drops $P_{\ce{CO2}}$ to ~0 atm, lowering solubility and causing bubbling.
![Henry](../../attachments/image.jpeg)
- 来源与回链 / Sources & backlink：[[attachments/Lecture+32+PLA.pdf]]；[[journal/2025-11-08]]

## 完整/净离子方程式 / Complete and Net Ionic Reactions
- 写法步骤 / How to write:
  - 将强电解质写成离子形式；分子物质、弱电解质、气体和沉淀保持分子形式。  Write strong electrolytes as ions; keep molecular species, weak electrolytes, gases, and precipitates intact.
  - 约去旁观离子，得到净离子方程式。  Cancel spectator ions to obtain the net ionic equation.
- 示例（沉淀反应）/ Example (precipitation):
  - 分子方程 / Molecular: $\ce{BaCl2(aq) + Na2SO4(aq) -> BaSO4(s) + 2 NaCl(aq)}$
  - 完整离子 / Complete ionic: $\ce{Ba^{2+}(aq) + 2 Cl^{-}(aq) + 2 Na^{+}(aq) + SO4^{2-}(aq) -> BaSO4(s) + 2 Na^{+}(aq) + 2 Cl^{-}(aq)}$
  - 净离子 / Net ionic: $\ce{Ba^{2+}(aq) + SO4^{2-}(aq) -> BaSO4(s)}$
- 来源与回链 / Sources & backlink：[[attachments/Lecture 33 PLA.pdf]]；[[journal/2025-11-11]]

## 来源 / Sources
- [[attachments/Lecture_31_PLA.pdf]]（导入自 Downloads；配套文本在 `attachments/Lecture_31_PLA.txt`）。  [[attachments/Lecture_31_PLA.pdf]] imported from Downloads; text extracted to `attachments/Lecture_31_PLA.txt`.
- [[journal/2025-10-31]]
- [[journal/2025-11-03]]
- [[attachments/Lecture+32+PLA.pdf]]
- [[journal/2025-11-08]]
- [[attachments/Lecture 33 PLA.pdf]]
- [[journal/2025-11-11]]

[//begin]: # "Autogenerated link references for markdown compatibility"
[Chemistry/6.Intermolecular_Forces/intermolecular_forces]: ../6.Intermolecular_Forces/intermolecular_forces.md "分子间作用力（IMFs）/ Intermolecular Forces (Lecture 19, CHEM 110B)"
[Chemistry/8.Gases/gases_and_kmt]: ../8.Gases/gases_and_kmt.md "气体与动理论 / Gases and Kinetic Molecular Theory"
[Chemistry/1.Atom_and_Mole/mass_percentage_calculations]: ../1.Atom_and_Mole/mass_percentage_calculations.md "元素质量百分比计算 / Mass Percentage Calculations"
[Chemistry/1.Atom_and_Mole/mole_concept]: ../1.Atom_and_Mole/mole_concept.md "5. 摩尔概念 / The Concept of Mole"
[Chemistry/7.Biological_Macromolecules/protein_structure_highlights]: ../7.Biological_Macromolecules/protein_structure_highlights.md "蛋白质结构要点 / Protein Structure Highlights"
[attachments/Lecture_31_PLA.pdf]: ../../attachments/Lecture_31_PLA.pdf "Lecture_31_PLA.pdf"
[journal/2025-10-31]: ../../journal/2025-10-31.md "2025-10-31"
[journal/2025-11-03]: ../../journal/2025-11-03.md "2025-11-03"
[//end]: # "Autogenerated link references"
