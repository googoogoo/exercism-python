class Matrix:
    def __init__(self, matrix_string):
        self.matrix = matrix_string

    def row(self, index):
        rows = []
        for line in self.matrix.splitlines():
            m_rows = [int(x) for x in line.split(' ')]
            rows.append(m_rows)
        k = index - 1
        return rows[k]

    def column(self, index):
        rows = []
        for line in self.matrix.splitlines():
            m_rows = [int(x) for x in line.split(' ')]
            rows.append(m_rows)
        k = index - 1
        col = [position[k] for position in rows]
        return col 
