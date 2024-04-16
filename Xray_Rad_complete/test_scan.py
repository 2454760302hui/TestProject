import time
import subprocess
import os
#rad名字（必须将此文件与rad程序放在同一目录）
radName="rad_windows_amd64.exe"
#xray名字(必须将此文件与rad程序放在同一目录)
xrayName="xray_windows_amd64.exe"
#xray代理地址
xrayProxy="127.0.0.1:7777"
def Scan(target):
	cmd = [radName,"-t",target,"-http-proxy",xrayProxy]
	rsp=subprocess.Popen(cmd,start_new_session=True)
	rsp.communicate()
with open("target.txt","r") as targats:
	outputPath=time.strftime("%Y%m%d%H%M%S",time.localtime())
	xrayShell = "start cmd /k "+xrayName+" webscan"+" --listen "+xrayProxy+" --html-output "+outputPath+".html"
	os.system(xrayShell)
	while targat :=targats.readline().strip("\n"):
		Scan(targat)

