import daemon
from scan_activities import *

if __name__ == "__main__":
    with daemon.DaemonContext():
        run()