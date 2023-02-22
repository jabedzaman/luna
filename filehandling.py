import os

def move_file(src_path, dest_path):
    if not os.path.isfile(src_path):
        print(f"Error: {src_path} is not a file.")
        return False
    
    try:
        os.rename(src_path, dest_path)
        print(f"Moved {src_path} to {dest_path}.")
        return True
    except:
        print("Error: Could not move file.")
        return False
    

def rename(src_path, new_name):
    if not os.path.isfile(src_path):
        print(f"Error: {src_path} is not a file.")
        return False
    
    try:
        os.rename(src_path, new_name)
        print(f"Renamed {src_path} to {new_name}.")
        return True
    except:
        print("Error: Could not rename file.")
        return False
    
# def delete(src_path):
#     #  check if its a file 
#     if not os.path.isfile(src_path):
#         print(f"Error: {src_path} is not a file.")
#         #  so its a directory and delete it
        
