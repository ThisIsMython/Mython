#!/bin/env python
#coding:utf-8
#author:dxw
#function: rupdate
#date:2016-07-13

import argparse
from string import Template
import os 
import sys

if len(sys.argv) < 11:
    eg = "eg: --projectName ebomp --port 22 --user bebepay --userDir run_pkgs --iplist 192.168.114.11,192.168.114.12,192.168.114.13,192.168.114.14 > rupdate_bbpayapi.sh"
    print(eg)
    exit(1)


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("--projectName", action="store", dest="projectName")
parser.add_argument("--port", action="store", dest="port")
parser.add_argument("--user", action="store", dest="user")
parser.add_argument("--userDir", action="store", dest="userDir")
parser.add_argument("--iplist", action="store", dest="iplist")
result = parser.parse_args()

strsh='''
#!/bin/bash
#rupdate_dxw_${projectName}.sh

PLATFORM_DIR=/home/dada/bebepayplatform
DEPLOY_DIR=$PLATFORM_DIR/deploy

# COPY FILE TO REMOTE HOST

'''

strp='''
echo "Beginning ${ip} update_${projectName}.sh-------"
ssh -p ${port} -t ${user}@${ip} /home/${user}/${userDir}/update_dxw_${projectName}.sh
'''

#print("userDir: %s"%(result.userDir))

d1 = dict(projectName=result.projectName)
#print("d: %s"%(d) )
print( Template(strsh).safe_substitute(d1) )

d0 = dict(port=result.port, user=result.user, userDir=result.userDir, projectName=result.projectName)

ips=result.iplist.split(',')
#print("iplist: %s"%(ips))

for lip in ips:
    t=dict(ip=lip)
    d=d0.copy()
    d.update(t)
    s = Template(strp).safe_substitute(d)
    print(s)
