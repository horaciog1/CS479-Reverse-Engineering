# Antivirus System Report: Detection and Removal of njRAT

### Introduction:
This report outlines the approach taken by my Antivirus (A/V) system to detect and remove njRAT, a notorious Remote Access Trojan (RAT) malware. The system employs a combination of techniques to identify indicators of compromise (IoCs) associated with njRAT and then removes the malicious program from the system.

### Detection Techniques:
1. File System Scanning:
    - The A/V system scans critical system directories and user-specific locations for files commonly associated with njRAT, such as "njq8.exe" and "njRAT.exe".
    - It also checks for filenames and patterns known to be used by njRAT, such as "ecc7c8c51c0850c1ec247c7fd3602f20.exe".
  

2. Process Monitoring:
    - The system monitors running processes to identify any instances of njRAT-related processes, such as "windows.exe", "ecc7c8c51c0850c1ec247c7fd3602f20.exe", and "njRAT.exe".
    - This technique helps identify active infections and potential instances of njRAT on the system.


3. Startup Program Analysis:
    - The A/V system checks startup programs and locations, such as the Windows Startup folder, for entries pointing to njRAT executables.
    - It identifies and removes any entries that may lead to the execution of njRAT upon system boot.
  

4. Temporary File Analysis:
    - Temporary directories, such as the user's local Temp folder, are scanned for njRAT-related temporary files.
    - This helps detect any temporary files created by njRAT during its execution and removes them to prevent persistence.
  

### Removal Process:

1. Process Termination:
    - The A/V system terminates any running processes associated with njRAT using the process termination API provided by the operating system.
    - This ensures that active instances of njRAT are stopped before removal.
  

2. File Deletion:
    - Identified njRAT files and artifacts are deleted from the system using the file deletion API.
    - This includes removing executable files, temporary files, and startup entries associated with njRAT.
  
### Notes
- I had to put the base64 version of the icon image because it was not working as I wanted and it was giving me a lot of errors
- The source code of my antivirus can be found on the "files" folder, the program is called "RatReaper.py"
- The executable can be found in this same directory, or by [clicking here to download](https://github.com/horaciog1/CS479-Reverse-Engineering/blob/main/Assignment%209/RatReaper.exe)
- There are sleep functions beetween each action to allow the system to kill processes and remove files, this process can take some time
- [Video can be found here]()
