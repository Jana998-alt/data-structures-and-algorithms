class Node:
    def __init__(self, type):
        self.value = type
        #  can be only "cat" or "dog"
        self.next = None


class AnimalShelter:
    def __init__(self):
        self.roof = None
        self.tail = None

        #   enqueue
        # Arguments: animal
        # animal can be either a dog or a cat object.
    def enqueue(self, animal):
        if self.roof == None and self.tail == None:
            self.tail = Node(animal)
        elif self.roof == None and self.tail != None:
            self.roof = Node(animal)
            self.roof.next = self.tail
        else:
            temp_node = self.roof
            self.roof = Node(animal)
            self.roof.next = temp_node

# dequeue
# Arguments: pref
# pref can be either "dog" or "cat"
# Return: either a dog or a cat, based on preference.

    def dequeue(self, pref='any'):

        # If pref is not "dog" or "cat" then return null.
        if pref != 'cat' or pref != 'dog' or pref != 'any':
            return None

        # If the queue is empty
        if self.roof == None and self.tail == None:
            raise ValueError('shelter is empty')

        # If pref is not specified or equal to tail
        elif pref == 'any' or pref == self.tail.value:
            return self.tail

        # If the queue has only one value & pref is specified and not maching
        elif self.roof == None and self.tail != None and pref != self.tail.value:
            return "your request is not available"

        else:
            animal_to_give = None
            current_animal = self.roof
            while current_animal.next != self.tail:
                if current_animal == pref:
                    animal_to_give = current_animal
                else:
                    continue
                current_animal = current_animal.next

            if animal_to_give == None:
                return "your request is not available"
            else:
                return animal_to_give


  # def __str__():


  #   while current


if __name__ == "___main__":
    pass
