class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None



class DoctorTree:
    def __init__(self):
        self.root = None

    #Taken from previous assignment
    def insert(self, manager_name, doctor_name, side, current_node=None):
        if self.root == None:
            print("Set head doctor to begin adding other doctors.")
            return


        if current_node == None:
            current_node = self.root


        if manager_name == current_node.name:
            if side.lower().strip() == "left":
                if current_node.left == None:
                    current_node.left = DoctorNode(doctor_name)
                    print(f'{doctor_name} added to the {side.upper()} of {manager_name}.')

                else:
                    print(f'{manager_name} already has an doctor on their {side.upper()} side. Try the other side.')


            elif side.lower().strip() == "right":
                if current_node.right == None:
                    current_node.right = DoctorNode(doctor_name)
                    print(f'{doctor_name} added to the {side.upper()} of {manager_name}.')

                else:
                    print(f'{manager_name} already has an doctor on their {side.upper()} side. Try the other side.')

            else:
                print("The selected doctor already has 2 direct subordinates.")

            return True # manager found



        else:
            if current_node.left != None:
                if self.insert(manager_name, doctor_name, side, current_node.left):
                    return True #manager found down this side, no need to keep checking

            
            if current_node.right != None:
                if self.insert(manager_name, doctor_name, side, current_node.right):
                    return True #manager found


            if current_node == self.root: #Implied based on the fact a return statment hasn't fired: the manager was not found anywhere in the tree
                print(f'No doctor with the name {manager_name} was found. Try checking the spelling.')
                return
            return False #Implied based on the fact a return statment hasn't fired: the manager was not found anywhere in the tree

# Test your DoctorTree and DoctorNode classes here
