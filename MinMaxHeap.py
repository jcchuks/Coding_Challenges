class Heap:
    def __init__(self, numbers=None, type="min"):
        self.array = numbers if numbers else []
        self.type = "min"
      
    def insert(self,value):
        self.array.append(value)
        self.bubbleUp(len(value)-1)
    
    def remove(self):
        self.swap(0,len(self.array)-1)
        value = self.array.pop()
        self.bubbleDown(0)
        return value
        
    def swap(self,indexA,indexB):
        self.array[indexA],self.array[indexB] = self.array[indexB],self.array[indexA]
    
    def bubbleUp(self,index):
        if self.type == "min":
            if index != 0:
                pindex = self.parent_index(index)
                if self.array[pindex] > self.array[index]:
                    self.swap(pindex,index)
                    self.bubbleUp(pindex)
        else:
            if index != 0:
                pindex = self.parent_index(index)
                if self.array[pindex] < self.array[index]:
                    self.swap(pindex,index)
                    self.bubbleUp(pindex)
    
    def bubbleDown(self,index):
        if index == len(self.array) - 1:
            return
        lcindex = self.lchild_index(index)
        if lcindex == 0:
            return
        rcindex = self.rchild_index(index)
        if self.type == "min":
            if rcindex == 0:
                if self.array[lcindex] < self.array[index]:
                    self.swap(lcindex,index)
            else:
                min_index = lcindex if self.array[rcindex] > self.array[lcindex] else rcindex
                if self.array[min_index] < self.array[index]:
                    self.swap(min_index,index)
                    self.bubbleDown(min_index)
        else:
            if rcindex == 0:
                if self.array[lcindex] > self.array[index]:
                    self.swap(lcindex,index)
            else:
                min_index = lcindex if self.array[rcindex] < self.array[index] else rcindex
                if self.array[min_index] > self.array[index]:
                    self.swap(min_index,index)
                    self.bubbleDown(min_index)
        
    
    def parent_index(self,index):
        if index > 0:
            return (index - 1)/2
        return 0
    def rchild_index(self,index):
        val = (2*index) + 2
        if val <= (len(self.array ) -1):
            return val
        return 0
    
    def lchild_index(self,index):
        val = (2*index) + 1
        if val <= (len(self.array) - 1):
            return val
        return 0
    
