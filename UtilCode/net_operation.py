import subprocess, datetime, os, time, signal

def TIMEOUT_COMMAND(dirname, command, timeout):
    """call shell-command and either return its output or kill it
    if it doesn't normally exit within timeout seconds and return None"""
    start = datetime.datetime.now()
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, cwd=dirname)
    while process.poll() is None:
        time.sleep(0.2)
        now = datetime.datetime.now()
        if (now - start).seconds> timeout:
            os.kill(process.pid, signal.SIGKILL)
            os.waitpid(-1, os.WNOHANG)
            return ["timeout"], [""]
    res_err = process.stderr.readlines()
    res_out = process.stdout.readlines()
    return res_err, res_out

#print TIMEOUT_COMMAND("sh x_sleep.sh", 1)
#print TIMEOUT_COMMAND("./x_run_env", "python test.py", 3)
#print TIMEOUT_COMMAND("cd x_run_env", 1)
