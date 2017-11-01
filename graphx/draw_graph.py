import matplotlib.pyplot as plt
import matplotlib.pylab as pl

def draw_net(adj_mat):
    import networkx as nx
    g = nx.Graph()
    num = len(adj_mat)
    for i in range(num):
        for j in range(num):
            if adj_mat[i][j] == 1 and j < i:
                g.add_edge(i, j)
    plt.figure("visual network")
    ax1 = plt.subplot(211)  # 在图表2中创建子图1
    ax2 = plt.subplot(212)  # 在图表2中创建子图2
    plt.sca(ax1)  # 选择图表2的子图1
    nx.draw_networkx(g, pos=nx.random_layout(g), node_size=100, edge_color='b', font_size=8)
    # nx.draw(g, with_labels=True, node_size=200, font_size=10)
    plt.sca(ax2)  # 选择图表2的子图2
    nx.draw_networkx(g, pos=nx.circular_layout(g), node_size=100, edge_color='b', font_size=8)
    plt.show()

def draw_degree_distribution(degree_hist):
    x = range(len(degree_hist))
    y = [i / int(sum(degree_hist)) for i in degree_hist]
    plt.loglog(x, y, color='blue', linewidth=2, marker='o')
    plt.title('Degree Distribution')
    plt.ylabel('Probability')
    plt.xlabel('Degree')
    plt.show()

# def draw_robustness(f, S, l):
#     plt.figure("visual network")
#     ax1 = plt.subplot(211)  # 在图表2中创建子图1
#     ax2 = plt.subplot(212)  # 在图表2中创建子图2
#     plt.sca(ax1)  # 选择图表2的子图1
#     plt.plot(f, S, color='red', linewidth=2, marker='o')
#     plt.ylabel('S')
#     # nx.draw(g, with_labels=True, node_size=200, font_size=10)
#     plt.sca(ax2)  # 选择图表2的子图2
#     plt.plot(f, l, color='blue', linewidth=2, marker='o')
#     plt.xlabel('f')
#     plt.ylabel('l')
#     plt.show()
#     return

def draw_robustness(f, S, l, f_r, S_r, l_r):
    plt.figure("network_attack")
    ax1 = plt.subplot(221)  # 在图表2中创建子图1
    ax2 = plt.subplot(223)
    ax3 = plt.subplot(222)
    ax4 = plt.subplot(224)
    plt.sca(ax1)  # 选择图表2的子图1
    plt.title('intentional')
    plt.plot(f, S, color='red', linewidth=2, marker='o')
    plt.ylabel('S')
    # nx.draw(g, with_labels=True, node_size=200, font_size=10)
    plt.sca(ax2)  # 选择图表2的子图2
    plt.plot(f, l, color='red', linewidth=2, marker='o')
    plt.xlabel('f')
    plt.ylabel('l')
    plt.sca(ax3)
    plt.plot(f_r, S_r, color='blue', linewidth=2, marker='o')
    plt.title('random')
    # nx.draw(g, with_labels=True, node_size=200, font_size=10)
    plt.sca(ax4)
    plt.plot(f_r, l_r, color='blue', linewidth=2, marker='o')
    plt.xlabel('f')
    plt.show()
    plt.close()

def draw_degree_hist(degrees):
    x = list(degrees.values())
    pl.hist(x, bins=50)
    pl.show()

def plot_node_degree(degrees):
    x = list(degrees.keys())
    y = list(degrees.values())
    plt.plot(x, y, color='blue', marker='o')
    plt.show()