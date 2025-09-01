import curses
from curses import textpad
import time 

def main(stdscr): 
    # terminal color theming  
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)  
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLUE)

    # setup windows  
    stdscr = curses.initscr()  
    stdscr.clear()  

    promptbar = stdscr.subwin(1, stdscr.getmaxyx()[1], 0, 0)  
    textbox = stdscr.subwin(10, 100, 1, 1)  

    # layout  
    promptbar.addstr(">>", curses.color_pair(2))  
    textbox.box() 

    # text box  
    editwin = textpad.Textbox(textbox)

    # flash
    def do_flash(stdscr):
        stdscr.addstr(0, 0, " ***FLASH*** ")
        stdscr.refresh()
        time.sleep(0.3)
        stdscr.addstr(0, 0, " " * 13) # clear  
        stdscr.refresh()

    # input loop  
    while True:
        # draw  
        promptbar.refresh()  
        textbox.refresh()

        # flash   
        do_flash(stdscr)

        # input
        key = stdscr.getch()  

        if key == ord('q'): # exit
            break     

    # shutdown  
    stdscr.keypad(False)
    curses.echo() 
    curses.endwin()

curses.wrapper(main)