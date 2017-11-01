import xlrd as xd


def load_data(fileName, sheet):
    workbook = xd.open_workbook(fileName)
    datasheet = workbook.sheets()[sheet]
    return datasheet


def get_matrix(m, n):
    return [[0 for i in range(n)] for j in range(m)]


def make_mat(datasheet):
    nrows = datasheet.nrows
    ncols = datasheet.ncols
    adj_mat = get_matrix(nrows - 1, ncols - 1)
    for i in range(1, nrows):
        for j in range(1, ncols):
            cell = str(datasheet.cell_value(i, j))
            if cell == 'y':
                adj_mat[i - 1][j - 1] = 1
            else:
                adj_mat[i - 1][j - 1] = 0
    return adj_mat


def make_set_mat(filename):
    import numpy as np
    n = 1200000
    mat = np.zeros((n, n))
    with open(filename, 'r') as f:
        for line in f:
            cols = line.strip().split('\t')
            mat[int(cols[0]) - 1][int(cols[1]) - 1] = 1
            mat[int(cols[1]) - 1][int(cols[0]) - 1] = 1
    return mat


def set_node_mat(node_map, node, node_list):
    '''
    Adjacent list to adjacent matrix
    :param node_map:
    :param node:
    :param node_list:
    :return: Adjacent matrix
    '''
    for x, y, val in node_list:
        node_map[node.index(x)][node.index(y)] = node_map[node.index(y)][node.index(x)] = val
