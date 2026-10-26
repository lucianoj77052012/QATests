# QATests
A collection of tests aimed at ensuring automation practice sites work as expected both from front end and back end perspectives

# HOW TO BUILD

Install Docker at https://docs.docker.com/desktop/setup/install/windows-install/ (for Windows). Make sure the daemon is running (opening Docker Desktop runs it). Then run:

`docker build -t qatests .`

And:

`docker run -v ./reports:/usr/src/app/reports qatests`

The -v option makes it such that the screenshots taken (reports) are saved into the host machine.