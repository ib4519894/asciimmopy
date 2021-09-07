python=python
client_entrypoint=./client/main.py
server_entrypoint=./server/main.py

help:
	@echo "-help-"
	@echo "make, make help - display this message"
	@echo "make setup - install dependencies"
	@echo "make devsetup - install dev dependencies"
	@echo "make runclient - run client"
	@echo "make runserver - run server"

setup:
	@echo "-setup-"
	${python} -m pip install -r requirements.txt

devsetup: setup
	@echo "-devsetup-"
	${python} -m pip install -r requirements-dev.txt

runclient:
	@echo "-runclient-"
	${python} ${client_entrypoint}

runserver:
	@echo "-runserver-"
	${python} ${server_entrypoint}
