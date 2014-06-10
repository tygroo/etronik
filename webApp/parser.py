import subprocess
import sys

document = sys.argv[1]

out= subprocess.call(['java', '-jar', 'tika-app-1.5.jar', '-t', document])
print out
