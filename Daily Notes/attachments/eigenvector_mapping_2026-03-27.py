"""
Generate a clean 2D vector diagram for the 2026-03-27 journal note.

The plot shows the matrix
    A = [[-4, 5],
         [10, 1]]
and the two eigen-directions used in class:
    u = [1, 2],   Au = [6, 12] = 6u
    w = [-1, 1],  Aw = [9, -9] = -9w
"""

from __future__ import annotations

import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/codex-matplotlib-config")
Path(os.environ["MPLCONFIGDIR"]).mkdir(parents=True, exist_ok=True)

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch


SCRIPT_DIR = Path(__file__).resolve().parent
OUT_PATH = SCRIPT_DIR / "eigenvector_mapping_2026-03-27.png"


def draw_vector(ax, vec, color, label, *, lw=2.4, alpha=1.0, linestyle="-", text_offset=(0.2, 0.2)):
    """Draw a vector from the origin with a label near the tip."""
    x, y = vec
    arrow = FancyArrowPatch(
        (0, 0),
        (x, y),
        arrowstyle="-|>",
        mutation_scale=14,
        linewidth=lw,
        color=color,
        alpha=alpha,
        linestyle=linestyle,
        shrinkA=0,
        shrinkB=0,
    )
    ax.add_patch(arrow)
    ax.text(
        x + text_offset[0],
        y + text_offset[1],
        label,
        color=color,
        fontsize=10,
        weight="bold",
    )


def draw_eigenline(ax, direction, color, label, x_span=(-10, 10), *, linestyle="--"):
    """Draw the full eigenspace line through the origin."""
    direction = np.asarray(direction, dtype=float)
    direction = direction / np.linalg.norm(direction)
    t = np.array(x_span, dtype=float)
    pts = np.outer(t, direction)
    ax.plot(pts[:, 0], pts[:, 1], color=color, linestyle=linestyle, linewidth=1.8, alpha=0.75)
    ax.text(
        pts[1, 0] * 0.8,
        pts[1, 1] * 0.8,
        label,
        color=color,
        fontsize=10,
        weight="bold",
        ha="left",
        va="bottom",
    )


def main(out_path: Path = OUT_PATH) -> Path:
    A = np.array([[-4, 5], [10, 1]], dtype=float)
    u = np.array([1, 2], dtype=float)
    w = np.array([-1, 1], dtype=float)

    Au = A @ u
    Aw = A @ w

    # Sanity checks from the lecture.
    assert np.allclose(Au, 6 * u)
    assert np.allclose(Aw, -9 * w)

    plt.figure(figsize=(8.2, 7.2), dpi=180)
    ax = plt.gca()
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(-11, 11)
    ax.set_ylim(-11, 13)
    ax.set_xticks(np.arange(-10, 11, 2))
    ax.set_yticks(np.arange(-10, 13, 2))
    ax.grid(True, alpha=0.18, linewidth=0.8)
    ax.axhline(0, color="black", linewidth=1.0)
    ax.axvline(0, color="black", linewidth=1.0)

    # Eigen-directions.
    draw_eigenline(ax, u, "#d62728", "eigenline, λ = 6", x_span=(-10, 10))
    draw_eigenline(ax, w, "#1f77b4", "eigenline, λ = -9", x_span=(-10, 10))

    # Original vectors and their images.
    draw_vector(ax, u, "#b22222", "u = [1, 2]", lw=2.2, alpha=0.65, text_offset=(0.15, 0.25))
    draw_vector(ax, Au, "#d62728", "Au = [6, 12]", lw=3.0, alpha=0.95, text_offset=(0.15, 0.25))
    draw_vector(ax, w, "#3778bf", "w = [-1, 1]", lw=2.2, alpha=0.65, text_offset=(0.15, 0.1))
    draw_vector(ax, Aw, "#1f77b4", "Aw = [9, -9]", lw=3.0, alpha=0.95, text_offset=(0.15, -0.35))

    # Matrix summary and key relation.
    ax.text(
        0.02,
        0.98,
        "A = [[-4, 5], [10, 1]]\nA v = λ v",
        transform=ax.transAxes,
        fontsize=11,
        va="top",
        ha="left",
        bbox=dict(boxstyle="round,pad=0.35", facecolor="white", edgecolor="#777777", alpha=0.9),
    )
    ax.text(
        0.98,
        0.02,
        "u maps to 6u\nw maps to -9w",
        transform=ax.transAxes,
        fontsize=10,
        va="bottom",
        ha="right",
        color="#333333",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="#cccccc", alpha=0.85),
    )

    ax.set_xlabel("x")
    ax.set_ylabel("y", rotation=0)
    ax.yaxis.set_label_coords(-0.04, 1.01)
    ax.set_title("Eigenvectors and images for the classroom matrix", fontsize=13, pad=12)

    plt.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path, bbox_inches="tight")
    plt.close()
    return out_path


if __name__ == "__main__":
    path = main()
    print(f"Saved: {path}")
