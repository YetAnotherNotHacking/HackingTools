#built in imports
import os
import time
from cli import cli

#initiate error variables
criterr = 0
warnerr = 0
def getcrit():
    return criterr

def getwarn():
    return warnerr

#special imports
def si_colorama():
    try:
        import colorama
        exitcode = 0
    except ImportError:
        print("colorama not installed, installing now")
        os.system("pip install colorama")
        time.sleep(2)
        import colorama
        exitcode = 1
    finally:
        print("Fixed import error")

def si_pyfiglet():
    try:
        import pyfiglet
        exitcode = 0
    except ImportError:
        print("pyfiglet not installed, installing now")
        os.system("pip install pyfiglet")
        time.sleep(2)
        import pyfiglet
        exitcode = 1
    finally:
        print("Fixed import error")
#run special imports
si_colorama()
import colorama
si_pyfiglet()
import pyfiglet


class colors:
    def greent(text):
        return colorama.Fore.GREEN + text + colorama.Fore.RESET

    def redt(text):
        return colorama.Fore.RED + text + colorama.Fore.RESET

    def bluet(text):
        return colorama.Fore.BLUE + text + colorama.Fore.RESET

    def yellowt(text):
        return colorama.Fore.YELLOW + text + colorama.Fore.RESET

    def magentat(text):
        return colorama.Fore.MAGENTA + text + colorama.Fore.RESET

    def cyant(text):
        return colorama.Fore.CYAN + text + colorama.Fore.RESET

    def whitet(text):
        return colorama.Fore.WHITE + text + colorama.Fore.RESET

    def oranget(text):
        return colorama.Fore.ORANGE + text + colorama.Fore.RESET

    def brightgreent(text):
        return colorama.Fore.LIGHTGREEN_EX + text + colorama.Fore.RESET

def clear_screen():
    #determine teriminal type (linux, unix windows)
    if os.name == 'nt':
        #if windows, use cls
        _ = os.system('cls')
    else:
        #for linux, use cls
        _ = os.system('clear')

def miprnox(text):
    # Get the size of the terminal
    terminal_size = os.get_terminal_size()

    # Calculate the position to center the text horizontally
    center_x = (terminal_size.columns - len(text)) // 2

    # Print the text at the calculated position
    print('\033[{};{}H{}'.format(terminal_size.lines // 2, center_x, text))

def miprnox1(text, delay=0.1):
    # Get the size of the terminal
    terminal_size = os.get_terminal_size()

    # Calculate the starting position to center the text vertically
    start_y = (terminal_size.lines - text.count('\n')) // 2

    # Print each line of the multiline text with a delay
    for i, line in enumerate(text.split('\n')):
        # Calculate the position to center the text horizontally
        center_x = (terminal_size.columns - len(line)) // 2

        # Set the cursor position and print the line
        print('\033[{};{}H{}'.format(start_y + i, center_x, line))
        
        # Pause for the specified delay
        time.sleep(delay)

class log:
    def success(message):
        timestamp = time.strftime("%Y-%m-%d-/-/-%H:%M:%S.") + "{:03d}".format(int(time.time() * 1000) % 1000)
        print(f"[{timestamp}] --- {colors.greent(message)}")
    def status(message):
        timestamp = time.strftime("%Y-%m-%d-/-/-%H:%M:%S.") + "{:03d}".format(int(time.time() * 1000) % 1000)
        print(f"[{timestamp}] --- {colors.cyant(message)}")
    def warn(message):
        timestamp = time.strftime("%Y-%m-%d-/-/-%H:%M:%S.") + "{:03d}".format(int(time.time() * 1000) % 1000)
        print(f"[{timestamp}] --- {colors.yellowt(message)}")
    def critical(message):
        timestamp = time.strftime("%Y-%m-%d-/-/-%H:%M:%S.") + "{:03d}".format(int(time.time() * 1000) % 1000)
        print(f"[{timestamp}] --- {colors.redt(message)}")

def run_command(command):
    os.system(command)
    log.status(f"Executed command: {command}")

def getlogo():
    logoascii = pyfiglet.figlet_format("Sploit-tables")
    return logoascii

def logoshow():
    clear_screen()
    miprnox1(getlogo())
    clear_screen()
    time.sleep(2)
    miprnox("Welcome to Sploit-tables")
    time.sleep(0.5)















log.success("All objects loaded succesfully)")
log.status("All functions defined succesfully")

if __name__ == "__main__":
    logoshow()
