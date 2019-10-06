start:
	make try_install
	python3 nodes/pycozmo_driver.py

try_install:
	if [ ! -d "pycozmo" ]; then \
		make install; \
	fi;

install:
	git clone https://github.com/zayfod/pycozmo.git;
	cd pycozmo && pip3 install -e .
