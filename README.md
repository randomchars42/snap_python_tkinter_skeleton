A skeleton to package python3/tkinter apps as snaps in the future.

At the moment the resulting snap crashes when running tkinter (Bug:
<https://bugs.launchpad.net/snapcraft/+bug/1847321>, might be related to:
<https://bugs.launchpad.net/snapcraft/+bug/1709060>).

## Steps to reproduce

 0. Install Snapcraft ;)
 1. Clone this repo: `git clone https://github.com/randomchars42/snap_python_tkinter_skeleton.git`
 2. `cd snap_python_tkinter_skeleton`
 3. `snapcraft try`
 4. `sudo snap try prime --devmode`
 5. `python-tkinter-skeleton`
