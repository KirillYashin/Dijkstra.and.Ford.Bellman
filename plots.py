import matplotlib.pyplot as plt

mode = int(input('Введите номер желаемого графика (1 - 7)\n'))

if mode == 1:
    with open('output1.txt', 'r') as input_file:
        d_y, fb_y, x = [], [], []
        for line in input_file:
            d_y.append(float(line.split()[0]))
            fb_y.append(float(line.split()[1]))
            x.append(int(line.split()[2]))
    plt.scatter(x, d_y, c='b')
    plt.scatter(x, fb_y, c='r')
    plt.title('3.1 (а), синий - алг. Дийкстры, красный - алг. Форда-Беллмана')
    plt.show()

elif mode == 2:
    with open('output2.txt', 'r') as input_file:
        d_y, fb_y, x = [], [], []
        for line in input_file:
            d_y.append(float(line.split()[0]))
            fb_y.append(float(line.split()[1]))
            x.append(int(line.split()[2]))
    plt.scatter(x, d_y, c='b')
    plt.scatter(x, fb_y, c='r')
    plt.title('3.1 (б), синий - алг. Дийкстры, красный - алг. Форда-Беллмана')
    plt.show()

elif mode == 3:
    with open('output3.txt', 'r') as input_file:
        d_y, fb_y, x = [], [], []
        for line in input_file:
            d_y.append(float(line.split()[0]))
            fb_y.append(float(line.split()[1]))
            x.append(int(line.split()[2]))
    plt.scatter(x, d_y, c='b')
    plt.scatter(x, fb_y, c='r')
    plt.title('3.2 (а), синий - алг. Дийкстры, красный - алг. Форда-Беллмана')
    plt.show()

elif mode == 4:
    with open('output4.txt', 'r') as input_file:
        d_y, fb_y, x = [], [], []
        for line in input_file:
            d_y.append(float(line.split()[0]))
            fb_y.append(float(line.split()[1]))
            x.append(int(line.split()[2]))
    plt.scatter(x, d_y, c='b')
    plt.scatter(x, fb_y, c='r')
    plt.title('3.2 (б), синий - алг. Дийкстры, красный - алг. Форда-Беллмана')
    plt.show()

elif mode == 5:
    with open('output5.txt', 'r') as input_file:
        d_y, fb_y = [], []
        for line in input_file:
            d_y.append(float(line.split()[0]))
            fb_y.append(float(line.split()[1]))
    x = [i for i in range(0, 10 ** 7 + 1, 10 ** 5)]
    plt.scatter(x, d_y, c='b')
    plt.scatter(x, fb_y, c='r')
    plt.title('3.3, синий - алг. Дийкстры, красный - алг. Форда-Беллмана')
    plt.show()

elif mode == 6:
    with open('output6.txt', 'r') as input_file:
        d_y, fb_y = [], []
        for line in input_file:
            d_y.append(float(line.split()[0]))
            fb_y.append(float(line.split()[1]))
    x = [i for i in range(1, 201)]
    plt.scatter(x, d_y, c='b')
    plt.scatter(x, fb_y, c='r')
    plt.title('3.4 (а), синий - алг. Дийкстры, красный - алг. Форда-Беллмана')
    plt.show()

elif mode == 7:
    with open('output7.txt', 'r') as input_file:
        d_y, fb_y = [], []
        for line in input_file:
            d_y.append(float(line.split()[0]))
            fb_y.append(float(line.split()[1]))
    x = [i for i in range(1, 201)]
    plt.scatter(x, d_y, c='b')
    plt.scatter(x, fb_y, c='r')
    plt.title('3.4 (б), синий - алг. Дийкстры, красный - алг. Форда-Беллмана')
    plt.show()