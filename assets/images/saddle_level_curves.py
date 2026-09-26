"""Plot z=x^2-3y^2 and its level curves; run with the repository .venv."""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.lines import Line2D
import numpy as np

font = Path('/usr/share/fonts/noto-cjk/NotoSansCJK-Regular.ttc')
if font.exists():
    font_manager.fontManager.addfont(str(font))
    plt.rcParams['font.family'] = font_manager.FontProperties(fname=str(font)).get_name()
plt.rcParams.update({'font.size': 11, 'axes.unicode_minus': False})
colors = {-6: '#225ea8', -3: '#39a6b5', 0: '#454545', 3: '#e88721', 6: '#c33b39'}
fig = plt.figure(figsize=(14, 7.5), facecolor='white')
ax = fig.add_subplot(121)
surface = fig.add_subplot(122, projection='3d')
fig.suptitle(r'$f(x,y)=x^2-3y^2$', fontsize=23, y=.97)
ax.set_title('等高线图 / Contour map', pad=16)
surface.set_title('三维马鞍面 / Saddle surface', pad=18)
x = np.linspace(-3.5, 3.5, 100)
y = np.linspace(-2.3, 2.3, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 - 3*Y**2
surface.plot_surface(X, Y, Z, color='#b9c9d3', alpha=.28,
                     edgecolor='none', rcount=45, ccount=45)
surface.plot_wireframe(X, Y, Z, rstride=10, cstride=10,
                       color='#78909c', linewidth=.45, alpha=.4)
for c, color in colors.items():
    for sign in [-1, 1]:
        if c > 0:
            yy = np.linspace(-np.sqrt((3.5**2-c)/3), np.sqrt((3.5**2-c)/3), 500)
            xx = sign*np.sqrt(c+3*yy**2)
        elif c < 0:
            xx = np.linspace(-3.5, 3.5, 500)
            yy = sign*np.sqrt((xx**2-c)/3)
            valid = np.abs(yy) <= 2.3
            xx, yy = xx[valid], yy[valid]
        else:
            xx = np.linspace(-3.5, 3.5, 500)
            yy = sign*xx/np.sqrt(3)
        assert np.allclose(xx**2 - 3*yy**2, c)
        style = '--' if c == 0 else '-'
        ax.plot(xx, yy, color=color, ls=style, lw=2.3)
        surface.plot(xx, yy, np.full_like(xx, c), color=color, ls=style, lw=2.5)
    if c:
        vx, vy = (np.sqrt(c), 0) if c > 0 else (0, np.sqrt(-c/3))
        ax.scatter([vx, -vx], [vy, -vy], color=color, s=24, zorder=5)
        ax.annotate(f'c = {c}', (vx, vy), xytext=(7, 10 if c > 0 else 5),
                    textcoords='offset points', color=color, fontsize=11,
                    bbox=dict(facecolor='white', edgecolor='none', alpha=.85, pad=1))
ax.text(-3.3, -2.13, r'$c=0:\ y=\pm x/\sqrt{3}$', fontsize=12,
        bbox=dict(facecolor='white', edgecolor='none', alpha=.9))
ax.axhline(0, color='#9da8af', lw=.7, zorder=0)
ax.axvline(0, color='#9da8af', lw=.7, zorder=0)
ax.set(xlim=(-3.5, 3.5), ylim=(-2.3, 2.3), xlabel='$x$', ylabel='$y$')
ax.set_aspect('equal')
ax.grid(alpha=.18)
for spine in ax.spines.values():
    spine.set_color('#c6cdd2')
surface.set(xlim=(-3.5, 3.5), ylim=(-2.3, 2.3), zlim=(-16, 13),
            xlabel='$x$', ylabel='$y$', zlabel='$z$')
surface.view_init(elev=27, azim=-58)
surface.set_box_aspect((1, 1, .85))
surface.tick_params(labelsize=9)
handles = [Line2D([0], [0], color=color, lw=2.5,
                  ls='--' if c == 0 else '-', label=f'c = {c}') for c, color in colors.items()]
fig.legend(handles=handles, loc='lower center', bbox_to_anchor=(.5, .10),
           ncol=5, frameon=False)
fig.text(.5, .055, '正高度：左右开口；负高度：上下开口；零高度：相交直线。', ha='center')
fig.text(.5, .02, 'Positive: left/right; negative: up/down; zero: intersecting lines. Same colors indicate the same height.',
         ha='center', fontsize=10, color='#425563')
fig.subplots_adjust(left=.055, right=.95, top=.85, bottom=.23, wspace=.19)
fig.savefig(Path(__file__).with_suffix('.png'), dpi=180, facecolor='white')
plt.close(fig)
