class HashTable:
    def __init__(self,size = 7):
        self.data_map = [None] * size

    def __hash(self,key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_hash(self):
        for i,val in enumerate(self.data_map):
            print(i,": ",val)

    def set(self,key,value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])

    def get(self,key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i,v in self.data_map[index]:
                if i == key:
                    return v   
        return None
    
    def keys(self):
        all_keys = []
        for i,data in enumerate(self.data_map):
            if data is not None:
                for i,v in data:
                    all_keys.append(i)
        return all_keys
    
def item_in_common(list1,list3):
    my_dict = {}
    for i in list1:
        my_dict[i] = True  
    for i in list3:
        if i in my_dict:
            return True
    return False      



hash = HashTable()
hash.set('bolts',4900)
hash.set('washers',4940)
hash.set('hammer',4900)
print(item_in_common([1,3,6],[5,7,9]))
# hash.print_hash()