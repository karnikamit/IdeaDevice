__author__ = 'amit'
import subprocess


def create(data):
    cmd = ['sudo','-p','','-S']
    cmd.append("adduser")
    cmd.append(data['username'])
    if data["home_folder"]:
        cmd.append("--home")
        cmd.append(data["home_folder"])
    if data["shell"]:
        cmd.append("--shell")
        cmd.append(data["shell"])
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    proc.stdin.write(data["sys_pass"]+'\n')
    proc.stdin.write(data["password"]+'\n')
    proc.stdin.write(data["password"]+'\n')
    proc.stdin.write(''+'\n')
    proc.stdin.write(''+'\n')
    proc.stdin.write(''+'\n')
    proc.stdin.write(''+'\n')
    proc.stdin.write(''+'\n')
    proc.stdin.write("Y"+'\n')
    proc.stdin.close()
    return "Done!"


def deluser(data):
    response = "deleted!"
    try:
        proc = subprocess.Popen(['sudo','-p','','-S',
                                 'deluser', data["username"]],
                                stdin=subprocess.PIPE)
        proc.stdin.write(data["sys_pass"]+'\n')
        proc.stdin.close()
        proc.wait()
    except Exception, e:
        response = "failed!"
        print "exception", e.__str__()
    return response


def modify(data):
    response = "Modified!"
    cmd = ['sudo','-p','','-S', "usermod"]
    try:
        if data["new_home_folder"]:
            cmd.append("--home")
            cmd.append(data["new_home_folder"])
        if data["new_userPassword"]:
            cmd.append('--password')
            cmd.append(data["new_userPassword"])
        if data["newuserName"]:
            cmd.append('--login')
            cmd.append(data['newuserName'])
    except Exception, e:
        print "Exception", e.__str__()
    cmd.append(data["olduserName"])
    try:

        proc = subprocess.Popen(cmd)
        use_sudo = proc.stdin
        if use_sudo:
            proc.stdin.write(data["sys_pass"]+'\n')
            proc.stdin.close()
            proc.wait()
    except Exception, e:
        print "exception", e.__str__()
        response = "failed!"
    return response
