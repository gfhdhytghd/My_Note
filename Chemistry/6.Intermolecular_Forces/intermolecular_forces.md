# 分子间作用力（IMFs）/ Intermolecular Forces (Lecture 19, CHEM 110B)

## 一、本质 / Nature

- 所有分子间作用力本质上都源自静电相互作用。  
  All intermolecular forces are ultimately electrostatic in origin.
- 库仑定律：  
  Coulomb's law:  
  $$F=k\frac{Q_1Q_2}{r^2}$$
- 影响强度的关键参数：电荷 $Q$、偶极矩 $\mu$、极化率 $\alpha$、距离 $r$。  
  Key determinants: charge $Q$, dipole moment $\mu$, polarizability $\alpha$, separation $r$.
- 实验指示：沸点/熔点越高通常意味着更强的分子间作用力。  
  Empirical indicator: higher boiling/melting point implies stronger IMFs.

## 二、分子可能的“带电特性”/ Molecular Sources of Charge

1) 离子（ion）：具有真实电荷 $Q$  
   Ions with formal charge $Q$  
2) 极性分子（polar molecule）：具有永久偶极矩 $\mu$  
   Polar molecules with permanent dipole $\mu$  
3) 非极性分子（nonpolar molecule）：可被极化，形成瞬时/诱导偶极，能力由 $\alpha$ 决定  
   Nonpolar molecules can be polarized; instantaneous/induced dipoles scale with $\alpha$

> 即便是非极性分子，也会因电子云瞬时偏移产生瞬时偶极；这类相互作用称为伦敦分散力。  
> Even nonpolar molecules form instantaneous dipoles due to electron cloud fluctuations; the interaction is London dispersion.

### 符号说明：偶极矩 μ / Symbol Note: Dipole Moment μ

- 定义：描述分子内电荷分离程度的矢量；在简化二电荷模型下有$\mu=qr$，分子总偶极是各键偶极的矢量和，受构型与对称性强烈影响。  
  Definition: a vector quantifying charge separation; in a simple two‑charge model $\mu=qr$. The molecular dipole is the vector sum of bond dipoles, strongly dependent on geometry and symmetry.
- 单位：德拜（Debye, D）为常用化学单位；$1\,\mathrm{D}=3.336\times10^{-30}\,\mathrm{C\cdot m}$；也可直接用国际单位$\mathrm{C\cdot m}$。  
  Units: Debye (D) is common in chemistry; $1\,\mathrm{D}=3.336\times10^{-30}\,\mathrm{C\cdot m}$. SI unit is $\mathrm{C\cdot m}$.
- 意义：$\mu$越大，偶极相关的分子间作用（如偶极–偶极、离子–偶极）越强；在质量相近的分子中通常体现为更高的沸点。  
  Implication: larger $\mu$ strengthens dipole‑driven IMFs (dipole–dipole, ion–dipole), often yielding higher boiling points among similar‑mass molecules.
- 示例：乙腈的$\mu\approx3.9\,\mathrm{D}$。更多判定见 → [[molecular_polarity]]。  
  Example: acetonitrile has $\mu\approx3.9\,\mathrm{D}$. See [[molecular_polarity]] for determination.

## 三、作用力类型 / Types of IMFs

| 类型 / Type | 参与者 / Participants | 主依赖 / Depends on | 典型特征 / Notes |
| --- | --- | --- | --- |
| 离子–离子 / Ion–Ion | 离子–离子 / ion–ion | $Q$–$Q$ | 最强；晶格能大；高熔沸点  
Strongest; large lattice energies; high Tm/Tb |
| 离子–偶极 / Ion–Dipole | 离子–极性分子 / ion–polar | $Q$–$\mu$ | 溶解过程常见（如盐溶于水）  
Common in solvation (e.g., salts in water) |
| 离子–诱导偶极 / Ion–Induced Dipole | 离子–非极性 / ion–nonpolar | $Q$–$\alpha$ | 电荷使邻近分子极化  
Charge polarizes nearby molecules |
| 偶极–偶极 / Dipole–Dipole | 极性–极性 / polar–polar | $\mu$–$\mu$ | 比离子型弱；取向依赖  
Weaker than ionic; orientation dependent |
| 偶极–诱导偶极 / Dipole–Induced Dipole | 极性–非极性 / polar–nonpolar | $\mu$–$\alpha$ | 永久偶极诱导邻近分子  
Permanent dipole induces neighbor |
| 诱导–诱导（分散）/ Dispersion (London) | 非极性–非极性 / nonpolar–nonpolar | $\alpha$–$\alpha$ | 最弱但普遍存在；随电子数与表面积增大而增强  
Weakest but universal; increases with e− count and surface area |
| 氢键 / Hydrogen Bond | 特殊偶极–偶极 / special dipole–dipole | 方向性强；H–N/O/F | 极强的偶极–偶极；需要 H 与 N/O/F 键连  
Strong, highly directional dipole–dipole; requires H bound to N/O/F |

- 相关：极性来源与判定 → [[molecular_polarity]]；
- 电负性与键类型 → [[electronegativity_and_bond_types]]；
- 概览见 [[chemical_bond_types]]
- Related: polarity origin/judgment → [[molecular_polarity]]; 
- electronegativity/bond types → [[electronegativity_and_bond_types]]; 
- overview in [[chemical_bond_types]].

### 术语注记 / Terminology Note

- “范德华力”通常作广义集合，包含偶极–偶极、偶极–诱导偶极与伦敦分散力（部分教材将氢键视为其中特殊情形，亦有将氢键单独列出）。  
  “van der Waals forces” often serves as an umbrella term encompassing dipole–dipole, dipole–induced dipole, and London dispersion (some texts include hydrogen bonding as a special case; others list it separately).

### 氢键详解 / Hydrogen Bonding

- 定义：当氢原子与高电负性原子 X（常见 X = N, O, F）以共价键相连，H 在另一个富孤对的电负性原子 Y 邻近时形成的强、定向的分子间相互作用，常记作 D–H···A（D 为供体，A 为受体）。  
  Definition: a strong, directional interaction formed when H covalently bound to a highly electronegative atom X (commonly N, O, F) approaches a lone‑pair bearing electronegative atom Y; denoted D–H···A (donor–H···acceptor).
- 几何特征：趋近线性，∠D–H···A 通常 > 150°；H···A 距离短于范德华接触距离；方向性与“配位饱和”特征明显。  
  Geometry: near‑linear with ∠D–H···A typically > 150°; H···A shorter than van der Waals contact; highly directional and saturating.
- 成键条件：
  • 供体（H‑bond donor）：必须含 X–H（X 多为 N/O/F），H 需带显著正电性；酸性越强通常供体越强（如 RCOOH > ROH > RCH3）。  
  • 受体（H‑bond acceptor）：需有可用孤对电子，常见为 N、O；阴离子是很强的受体；S/Cl 等可形成较弱氢键。  
  Requirements: donors require X–H (X = N/O/F) with sufficiently δ+ H; stronger acidity generally increases donor strength. Acceptors need available lone pairs (commonly N, O); anions are strong acceptors; S/Cl give weaker H‑bonds.
- 强度范围：典型分子间氢键约 5–40 kJ·mol⁻¹；带电辅助（如 O–H···O⁻）更强；强于一般偶极–偶极，弱于共价键。  
  Strength: typical intermolecular H‑bonds ~5–40 kJ·mol⁻¹; charge‑assisted can be stronger; stronger than ordinary dipole–dipole but weaker than covalent bonds.
- 物性影响：显著抬升沸点/熔点、增加黏度与表面张力；引发“异常”趋势，如 H2O、HF、NH3 相对其同族氢化物沸点偏高。  
  Properties: elevate boiling/melting points, increase viscosity and surface tension; cause anomalies such as high Tb of H2O, HF, NH3 vs heavier congeners.
- 典型示例：
  • 水：三维氢键网络解释高沸点、冰的低密度与 4 ℃ 密度极大等性质。  
  • 羧酸：易形成头‑尾二聚体 R–COOH···HOOC–R，显著抬升沸点。  
  • 醇 vs 醚 vs 烷烃：R–OH（既可供体又可受体）> R–O–R′（仅受体）> 烷烃（无 HBD/HBA）。  
  Examples: water’s 3D H‑bond network explains high Tb and density anomalies; carboxylic acids form dimers, raising Tb; alcohols (HBD+HBA) > ethers (HBA only) > alkanes (neither).
- 分子内与分子间：分子内氢键可“锁定”构象（如邻位羟基取代的芳香族化合物），影响反应性与光谱；分子间氢键主导聚集与结晶形态。  
  Intra vs inter: intramolecular H‑bonds can lock conformations (e.g., ortho‑hydroxy aromatics), altering reactivity/spectra; intermolecular H‑bonds drive aggregation and crystal packing.
- 生物相关：蛋白质二级结构（α‑螺旋、β‑折叠）与核酸碱基配对本质上由定向氢键网络稳定。  
  Bio relevance: directional H‑bond networks stabilize protein secondary structures (α‑helices, β‑sheets) and nucleic acid base pairing.
- 快速识别：统计 HBD/HBA 数与空间可接近性；供体/受体数量与立体位阻共同决定可形成氢键的数量与强度。  
  Quick screening: count H‑bond donors/acceptors and assess steric accessibility; counts and sterics together set feasible H‑bonding capacity.

## 四、叠加效应 / Additivity

- 同一物质通常同时拥有多种分子间作用力；总体强度为多种作用的综合。  
  A substance typically exhibits multiple IMFs; overall strength is the sum of contributions.
- 例如水：既有氢键也有分散力；生物大分子（如蛋白质）内几乎包含所有类型的相互作用。  
  Example: water has hydrogen bonding and dispersion; biomacromolecules (e.g., proteins) feature nearly all types.

## 五、链长与表面积对分散力 / Chain Length & Surface Area on Dispersion

- 极化率与尺寸 / Polarizability vs size  
  更长的烃链与更大的分子体积通常具有更大的$\alpha$，因此诱导偶极/伦敦分散力更强，沸点随同系物链长上升。  
  Longer chains and larger molecular volume yield larger $\alpha$, strengthening induced dipole/dispersion; boiling points rise along a homologous series.

- 表面积与构型 / Surface area vs conformation  
  线性或伸展构型提供更大的分子接触表面积，从而分散力更强；支化使分子更“紧凑”，接触表面积变小，分散力变弱，沸点降低。  
  Extended/linear shapes maximize contact area, increasing dispersion; branching compacts molecules, reduces contact area, weakens dispersion, and lowers boiling point.

- 异构体比较（示例）/ Isomer trend (example)  
  正戊烷 > 异戊烷 > 新戊烷（分散力与沸点依次减弱/降低）；差异主要源于形状与可接触表面积而非化学组成。  
  n-Pentane > isopentane > neopentane in dispersion strength/boiling point; differences arise from shape and accessible surface area, not composition.

- 相关链接 / Related  
  [[isomerism]] · [[hydrocarbon_nomenclature]]  
  Shape/surface effects often discussed with structural isomers and alkane families.

### 极性与质量的综合 / Polarity and Mass Combined

- 分子间作用力强度与沸点正相关，受两大因素共同影响：分子质量/电子数/表面积（影响极化率与分散力）与分子极性（偶极矩，影响偶极相关作用）。  
  Boiling point correlates with net IMF strength, co‑determined by two levers: molecular mass/electron count/surface area (governing polarizability and dispersion) and molecular polarity (dipole moment, governing dipolar interactions).
- 在质量相近的一组分子中，极性（偶极矩）越大，通常沸点越高；当质量差异显著时，更大的分散力可能主导趋势。  
  For molecules of similar mass, larger dipole moments generally raise boiling points; when masses diverge, stronger dispersion can dominate the trend.
- 示例：乙腈（μ=3.9 D）在相近质量的小分子对比中表现出更高的沸点，说明极性对沸点的提升作用十分显著。  
  Example: acetonitrile (μ=3.9 D) exhibits a higher boiling point among similar‑mass small molecules, highlighting the strong influence of polarity.

## 六、一句话总结 / One‑Line Summary

> 分子间作用力把“分子结构”连接到“物理性质”：结构决定可形成的作用力类型，综合强度决定沸点、溶解性、柔韧性与生物活性等宏观性质。  
> IMFs connect molecular structure to macroscopic properties: structure sets interaction types; net strength governs boiling point, solubility, flexibility, and bioactivity.

## 相关链接 / Related Links

- [[molecular_polarity]] · [[electronegativity_and_bond_types]] · [[chemical_bond_types]]
- 来源 / Source：[[journal/2025-10-14]]
[//begin]: # "Autogenerated link references for markdown compatibility"
[molecular_polarity]: ../4.Chemical_Bonds/molecular_polarity.md "分子极性判断 / Molecular Polarity"
[electronegativity_and_bond_types]: ../4.Chemical_Bonds/electronegativity_and_bond_types.md "电负性与化学键类型 / Electronegativity and Bond Types"
[chemical_bond_types]: ../1.Atom_and_Mole/chemical_bond_types.md "化学键类型 / Chemical Bond Types"
[isomerism]: ../5.Organic_Nomenclature/isomerism.md "同分异构体与几何异构体 / Isomerism and Geometric Isomers"
[hydrocarbon_nomenclature]: ../5.Organic_Nomenclature/hydrocarbon_nomenclature.md "有机物命名：烷/烯/炔 / IUPAC Nomenclature: Alkanes/Alkenes/Alkynes"
[journal/2025-10-14]: ../../journal/2025-10-14.md "2025-10-14"
[//end]: # "Autogenerated link references"
