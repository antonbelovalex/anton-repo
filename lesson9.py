# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных
# подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
import hashlib


def search(s):
    assert len(s) > 0, "Строка не может быть пустой"
    result2 = set()
    result = set()
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            h_subs = hashlib.sha1(s[i:j].encode('utf-8')).hexdigest()
            result2.add(s[i:j])
            result.add(h_subs)
    print(result2)
    return len(result)


s_1 = input("Введите строку: ")
res = search(s_1)-1
print(f"Подстрок найдено: {res}")




# 2. Закодируйте любую строку по алгоритму Хаффмана.

import heapq
from collections import Counter, namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))

    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code


def main():
    s = input("Введите строку: ")
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    for ch in sorted(code):
        print(f"{ch}: {code[ch]}")
    print(encoded)


if __name__ == "__main__":
    main()
