# 寡头与博弈论 / Oligopoly & Game Theory

## 概览 / Overview
- Examples: Smartphones, Airlines, Lowe's & Home Depot → **oligopolies**
  例子：智能手机、航空业、Lowe's 与 Home Depot 属于**寡头**。
- Firms in oligopolies react strategically to **price** and **output** changes.
  寡头企业会对**价格**与**产量**变化做出**战略性反应**。

## 博弈论定义 / Game Theory Definition
- Economic study of how agents interact in strategic situations.
  研究主体在战略情境中如何互动的经济学。

## 适用场景 / Applications
- Oligopoly, War, Chess, Strategic communication.
  寡头、战争、国际象棋、战略性沟通。

## 市场结构比较 / Market Structure Comparison
| Perfect Competition / 完全竞争 | Oligopoly / 寡头 | Monopoly / 垄断 |
|-|-|-|
| Many sellers / 众多卖方 | A few sellers / 少数卖方 | One seller / 单一卖方 |
| Identical products / 同质产品 | Differentiated products / 差异化产品 | A unique product (no close substitutes) / 独特产品（无近似替代品） |
| Free entry/exit / 自由进出 | Significant barriers to entry / 显著进入壁垒 | Very high barriers to entry / 极高进入壁垒 |

## 博弈三要素 / Game Components

- **Players**: Must be two or more / **参与者**：至少两名

- **Strategies**: A completely contingent plan of action. Payoffs depend on all players' strategies / **策略**：完全的行动计划。收益取决于所有参与者的策略
  - In this case: Can think of a strategy as the actions of players / 在此情况下：可将策略视为参与者的行动
  - Note: If you take more advanced game theory, this simplified definition will be incorrect / 注意：如果学习更高级的博弈论，这个简化定义将不正确
- **Payoffs**: Outcomes, typically represented by "utility" (how happy someone is) / **收益**：结果，通常以“效用”度量（反映满意度/偏好）。


### 详细要素 / Detailed Components
- Players: must be two or more.
  参与者：至少两名。
- Strategies: a completely contingent plan of action; payoffs depend on all players' strategies.
  策略：完全的行动计划；收益取决于所有参与者的策略。
- In this note we may think of a strategy as the actions of players; advanced game theory uses a stricter definition.
  在此可将“策略”视为参与者采取的行动；更高阶博弈论中“策略”定义更为严格。
- Payoffs: outcomes, typically represented by utility (how happy someone is).
  收益：结果，通常以“效用”表征（反映满意度/偏好）。

## 占优策略 / Dominant Strategy
- A strategy that yields the best outcome for a player regardless of what others play.
  不论他人如何行动都能带来该参与者最佳结果的策略。
- Note: A dominant strategy need not maximize total (joint) payoffs.
  注意：占优策略不一定带来整体（联合）最优。

## 纳什均衡 / Nash Equilibrium
- A strategy profile such that, given others' strategies, no player can unilaterally deviate and do better.
  在既定他人策略下，任何参与者都无法通过单方面偏离而使自身更好。
- Equivalent view: a Nash equilibrium is where all players best respond to each other.
  等价表述：各参与者彼此给出最优回应（相互的最佳反应）。
- Stability: given others' strategies, no profitable unilateral deviation exists.
  稳定性：在他人策略既定时不存在单方有利的偏离。
- Notation: describe equilibria by strategies, not payoffs; e.g., (High, High).
  书写：用“策略”而非“收益/利润”描述均衡；例如：(高产量, 高产量)。
- Example (10/22 matrix game): each firm has a dominant strategy of High Output; (High, High) is the unique Nash equilibrium.
  示例（见 [[journal/2025-10-22]] 的矩阵博弈）：两家企业的占优策略均为高产量；(高产量, 高产量) 为唯一纳什均衡。

## 双寡头产量博弈矩阵 / Duopoly Output Game Matrix
- This is a matrix (strategic-form) game; both players choose simultaneously.
  这是一个矩阵（战略式）博弈，双方同时选择。
- Players: Firm 1 (row) and Firm 2 (column).
  参与者：企业1（行玩家）与企业2（列玩家）。
- Strategies: High output, Low output.
  策略：高产量、低产量。
- Payoffs in boxes: first = Firm 1; second = Firm 2.
  矩阵中的收益：第一个数为企业1，第二个数为企业2。

|                         | **Firm 2: High Output** | **Firm 2: Low Output** |
| ----------------------- | ----------------------- | ---------------------- |
| **Firm 1: High Output** | (1, 1)                  | (15, −5)               |
| **Firm 1: Low Output**  | (−5, 15)                | (10, 10)               |

**分析 / Analysis：** If both choose Low Output, they mimic a monopoly and split profits. If one chooses High while the other chooses Low, the High‑output firm earns more because price remains higher. If both choose High, price and profits are lower than when both choose Low.
分析：若双方都选低产量，表现如同垄断并平分利润；若一高一低，因价格较高，高产量方获利更多；若双方都选高产量，价格与利润均低于双方低产量时。

## 顺序投资博弈 / Sequential Investment Game

- Players A, B, C move sequentially and at each decision node choose between Invest or Leave.
  玩家A、B、C依序行动，在各自节点上选择投资或离开。
- Each investment imposes a cost of 2 on the acting player, so repeated investing accumulates personal costs.
  每次投资会让当前行动者承担2的成本，因此连续投资会累积个人代价。
- Key payoff branches outline the incentives:
  关键节点的收益如下所示：
  - All three invest → (3, 3, 3).
    三人都投资时收益为(3,3,3)。
  - A invests while B leaves → (−2, 2, 0).
    A投资而B离开时收益为(−2,2,0)。
  - A and B invest while C leaves → (−2, −2, 4).
    A与B投资而C离开时收益为(−2,−2,4)。
  - A leaves immediately → (0, 0, 0).
    A立刻离开时收益为(0,0,0)。
- Backward induction predicts the equilibrium (Leave, Leave, Leave) because each player anticipates later deviations and prefers exiting earlier.
  逆向归纳得到均衡(离开,离开,离开)，因为各参与者预期后续偏离因而选择提前退出。

## 博弈类别 / Game Classes

- A zero-sum game keeps total payoffs constant: one player’s gain exactly offsets another player’s loss.
  零和博弈保持总收益恒定：一方所得正好抵消另一方损失。

## 囚徒困境 / Prisoner's Dilemma

|                 | Bob: **Coop** | Bob: **Defect** |
| --------------- | ------------- | --------------- |
| **Ann: Coop**   | **3, 3**      | **0, 4**        |
| **Ann: Defect** | **4, 0**      | **2, 2**        |

- Oligopoly competition mirrors a prisoner’s dilemma: firms have incentives to undercut even though mutual cooperation raises joint profits.
  寡头竞争映射为囚徒困境：即便合作能带来更高的联合利润，各企业仍有削价偏离的激励。
- Prisoner’s dilemmas arise in everyday coordination issues such as standing at concerts, shouting at parties, and holding doors for others.
  囚徒困境常见于日常协调问题，例如演唱会站立、派对上大声说话以及为他人扶门。
- Repeating the prisoner’s dilemma infinitely many times opens room for strategies that reward cooperation and punish deviations.
  将囚徒困境无限重复时，可运用奖惩结合的策略来维持合作并惩罚背离。

### 针锋相对策略 / Tit-for-Tat Strategy

- Start by cooperating in period 1, then copy the opponent’s previous action to sustain trust and discipline deviations.
  第一期先选择合作，之后各期复制对手上一期的选择，以维持互信并约束背离。

### 长期默契合谋 / Tacit Collusion

- In long-run repeated settings, firms can sustain tacit collusion by punishing deviation from cooperative behavior without an explicit agreement.
  在长期重复博弈中，企业可通过惩罚偏离合作的行为来维持默契合谋，而无需明示合约。

---

- 回链 / Backlink：[[journal/2025-10-22]]
- 回链 / Backlink：[[journal/2025-10-29]]
