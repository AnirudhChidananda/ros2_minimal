#! /bin/bash

# Launch publisher and subscriber nodes with cleanup handling

cleanup(){
    echo "Restarting ROS 2 daemon to cleanup before shutting down all processes.."
    ros2 daemon stop
    sleep 1
    ros2 daemon start
    echo "Terminating all processes.."
    kill 0
    exit
}

trap 'cleanup' SIGINT

# Launch the publisher node
ros2 run ros2_fundamentals py_minimal_publisher.py &

sleep 2

ros2 run ros2_fundamentals py_minimal_subscriber.py

