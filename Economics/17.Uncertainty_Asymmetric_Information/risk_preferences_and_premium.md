# 风险偏好与风险溢价 / Risk Preferences and Risk Premium

## 效用与期望效用 / Utility & Expected Utility
- 例函数 / Example: $U(m)=\sqrt{m}$（钱数 $m$），体现边际效用递减（曲线凹）。  Concave $U(m)=\sqrt{m}$ captures diminishing marginal utility of money.
- 期望效用 / Expected utility: $EU=\sum_i p_i\,U(m_i)$。  Probability-weighted utility.
- 对比示例 / Options compared（基于 $U(m)=\sqrt{m}$）:
  - A：确定 \$80 → $EU\approx8.94$。  Sure \$80.
  - B：50% \$150 / 50% \$50 → $EU\approx9.66$。  50–50 gamble.
  - C：20% \$250 / 80% \$0 → $EU\approx3.16$。  20% high payoff, 80% zero.
- 选择解读 / Interpretation: 选 A 表示风险厌恶；选 C 表示风险寻求；风险中性通常选与 EV 最大的方案。  Choosing A implies risk-averse; choosing C implies risk-seeking; risk-neutral tends to pick highest EV.

## 风险偏好类型 / Risk Attitudes
- 风险厌恶 / Risk-averse: 偏好确定额而非同等 EV 赌局，效用凹；Risk premium > 0。  Prefers certainty; concave $U$; $RP>0$.
- 风险中性 / Risk-neutral: 只看 EV，效用近线性；Risk premium = 0。  Indifferent at equal EV; linear $U$; $RP=0$.
- 风险寻求 / Risk-seeking: 偏好冒险，效用凸；Risk premium < 0。  Prefers gambles; convex $U$; $RP<0$.

## 确定等价与风险溢价 / Certainty Equivalent & Risk Premium
- 确定等价物 $CE$：满足 $U(CE)=EU$ 的确定金额。  Solve $U(CE)=EU$ to find certainty equivalent.
- 风险溢价 $RP$：$RP=EV-CE$；厌恶者 $RP>0$ 愿为避险让利，中性 $RP=0$，寻求者 $RP<0$ 愿付费冒险。  $RP=EV-CE$; averse pay to avoid risk, neutral zero, seekers pay to take risk.
- 简算示例 / Example (option B above, $EV=100$): $EU\approx9.66 \Rightarrow CE\approx93.3$，$RP\approx6.7$。  For option B, $CE\approx93.3$, so $RP\approx6.7$.

## 关联 / Related
- 期望值：[[Economics/17.Uncertainty_Asymmetric_Information/expected_value]]  
- 效用与消费选择：[[Economics/6.Household_Behavior_Consumer_Choice/utility_and_consumer_choice]]

来源 / Source：[[journal/2025-11-13]]
