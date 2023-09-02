import sys
from collections import deque

input = sys.stdin.readline

TC = int(input())
queue = deque()
# dq = deque(maxlen=n)
# 작은 공간을 가지고 이중 연결리스트로 되어있다.

for i in range(TC):
    queue.append(i+1)

while(len(queue) !=1):
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])

# double ended List
# deque 이중 연결리스트 아래와 같이 구현되어 있다.

# typedef struct BLOCK {
#     struct BLOCK *leftlink;
#     PyObject *data[BLOCKLEN];
#     struct BLOCK *rightlink;
# } block;
#
# +
# −typedef struct {
#     PyObject_VAR_HEAD
#     block *leftblock;
#     block *rightblock;
#     Py_ssize_t leftindex;       /* 0 <= leftindex < BLOCKLEN */
#     Py_ssize_t rightindex;      /* 0 <= rightindex < BLOCKLEN */
#     size_t state;               /* incremented whenever the indices move */
#     Py_ssize_t maxlen;
#     PyObject *weakreflist;
# } dequeobject;

# 3항 연산자
# elif cmd[0] == "pop_front":
# print(dq.popleft() if dq else -1)