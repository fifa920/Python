class Node :
    def __init(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0




def addList(lst, arr):


    first = last = Node(arr[0])
    for val in arr[1:]:
        new = Node(val, last)
        last.nex = new
        last = new
    if lst.head is None :
        lst.head, lst.tail = first, last
    else :
        cur = lst.head
        while cur is not None:
            if cur.data > arr[0] : break
            cur = cur.next
        if cur is None : #뒤에 추가
            first.prev = lst.tail
            lst.tail.next = first
            lst.tail = last

        elif cur.prev is None : #앞에 추가
            last.next = lst.head
            lst.head.prev = last
            lst.head = first
        else : #중간에 추가
            prev = cur.prev
            first.prev = prev
            last.next = cur
            prev.next = first
            cur.prev = last
    lst.size += len(arr)

#addLast 함수
# def addList(lst, new):
    # if lst.head is None :
    #     lst.head = lst.tail = new
    # else :
    #     new.prev = lst.tail
    #     #이 2개 순서 바뀌면 안된다.
    #     lst.tail.next = new
    #     lst.tail = new
    # lst.size += 1


def printList(lst):
    if lst.head is None : return
    cur = lst.head
    while cur is not None :
        print(cur.data, end=' ')
        cur = cur.next
    print()
    cur = lst.tail
    while cur is not None :
        print(cur.data, end= ' ')
        cur = cur.prev
    print()

mylist = LinkedList()
arr = [1,3,5,7,9]

for val in arr :
    addList(mylist, Node(val))
printList(mylist)