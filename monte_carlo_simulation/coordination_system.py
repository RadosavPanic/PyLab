import matplotlib.pyplot as plot


def create_coordination_system(x_range, y_range, title="Coordination system", slope=None, areas=None):
    """
    :param x_range: tuple with min-max values for x-axis
    :param y_range: tuple with min-max values for y-axis
    :param title: title used for coordination system
    :param slope: 2 tuples with slopes used to form U-shape in coordination system
    :param areas: individual areas and sum of areas for display in form of dots
    :return:
    """

    # destructuring min-max values from a tuple
    x_min, x_max = x_range
    y_min, y_max = y_range

    # background creation
    plot.figure(figsize=(6, 6), facecolor="white", edgecolor="black")
    plot.grid(True, linestyle="--", alpha=0.6)

    # drawing x and y axis
    plot.axvline(0, color='black', linewidth=0.5)
    plot.axhline(0, color="black", linewidth=0.5)

    # setup of x and y limits
    plot.xlim(x_min, x_max)
    plot.ylim(y_min, y_max)

    # setup ticks for x and y
    plot.xticks(range(x_min, x_max + 1))
    plot.yticks(range(y_min, y_max + 1))

    # setup text for lines of coord system
    for i in range(x_min, x_max + 1):
        if i != 0:
            plot.text(i + 0.1, 0.2, str(i), color='black')
    for i in range(y_min, y_max + 1):
        plot.text(0.2, i + 0.1, str(i), color="black")

    # setup of title and height above coord system
    plot.title(title, y=1.09)

    # creation of slope for first and second quadrant
    if slope:
        x_slope1, y_slope1, text1 = slope[0]
        x_slope2, y_slope2, text2 = slope[1]
        plot.scatter(x_slope1, y_slope1, label=text1, color="red")
        plot.scatter(x_slope2, y_slope2, label=text2, color="green")
        if areas:
            area1, area2, areas_sum = areas
            plot.scatter(-0.05, area1, label=f'area 1 = {area1}', color='blue')
            plot.scatter(0.05, area2, label=f'area 2 = {area2}', color='purple')
            plot.scatter(0, areas_sum, label=f'areas sum = {areas_sum}', color='orange')
        plot.legend()
        plot.show()
