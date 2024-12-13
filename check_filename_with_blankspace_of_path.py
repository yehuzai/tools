import os

def check_spaces_in_file_paths(directory):
    file_count = 0  # init count

    # scan all files and directories
    try:
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            # is directory
            if os.path.isdir(item_path):
                file_count += check_spaces_in_file_paths(item_path)  # add count of directory
            # is file, check filename
            elif os.path.isfile(item_path):
                file_count += 1  # count it
                if ' ' in item_path:
                    print(f"Find a file: {item_path}")
    except PermissionError:
        print(f"PermissionError: Can not access {directory}")
    except Exception as e:
        print(f"Exception: {str(e)}")

    return file_count  # return file count of directory

# User can input the directory
directory_to_check = input("Please Input the directory for scan:")
total_files = check_spaces_in_file_paths(directory_to_check)
print(f"Over, we have checked {total_files} files.")
