import distutils.sysconfig
import sys
import os
from utils import _
import traceback
import cexceptions
import os
import sys
import time
import urllib2
import json

plib = distutils.sysconfig.get_python_lib()
mod_path="%s/cobbler" % plib
sys.path.insert(0, mod_path)

def register():
    # this pure python trigger acts as if it were a legacy shell-trigger, but is much faster.
    # the return of this method indicates the trigger type
    return "/var/lib/cobbler/triggers/install/pre/*"
def my_get_process(server,ip):
    # return install process
    # By Aydon
    #my_url = 'http://10.68.18.101:8000/install_process?server=%s&ip=%s&stat=start' %(server,ip)
    #my_url = 'http://10.102.200.2:8080/isp_kuaiyun_ywht/interface/updateProcess.action?name=%s&status=3' %(server)
    #my_url = 'http://10.100.0.6:8080/restfulapi/auto-deploy/tasks/%s' %(server)
    my_url = 'http://10.220.103.101:38085/restfulapi/auto-deploy/tasks/%s' %(server)
    data = {"update_state":{"state":3}}
    data = json.dumps(data)
    headers = { 
      'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; AYDONURL; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
      'Content-Type': 'application/json'
    }
    try:
        request = urllib2.Request(my_url,data=data,headers=headers)
        request.get_method = lambda: 'PUT'
        response = urllib2.urlopen(request,timeout=30)
        fd = open("/var/log/cobbler/install.log","a+")
        fd.write("%s\t start \n" %my_url)
        fd.close()
    except urllib2.URLError,e:
        pass

def run(api, args, logger):
    objtype = args[0] # "system" or "profile"
    name    = args[1] # name of system or profile
    ip      = args[2] # ip or "?"

    # FIXME: use the logger

    fd = open("/var/log/cobbler/install.log","a+")
    fd.write("%s\t%s\t%s\tstart\t%s\n" % (objtype,name,ip,time.time()))
    fd.close()
    my_get_process(name,ip)

    return 0
