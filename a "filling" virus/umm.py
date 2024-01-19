import os
import random
import subprocess
import string

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

random = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

try:
    output = subprocess.check_output("pwd")
except subprocess.CalledProcessError as e:
    output = e.output
print(output)
out = output.decode()
out1 = out.replace("\n'", '')
out2 = out1.replace("b'", '')


script_path = os.path.join("apple," + random + ".py")
f = open(script_path, "w")
f.write("import os/n")
f.write("os.system('python3 "+ out +"umm.py')")
f.close()

os.system("python3 "+ random +".py")

