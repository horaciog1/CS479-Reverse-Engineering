import os

def deleteFiles():
    removeRoot()
    removeStartup()

def removeRoot():
    root_path = "C:\\"
    # List of file names to be deleted
    file_names = ["njq8.exe", "njRAT.exe"]

    for file_name in file_names:
        file_path = os.path.join(root_path, file_name)
        # Check if the file exists and delete it if found
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except OSError as e:
                print(f"Error: {file_path} - {e}")
        else:
            print(f"File not found: {file_path}")


def removeStartup():
    # Get the user's profile directory
    profile_dir = os.environ.get('USERPROFILE')
    if not profile_dir:
        print("Failed to retrieve user profile directory.")
        return

    # Directory containing the Startup file to be deleted
    startup_path = os.path.join(profile_dir, 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

    # File name to be deleted
    file_name = "ecc7c8c51c0850c1ec247c7fd3602f20.exe"

    # Construct the full path to the file
    file_path = os.path.join(startup_path, file_name)

    # Check if the file exists and delete it if found
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except OSError as e:
            print(f"Error: {file_path} - {e}")
    else:
        print(f"File not found: {file_path}")

def removeTestFile():
    # Get the user's profile directory
    profile_dir = os.environ.get('USERPROFILE')
    if not profile_dir:
        print("Failed to retrieve user profile directory.")
        return

    # Directory containing the test file to be deleted
    testpath = os.path.join(profile_dir, 'Downloads')
    
    # Test file name
    testfile = "test.txt"

    # Construct the full path to the test file
    file_path = os.path.join(testpath, testfile)

    # Check if the test file exists and delete it if found
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except OSError as e:
            print(f"Error: {file_path} - {e}")
    else:
        print(f"File not found: {file_path}")

# Call the function to remove the test file
removeTestFile()
deleteFiles()
