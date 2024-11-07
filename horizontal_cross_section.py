import numpy as np
import matplotlib.pyplot as plt

"""Horizontal Cross-section Area"""
def euclidean_distance(point1, point2):
    """ Calculate the Euclidean distance between two points """
    return np.sqrt((point1[0] - point2[0]) ** 2 + 
                (point1[1] - point2[1]) ** 2 + 
                (point1[2] - point2[2]) ** 2)

def cayley_menger_area_3points(a, c):
    # Define the three vertices
    points = [
        (a, 0, c),
        (a, 0, -c),
        (0, 0, 0)
    ]
    
    # Construct the distance matrix
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
    area_squared = ((-1) ** (n + 1) / (2 ** (n-2) * (np.math.factorial(n-2) ** 2))) * determinant
    if area_squared < 0:
        area_squared = 0  # Handle potential negative values caused by floating-point precision errors.
    area = np.sqrt(area_squared)
    
    return area
Hareas_array = []

if __name__ == "__main__":
    # Iterate over all combinations of a and c in the range [0, 50] with a step size of 5
    a_values, c_values, areas = [], [], []
    step = 5
    for a in range(0, 51, step):
        for c in range(0, 51, step):
            area = cayley_menger_area_3points(a, c)
            Hareas_array.append(area)
            a_values.append(a)
            c_values.append(c)
            areas.append(area)

    # Plot the area as a function of the parameters
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    sc = ax.scatter(a_values, c_values, areas, c=areas, cmap='viridis')
    ax.set_xlabel('a')
    ax.set_ylabel('c')
    ax.set_zlabel('Area')
    plt.colorbar(sc, label='Triangle Area')

    plt.title('Area of Triangle Formed by (a,0,c), (a,0,-c), and (0,0,0) for Different a, c Values')
    plt.show()
