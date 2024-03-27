import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter
import random
def prove():
    list1 = [random.random() for _ in range(1000000)]
    list2 = [random.random() for _ in range(1000000)]
    array1 = np.array(list1)
    array2 = np.array(list2)

    start_time = perf_counter()
    result_list = [a * b for a, b in zip(list1, list2)]
    end_time = perf_counter()
    time_list = end_time - start_time

    start_time = perf_counter()
    result_array = np.multiply(array1, array2)
    end_time = perf_counter()
    time_array = end_time - start_time
    if time_array - time_list < 0:
        print('Доказано:)') 

def hist():
    num_bins=50
    lower_bound=10000
    upper_bound=40000
    num_rows=2
    num_cols=1
    figure_width=6
    figure_height=8
    arr = np.genfromtxt('data2.csv', delimiter=',')
    arr = arr[1:]

    Solids = np.int_(arr[:,2])

    fig, (ax1, ax2) = plt.subplots(num_rows, num_cols, figsize=(figure_width, figure_height))
    ax1.hist(Solids, num_bins, (lower_bound, upper_bound))
    ax1.set_title("Гистограмма")
    ax1.grid()

    ax2.hist(Solids, num_bins, (lower_bound, upper_bound), density=True)
    ax2.set_title('Нормализованная гистограмма')
    ax2.grid()

    plt.tight_layout()
    plt.show()
    standard_deviation=np.std(Solids) 
    print('Среднеквадратичное отклонение=', standard_deviation)



def plot3d():
    num_points=20
    num_subplot=111
    xs = np.linspace(-np.pi, np.pi, num_points)
    ys = 1 / xs
    zs = np.sin(xs)

    fig = plt.figure()
    ax = fig.add_subplot(num_subplot, projection='3d')
    ax.plot(xs, ys, zs, marker='x', c='red')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

if __name__ == '__main__':
    #prove()
    #hist()
    plot3d()