# data & reference/link
#operations on a SINGLE node

class Node(object): #blueprint for instances
    
    def __init__(self, data): #method to create a node
        self.data = data;
        self.nextNode = None;
    
    def remove(self, data, previousNode): #method to remove a node
        if self.data == data:
            previousNode.nextNode = self.nextNode; #update reference
            del self.data; #remove data
            del self.nextNode; #remove reference            
        else:
            if self.nextNode is not None:
                self.nextNode.remove(data, self)