import subprocess


def runCmd(cmd):
    p = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if p.returncode != 0:
        print(
            f"\tERROR from command: {cmd}\n\tError Message: {str(err, encoding='utf-8')}")
        return str(err, encoding='utf-8')
    return str(out, encoding='utf-8')


res = runCmd("ls -l")
print(res)
res1 = runCmd("mkdir testdir")
print(res1)
