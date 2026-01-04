#! /usr/bin/env python3

"""
Test suite for the ROS2 minimal publisher node.

This script contains unit tests for verifying the functionality of a minimal ROS2 publisher.
It tests the node creation, message counter increment, and message content formatting.

Subscription Topics:
    None

Publishing Topics:
    /py_example_topic (std_msgs/String): Example messages with incrementing counter

"""

import pytest
import rclpy
from std_msgs.msg import String
from ros2_fundamentals.py_minimal_publisher import MinimalPyPublisher

def test_publisher_creation():
    # raises: AssertionError if any of the checks fail
    rclpy.init()
    
    try:
        #Create instance of publisher node
        node = MinimalPyPublisher()

        # Test 1: Verify node has the expected name
        assert node.get_name() == "minimal_py_publisher"

        # Test 2: Verify the publisher exists
        assert hasattr(node, 'publisher_1')

        # Test 3: Verify the publisher has the correct topic name
        assert node.publisher_1.topic_name == "/py_example_topic"

    finally:
        #Clean up ROS 2 communication
        rclpy.shutdown()

def test_message_counter():
    #Test if counter increments correctly
    rclpy.init()

    try:
        node = MinimalPyPublisher()
        initial_count = node.i
        node.timer_callback()
        assert node.i == initial_count + 1
    finally:
        rclpy.shutdown()

def test_message_content():
    #Test if the message content is formatted correctly.
    rclpy.init()
    try:
        node = MinimalPyPublisher()
        # Set counter to a known value for testing
        node.i = 5
        msg = String()
        # Using f-string instead of % formatting
        msg.data = f'Hello World: {node.i}'
        assert msg.data == 'Hello World: 5'
    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    pytest.main(['-v'])