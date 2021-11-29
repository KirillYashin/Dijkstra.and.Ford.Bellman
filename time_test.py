from algs import generator, converter, dijkstra, ford_bellman
from time import time
file_1 = open('output1.txt', 'w')
file_2 = open('output2.txt', 'w')
file_3 = open('output3.txt', 'w')
file_4 = open('output4.txt', 'w')
file_5 = open('output5.txt', 'w')
file_6 = open('output6.txt', 'w')
file_7 = open('output7.txt', 'w')

for vertex_count in range(1, 10**4 + 2, 100):
    p = 0.2
    edges = generator(p, vertex_count, 1, 10**6)
    adj_matrix = converter(edges, vertex_count)
    d_start = time()
    d = dijkstra(adj_matrix, 0, vertex_count)
    d_end = time() - d_start
    fb_start = time()
    fb = ford_bellman(edges, 0, vertex_count)
    fb_end = time() - fb_start
    file_1.write(str(d_end) + ' ' + str(fb_end) + ' ' + str(vertex_count) + '\n')
    print(vertex_count, 1)

for vertex_count in range(1, 10**4 + 2, 100):
    p = 0.95
    edges = generator(p, vertex_count, 1, 10**6)
    adj_matrix = converter(edges, vertex_count)
    d_start = time()
    d = dijkstra(adj_matrix, 0, vertex_count)
    d_end = time() - d_start
    fb_start = time()
    fb = ford_bellman(edges, 0, vertex_count)
    fb_end = time() - fb_start
    file_2.write(str(d_end) + ' ' + str(fb_end) + ' ' + str(vertex_count) + '\n')
    print(vertex_count, 2)

for vertex_count in range(1, 10**4 + 2, 100):
    p = 200 / vertex_count
    edges = generator(p, vertex_count, 1, 10**6)
    adj_matrix = converter(edges, vertex_count)
    d_start = time()
    d = dijkstra(adj_matrix, 0, vertex_count)
    d_end = time() - d_start
    fb_start = time()
    fb = ford_bellman(edges, 0, vertex_count)
    fb_end = time() - fb_start
    file_3.write(str(d_end) + ' ' + str(fb_end) + ' ' + str(vertex_count) + '\n')
    print(vertex_count, 3)

for vertex_count in range(1, 10**4 + 2, 100):
    p = 2000 / vertex_count
    edges = generator(p, vertex_count, 1, 10**6)
    adj_matrix = converter(edges, vertex_count)
    d_start = time()
    d = dijkstra(adj_matrix, 0, vertex_count)
    d_end = time() - d_start
    fb_start = time()
    fb = ford_bellman(edges, 0, vertex_count)
    fb_end = time() - fb_start
    file_4.write(str(d_end) + ' ' + str(fb_end) + ' ' + str(vertex_count) + '\n')
    print(vertex_count, 4)

for edges_count in range(0, 10**7 + 1, 10**5):
    p = (2 * edges_count) / (10**8 + 10**4)
    vertex_count = 10**4 + 1
    edges = generator(p, vertex_count, 1, 10**6)
    adj_matrix = converter(edges, vertex_count)
    d_start = time()
    d = dijkstra(adj_matrix, 0, vertex_count)
    d_end = time() - d_start
    fb_start = time()
    fb = ford_bellman(edges, 0, vertex_count)
    fb_end = time() - fb_start
    file_5.write(str(d_end) + ' ' + str(fb_end) + ' ' + str(vertex_count) + '\n')
    print(vertex_count, 5)

for q in range(1, 201, 1):
    p = 0.95
    vertex_count = 10 ** 4 + 1
    edges = generator(p, vertex_count, 1, q)
    adj_matrix = converter(edges, vertex_count)
    d_start = time()
    d = dijkstra(adj_matrix, 0, vertex_count)
    d_end = time() - d_start
    fb_start = time()
    fb = ford_bellman(edges, 0, vertex_count)
    fb_end = time() - fb_start
    file_6.write(str(d_end) + ' ' + str(fb_end) + ' ' + str(vertex_count) + '\n')
    print(vertex_count, 6)

for q in range(1, 201, 1):
    p = 0.2
    vertex_count = 10 ** 4 + 1
    edges = generator(p, vertex_count, 1, q)
    adj_matrix = converter(edges, vertex_count)
    d_start = time()
    d = dijkstra(adj_matrix, 0, vertex_count)
    d_end = time() - d_start
    fb_start = time()
    fb = ford_bellman(edges, 0, vertex_count)
    fb_end = time() - fb_start
    file_7.write(str(d_end) + ' ' + str(fb_end) + ' ' + str(vertex_count) + '\n')
    print(vertex_count, 7)
