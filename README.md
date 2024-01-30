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

**System Isolation:** In this course we will be analyzing malware. Which means we will run the malware or parts of it to understand how it works. It is essential to keep the malware contained in a safe testing enviroment isolated of our computer. To isolate the malware we create a Virtual Machine to interact and analyze it. All the malware in this course was designed for Windows OS. To isolate even more, the main OS running the VM will be different, such as in my case, Kali Linux. If the malware accidentally escapes our isolation, it is unlikely to also work in the hypervisor host OS.

**Network Isolation:** To prevent malware from scaping, we will block all network capabilities of the VM. This can be acomplished from the VirtualBox menu in the Network tab. Once inside the network tab, we just need to uncheck the "Enable Network Adapter" box. We will disable the connectivity once we finished installing all the tools required for the class.

### Why Isolation?

In this course, malware analysis involves both static and dynamic analysis, these requieres running parts of the malware. Isolation is crucial to prevent potential harm to the host system and network. Using a virtual machine as a sandbox ensures that any malware escape is contained within the virtual environment.

### Permanent Disabling of Windows Defender
Windows Defender can interfere with malware analysis by detecting, putting it into quarantine, and deleting samples, potentially leaking sensitive information to third parties.
To do this I decided to first try to do the following method: https://woshub.com/disable-windows-defender-antivirus/#h2_2

1. **Boot into Safe Mode:**
   - Press Win + R to open the Run dialog.
   - Type msconfig and press Enter.
   - In the System Configuration window, go to the Boot tab.
   - Select Safe boot -> Minimal.
   - Click OK and restart your computer.
2. **Disable Defender Services via Registry:**
   - Open Registry Editor (regedit.exe).
   - Navigate to HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services.
   - Disable the startup of the following services by changing the **Start** parameter value to **4**:
   - Sense
   - WdBoot
   - WdFilter
   - WdNisDrv
   - WdNisSvc
   - WinDefend
- **Alternatively, you can also use the provided PowerShell script:**
```
$regpath='HKLM:\SYSTEM\CurrentControlSet\Services'
Set-ItemProperty -Path ($regpath+"\WinDefend") -Name Start -Value 4
Set-ItemProperty -Path ($regpath+"\Sense") -Name Start -Value 4
Set-ItemProperty -Path ($regpath+"\WdFilter") -Name Start -Value 4
Set-ItemProperty -Path ($regpath+"\WdNisDrv") -Name Start -Value 4
Set-ItemProperty -Path ($regpath+"\WdNisSvc”) -Name Start -Value 4
Set-ItemProperty -Path ($regpath+"\WdBoot") -Name Start -Value 4
```
- **The script provided by Dr. Reynolds also works:**
```
reg add "HKLM\System\CurrentControlSet\Services\WdFilter" /v "Start" /t REG_DWORD /d "4" /f
reg add "HKLM\System\CurrentControlSet\Services\WdNisDrv" /v "Start" /t REG_DWORD /d "4" /f
reg add "HKLM\System\CurrentControlSet\Services\WdNisSvc" /v "Start" /t REG_DWORD /d "4" /f
reg add "HKLM\System\CurrentControlSet\Services\WinDefend" /v "Start" /t REG_DWORD /d "4" /f
reg add "HKLM\System\CurrentControlSet\Services\Sense" /v "Start" /t REG_DWORD /d "4" /f
reg add "HKLM\System\CurrentControlSet\Services\WdBoot" /v "Start" /t REG_DWORD /d "4" /f
```
3. **Boot back into normal mode:**
   - Run `taskschd.msc` as an administrator
   - Navigate to `Task Scheduler Library` --> `Microsoft` --> `Windows` --> `Windows Defender`.
   - Disable the following tasks:
      - `Windows Defender Cache Maintenance`
      - `Windows Defender Cleanup`
      - `Windows Defender Scheduled Scan`
      - `Windows Defender Verification`
4. Reboot and verify that Windows Defender remains disabled.
   - Run the Windows Security app.
   - Ensure that Microsoft Defender Antivirus is now disabled.
   - You should see the message: "Threat service has stopped. Restart it now."
