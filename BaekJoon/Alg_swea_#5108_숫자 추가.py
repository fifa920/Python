import sys
sys.stdin = open("Alg_swea_#5108_숫자 추가.txt", "r")

class Node:
    def __init__(self,d=0,n=None):
        self.data = d
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

def printList(lst):
    if lst.head is None:
        print(lst.size,'[',']')
    else:
        print(lst.size,'[',end=' ')
        while lst.head.next is not None:
            print(lst.head.data,end= ' ')
            lst.head = lst.head.next
        print(lst.head.data,']')

def insert_val(lst,idx,new):
    if lst.head is None: #빈 배열에 추가
        lst.head = new
        lst.tail = new

    elif idx == 0: #맨 처음에 추가
        new.next = lst.head
        lst.head = new

    elif idx == lst.size: # 맨 끝에 추가
        lst.tail.next = new
        lst.tail = new

    else:   # 중간에 추가
        pre,cur = None,lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next
        new.next = cur
        pre.next = new
    lst.size += 1

def search(lst,idx):
    if lst.head is None:
        return
    else:
        for _ in range(idx):
            lst.head = lst.head.next
        return lst.head.data


T = int(input())

for t in range(1,T+1) :
    N,M,L = map(int, input().split())
    data = list(map(int, input().split()))
    data_list = LinkedList()
    for i in range(len(data)):
        insert_val(data_list, i, Node(data[i]))
    for i in range(M):
        idx, val = map(int, input().split())
        insert_val(data_list, idx, Node(val))
    # printList(data_list)
    result = search(data_list, L)
    print('#{} {}'.format(t, result))
