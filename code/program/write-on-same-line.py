import sys
import time

"""
For more detail check below link;

https://web.archive.org/web/20121225024852/http://www.climagic.org/mirrors/VT100_Escape_Codes.html
"""


class WriteOnSame1:
    def __call__(self, *args, **kwds):
        sys.stdout.write('some data')
        sys.stdout.flush()
        time.sleep(2) # wait 2 seconds...
        self.restart_line()
        sys.stdout.write('other data')
        sys.stdout.flush()
        
    def restart_line(self):
        sys.stdout.write('\r')
        sys.stdout.flush()
        

class WriteOnSame2:
    def __call__(self, *args, **kwds):
        self.print_10()
    
    def move_cursor_upper_left(self):
        print("\033[H\r", end="")
        sys.stdout.flush()
    
    def clear_screen(self):
        print('\033[2J\r')
        # sys.stdout.flush()
        
    def clear_line(self):
        print('\033[2K\r', end="")
        sys.stdout.flush()
        sys.stdout.write('\033[2K\r')
        sys.stderr.flush()
        
    def load(self):
        for i in range(1, 4):
            sys.stdout.write("Starting " + "."*i + "\r")
            time.sleep(.5)
            self.clear_line()
        
        
    def print_10(self, counter: int = 10):
        
        # clear screen 
        # and reset cursor to upper left
        self.clear_screen()
        self.move_cursor_upper_left()
        
        
        print("Counting the numbers till %d\n" % counter)
        sys.stdout.flush()
        
        
        # Clear starting message
        self.load()
        self.clear_line()
        self.load()
        self.clear_line()
        
        
        for i in range(counter):
            sys.stdout.write("\rCurrent number: %d" % i)
            sys.stdout.flush()
            time.sleep(0.1)

if __name__ == "__main__":
    wos = WriteOnSame2()
    wos()