import random
from copy import deepcopy

import graphx.draw_graph as dg


class Graph:
    def __init__(self, adj_mat=[], node_list=[]):
        self.adj_mat = adj_mat  # adjacent matrix of graph
        self.node_list = node_list  # int or string
        # self.node_num = nodeNum
        # self.edge_num = edgeNum
        self.node_num = self.node_num()
        self.edge_num = self.edge_num()

    def node_num(self):
        if self.adj_mat is []:
            return 0
        self.node_num = len(self.adj_mat)
        return self.node_num

    def edge_num(self):
        if self.adj_mat is []:
            return 0
        edgeNum = 0
        for i in range(self.node_num):
            for j in range(self.node_num):
                if self.adj_mat[i][j] == 1:
                    edgeNum += 1
        return edgeNum/2

    def insert_node(self):
        for i in range(self.node_num):
            self.adj_mat[i].append(0)
        self.node_num += 1
        ls = [0] * self.node_num
        self.adj_mat.append(ls)

    def delete_node(self, index):
        for i in range(self.node_num):
            if self.adj_mat[i][index] == 1:
                self.adj_mat[i][index] = 0
                self.edge_num -= 1
            if self.adj_mat[index][i] == 1:
                self.adj_mat[index][i] = 0
                self.edge_num -= 1

    def add_edge(self, x, y, directed=1):
        if self.adj_mat[x][y] == 0:
            self.adj_mat[x][y] = 1
            self.edge_num += 1
        if self.adj_mat[y][x] is 0 and directed is 0:
            self.adj_mat[y][x] = 1

    def remove_edge(self, x, y):
        if self.adj_mat[x][y] == 1:
            self.adj_mat[x][y] = 0
            self.edge_num -= 1

    def bfs_search(self):
        def BFS(self, i):
            visited[i] = 1
            for k in range(self.node_num):
                if self.adj_mat[i][k] == 1 and visited[k] == 0:
                    BFS(self, k)

        visited = [0] * self.node_num
        for i in range(self.node_num):
            if visited[i] is 0:
                BFS(self, i)

    def dfs_search(self):
        def DFS(self, i, queue=[], paths=[]):
            queue.append(i)
            visited[i] = 1
            if len(queue) != 0:
                w = queue.pop(0)
                for k in range(self.node_num):
                    if self.adj_mat[w][k] is 1 and visited[k] is 0:
                        paths += [i]
                        DFS(self, k, queue, paths)

        visited = [0] * self.node_num
        queue = []
        paths = []
        for i in range(self.node_num):
            if visited[i] is 0:
                DFS(self, i, queue, paths)
        return paths

    # ======================================== #
    #  The property of path
    # ======================================== #
    # def dfs_path(self, start):
    #     '''
    #     DFS of single source
    #     :param start:
    #     :return:
    #     '''
    #     paths = [-1 for i in range(self.node_num)]
    #     visited = [0] * self.node_num
    #     queue = []
    #
    #     index = start - 1
    #     node = Node(index, 0)
    #     visited[index] = 1
    #     queue.append(node)
    #     while len(queue) > 0:
    #         cur_node = queue.pop(0)
    #         for j in range(self.node_num):
    #             if self.adj_mat[cur_node.id][j] == 1 and visited[j] == 0:
    #                 visited[j] = 1
    #                 cnode = Node(j, cur_node.level + 1)
    #                 paths[j] = cnode.level
    #                 queue.append(cnode)
    #     return paths

    def ave_shortest_path(self):
        total = 0
        num_path = 0
        subgraph, max_size = largest_subgraph(self.adj_mat)
        clone_mat = deepcopy(self.adj_mat)
        for i in range(len(subgraph)):
            if subgraph[i] is 0:
                mark_removed(clone_mat, i)
        for i in range(self.node_num):
            paths = dfs_path(clone_mat, i + 1)
            for j in range(i + 1, len(paths)):
                if paths[j] > 0:
                    total += paths[j]
                    num_path += 1
        if num_path == 0:
            return 0
        return float(total) / num_path

    def bool_connected(self):
        """
        To judge whether it is a connected or not
        :return: Boolean value
        """
        # paths = self.dfs_path(1)
        # for x in paths:
        #     if x is -1:
        #         return False
        # return True
        paths = self.dfs_search()
        print("paths: " + str(paths))
        print(len(paths))
        if len(paths) == self.node_num:
            return True
        else:
            return False

    def shortest_path(self, node1, node2):
        paths = self.dfs_path(node1)
        return paths[node2 - 1]

    # ======================================== #
    #  The property of degree
    # ======================================== #
    def node_degree(self, node):
        degree = 0
        for i in range(self.node_num):
            if self.adj_mat[node][i] == 1:
                degree += 1
        return degree

    def average_degree(self):
        sum = 0
        nodeNum = self.node_num
        for i in range(nodeNum):
            sum += self.node_degree(i)
        return sum / nodeNum

    def distribution_of_degree(self):
        results = {}
        for i in range(self.node_num):
            degree = self.node_degree(i)
            results[degree] += 1
        return results

    def distribution_of_node_degree(self):
        results = {}
        nodeNum = self.node_num
        for i in range(nodeNum):
            results[i] = self.node_degree(i)
        return results

    def max_degree(self):
        degrees = self.distribution_of_node_degree()
        return max(degrees.values())

    def max_degree_node(self):
        degrees = self.distribution_of_node_degree()
        node = 0
        max = -1
        for k, v in degrees.items():
            if v > max:
                node, max = k, v
        return node

    def degree_hist(self):
        deg_distri = self.distribution_of_node_degree()
        print(deg_distri)
        deglist = list(deg_distri.values())

        dmax = max(deglist) + 1
        freq = [0 for i in range(dmax)]
        for v in deglist:
            freq[v] += 1
        return freq

    # ======================================== #
    #  The property of clustering coefficient
    # ======================================== #
    def neighbors(self, node):
        '''
        Get the neighbors of a node
        :param node:
        :return: neighbors
        '''
        neighbors = []
        for x in range(self.node_num):
            if self.adj_mat[node][x] == 1:
                neighbors.append(x)
        return neighbors

    def bool_neighbor(self, node1, node2):
        """
        To judge whether they is a neighbor or not
        :param node1:
        :param node2:
        :return: Boolean value
        """
        return self.adj_mat[node1][node2] == 1

    def edges_of_neighbors(self, node):
        neighbors = self.neighbors(node)
        edges = 0
        for i in range(len(neighbors)):
            for j in range(len(neighbors)):
                if i < j:
                    node1 = neighbors[i]
                    node2 = neighbors[j]
                    if self.bool_neighbor(node1, node2):
                        edges += 1
        return edges

    def clustering(self):
        def max_edges_of_neighbors(node):
            degree = self.node_degree(node)
            return degree * (degree - 1) / 2

        clusterc = {}
        for i in range(self.node_num):
            edges_of_neighbors = self.edges_of_neighbors(i)
            max_edges = max_edges_of_neighbors(i)
            if max_edges == 0:
                clusterc[i] = 0.0
            else:
                clusterc[i] = float(edges_of_neighbors) / max_edges
        return clusterc

    def average_clustering(self):
        clusterc = self.clustering()
        sum = 0
        for i in range(len(clusterc)):
            sum += clusterc[i]
        return float(sum) / self.node_num

        # def shotest_path(self, node1, node2):

    # ======================================== #
    #  The property of coreness
    # ======================================== #
    def nodes_coreness(self):
        def mat_degrees(adj_mat):
            degrees = [0 for i in range(len(adj_mat))]
            for i in range(len(adj_mat)):
                degree = 0
                for j in range(len(adj_mat[0])):
                    if adj_mat[i][j] == 1:
                        degree += 1
                degrees[i] = degree
            return degrees

        corenesses = [0 for i in range(self.node_num)]
        max_degree = self.max_degree()
        clone_mat = deepcopy(self.adj_mat)
        k = 0
        while k <= max_degree:
            marked = False
            degrees = mat_degrees(clone_mat)
            for i in range(len(degrees)):
                if clone_mat[i][i] != -1:
                    if degrees[i] < k:
                        clone_mat = mark_removed(clone_mat, i)
                        corenesses[i] = k - 1
                        marked = True
                        break
                    else:
                        corenesses[i] = k
            if marked:
                k -= 1
            if max(degrees) == 0:
                break
            k += 1
        return corenesses

    def node_coreness(self, node):
        corenesses = self.nodes_coreness()
        return corenesses[node - 1]

    def coreness(self):
        corenesses = self.nodes_coreness()
        return max(corenesses)

    def draw_degree_distribution(self):
        degree_hist = self.degree_hist()
        print(degree_hist)
        dg.draw_degree_distribution(degree_hist)


class Node:
    def __init__(self, id=0, level=0):
        self.id = id
        self.level = level


def mark_removed(adj_mat, index):
    for i in range(len(adj_mat)):
        # if adj_mat[i][index] == 1:
        adj_mat[i][index] = -1
        # if adj_mat[index][i] == 1:
        adj_mat[index][i] = -1
    return adj_mat


def is_marked(adj_mat, index):
    return adj_mat[index][index] is -1


def is_all_marked(adj_mat):
    for i in range(len((adj_mat))):
        if adj_mat[i][i] != -1:
            return False
    return True


def sub_graph(adj_mat):
    start_node = 0
    node_num = len(adj_mat)
    for i in range(node_num):
        if not is_marked(adj_mat, i):
            start_node = i
            break
    visited = [0] * node_num
    queue = []

    visited[start_node] = 1
    queue.append(start_node)
    while len(queue) > 0:
        cur_node = queue.pop(0)
        for j in range(node_num):
            if adj_mat[cur_node][j] is 1 and visited[j] is 0:
                visited[j] = 1
                queue.append(j)
    return visited


def connected_graphs(adj_mat):
    graphs = []
    adj_mat_clone = deepcopy(adj_mat)
    while not is_all_marked(adj_mat_clone):
        sub = sub_graph(adj_mat_clone)
        for i in range(len(sub)):
            if sub[i] is 1:
                mark_removed(adj_mat_clone, i)
        graphs.append(sub)
    return graphs


def largest_subgraph(adj_mat):
    sub_graphs = connected_graphs(adj_mat)
    max_size = 0
    ind = -1
    for i in range(len(sub_graphs)):
        size = sum(sub_graphs[i])
        if size > max_size:
            ind = i
            max_size = size
    return sub_graphs[ind], max_size


def dfs_path(adj_mat, start):
    '''
    DFS of single source
    :param start:
    :return:
    '''
    nodeNum = len(adj_mat)
    paths = [-1 for i in range(nodeNum)]
    visited = [0] * nodeNum
    queue = []

    index = start - 1
    node = Node(index, 0)
    visited[index] = 1
    queue.append(node)
    while len(queue) > 0:
        cur_node = queue.pop(0)
        for j in range(nodeNum):
            if adj_mat[cur_node.id][j] == 1 and visited[j] == 0:
                visited[j] = 1
                cnode = Node(j, cur_node.level + 1)
                paths[j] = cnode.level
                queue.append(cnode)
    return paths


def intentional_attack(adj_mat):
    adj_mat_clone = deepcopy(adj_mat)
    node_num = len(adj_mat_clone)
    S, l, f = [], [], []
    subgraph, max_subgraph_size = largest_subgraph(adj_mat_clone)
    start_ave_path = Graph(adj_mat_clone).ave_shortest_path()
    S.append(1.0)
    l.append(start_ave_path)
    f.append(0.0)
    for i in range(node_num):
        temp = Graph(adj_mat_clone)
        attack_node = temp.max_degree_node()
        mark_removed(adj_mat_clone, attack_node)
        subgraph, subgraph_size = largest_subgraph(adj_mat_clone)
        ave_path = temp.ave_shortest_path()
        S.append(float(subgraph_size)/max_subgraph_size)
        l.append(ave_path)
        f.append(float(i+1)/node_num)
    return f, S, l


def random_attack(adj_mat):
    adj_mat_clone = deepcopy(adj_mat)
    node_num = len(adj_mat_clone)
    li = [i for i in range(node_num)]
    queue = sample(li, node_num)
    S, l, f = [], [], []
    subgraph, max_subgraph_size = largest_subgraph(adj_mat_clone)
    start_ave_path = Graph(adj_mat_clone).ave_shortest_path()
    S.append(1.0)
    l.append(start_ave_path)
    f.append(0.0)
    for i in range(node_num-1):
        temp = Graph(adj_mat_clone)
        attack_node = queue.pop(0)
        mark_removed(adj_mat_clone, attack_node)
        subgraph, subgraph_size = largest_subgraph(adj_mat_clone)
        ave_path = temp.ave_shortest_path()
        S.append(float(subgraph_size)/max_subgraph_size)
        l.append(ave_path)
        f.append(float(i+1)/node_num)
    return f, S, l


def sample(li, num):
    max_ = len(li)
    res = []
    for i in range(num):
        t = random.randint(i, max_ - 1)
        res.append(li[t])
        li[i], li[t] = li[t], li[i]
    return res
