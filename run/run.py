from subprocess import call
call (["docker", "build", "-t", "chinch/wuds1", "/home/wtmf/dock/kali-wuds"])

call (["docker", "run", "-ti", "--privileged", "--net=host", "-v", "/dev/bus/usb:/dev/bus/usb", "chinch/wuds1"])


