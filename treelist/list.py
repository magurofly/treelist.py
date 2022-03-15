# TreeList
# License: CC0 1.0 Universal
# ご自由に使用、改変、再配布していただいて構いません

class TreeList:
    """
    トップダウン RBST で実装されたリスト

    計算量において、簡潔さのために `len(self)` を n と表記する
    """

    def __init__(self, it = None):
        """
        新しい `TreeList` を作成する
        `it` に iterable な値を指定できる
        """
        self.root = it if type(it) is self.Node else self.Node.build(it) if it else None

    def append(self, x):
        """
        末尾に `x` を追加する
        計算量 O(log n)
        """
        self.insert(len(self), x)

    def unshift(self, x):
        """
        先頭に `x` を追加する
        計算量 O(log n)
        """
        self.insert(0, x)

    def extend(self, it):
        """
        `it` を末尾に追加する
        計算量 O(len(it) log(n + len(it)))
        """
        if not it: return
        node = it if type(it) is self.Node else self.Node.build(it)
        self.root = self.Node.merge(self.root, it)

    def insert(self, i: int, x):
        """
        `i` 番目の要素の前に `x` を挿入する
        計算量 O(log n)
        """
        assert -len(self) <= i < len(self)
        if i < 0: i += len(self)
        if i >= len(self): raise IndexError()
        (left, right) = self.Node.split(self.root, i)
        node = self.Node.merge(self.Node(x), right)
        self.root = self.Node.merge(left, node)

    def insert_all(self, i: int, xs):
        """
        `i` 番目の要素の前に `xs` に含まれる要素をすべて挿入する
        計算量 O(log n + len(xs))
        """
        assert -len(self) <= i < len(self)
        if i < 0: i += len(self)
        if i >= len(self): raise IndexError()
        node = xs if type(xs) is self.Node else self.Node.build(xs)
        if not node: return
        (left, right) = self.Node.split(self.root, i)
        node = self.Node.merge(node, right)
        self.root = self.Node.merge(left, node)

    def pop(self, n: int = None):
        """
        末尾から要素を削除し、削除した要素を返す
        `n` を指定すると、末尾から `n` 個の要素を削除し、それらを `TreeList` として返す
        """
        l = len(self)
        if n is None:
            if l < 1: raise IndexError("pop from empty list")
            if self.root: return self.remove_at(l - 1)
        else:
            assert 0 <= n <= len(self)
            if l < n: raise IndexError("pop index out of range")
            return self.remove_range(l - n, l)
    
    def shift(self, n: int = None):
        """
        先頭から要素を削除し、削除した要素を返す
        `n` を指定すると、先頭から `n` 個の要素を削除し、それらを `TreeList` として返す
        """
        l = len(self)
        if n is None:
            if l < 1: raise IndexError("shift from empty list")
            if self.root: return self.remove_at(0)
        else:
            assert 0 <= n <= len(self)
            if l < n: raise IndexError("shift index out of range")
            return self.remove_range(0, n)

    def remove(self, x):
        """
        `x` を削除する
        計算量 O(n)
        """
        self.remove_if(lambda y: x == y)
    
    def remove_if(self, p):
        """
        条件 `p` を満たす要素をすべて削除する
        """
        self.root = self.Node.build([x for x in self if p(x)])

    def remove_at(self, i: int):
        """
        `i` 番目の要素を削除する
        計算量 O(log n)
        """
        assert -len(self) <= i < len(self)
        if i < 0: i += len(self)
        if i >= len(self): raise IndexError()
        removed = self.remove_range(i, i + 1)
        return removed.root.value

    def remove_range(self, l: int, r: int):
        """
        `l` 番目以上 `r` 番目未満の要素を削除し、それらを `TreeList` として返す
        計算量 O(log n)
        """
        if l < 0: l += len(self)
        if r < 0: r += len(self)
        assert 0 <= l <= r <= len(self)
        if not (0 <= l <= r <= len(self)): raise IndexError()
        if l == r: return TreeList()
        (left, mid) = self.Node.split(self.root, l)
        (mid, right) = self.Node.split(mid, r - l)
        self.root = self.Node.merge(left, right)
        return TreeList(mid)

    def clear(self):
        self.root = None

    def copy(self):
        return TreeList(self.Node.copy(self.root))

    def count(self, x):
        """
        `x` の個数を数える
        計算量 O(n)
        """
        c = 0
        for y in self:
            if x == y: c += 1
        return c
    
    def index(self, x):
        """
        `x` が存在する最初のインデックスを返す
        計算量 O(n)
        """
        for i, y in enumerate(self):
            if x == y: return i
        raise ValueError()

    def bisect(self, x):
        """
        `self` がソート済みの時、ソートされた順序を保ったまま `x` を挿入できる点を見つける
        計算量 O(log n)
        """
        return self.bisect_left(x)

    def bisect_left(self, x):
        """
        `self` がソート済みの時、ソートされた順序を保ったまま `x` を挿入できる最も左の点を見つける
        計算量 O(log n)
        """
        return self.leftmost(lambda y: y >= x)

    def bisect_right(self, x):
        """
        `self` がソート済みの時、ソートされた順序を保ったまま `x` を挿入できる最も右の点を見つける
        計算量 O(log n)
        """
        return self.leftmost(lambda y: y > x)

    def leftmost(self, p):
        """
        条件 `p` を満たす最初の要素のインデックスを返す
        そのような要素が存在しなければ `len(self)` を返す
        
        前提条件 `i < j` かつ `p(self[i]) and not p(self[j])` となる `(i, j)` が存在しない
        計算量 O(log n)
        """
        return self.Node.leftmost(self.root, p)
    
    def sort(self):
        """
        `self` をソートする
        計算量 O(n log n)
        """
        self.root = self.Node.build(sorted(self))

    def __len__(self):
        """
        要素数を取得する
        計算量 O(1)
        """
        return self.root.len if self.root else 0

    def __getitem__(self, i):
        """
        `i` 番目の要素を取得する
        計算量 O(log n)
        """
        assert 0 <= i < len(self)
        if i < 0: i += len(self)
        if i >= len(self): raise IndexError()
        return self.root.at(i).value
    
    def __contains__(self, x):
        """
        `x` が存在するかどうかを返す
        計算量 O(n)
        """
        for y in self:
            if x == y: return True
        return False

    # `self` と `other` を連結する
    def __add__(self, other):
        res = self.copy()
        res.extend(other)
        return res

    # イテレータ
    def __iter__(self):
        it = self.Iter()
        it.append(self.root)
        return it
    
    def __repr__(self):
        reprs = []
        for x in self:
            reprs.append(repr(x))
        return 'TreeList[' + ', '.join(reprs) + ']'

    class Node:
        def __init__(self, x):
            self.value = x
            self.len = 1
            self.left = self.right = None

        @classmethod
        def build(Self, it, l = 0, r = None):
            if not r: r = len(it)
            if l == r: return None
            if l + 1 >= r: return Self(it[l])
            return Self.merge(Self.build(it, l, (l + r) >> 1), Self.build(it, (l + r) >> 1, r))

        @classmethod
        def copy(Self, node):
            if not node: return None
            copied = Self(node.value)
            copied.left = Self.copy(node.left)
            copied.right = Self.copy(node.right)
            copied.len = node.len
            return copied

        @classmethod
        def merge(Self, l, r):
            if not l: return r
            if not r: return l
            if l._xor128() % (l.len + r.len) < l.len:
                l.right = Self.merge(l.right, r)
                l._update()
                return l
            else:
                r.left = Self.merge(l, r.left)
                r._update()
                return r

        def split(self, at: int):
            if not self: return (None, None)
            assert 0 <= at <= self.len
            if at == 0: return (None, self)
            llen = 0
            if self.left:
                llen = self.left.len
                if at <= llen:
                    (l, r) = self.left.split(at)
                    self.left = r
                    self._update()
                    return (l, self)
            if not self.right: return (self, None)
            (l, r) = self.right.split(at - llen - 1)
            self.right = l
            self._update()
            return (self, r)
        
        def at(self, index: int):
            if not self: return None
            llen = 0
            if self.left:
                llen = self.left.len
                if index < llen: return self.left.at(index)
            if index == llen: return self
            return self.right.at(index - llen - 1)
        
        def leftmost(self, p):
            if not self: return 0
            if p(self.value):
                return self.left.leftmost(p) if self.left else 0
            llen = self.left.len if self.left else 0
            ridx = self.right.leftmost(p) if self.right else 0
            return llen + 1 + ridx

        # XorShift
        _x = 123456789
        _y = 362436069
        _z = 521288629
        _w = 88675123
        @classmethod
        def _xor128(Self):
            t = Self._x ^ (Self._x << 1)
            Self._x = Self._y
            Self._y = Self._z
            Self._z = Self._w
            Self._w = (Self._w ^ (Self._w >> 19)) ^ (t ^ (t >> 8))
            return Self._w
        
        def _update(self):
            self.len = 1 + (self.left.len if self.left else 0) + (self.right.len if self.right else 0)

    class Iter:
        def __init__(self):
            self._stack = []
        
        def append(self, node):
            while node:
                self._stack.append(node)
                node = node.left

        def __next__(self):
            if not self._stack: raise StopIteration()
            node = self._stack.pop()
            self.append(node.right)
            return node.value