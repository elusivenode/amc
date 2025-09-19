import os
from pathlib import Path

mpl_cache_dir = Path(__file__).parent / ".mplconfig"
mpl_cache_dir.mkdir(exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(mpl_cache_dir))

import matplotlib.pyplot as plt

# Compose each equation as mathtext so LaTeX is not required locally.
equations = [
    r"$e^x = 1 + \frac{x}{1!} + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$",
    r"$\cos(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots$",
    r"$\sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots$",
    r"$e^{ix} = 1 + \frac{ix}{1!} + \frac{(ix)^2}{2!} + \frac{(ix)^3}{3!} + \cdots$",
    r"$= \left(1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots\right) + i\left(x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots\right)$",
    r"$e^{ix} = \cos(x) + i\sin(x)$",
    r"$e^{i\pi} = \cos(\pi) + i\sin(\pi) = -1$",
    r"$e^{i\pi} + 1 = 0$",
]

plt.rcParams["font.family"] = "STIXGeneral"


def render_equations(
    output_path: Path,
    background: str,
    text_color: str,
    text_alpha: float = 1.0,
    fontweight: str | int = "normal",
) -> None:
    """Render the Euler derivation with the requested color palette."""

    fig = plt.figure(figsize=(12, 10), facecolor=background)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis("off")
    ax.text(
        0.05,
        0.95,
        "\n\n".join(equations),
        ha="left",
        va="top",
        fontsize=24,
        color=text_color,
        alpha=text_alpha,
        fontweight=fontweight,
    )
    fig.savefig(output_path, dpi=200, facecolor=background, bbox_inches="tight")
    plt.close(fig)


render_equations(
    Path(__file__).with_name("euler_derivation_dark.png"),
    background="black",
    text_color="white",
)

render_equations(
    Path(__file__).with_name("euler_derivation_light.png"),
    background="white",
    text_color="#111111",
    text_alpha=0.1,
    fontweight=300,
)
