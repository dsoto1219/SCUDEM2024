import numpy as np
import matplotlib.pyplot as plt


# Calculating the Volume
def euclidean_distance(point1, point2):
    """ Calculate the Euclidean distance between two points """
    return np.sqrt((point1[0] - point2[0]) ** 2 + 
                   (point1[1] - point2[1]) ** 2 + 
                   (point1[2] - point2[2]) ** 2)


def cayley_menger_volume(a, b, c):
    # Define the coordinates of five vertices
    points = [
        (a, b, c),
        (a, b, -c),
        (a, -b, -c),
        (a, -b, c),
        (0, 0, 0)
    ]
    
    # Construct the distance matrix
    n = len(points)
    D = np.ones((n+1, n+1))
    
    # Calculate the square of the distance matrix
    for i in range(n):
        for j in range(n):
            if i != j:
                D[i+1, j+1] = euclidean_distance(points[i], points[j]) ** 2
            else:
                D[i+1, j+1] = 0  # The diagonal elements are zero
    
    # Calculate the Cayley-Menger determinant
    determinant = np.linalg.det(D)
    
    # Calculate the volume of the tetrahedron based on the determinant
    volume_squared = ((-1) ** (n + 1) / (2 ** (n-2) * (np.math.factorial(n-1) ** 2))) * determinant
    if volume_squared < 0:
        volume_squared = 0  # Handle potential negative values caused by floating-point precision errors
    volume = np.sqrt(volume_squared)
    
    return volume


if __name__ == "__main__":
    # Iterate over all combinations of a, b, and c in the range [0, 50] with a step size of 5
    a_values, b_values, c_values, volumes = [], [], [], []
    step = 5
    for a in range(0, 51, step):
        for b in range(0, 51, step):
            for c in range(0, 51, step):
                volume = cayley_menger_volume(a, b, c)
                a_values.append(a)
                b_values.append(b)
                c_values.append(c)
                volumes.append(volume)

    # Create a 3D plot.
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    sc = ax.scatter(a_values, b_values, c_values, c=volumes, cmap='viridis')
    ax.set_xlabel('a')
    ax.set_ylabel('b')
    ax.set_zlabel('c')
    plt.colorbar(sc, label='Volume')

    plt.title('Cayley-Menger Determinant Volume for Different a, b, c Values')
    plt.show()