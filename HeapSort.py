'''Code below was motivated from the question ==> https://www.hackerrank.com/challenges/ctci-find-the-running-median'''
#The solution to the question above requires finding the running median in constant time. 
#An intuition to solving it is to split the array in to two halves(lower&higher) and maintain a Max Heap and Min Heap of sub-arrays respectively.
#Then the running median can be accessed in constant time.
#code below implements Heap functions as seen in the python 'heapify' library and also Heap Sort with sorting "In Place".

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

def findMedian(array):
    indexA = 0
    indexB = 0
    lenarr = len(array)
    if lenarr ==1:
        return array[0]
    elif len(array)%2==1 :
        index = lenarr/2 
        return array[index]
    else:
        indexA = lenarr/2 
        indexB  = (lenarr/2) - 1
        valA = array[indexA]
        valB = array[indexB]
        value =  (valA + valB)/2.0
        #print array,value, valA,valB,indexA,indexB
        return value
    


class Heapify(object):
    def __init__(self):
        self.array = []
        self.size = 0 
    
    def siftUp(self,index):
        par_idx = self.parentIndex(index)
        if par_idx > -1 and self.array[par_idx] > self.array[index]:
            self.swap(par_idx,index)
            self.siftUp(par_idx)
            
    def siftDown(self,index):
        left_idx = self.leftIndex(index)
        minIndex = index
        if left_idx > -1:
            if self.array[left_idx] < self.array[minIndex]:
                minIndex = left_idx
            
            right_idx = self.rightIndex(index)
            if right_idx > -1:
                if self.array[right_idx] < self.array[minIndex]:
                    minIndex = right_idx
        
        if minIndex != index:
            self.swap(minIndex,index)
            self.siftDown(minIndex)
        
    def append(self,value):
        self.size += 1
        self.array.append(value)
        idx = self.size - 1
        self.siftUp(idx)
        
    def reheap(self):
        n = self.size/2
        while n+1 > 0:
            self.siftDown(n)
            n -= 1
    def popMax(self):
        #value = -1
        if self.size > 0: 
            self.swap(0,self.size -1)
            #print "#",self.array[self.size-1]
            self.size -= 1
            self.siftDown(0)
            #value = self.array.pop()
        #return value
     
    def sort(self):
        n = self.size
        size = n
        while n > 0:
            self.popMax()
            n -= 1
        self.size = size
        return self.array
    
    def leftIndex(self,index):
        left = (2*index) + 1
        if left > self.size-1:
            return -1
        return left
    
    def swap(self,a,b):
        self.array[a],self.array[b] = self.array[b],self.array[a]
    
    def rightIndex(self,index):
        right = (2*index) + 2
        if right > self.size-1:
            return -1
        return right
    
    def parentIndex(self,index):
        if index == 0:
            return -1
        return (index - 1)/2
    
heap = Heapify()
heap.append(a[0])
array = heap.sort() 
heap.reheap() 
#print "{0:.1f}".format(findMedian(array))
for i in range(n-1):
    heap.append(int(raw_input().strip()))
    array = heap.sort()  
    #print array 
    print "{0:.1f}".format(findMedian(array))
    heap.reheap()
    

