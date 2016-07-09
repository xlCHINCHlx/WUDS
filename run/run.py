from subprocess import call

call (["docker", "run", "-ti", "--privileged", "--net=host", "-v", "/dev/bus/usb:/dev/bus/usb", "chinch/WUDS"])


