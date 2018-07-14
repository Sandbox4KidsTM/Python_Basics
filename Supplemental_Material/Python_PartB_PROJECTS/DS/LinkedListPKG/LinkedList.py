# set of nodes with operations

from LinkedListPKG.Node import Node;

class LinkedList(object):

    def __init__(self): #method to create a linked list
        self.head = None; #make an empty linked list
        self.counter = 0; #therefore the counter is set to 0
    
    def remove(self, data):
        self.counter -= 1;
        pass
    
    def insertStart(self, data):
        self.counter += 1;
        newNode = Node(data);
        
        if not self.head: #if this is the first item on the linked list
            self.head = newNode;      
        else:
            newNode.nextNode = self.head;
            self.head = newNode;
    
    def insertEnd(self, data):
        self.counter += 1;
        pass
    
    def traverse(list): #to find out or read items in the linked list
        actualNode = self.head;        
        while actualNode is not None:
            print("%d " %actualNode.data);
            actualNode = actualNode.nextNode;
    
    def size(self):
        return self.counter;
        pass