import matplotlib.pyplot as plt
from math import ceil

class ColorPlotter:
    def __init__(self, hex_colors, cols=10, max_colors=100):
        self.hex_colors = hex_colors[:max_colors]
        self.cols = cols
        self.rows = ceil(len(self.hex_colors) / cols)

    def plot(self):
        fig, ax = plt.subplots(self.rows, self.cols, figsize=(self.cols, self.rows))

        for i in range(self.rows * self.cols):
            row, col = divmod(i, self.cols)
            axis = ax[row, col] if self.rows > 1 else ax[col]

            if i < len(self.hex_colors):
                axis.set_facecolor(self.hex_colors[i])
                axis.set_title(self.hex_colors[i], fontsize=7)
            else:
                axis.set_visible(False)
            axis.set_xticks([])
            axis.set_yticks([])

        plt.tight_layout()
        return fig
