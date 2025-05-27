from typing import List


def calculate_z(
    x_list: List[float], y_list: List[float], c: complex, max_iter: int
) -> List[int]:
    """Calculate output list using Julia update rule"""
    # set output as a list of zeros
    total_elements = len(x_list) * len(y_list)
    output = [0] * total_elements

    for i, y in enumerate(y_list): #2000 time loop
        for j, x in enumerate(x_list): #2000 time loop
            z = complex(x, y) #z=0

            n = 0  #use abs to calc 복수소
            while abs(z) < 2 and n < max_iter:  #since cannot loop infinity, we loop max iterartion
                z = z * z + c #if z>2 then 발산,  then it will consider in julia set
                n += 1

            output[i * len(y_list) + j] = n #[실수부, 호수부]

    return output


