#application of linked lists
from LinkedListPKG import LinkedList;

myLL = LinkedList();

myLL.insertStart(11);
myLL.insertStart(22);
myLL.insertStart(33);
#myLL.insertEnd(99);

myLL.traverse();
print(myLL.size())