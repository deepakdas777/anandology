"""Write a program to list all files in the given directory."""

import os
for file in os.listdir("."):
    print(file)
