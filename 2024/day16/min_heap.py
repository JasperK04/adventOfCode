
class minHeap(list):
    def __init__(self, *args):
        """Initialize the heap with optional initial values."""
        super().__init__(*args)
        if args:
            self.build_heap()
    
    def push(self, value):
        """Add a new value to the heap."""
        self.append(value)
        self._heapify_up(len(self) - 1)
    
    def pop(self):
        """Remove and return the smallest element from the heap."""
        if not self:
            raise IndexError("pop from empty heap")
        if len(self) == 1:
            return super().pop()
        root = self[0]
        # Move the last element to the root and remove it from the end
        last_element = self[-1]
        del self[-1]  # Remove the last element without using pop with an argument
        self[0] = last_element
        self._heapify_down(0)
        return root
    
    def build_heap(self):
        """Turn the current list into a valid heap."""
        for i in reversed(range(len(self) // 2)):
            self._heapify_down(i)
    
    def _heapify_up(self, index):
        """Ensure the heap property is maintained while adding an element."""
        parent = (index - 1) // 2
        if parent >= 0 and self[index][0] < self[parent][0]:
            self[index], self[parent] = self[parent], self[index]
            self._heapify_up(parent)
    
    def _heapify_down(self, index):
        """Ensure the heap property is maintained while removing an element."""
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        
        if left < len(self) and self[left][0] < self[smallest][0]:
            smallest = left
        if right < len(self) and self[right][0] < self[smallest][0]:
            smallest = right
        if smallest != index:
            self[index], self[smallest] = self[smallest], self[index]
            self._heapify_down(smallest)
