
# coding: utf-8

# In[3]:


class Node():
    def __init__(self,value=0,next=None):
        self.value=value
        self.next=next
        
class linked_list():
    def __init__(self,head=Node(),tail=None):
        self.head=head
        self.tail=tail
        
    
    def addnode(self,value):
        node=Node()
        node.value=value
        if(self.tail!=None):
            self.tail.next=node
            self.tail=node
            self.tail.next=None
        else:
            self.head.next=node
            self.tail=node
            self.tail.next=None
        
    def printnode(self):
        q=Node()
        q=self.head
        while(q!=None):
            print(q.value)
            q=q.next
    def insertnode(self,value,pos):
        node=Node()
        node.value=value
        i=0
        q=self.head
        while(i<pos):
            if i==pos-1:
                print("in")
                if q.next!=None:
                    p=q.next
                    q.next=node
                    q.next.next=p
                    break
                else:
                    q.next=node
                    q.next.next=None
                    break
            elif q==None and i!=pos-1:
                print("Position not available")
                break
            elif q!=None:
                q=q.next
                i+=1
    def deletenode(self,pos):
        i=0
        q=self.head
        while(i<pos):
            if i==pos-2:
                print("in")
                if q.next!=None:
                    p=q.next.next
                    
                    q.next.next=None
                    q.next=None
                    q.next=p
                    break
                else:
                    print("Position not available")
                    break
            elif q==None and i!=pos-1:
                print("Position not available")
                break
            elif q!=None:
                q=q.next
                i+=1
    def reversenode(self):
        prev=self.head
        curr=prev.next
        prev.next=None
        
        while curr.next!=None:
            
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex
            continue
        curr.next=prev
        self.head=curr
            
        
head=Node()
head.value=1
lis=linked_list(head)
lis.addnode(5)
lis.addnode(6)
lis.printnode()
lis.insertnode(2,1)
lis.printnode()
lis.deletenode(2)
lis.printnode()
lis.reversenode()
lis.printnode()

