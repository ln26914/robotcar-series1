import pygame
success, fail = pygame.init()
pygame.joystick.init()

print("Modules imported properly: ",success,"Modules failed: ",fail)

"""
ROS Modules: What are they, and how to use them

A node is a process that performs computation. Nodes are combined
together into a graph and communicate with one another. The nodes
are meant to operate at a fine-grained scale. A robot's control
system will usually have many nodes.

In our robot car example, we would need to write a node for each
of the motors and a publisher node. For future functionality, we'd need
another module for a line follower.

rosnode is a command-line tool for displaying information about Nodes,
such as listing the currently running Nodes.



http://wiki.ros.org/Nodes

"""