"""
短期成本曲线与价格线示意图生成脚本 / Script to generate short‑run cost curves diagram

用法 / Usage:
  - 在仓库根目录（已激活 venv，见仓库指南）执行：
      python attachments/firm_sr_diagram_2025-10-13.py
  - 输出 PNG 保存至 `attachments/firm_sr_diagram_2025-10-13.png`

参数说明 / Parameters:
  - 成本函数示意：AVC = a*Q^2 - b*Q + c；ATC = AVC + F/Q；MC = d(AVC*Q)/dQ
  - 价格线：P1、P2、P3 分别对应 D=MR 水平线

备注 / Notes:
  - 本图用于课堂/笔记示意，参数为可视化友好而选取，并非特定行业校准。
  - 可根据需要调整 a,b,c,F 与价格，或添加更多标注（如利润矩形、停产阈值 min(AVC) 等）。
"""

from __future__ import annotations

import os
from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt


@dataclass
class CostParams:
    a: float = 0.06  # 二次项 / quadratic term
    b: float = 0.6   # 一次项 / linear term
    c: float = 5.0   # 常数项 / constant term
    F: float = 8.0   # 固定成本 / fixed cost


@dataclass
class PriceLines:
    P1: float = 7.0
    P2: float = 4.6
    P3: float = 3.0


def generate_diagram(
    out_path: str = "attachments/firm_sr_diagram_2025-10-13.png",
    Q_min: float = 0.1,
    Q_max: float = 12.0,
    n_points: int = 500,
    cost: CostParams = CostParams(),
    price: PriceLines = PriceLines(),
) -> str:
    """生成并保存短期成本曲线图；返回输出路径 / Generate diagram and return path."""
    Q = np.linspace(Q_min, Q_max, n_points)

    # 成本曲线 / Cost curves
    AVC = cost.a * Q ** 2 - cost.b * Q + cost.c
    AFC = cost.F / Q
    ATC = AVC + AFC
    # MC from VC = AVC*Q -> d(AVC*Q)/dQ
    MC = 3 * cost.a * Q ** 2 - 2 * cost.b * Q + cost.c

    # 选择一个代表性价格用于标记 Q*（示例取 P2）/ mark Q* for P2
    P2 = price.P2
    idx2 = int(np.argmin((MC - P2) ** 2))
    Q2 = Q[idx2]

    plt.figure(figsize=(9, 6), dpi=150)
    plt.plot(Q, MC, label="MC", color="#d62728", linewidth=2.2)
    plt.plot(Q, ATC, label="ATC", color="#1f77b4", linewidth=2.0)
    plt.plot(Q, AVC, label="AVC", color="#2ca02c", linewidth=2.0)

    # 价格线 / Price (D=MR) lines
    for P, name, color in [
        (price.P1, "P1", "#9467bd"),
        (price.P2, "P2", "#8c564b"),
        (price.P3, "P3", "#7f7f7f"),
    ]:
        plt.hlines(
            P, Q.min(), Q.max(), colors=color, linestyles="--", linewidth=1.6, label=f"{name}: D=MR"
        )

    # 标注 P2 的最优产量 / mark optimal quantity at P2
    plt.vlines(Q2, 0, P2, colors="#8c564b", linestyles=":", linewidth=1.6)
    plt.scatter([Q2], [P2], color="#8c564b", zorder=5)
    plt.annotate(
        "Q* at MR=MC",
        xy=(Q2, P2),
        xytext=(Q2 + 0.5, P2 + 0.5),
        arrowprops=dict(arrowstyle="->", color="#8c564b"),
        fontsize=9,
    )

    plt.xlim(Q_min, Q_max)
    plt.ylim(0, 20)  # 限制 y 轴范围为 0 到 20
    plt.xlabel("Q (Quantity)")
    plt.ylabel("P, Cost")
    plt.title("Short-run Cost Curves and Price Lines (D=MR)")
    plt.legend(loc="upper right", frameon=False)
    plt.grid(alpha=0.15)

    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    plt.tight_layout()
    plt.savefig(out_path, transparent=False)
    return out_path


if __name__ == "__main__":
    out = generate_diagram()
    print("Saved:", out)

