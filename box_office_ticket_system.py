


class TicketQueue:

    def __init__(self):
        self.elements = []

    def enqueue(self,item):
        self.elements.append(item)

    def dequeue(self):
        item = self.elements.pop(0)
        return item

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return len(self.elements) == 0

    def front(self):
        return self.elements[-1]

    def get_queue(self):
        return self.elements

class TicketSystem(TicketQueue):
    
    def __init__(self, no_of_windows, window_size):
        self.no_of_windows = no_of_windows
        self.window_size = window_size
        self.ticket_queues = [TicketQueue() for i in range(self.no_of_windows)]
        self.queue_ends = [self.ticket_queues[i].size() for i in range(self.no_of_windows)]
        self.open_windows = [False for window in range(self.no_of_windows)]
        self.open_windows[0] = True
        
    def is_window_open(self, window):
        return self.open_windows[window-1] == True
    
    #Get length of the Queue if Queue is open
    def get_window(self, window):
        if self.open_windows[window-1] == False:
            return []
        else:
            return len(ticket_queues[window])
    
    #Getting Queue which has least number of people
    def get_priority_window(self):
        temp_window_size = self.window_size
        window = 0
        for i in range(self.no_of_windows):
            if self.open_windows[i] == True:
                if self.ticket_queues[i].size() < temp_window_size:
                    temp_window_size = self.ticket_queues[i].size()
                    window = i
        return window
        
    #Checking whether all Queues are full or not
    def check_all_windows_full(self):
        #open_windows.index(i) for i in range(open_windows) if i == True]
        for i in range(self.no_of_windows):
            if self.ticket_queues[i].size() == (window_size - 1):
                continue
            else:
                return False
        return True
    
    def add_person(self, person_id):
        is_all_windows_full = check_all_windows_full()
        if is_all_windows_full is False:
            print("All Queues are Full.")
            return
        
        
        
