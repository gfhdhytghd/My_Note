import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon


def main(out_path: str = "attachments/ramachandran_plot_2025-10-14.png") -> None:
    plt.figure(figsize=(6.8, 5.1), dpi=150)

    # Axes for phi (x) and psi (y)
    ax = plt.gca()
    ax.set_xlim(-180, 180)
    ax.set_ylim(-180, 180)
    ax.set_xlabel("φ", fontsize=11)
    ax.set_ylabel("ψ", fontsize=11, rotation=0)
    ax.yaxis.set_label_coords(-0.06, 1.02)
    ax.set_xticks([-180, -90, 0, 90, 180])
    ax.set_yticks([-180, -90, 0, 90, 180])
    ax.axhline(0, color="black", lw=1)
    ax.axvline(0, color="black", lw=1)

    # Allowed regions (approximate polygons/ellipses)
    # Beta-strand (upper-left) region polygon (roughly around φ~ -120, ψ~ 120)
    beta_poly = np.array([
        [-160, 160],
        [-140, 150],
        [-120, 130],
        [-110, 100],
        [-120, 70],
        [-150, 90],
        [-170, 140],
    ])
    ax.add_patch(Polygon(beta_poly, closed=True, facecolor="#cf6a6a", edgecolor="none", alpha=0.9, label="β-strand"))

    # Right-handed alpha-helix (lower-left quadrant), use an ellipse centered near (-60, -45)
    ahelix = Ellipse(xy=(-60, -45), width=120, height=90, angle=-25, facecolor="#5aa9e6", edgecolor="none", alpha=0.9)
    ax.add_patch(ahelix)

    # Left-handed alpha-helix (upper-right small blob) near (60, 60)
    lhelix = Ellipse(xy=(60, 60), width=35, height=70, angle=-20, facecolor="#61d095", edgecolor="none", alpha=0.9)
    ax.add_patch(lhelix)

    # Optional tiny beta-strand pocket (lower-left extreme) to echo textbook plots
    beta_small = np.array([
        [-175, -170],
        [-165, -175],
        [-150, -175],
        [-170, -160],
    ])
    ax.add_patch(Polygon(beta_small, closed=True, facecolor="#cf6a6a", edgecolor="none", alpha=0.8))

    # Labels
    ax.text(-40, -10, "α-helix", color="white", fontsize=10, weight="bold")
    ax.text(70, 55, "α-helix\n(left-handed)", color="black", fontsize=9)
    ax.text(-155, 140, "β-strand", color="black", fontsize=10, weight="bold")

    # Title
    plt.title("Dihedral (φ and ψ) angles that minimize steric clash are favored", fontsize=11)
    plt.tight_layout()
    plt.savefig(out_path, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    main()

