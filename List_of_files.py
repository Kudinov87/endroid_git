# Python program to explain os.listdir() method

# importing os module
import os

# Get the path of current working directory
path = os.getcwd()

# Get the list of all files and directories
# in current working directory
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")
# print the list
print(dir_list)

# Path
path = os.getcwd()

# Check whether the
# specified path is an
# existing directory or not
isdir = os.path.isdir(path)
print(isdir)

# Path
path = '/home/User/Desktop/file.txt'

# Check whether the
# specified path is
# an existing file
isFile = os.path.isfile(path)
print(isFile)

''' Split the pathname path into a pair (root, ext) such that root + ext == path, 
and the extension, ext, is empty or begins with a period and contains at most one period.
'''
path = '/home/User/Desktop/file.txt'
os.path.splitext(path)
print(path)
