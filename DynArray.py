class DynArray:
    def __init__(self):
        self._size = 0
        self._capacity = 1
        self._num_array = 1
        self._array = []
        self._array.append([0] * 1)
    def __grow(self):
        self._array.append([0] * (self._capacity + 1))
        self._num_array += 1
        self._capacity = 2 * self._capacity + 1
        print('_array expanded from', self._capacity // 2, 'to', self._capacity)
    def __translate(self, pos):
        h = (pos + 1).bit_length() - 1
        return h, (pos + 1) & ~ (-1 << h)
    def print(self):
        h, g = self.__translate(self._size)
        print('[', end = '')
        for i in range(h + 1):
            for j in range(1 << i if i < h else g):
                print((', %d' if i > 0 else '%d') % self._array[i][j], end = '')
        print(']')
    def modify_at(self, val, pos):
        h, g = self.__translate(pos)
        self._array[h][g] = val
    def append(self, val):
        if self._size == self._capacity:
            self.__grow()
        self.modify_at(val, self._size)
        self._size += 1
    def insert_at(self, val, pos):
        if self._size == self._capacity:
            self.__grow()
        h, g = self.__translate(self._size)
        for i in range(self._size, pos, -1):
            if g > 0:
                self._array[h][g] = self._array[h][g-1]
                g -= 1
            else:
                gg = (1 << (h - 1)) - 1
                self._array[h][g] = self._array[h-1][gg]
                h -= 1
                g = gg
        self._size += 1
        self._array[h][g] = val

da = DynArray()
da.print()
for i in range(16):
    da.append(i + 1)
da.print()