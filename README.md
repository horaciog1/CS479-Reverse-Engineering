<h1 align="center">  CS479/579 Reverse Engineering at NMSU </h1>

## Summary
This repository, maintained by Horacio Gonzalez, contains reports on reverse engineering malware samples from "Practical Malware Analysis" for the CS479/579 Reverse Engineering course at NMSU.


## System Setup
### Reverse Engineering System Setup

I. **Operating System:**
   - Start with a Unix-based OS like Linux or MacOS. Using a Unix operating system as the host provides an additional layer of security for the sandbox, preventing potential malware escape from the Windows VM that will run the malware.

      *In my case, I have set up two computers in case of them fails:*
      1. *The first computer runs Parrot OS (Debian-based) as its primary OS.*
      2. *The second computer runs Kali Linux in a dual-boot configuration with Windows.*
     
II. **Hypervisor:**
   - After setting up the Linux computers I procceded to install VirtualBox as the Hypervisor of my choice. This hypervisor will serve as the virtualization platform for running the Windows 11 VM.

III. **Windows 11 VM:**
   - I downloaded a Windows 11 VM from [here](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/). This is a VirtualBox preconfigured Windows 11 VM which is used only for demos. This VM restarts every hour and it will stop working on April. I decided to use this option since the installation is very fast and easy.
   - There is also another option to create your own ISO [here](https://www.microsoft.com/en-us/software-download/windows11). But if you create your own installation, you will need to add a license key later on.
