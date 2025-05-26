"""Julia set generator without optional PIL-based image drawing"""

import array
import time
from typing import List

import julia_fn2 as julia_fn_cython
from PIL import Image

# area of complex space to investigate
X1, X2 = -1.8, 1.8 #실수부
Y1, Y2 = -1.8, 1.8 #호수부부
# C = complex(-0.62772, -0.42193)
C = complex(-0.8, 0.156) #based on c value the shape and time of fractal can be different


def show_grey_scale(
    output_raw: List[int], width: int, height: int, max_iterations: int
):
    """Convert list to array, show using PIL"""
    max_iterations = float(max(output_raw))
    scale_factor = float(max_iterations)
    scaled = [int(o / scale_factor * 255) for o in output_raw]

    im = Image.new("L", (width, height))
    im.frombytes(array.array("B", scaled).tobytes(), "raw", "L", 0, -1)
    im.show()


def calc_julia(
    desired_width: int, max_iterations: int, draw_image: bool = False, iters=5
) -> List[int]:
    """
    Create a list of complex co-ordinates (zs) and complex parameters (cs),
    build Julia set and display
    """
    x_step = (X2 - X1) / desired_width
    y_step = (Y2 - Y1) / desired_width
    x_list, y_list = [], []

    ycoord = Y1
    while ycoord < Y2:
        y_list.append(ycoord)
        ycoord += y_step

    xcoord = X1
    while xcoord < X2:
        x_list.append(xcoord)
        xcoord += x_step

    # set width and height to the generated pixel counts
    width, height = len(x_list), len(y_list)

    print(
        f"Total elements: {len(x_list) * len(y_list)}, width: {width}, height: {height}"
    )

    average_time = 0
    for _ in range(iters):
        start_time = time.perf_counter()
        output = julia_fn_cython.calculate_z(x_list, y_list, C, max_iterations)
        end_time = time.perf_counter()
        duration = end_time - start_time
        average_time += duration

    average_time /= iters
    print(f"{julia_fn_cython.calculate_z.__name__} took {average_time} seconds")

    if draw_image:
        show_grey_scale(output, width, height, max_iterations)

    return output


if __name__ == "__main__":
    calc_julia(desired_width=2000, max_iterations=1000, draw_image=True, iters=5)
