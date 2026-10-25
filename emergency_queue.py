class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency



class MinHeap:
    def __init__(self):
        self.data = []


    def heapify_up(self, index=None):
        if index == None: #new node, starting from back
            index = len(self.data) - 1

        if index == 0: #reached top, everything is heaped correctly
            return

        parent_index = (index - 1) // 2
        #TODO REMOVE
        print("")
        print(f'{self.data[index].name} {self.data[index].urgency}  i: {index}')
        print(f'{self.data[parent_index].name} {self.data[parent_index].urgency}  i: {parent_index}')
        #TODO REMOVE
        if self.data[index].urgency < self.data[parent_index].urgency: #urgency is backwards, 1 has greatest urgency 
            temp = self.data[index]
            self.data[index] = self.data[parent_index]
            self.data[parent_index] = temp
            print(f'Moveed {temp.name} up')
            print("")
            self.heapify_up(parent_index)#move node as high up as needed


    def heapify_down(self, index=None):
            if index == 0: #deletion, starting from top
                index = len(self.data) - 1
    
            if index >= len(self.data): #reached bottom, everything is heaped correctly
                return
    
            left_index = index * 2 + 1
            right_index = index * 2 + 2
            smallest_index = index

            if self.data[smallest_index].urgency > self.data[left_index].urgency: #urgency is backwards, 1 has greatest urgency 
                smallest_index = left_index

            if self.data[smallest_index].urgency > self.data[right_index].urgency: #urgency is backwards, 1 has greatest urgency 
                smallest_index = right_index

            if index != smallest_index:
                temp = self.data[index]
                self.data[index] = self.data[smallest_index]
                self.data[smallest_index] = temp

                self.heapify_down(smallest_index)

# Test your MinHeap class here including edge cases
