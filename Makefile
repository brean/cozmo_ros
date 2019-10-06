run:
	docker-compose up

shell:
	docker

run_pkg:
	# ros2 run <package_name> <node>
	ls

down:
	docker-compose down

create:
	docker build -t ros2 \
		ros2
	docker run -t \
		-v `pwd`/cozmo:/cozmo \
		-w /cozmo \
	 	ros2 \
		-c ros2 pkg create cozmo_driver
	# ros2 pkg create cozmo_driver
