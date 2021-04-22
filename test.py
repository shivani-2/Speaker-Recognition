import os

name = input("Enter name:")

check_dir = "dataset_train\\" + name 
print(check_dir)
# Check whether the specified path is an existing directory or not 
isdir = os.path.isdir(check_dir) 
print (isdir)

if not isdir:
    # Parent Directory path
    parent_dir = "dataset_train\\"
  
    # Path
    path = os.path.join(parent_dir, name)
  
    os.makedirs(path)