###################################### ---Q4--- ######################################

import matplotlib.pyplot as plt


def display(image):
    plt.imshow(image, cmap="gist_gray")
    plt.show()


def read_image(pathway):
    try:
        f = open(pathway, "r")
        f.close()
    except FileNotFoundError:
        print("The pathway is not correct")
    else:
        output_image = []
        with open(pathway, "r") as file:
            for line in file:
                to_add = [int(item) for item in line.rstrip("\n").split(" ")]
                output_image.append(to_add)
        return output_image


def edge_detection(image_nested_list, x_matrix, y_matrix):
    """
    The function receives an image represented by a two-dimensional list and runs the border detection
    algorithm on it. The function returns a two-dimensional list of integer values, which represents
    the image after running the algorithm.
    :param image_nested_list: An image represented by a two-dimensional list
    :param x_matrix: The matrix that performs convolution on the x-axis
    :param y_matrix: The matrix that performs convolution on the y-axis
    :return: An image after the convolution
    """
    image = image_nested_list
    matrix_x = []
    matrix_y = []
    matrix = x_matrix
    new_matrix = []
    new_row = []
    value = 0
    rows = 0
    matrix_1 = []
    row_in_matrix = []
    while len(image) > 2:
        for i in range(3):
            row = image[i]
            for u in range(rows, rows + 3):
                pixel = row[u]
                row_in_matrix.append(pixel)
            matrix_1.append(row_in_matrix)
            row_in_matrix = []
        for r in range(3):
            for i in range(3):
                value += matrix[r][i] * matrix_1[r][i]
        new_row.append(value)
        value = 0
        matrix_1 = []
        if rows == len(image[0]) - 3:
            new_matrix.append(new_row)
            new_row = []
            image = image[1:]
            rows = 0
        else:
            rows += 1
        if len(image) < 3:
            if matrix == x_matrix:
                matrix_x = new_matrix
                new_matrix = []
                matrix = y_matrix
                rows = 0
                image = image_nested_list
            elif matrix == y_matrix:
                matrix_y = new_matrix
    new_image = []
    row_in_image = []
    for i in range(len(matrix_x)):
        for u in range(len(matrix_x[0])):
            G = int(((matrix_x[i][u]) ** 2 + (matrix_y[i][u] ** 2)) ** 0.5)
            row_in_image.append(G)
            G = 0
        new_image.append(row_in_image)
        row_in_image = []
    return new_image


################# Tests ####################
SanFrancisco_image = read_image("SanFrancisco.txt")
display(SanFrancisco_image)
x_structure = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
y_structure = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
SanFrancisco_post_ED_image = edge_detection(SanFrancisco_image, x_structure, y_structure)
display(SanFrancisco_post_ED_image)
