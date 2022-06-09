#Python program
#Count all possible paths between two vertices
#Using DFS
class AjLinkeNode:
  def __init__(self,data):
    self.id=data
    self.next=None

class Vertices:
  def __init__(self,data):
    self.data=data
    self.next=None

class Graph:
  """Constructor for Graph"""
  def __init__(self, size):
    self.size=size
    self.node=[]
    self.result=0
    

  def setData(self):
    if(self.size>0 and self.node!=None):

      index=0
      while(index<self.size):

        self.node.append(Vertices(index))

        index+=1


  #connect two node with  edge
  def connect(self,start,end):

    new_edge=AjLinkeNode(end)

    if(self.node[start].next==None):

      self.node[start].next=new_edge
    else:

      temp=self.node[start].next

      while(temp.next!=None):

        temp=temp.next

      temp.next=new_edge  

  #add edge
  def addEdge(self,start,end):
     
    #start,end is two nodes
    if(self.size > start and self.size > start):
      
      self.connect(start,end)

    else:
      print("Invalid nodes")


  def printGraph(self):

    if(self.size>0 and self.node!=None):

      index=0

      while(index < self.size):

        print("\nAdjacency list of vertex {0} : ".format(index),end=" ")
        
        temp=self.node[index].next
        
        while temp!=None:

          print(" {0}".format(temp.id),end=" ")

          temp=temp.next

        index+=1

  
  #This function are capable to count all path between two nodes
  def count_path(self,start,end,visit) :

    if(start >self.size  or  end >self.size or start<0 or end<0 or self.node==None) :

      #invalid node location
      return 
    if(visit[start]==True) :

      #node is already visited
      return
    if(start==end) :

      #when source and destination are get
      self.result+=1

    #active the visiting node status
    visit[start]=True
    temp=self.node[start].next
    while(temp!=None) :

      #check node by edges
      self.count_path(temp.id,end,visit) 
      temp=temp.next

    #inactive current visiting node status
    visit[start]=False

  def  total_path(self,source,destination) :

    #for resultant paths
    self.result=0
    visit=[False]*self.size

    self.count_path(source,destination,visit)
    print("\n Possible Path : ",self.result)
    


    
def main():
  g=Graph(6)
  g.setData() 
  #Connected two node with Edges
  g.addEdge(0, 1) 
  g.addEdge(0, 3) 
  g.addEdge(1, 2) 
  g.addEdge(1, 4) 
  g.addEdge(2, 3) 
  g.addEdge(2, 4) 
  g.addEdge(2, 5) 
  g.addEdge(3, 1) 
  g.addEdge(3, 5) 
  g.addEdge(5, 4) 
  g.printGraph()
  #value 0 is source node
  source = 0
  #value 4 is destination node
  destination = 4
  g.total_path(source,destination)

if __name__=="__main__":
    main()
