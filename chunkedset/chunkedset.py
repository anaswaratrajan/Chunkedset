class Chunk(set):
    '''class for chunk. '''


    def __init__(self):
        '''initialises an empty chunk with 5 slots(k=5)'''
        self.data = set()
        self.slots = 5

    def set_data(self, data):
        ''' Assigns machine with given data if there is enough slot and returns true
            else doesn't set data and returns false'''
        if len(data)<=self.slots:
            self.data = data
            self.slots-=len(self.data)
            return True
        else:
            return False

    def reset(self):
        '''clears chunk'''
        self.data.clear()

    def get_hash(self):
        '''get hash values for each datapoints'''
        hash_ = set()
        for i in self.data:
            hash_.add(hash(i))
        return hash_

    def add_data(self, data):
        '''Add given set of datapoints'''
        for datapoint in data:
            self.data.add(datapoint)

    def remove_data(self, data):
        '''Removes given set of datapoints if exists'''
        for datapoint in data:
            self.data.discard(datapoint)

    def length(self):
        '''Returns number of slots filled'''
        return len(self.slots)




class ChunkedSet(Chunk):
    '''Class for ChunkedSet implemented as two hash_tables

            Data_table -
                hash_table1 : key   :  datapoint
                              value :  (chunk, slots)
            Slot_table -
                hash_table2 : key   :  slots
                              value :  [list of chunks]

            Node_table -
                hash_table3 : key   :  chunks
                              value :  datapoints in tuple

        '''

    def __init__(self):
        '''initialise empty hash tables '''

        self.data_table = [None] # Hashtable 1
        self.size = 0 # Size of hashtable 1
        self.slot_table = [[] for i in range(6)] # Hashtable 2
        self.node_table = [None]
        self.chunks = 0 # Number of chunks in the ChunkedSet

    def join(self, data):
        '''joins key value pairs in the hashtables
        Each time a chunk joins for each datapoint '''

        chunk = Chunk() # Initialise a new chunk
        duplicates = set() # Returns duplicates
        if chunk.set_data(data): # Initialise and check capacity
            '''To extend hash_table size'''
            m = max(data)
            if m>self.size:
                self.data_table = self.data_table + [None for i in range(m-self.size)]
                self.size = m
            self.chunks+=1
            self.node_table.append(None)
            slots = 5 - len(data)
            for datapoint in data:
                if self.data_table[datapoint]!=None:
                    duplicates.add(datapoint)          # Get duplicates
                    slots+=1
            l = []
            for datapoint in data:
                if self.data_table[datapoint]==None:
                    self.data_table[datapoint] = (self.chunks,slots) # Add to Datatable
                    l.append(datapoint)
            self.node_table[self.chunks]=set(l)
            self.slot_table[slots].append(self.chunks) # Add to Slottable
            return duplicates # Return duplicates to make necessary changes in the respective chunks
        else:
            return 'Cannot join, no capacity'

    def leave(self, data):
        ''' Remove node from both tables and update both with relocated chunk
        Datatable -
            key - id of datapoint to update
            value - new chunk to which the datapoint was relocated

        Slot_table - Remove chunk from the slots table and update slot numbers of other chunks'''

        chunk ,slots = self.data_table[min(data)] # Find which chunk the data belongs to
        self.slot_table[slots].remove(chunk)
        self.node_table[chunk]=None # Reset chunk values to none
        slots = 5-slots # Required number of slots for the given data
        d = data.copy()
        while len(data)>0:
            if len(self.slot_table[slots])!=0: # Get chunks with slots if exists
                for chunk in self.slot_table[slots]:
                    l=[]
                    if len(data) > slots:  # If data won't fit into the slot of this chunk alone
                        m=slots
                        for i in range(m):
                            l.append(data.pop())
                        self.node_table[chunk] = set(self.node_table[chunk].union(set(l)))
                        for i in self.node_table[chunk]:
                            self.data_table[i] = (chunk, slots-len(l))
                    else: # If data fits in
                        m=len(data)
                        for i in range(m):
                            l.append(data.pop())
                        break
            if len(data)==0: # All data relocated to other chunks
                self.node_table[chunk] = set(self.node_table[chunk].union(set(l)))
                for i in self.node_table[chunk]:
                    self.data_table[i] = (chunk, slots-m)
                self.slot_table[slots].remove(chunk)
                self.slot_table[slots-m].append(chunk)
                return 'chunk cleared'
            slots-=1
            if slots==0:
                slots = 5
        return 'Not enough space left'

    def get_set(self):
        return self.data_table

    def get_node(self):
        return self.node_table

    def get_slots(self):
        return self.slot_table
