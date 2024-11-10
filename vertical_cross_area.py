import numpy as np
import matplotlib.pyplot as plt


def euclidean_distance(point1, point2):
    """ Calculate the Euclidean distance between two points """
    return np.sqrt((point1[0] - point2[0]) ** 2 + 
                (point1[1] - point2[1]) ** 2 + 
                (point1[2] - point2[2]) ** 2)


def cayley_menger_area_4points(a, b, c):
    """Calculating Vertical Cross-section Area"""
    # Define the coordinates of the four vertices.
    points = [
        (a, b, c),
        (a, b, -c),
        (a, -b, -c),
        (a, -b, c)
    ]
    
    # Construct the distance matrix.
    n = len(points)
    D = np.ones((n+1, n+1))
    
    # Fill in the square of the distance matrix
    for i in range(n):
        for j in range(n):
            if i != j:
                D[i+1, j+1] = euclidean_distance(points[i], points[j]) ** 2
            else:
                D[i+1, j+1] = 0  # The diagonal elements are zero
    
    # Calculate the Cayley-Menger determinant to find the area
    determinant = np.linalg.det(D)
    area_squared = (((-1) ** (n + 1)) / (2 ** (n-2) * (np.math.factorial(n-2) ** 2))) * determinant
    if area_squared < 0:
        area_squared = 0  # Handle potential negative values caused by floating-point precision errors.
    area = np.sqrt(area_squared)
    
    return area

if __name__ == "__main__":
    areas_array = []
    a_values, b_values, c_values = [], [], []

    # Iterate over all combinations of a, b, and c in the range [0, 50] with a step size of 5.
    a_values, b_values, c_values, areas = [], [], [], []
    step = 5
    for a in range(0, 51, step):
        for b in range(0, 51, step):
            for c in range(0, 51, step):
                area = cayley_menger_area_4points(a, b, c)
                areas_array.append(area)
                a_values.append(a)
                b_values.append(b)
                c_values.append(c)
                areas.append(area)

    # Plot the area of the plane as a function of the parameters.fig = plt.figure(figsize=(10, 8))
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    sc = ax.scatter(a_values, b_values, c_values, c=areas, cmap='inferno')
    ax.set_xlabel('a')
    ax.set_ylabel('b')
    ax.set_zlabel('c')
    plt.colorbar(sc, label='Plane Area')

    plt.title('Area of Plane Formed by Four Points for Different a, b, c Values')
    plt.show()
