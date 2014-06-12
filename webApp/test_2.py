import subprocess
import sys

print "Creation des index"

subprocess.call(['bash','createIndexes.sh','M13_TEYSSIER.pdf']);

print "OK"
