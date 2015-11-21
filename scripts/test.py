__author__ = 'amit'
import subprocess


# Ask the user for input
host = raw_input("Enter a host to ping: ")

# Set up the echo command and direct the output to a pipe
p1 = subprocess.Popen([host], stdout=subprocess.PIPE)

# Run the command
output = p1.communicate()[0]
print output
# print '\npopen2:'
#
# proc = subprocess.Popen(['adduser'],
#                         stdin=subprocess.PIPE,
#                         stdout=subprocess.PIPE,
#                         )
# stdout_value = proc.communicate('tima')[0]
# print '\tpass through:', repr(stdout_value)

# cmd = ['sudo', 'ed', 'ls']
# proc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate("ls")
# print proc