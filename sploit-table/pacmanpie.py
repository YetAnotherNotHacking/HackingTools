        #this script is first to run to verify that all dependencies are installed
#time and os are default.
import time
import os


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

def si_requests():
    try:
        import requests
        exitcode = 0
    except ImportError:
        print("requests not installed, installing now")
        os.system("pip install requests")
        time.sleep(2)
        import requests
        exitcode = 1
    finally:
        print("Fixed import error")

def si_nltk():
    try:
        import nltk
        exitcode = 0
    except ImportError:
        print("nltk not installed, installing now")
        os.system("pip install nltk")
        time.sleep(2)
        import nltk
        exitcode = 1
    finally:
        print("Fixed import error")
