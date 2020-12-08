

# 1.3 Keeping the last N items
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


with open('somefile.txt') as f:
    for line, prevlines in search(f, 'RUS'):
        for pline in prevlines:
            print(pline)


# another example | bounded deque
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.append(5)
print(q)


# another example | not bounded deque
q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
q.appendleft(4)
print(q)
q.pop()
print(q)
q.popleft()
print(q)
