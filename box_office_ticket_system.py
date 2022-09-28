
from os.path import exists

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
        self.open_windows = [False for window in range(self.no_of_windows)]
        self.open_windows[0] = True
        
    def is_window_open(self, window):
        return self.open_windows[window-1] == True
    
    #Get length of the Queue if Queue is open
    def get_window(self, window):
        if self.open_windows[window-1] == False:
            return []
        else:
            return self.ticket_queues[window-1].get_queue()
    
    #Get the all current open windows
    def get_open_windows(self):
        curr_open_windows = []
        for i in range(self.no_of_windows):
            if self.open_windows[i] == True:
                curr_open_windows.append(i)
        return curr_open_windows
    
    #Getting Queue which has least number of people
    def get_priority_window(self):
        min_window_size = self.window_size
        min_window = -1
        curr_open_windows = self.get_open_windows()
        for i in curr_open_windows:
            if self.ticket_queues[i].size() < min_window_size:
                min_window_size = self.ticket_queues[i].size()
                min_window = i
        
        if min_window_size == (self.window_size):
            min_window = len(curr_open_windows)
            self.open_windows[min_window] = True
        return min_window
        
    #Checking whether all Queues are full or not
    def check_all_windows_full(self):
        #open_windows.index(i) for i in range(open_windows) if i == True]
        for i in range(self.no_of_windows):
            if self.ticket_queues[i].size() == self.window_size:
                continue
            else:
                return False
        return True

    #Adding person to ticket queue 
    def add_person(self, person_id):
        is_all_windows_full = self.check_all_windows_full()
        if is_all_windows_full is True:
            return 'All Queues are Full'
        
        at_window = self.get_priority_window()
        self.ticket_queues[at_window].enqueue(person_id)
        return (at_window + 1)
        
    #Issues tickets to person in the queue
    def issue_tickets(self):
        curr_open_windows = self.get_open_windows()
        tickets_issued = 0
        for window in curr_open_windows:
            if self.ticket_queues[window].size() > 0:
                self.ticket_queues[window].dequeue()
                tickets_issued += 1
        return tickets_issued
        
        
if __name__ == '__main__':
    if exists("inputPS16Q1.txt"):
        infile = "inputPS16Q1.txt"
    elif exists("promptsPS16Q1.txt"):
        infile = "promptsPS16Q1.txt"
    else:
        raise Exception("Input File Not Found!")
    outfile = open("outputPS16Q1.txt", "a")
    
    with open(infile,"r") as f:
        line = f.readline()
        action, no_of_windows, window_size = line.split(":")
        ticket_system = TicketSystem(int(no_of_windows), int(window_size))
        
        line = f.readline()
        while line:
            action, _ = line.split(":")
            if action == 'addPerson':
                outfile.write("{} {} {} \n".format(line.strip(), " >> ", ticket_system.add_person(int(_))))
            elif action == 'getWindow':
                outfile.write("{} {} {} \n".format(line.strip(), " >> ",  ticket_system.get_window(int(_))))
            elif action == 'isOpen':
                outfile.write("{} {} {} \n".format(line.strip(), " >> ",  ticket_system.is_window_open(int(_))))
            elif action == 'giveTicket':
                outfile.write("{} {} {} \n".format(line.strip(), " >> ",  ticket_system.issue_tickets()))
            line = f.readline()
        
    outfile.close()
