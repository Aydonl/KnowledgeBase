"""
(C) 2008-2009, Red Hat Inc.
Michael DeHaan <michael.dehaan AT gmail>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301  USA
"""

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
    return "/var/lib/cobbler/triggers/install/post/*"
def my_get_process(server,ip):
    # return install process
    # By Aydon
    #my_url = 'http://10.68.18.101:8000/install_process?server=%s&ip=%s&stat=stop' %(server,ip)
    #my_url = 'http://10.102.200.2:8080/isp_kuaiyun_ywht/interface/updateProcess.action?name=%s&status=4' %(server)
    #my_url = 'http://10.100.0.6:8080/restfulapi/auto-deploy/tasks/%s' %(server)
    my_url = 'http://10.220.103.101:38085/restfulapi/auto-deploy/tasks/%s' %(server)
    data = {"update_state":{"state":4}}
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
        fd.write("%s\t stop \n" %my_url)
        fd.close()
    except urllib2.URLError,e:
        pass

def run(api, args, logger):
    # FIXME: make everything use the logger, no prints, use util.subprocess_call, etc

    objtype = args[0] # "system" or "profile"
    name    = args[1] # name of system or profile
    ip      = args[2] # ip or "?"

    fd = open("/var/log/cobbler/install.log","a+")
    fd.write("%s\t%s\t%s\tstop\t%s\n" % (objtype,name,ip,time.time()))
    fd.close()
    my_get_process(name,ip)

    return 0
