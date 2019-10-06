start:
	make try_install
	python3 nodes/pycozmo_driver.py

try_install:
	make install

install:
	if [ ! -d "pycozmo" ]; then \
		git clone https://github.com/zayfod/pycozmo.git; \
	fi;
	cd pycozmo && pip3 install -e .
