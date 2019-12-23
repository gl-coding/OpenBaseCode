#encoding=utf8
import urllib2
import urllib
import json
import sys
import subprocess, datetime, os, time, signal

#timeout process
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

#api args set
def args_set(arg_type, *args):
    #type1
    if arg_type == "type1":
        api_url = 'http://api_url1'
        query_data = {"key":"val", "arg":args[0]}
    #type2
    if arg_type == "type2":
        api_url = 'http://api_url2'
        query_data = {"key":"val", "arg":args[0]}
    else:
        api_url = ""
        query_data = {}
        print "error"

    #url post process
    api_url += "&encoding=utf8"
    return api_url, query_data

#api request
def api_request(args):
    api_url, query_data = args
    data_json = json.dumps(query_data)
    request = urllib2.Request(api_url)
    request.add_header('content-TYPE', 'application/json')
    f = urllib2.urlopen(request, data=data_json)
    res = f.read()
    res_dic = json.loads(res)
    return res_dic

#api retry
def api_retry(times=3):
    time_count = 1
    while time_count < times:
        res = api_request(args_set("type1", "arg1"))
        if res == None:
            continue
        else:
            return res 

if __name__ == "__main__":
    #phrase
    print api_request(args_set("type1", "arg1"))
