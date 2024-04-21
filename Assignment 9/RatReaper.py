import os

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
