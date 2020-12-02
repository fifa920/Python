class Node:

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

mylist = LinkedList()


    def printList(lst) :
        if lst.head is None : return

        cur = lst.head
        print(lst.size, '[', end= ' ')

        while cur.next is not None:
            print(cur.data, end=' ')
            cur = cur.next
        print(']')


    def insertLast(lst, new):
        if lst.head is None :
            lst.head = lst.tail = new
        else :
            lst.tail.next = new
            #추가된 것이 마지막 노드인 것으로 해준다.
            lst.tail = new
        lst.size += 1

    def deleteLast(lst):
        if lst.head is None : return

        pre, cur = None, lst.head
        while cur.next is not None :
            pre = cur
            cur = cur.next
        if pre is None:
            lst.head = lst.tail = None
        else :
            pre.next = None
            lst.tail = pre
        lst.size -= 1

    def insertFirst(lst, new):
        if lst.head is None :
            lst.head = lst.tail = new
        else :
            new.next = lst.head
            lst.head = new

        lst.size += 1

    def deleteFirst(lst):
        if lst.head is None: return

        # 노드가 1개일 경우 주의한다.
        lst. head = lst.head.next  # 2번째 노드를 첫번 째 노드에 설정
        if lst.head is None :
            lst.tail = None
        lst.size -= 1

    def insertAt(lst, idx, new) :
        # 빈리스트일 경우, idx == 0
        if lst.head is None or idx == 0 :
            insertFirst(lst,new)
        # 마지막 추가하는 경우 idx >= lst.size
        elif idx >= lst.size:
            insertLast(lst,new)
        # 중간에 추가하는 경우
        else :
            pre, cur = None, lst.head
            for _ in range(idx):
                pre = cur
                cur = cur.next
            new.next = cur
            pre.next = new
            lst.size += 1

n5 = Node(5); n4 = Node(4, n5); n3 = Node(3, n4)
n2 = Node(2, n3); n1 = Node(1, n2)
mylist.head = n1; mylist.size = 5

for i in range(5):
    insertLast(mylist, Node(i))
    print(mylist)

# while mylist.size :
#     deleteLast(mylist)
#     printList(mylist)

for i in range(3):
    insertAt(mylist 2, Node(i+10))
    printList(mylist)
