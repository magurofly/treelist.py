# treelist

`TreeList` は平衡二分探索木の一種である RBST (Randomized Binary Search Tree) を使って実装されたリストです。
`list` のようなインタフェースを持ち、ランダムアクセス、挿入、削除などが対数時間で可能です。

## 競技プログラミングでの利用

1 ファイルで定義されているため、 treelist/list.py の内容をそのままコピー・貼り付けすることができます。

## 機能

### 初期化

- `TreeList()`: 空のリストを生成します
- `TreeList(iterable)`: `iterable` の内容で初期化されたリストを生成します

### 操作

`a` を `TreeList` のインスタンスとします。また、 `n` を `len(a)` とします。

- 以下の操作は O(1) でできます
  - `len(a)`: 要素数を取得します
  - `a.clear()`: 空にします
- 以下の操作は O(log n) でできます
  - 取得
    - `a[i]`: `i` 番目の要素を取得します
      - `i < 0` のとき、 `n - i` 番目の要素を取得します
      - 範囲外のインデックスを指定したとき、 `IndexError` が発生します
    - `a.leftmost(p)`: 条件 `p` が単調と仮定し、 `p(self[i])` を満たす最初のインデックス `i` を返します
    - `a.bisect(x)`: `a` がソートされていると仮定し、 `x` をソート順を保ったまま挿入できるインデックスを返します
    - `a.bisect_left(x)`: `a` がソートされていると仮定し、 `self[i] >= x` となる最初のインデックス `i` を返します
    - `a.bisect_right(x)`: `a` がソートされていると仮定し、 `self[i] > x` となる最初のインデックス `i` を返します
  - 挿入
    - `a.unshift(x)`: `x` を先頭に追加します
    - `a.append(x)`: `x` を末尾に追加します
    - `a.insert(i, x)`: `x` を `i` 番目の要素の直前に挿入します
      - `i < 0` のとき、 `n - i` 番目の要素の直前に挿入します
      - 範囲外のインデックスを指定したとき、 `IndexError` が発生します
  - 削除
    - `a.shift()`: 先頭の要素を削除して返します
      - `a` が空のとき、 `IndexError` が発生します
    - `a.shift(m)`: 先頭の要素 `m` 個を削除して `TreeList` として返します
      - `n < m` のとき、 `IndexError` が発生します
    - `a.pop()`: 末尾の要素を削除して返します
      - `a` が空のとき、 `IndexError` が発生します
    - `a.pop(m)`: 末尾の要素 `m` 個を削除して `TreeList` として返します
      - `n < m` のとき、 `IndexError` が発生します
    - `a.remove_at(i)`: `i` 番目の要素を削除して返します
      - `i < 0` のとき、 `n - i` 番目の要素を削除して返します
      - 範囲外のインデックスを指定したとき、 `IndexError` が発生します
    - `a.remove_range(l, r)`: `l` 番目から `r` 番目より前の要素を削除し、 `TreeList` として返します
      - 範囲外のインデックスを指定したとき、 `IndexError` が発生します
- 以下の操作は O(n log n) でできます
  - `a.extend(xs)`: `xs` に含まれる要素を末尾にすべて追加します
  - `a.insert_all(i, xs)`: `xs` に含まれる要素を `i` 番目の要素の前にすべて追加します
  - `a.sort()`: `a` をソートします
- 以下の操作は O(n) でできます
  - `a.copy()`: `a` をコピーします（浅いコピー）
  - `x in a`: `a` に `x` が含まれるか判定します
  - `a.count(x)`: `a` に `x` が含まれる個数を返します
  - `a.index(x)`: `x` が存在する最初のインデックスを返します
    - `a` に `x` が含まれないとき、 `ValueError` が発生します
  - `a.remove(x)`: `a` から `x` と等しい要素をすべて削除します
  - `a.remove_if(p)`: 条件 `p` を満たす要素をすべて削除します
