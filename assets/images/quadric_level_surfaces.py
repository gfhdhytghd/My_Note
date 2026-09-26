"""Generate the level-surface figures used in the September 18 notes."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent
plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})


def panels(title, limit):
    fig = plt.figure(figsize=(13, 4.8), layout="constrained")
    fig.suptitle(title, fontsize=19)
    axes = [fig.add_subplot(1, 3, i + 1, projection="3d") for i in range(3)]
    for ax in axes:
        ax.set(xlim=(-limit, limit), ylim=(-limit, limit), zlim=(-limit, limit),
               xlabel="$x$", ylabel="$y$", zlabel="$z$")
        ax.set_box_aspect((1, 1, 1))
        ax.view_init(elev=23, azim=-55)
        ax.set_xticks([-limit, 0, limit])
        ax.set_yticks([-limit, 0, limit])
        ax.set_zticks([-limit, 0, limit])
    return fig, axes


def surface(ax, x, y, z, color):
    ax.plot_surface(x, y, z, color=color, alpha=0.88, rstride=3, cstride=4,
                    linewidth=0.25, edgecolor=(1, 1, 1, 0.3), shade=True)


theta = np.linspace(0, 2 * np.pi, 97)
fig, axes = panels(r"Level surfaces: $x^2+y^2-z^2=c$", 3)
for ax, c, name, color in zip(
    axes, [1, 0, -1], ["One-sheet hyperboloid", "Double cone", "Two-sheet hyperboloid"],
    ["#287eb0", "#dc9635", "#8c63b6"],
):
    ax.set_title(f"$c={c}$\n{name}")
    # Plot halves separately to preserve the cone apex and two-sheet gap.
    for sign in [-1, 1]:
        zline = sign * np.linspace(1 if c < 0 else 0, 2.7, 70)
        t, z = np.meshgrid(theta, zline)
        r = np.sqrt(np.maximum(z * z + c, 0))
        x, y = r * np.cos(t), r * np.sin(t)
        assert np.allclose(x*x + y*y - z*z, c)
        surface(ax, x, y, z, color)
    if c == 1:
        ax.plot(np.cos(theta), np.sin(theta), np.zeros_like(theta), color="#163f60", lw=2)
    elif c == -1:
        ax.scatter([0, 0], [0, 0], [-1, 1], color="#4e276d", s=22)
fig.savefig(OUT / "hyperboloid_level_surfaces.png", dpi=180)
plt.close(fig)

fig, axes = panels(r"Level sets: $x^2+y^2+z^2=c$", 1.5)
t, p = np.meshgrid(theta, np.linspace(0, np.pi, 73))
x, y, z = np.sin(p)*np.cos(t), np.sin(p)*np.sin(t), np.cos(p)
assert np.allclose(x*x + y*y + z*z, 1)
surface(axes[0], x, y, z, "#369c8b")
axes[0].set_title("$c=1$\nSphere (radius 1)")
axes[1].scatter([0], [0], [0], s=65, color="#dc9635")
axes[1].set_title("$c=0$\nSingle point: the origin")
axes[2].set_title("$c=-1$\nEmpty set: no real points")
axes[2].text2D(0.5, 0.5, "No surface", transform=axes[2].transAxes,
               ha="center", color="#777777", fontsize=13)
fig.savefig(OUT / "sphere_level_surfaces.png", dpi=180)
plt.close(fig)
