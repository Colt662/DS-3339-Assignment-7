class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency

    def __str__(self):
        return f'{self.name} - ({self.urgency})'



class MinHeap:
    def __init__(self):
        self.data = []


    def heapify_up(self, index=None):
        if index == None: #new node, starting from back
            index = len(self.data) - 1

        if index == 0: #reached top, everything is heaped correctly
            return

        parent_index = (index - 1) // 2

        if self.data[index].urgency < self.data[parent_index].urgency: #urgency is backwards, 1 has greatest urgency 
            temp = self.data[index]
            self.data[index] = self.data[parent_index]
            self.data[parent_index] = temp

            self.heapify_up(parent_index)#move node as high up as needed


    def heapify_down(self, index=None):
            if index == None: #deletion, starting from top
                index = 0
    
            if index >= len(self.data): #reached bottom, everything is heaped correctly
                return
    
            left_index = index * 2 + 1
            right_index = index * 2 + 2
            smallest_index = index

            if left_index < len(self.data) and self.data[smallest_index].urgency > self.data[left_index].urgency: #urgency is backwards, 1 has greatest urgency 
                smallest_index = left_index

            if right_index < len(self.data) and self.data[smallest_index].urgency > self.data[right_index].urgency: #urgency is backwards, 1 has greatest urgency 
                smallest_index = right_index

            if index != smallest_index:
                temp = self.data[index]
                self.data[index] = self.data[smallest_index]
                self.data[smallest_index] = temp

                self.heapify_down(smallest_index)#move node as far down as needed


    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up()


    def print_heap(self):
        print("Current Patients In Queue: ")
        for patient in self.data:
            print(f'- {patient.name} ({patient.urgency})')


    def heap_peak(self):
        if len(self.data) > 0:
            return self.data[0]
        
        else:
            return None


    def remove_min(self):
        if len(self.data) == 0:
            return None

        elif len(self.data) == 1:
            return self.data.pop()

        else:
            result = self.data[0]
            self.data[0] = self.data.pop()
            self.heapify_down()
            return result
    
    




patient_heap = MinHeap()

print("Testing remove_min with never-populated heap:")
print(f'{patient_heap.remove_min()}')

patient_heap.insert(Patient("Jordan", 3))
patient_heap.insert(Patient("Taylor", 1))
patient_heap.insert(Patient("Avery", 5))
patient_heap.insert(Patient("Joe", 1))
patient_heap.insert(Patient("Mark", 8))
patient_heap.insert(Patient("Bob", 2))
patient_heap.print_heap()

print("Removing patients normally:")
for i in range(7): #doing more than nessecery to simulate empty heap
    print(f'{patient_heap.remove_min()}')
