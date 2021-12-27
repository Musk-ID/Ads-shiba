import sys
from time import sleep

class setup:

    def message(self,runing):
        for c in runing + "\n":
            sys.stdout.write(c)
            sys.stdout.flush()
            sleep(0.001)

    def countdown(self,second):
        while second:
            mins,secs = divmod(second,60)
            timer = "  \033[1;33m✒ \033[1;37mWaiting\033[1;37m \033[37m⟨\033[0;36m{:02d}:{:02d}\033[1;37m⟩ ".format(mins,secs)
            print(timer,end="\r")
            sleep(1)
            second -= 1
