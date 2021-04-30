import ctypes

class DynamicArray(object):
    '''
    Dynamic Array is similar to Python List
    '''
    def __init__(self):
        # actual elements
        self.n = 0
        self.capacity = 1
        self.arr = self.create_array(self.capacity)
        
    def __len__(self):
        return self.n
    
    def __getitem__(self, k):
        if not 0 <= k < self.n:
            return IndexError('Index Out of Bounds Exception')
        
        return self.arr[k]
    
    def append(self, item):
        if self.n == self.capacity:
            # Double the capacity
            self._resize(2*self.capacity)
            
        self.arr[self.n] = item
        self.n += 1
        
    def _resize(self, capacity):
        # Create an array with the new capacity
        arr2 = self.create_array(capacity)
        
        # Reference all values of old array
        for i in range(self.n):
            arr2[i] = self.arr[i]
            
        self.arr = arr2
        self.capacity = capacity
    
    def create_array(self, capacity):
        return (capacity * ctypes.py_object)()

arr = DynamicArray()
arr.append(1)
print("array length after adding first element: ", len(arr))

# capacity doubles
arr.append(2)
print("array length after adding second element: ", len(arr))


