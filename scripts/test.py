__author__ = 'amit'
import subprocess, getpass
# password = getpass.getpass()

proc = subprocess.Popen(
  ['sudo','-p','','-S','adduser','tia',
   "--home", "/etc/karnikamittima",
   "--shell", "/etc/sh"],
  stdin=subprocess.PIPE)
proc.stdin.write("edge@123"+'\n')
proc.stdin.write("qwe"+'\n')
proc.stdin.write("qwe"+'\n')
proc.stdin.write(''+'\n')
proc.stdin.write(''+'\n')
proc.stdin.write(''+'\n')
proc.stdin.write(''+'\n')
proc.stdin.write(''+'\n')
proc.stdin.write("Y"+'\n')

# proc.stdin.write("tima")
proc.stdin.close()
proc.wait()