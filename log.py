import common

import subprocess

def log():
  subprocess.call('git log', shell=True)


def log_p():
  subprocess.call('git log -p', shell=True)