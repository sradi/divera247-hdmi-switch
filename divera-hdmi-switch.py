#! /usr/bin/python3

import time
import daemon
import lockfile
import sys
import signal
from pathlib import Path

lockfile_path = '/Users/sradi/divera.pid'
pidfile = Path(lockfile_path)

def dummy():
    print("bla")

def main():
    print(pidfile.as_posix)
    if pidfile.exists:
        print("Daemon is already running... exiting.")
        sys.exit(0)
    print("Starting Divera Daemon...")
    while True:
        time.sleep(180)
        dummy()


def shutdown(signum, frame):  # signum and frame are mandatory
    sys.exit(0)

#https://dpbl.wordpress.com/2017/02/12/a-tutorial-on-python-daemon/
#chroot_directory=None,
#working_directory='/var/lib/divera'
with daemon.DaemonContext(stdout=sys.stdout,
                          stderr=sys.stderr,
                          pidfile=lockfile.FileLock(lockfile_path),
                          signal_map={
                              signal.SIGTERM: shutdown,
                              signal.SIGTSTP: shutdown
                          }):
    main()
