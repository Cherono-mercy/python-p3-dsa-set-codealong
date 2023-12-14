# Defining the MySet class
class MySet:
    # Setting up the __init__ method to keep track of all values in a passed in collection 
    def __init__(self, enumerable = []):
        # Storing the passed in collection in another data structure - a dictionary
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    # The has() method. This method checks if the value is already included in the set, 
    #and returns true if so, and false if not 
    def has(self, value):
        return value in self.dictionary 

    # The add() method  to add a value to the set if it isn't already present, and return the updated set
    def add(self, value):
        self.dictionary[value] = True   # Add the value as a key on the dictionary
        return self                     # Return the updated set              
    

    # delete() method removes a value from the set, and returns the updated set
    def delete(self, value):
        self.dictionary.pop(value, None) # Delete the value and return None if the value doesn't exist
        return self                      # Return the updated set
     
    # size() method needs to return the number of elements in the set.
    def size(self):
        return len(self.dictionary)
    
    # clear() method removes all the items from the set, and returns the updated set.
    def clear(self):
        self.dictionary.clear()
        

    # __str__() method to print the set in a readable format using the __str__ method. 
    def __str__(self):
        set_list = []
        for key, value in self.dictionary.items():
            set_list.append(str(key))
        return f'MySet: {{{",".join(set_list)}}}'
              
    
