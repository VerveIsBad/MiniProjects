from LinkList import Node
from LinkList import LinkedList

llist = linkedList()
llist.head = node(1)
second = node(2)
third = node(3)
# ================ #
llist.head.next = second
second.next = third
# ================ #

print(len(llist.head))
