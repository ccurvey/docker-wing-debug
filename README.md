**This is not working yet.  Still under development.**

# GETTING REMOTE WING DEBUGGING WORKING WITH DOCKER

1. Set your WINGHOME environment variable so that we don't break our local development
   environment.  Might want to put this in .bashrc, .profile, etc.

   $ WINGHOME=/usr/lib/wingide6 ; export WINGHOME

2. Copy your wingdbstub.py from the Wing directory to your working directory.  (You will
   need a real copy, not a symlink.)

   $ cp /usr/lib/wingide6/wingdbstub.py .

3. Copy your wingdebugpw file into your working directory

   $ cp ~/.wingide6/wingdebugpw .

3. Edit your copy of wingdbstub.py.  Around line 121, set

   WINGHOME=None

4. This is a good time to make sure you have remote debugging working on your
   local system (without getting docker involved).  Set a breakpoint at the
   last line of debugger_test.py and try it out

   $ python debugger_test.py

   *Do not proceed until Wing is stopping at that breakpoint.*  If it's not,
   you'll have to figure it out.

3. Copy (again, not symlink) the Wing debugger tarball into your working
   directory:

   $ cp /usr/lib/wingide6/bin/remote/wingide-debugger-x86_64-linux-6.0.12-1.tar.bz2 .

4. Build the docker image for the first time

   $ docker build -t wing-docker-debug -f Dockerfile.debug . --no-cache

5. Run the docker file.  *This will not stop at our breakpoint yet.*   What we
   want is that IP address

   $ docker run docker-wing-debug:latest
   ('IP Address = ', '172.17.0.2')

6. Tell Wing to accept connections from that IP Address.  Go to
   Edit->Preferences->Debugger->Advanced.

   a. In "Allowed Hosts", hit "Insert" add add the IP Address we got in Step 5.
   b. In "Location Map", hit "Insert".
   c. Use our IP address again for the "RemoteIP Address"
   d. Choose "Specify mapping".
   e. Hit "Insert"
   f: "Remote" should be "/opt/webapp" (no quotes)
   g: "Local" should be the path to your working directory (e.g. /home/chris...)
   h: Hit "OK" on all the dialogs to close and save them

7. Edit wingdbstub so that the remote program talks to your host.   The way we
   do this is different on Linux/Unix vs Mac/Windows.

   LINUX
       a. Use "ip a" to find your addresses.  Find the "docker0" section, and
          get the IP address from there.  It is probably 172.17.0.1
       b. In your copy of wingdbstub.py, around line 63, make

          kWingHostPort = '<ip-address-from-prior-step>:50005'

   WINDOWS and MAC: In your copy of wingdbstub.py, around line 63, make

       kWingHostPort = 'host.docker.internal:50005'

   REVIEWERS:  can you check that WINDOWS/MAC instruction?

8. Build the docker image for the second time:

   $ docker build -t wing-docker-debug -f Dockerfile.debug . --no-cache


