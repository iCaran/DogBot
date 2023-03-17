class body:
    def plot(ax):
        # body
        ax.quiver(-249.75, -126.25, 44, 499.5, 0, 0, arrow_length_ratio=0)
        ax.quiver(249.75, -126.25, 44, 0, 252.5, 0, arrow_length_ratio=0)
        ax.quiver(249.75, 126.25, 44, -499.5, 0, 0, arrow_length_ratio=0)
        ax.quiver(-249.75, 126.25, 44, 0, -252.5, 0, arrow_length_ratio=0)

        # shoulder
        ax.quiver(-249.75, -126.25, 44, -51, 0, 0, arrow_length_ratio=0)
        ax.quiver(-300.75, -126.25, 44, 0, -34.5, 0, arrow_length_ratio=0)

        ax.quiver(249.75, -126.25, 44, 51, 0, 0, arrow_length_ratio=0)
        ax.quiver(300.75, -126.25, 44, 0, -34.5, 0, arrow_length_ratio=0)

        ax.quiver(-249.75, 126.25, 44, -51, 0, 0, arrow_length_ratio=0)
        ax.quiver(-300.75, 126.25, 44, 0, 34.5, 0, arrow_length_ratio=0)

        ax.quiver(249.75, 126.25, 44, 51, 0, 0, arrow_length_ratio=0)
        ax.quiver(300.75, 126.25, 44, 0, 34.5, 0, arrow_length_ratio=0)