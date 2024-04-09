# Dynamic Analysis
On this week's report, we will perform dynamic analysis of a RAT, a Remote Access Trojan. We will analyze its behavior to quickly identify indicators
of compromise that could be used to detect this malware in the wild. The The RAT we will be looking at will come from the ZOO library used in assignment 2.
It is called NjRAT. Watch out that there is a Win32.NjRAT version and a plain NjRAT version. We will use the latter.
`hxxps://github.com/ytisf/theZoo/archive/refs/heads/master.zip`   This link will automatically download the malware library so be careful. You only need to change
`hxxps` for `https`.

## OSINT Investigation
NjRAT also known as Bladabindi, is a type of remote access Trojan (RAT) malware. RATs like NJRAT are designed to allow unauthorized access and control of a computer system. Once installed on a victim's machine, NJRAT can give the attacker full control over the system, enabling them to execute various malicious activities remotely, such as stealing sensitive information, monitoring user activity, installing additional malware, or using the infected machine as part of a botnet.

NJRAT gained notoriety for its widespread usage in cyber attacks and its ability to evade detection by traditional antivirus software. It's often spread through phishing emails, malicious websites, or bundled with other software. Like many RATs, NJRAT is considered a serious threat to cybersecurity and can cause significant damage if not detected and removed promptly. According to [Checkpoint.com](https://www.checkpoint.com/es/cyber-hub/threat-prevention/what-is-malware/what-is-njrat-malware/), this malware has the ability to propagate in different ways. Nevertheless, its main ways of infecting computer are phishing attacks and non-authorized downloads (such as files infected with the trojan, cracked programs). Newer versions of the malware have the ability to propagate trough infected USB media devices but the propagation method can be configured trough the C2 software of the malware.

According to the site [Checkpoint.com](https://www.checkpoint.com/es/cyber-hub/threat-prevention/what-is-malware/what-is-njrat-malware/) NjRAT was first seen in 2012, and was mainly targeting government agencies and organizations in the Middle East. As mentioned previously, this RAT has the ability to record keystrokes, use the target's camera, stealing passwords stored in browsers, uploading and downloading files (dropper), running files (launcher), performing process and file manipulations, change the registry, and remot accessing the target's desktop. This website also mentions that the malware uses different techniques to evade detection in an infected system. For example, this malware disguises as a "critical process", which makes it less likely to be eliminated by the users because of their fear to leave their system unusable. It also actively fights back deactivating the terminal security software and detecting if it being executed on a virtualized environment (VM), which makes it harder for analysts to investigate. According to [Wikipedia](https://en.wikipedia.org/wiki/NjRAT)this malware was made by a hacking organization from different countries called M38dHhM. It is believe that it was written by arabic speakers.

According to [Any.run](https://any.run/malware-trends/njrat) this malware was formaly seen in 1 January, 2013 and last seen 9 April, 2024; being this one of the most popular malware in the world. Newer version of the malware are also refered as `Njw0rm`. Here are some of the places where it has been recently seen:    

![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/e73c2379-c020-47ef-bf2c-d0bb06898223)   

This site believes that the creators of njRAT are members of a hacker community named Sparclyheason. In 2014, following a large malicious campaign, Microsoft shut down four million websites in an effort to filter traffic going through no-ip.com domains. From another perspective, [welivesecurity.com](https://www.welivesecurity.com/la-es/2021/09/29/que-es-njrat-troyano-acceso-remoto-utilizado-cibercriminales/) thinks that Njw0rm is a variant of NjRAT which was released by the same author years later. Njw0rm adds the ability to spread itself trough USB and replicate, something that older verions of NjRAT cant accomplish. The truth is that NjRAT functions as a template for cybercriminals to adapt the malware for their neccesities.

I have found an [Ethical Hacking Lab](https://github.com/Samsar4/Ethical-Hacking-Labs/blob/master/6-Malware/1-Using-njRAT.md) by Samsar4 where he shows the features of the malware to control and infect computers. Its simplicity is absurd, this is the perfect malware for "script kiddies".

Here are some pictures from [Samsar4 lab](https://github.com/Samsar4/Ethical-Hacking-Labs/blob/master/6-Malware/1-Using-njRAT.md) where he was testing the malware interface and functionality (Create an Executable Server with njRAT, Manipulate Files on Target machine, Manage the Processes, Manage the Connections, Manage the Registry, Launch a Remote Shell, Run Files, Launch a Remote Desktop Connection, and Perform Key Logging.):   

![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/4e05212d-65e5-4eb1-84fa-937590cc816d)
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/c0ff9362-61c3-448e-8ff8-f410b22b1e08)
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/b1933732-0409-4fe9-a117-c57c78695a0f)
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/bdb01fff-bf17-4c70-b5dc-2a7f01fa83f1)
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/f2894045-a496-419a-9a89-9d2cf5a5c0d8)
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/931abedd-2111-4317-8801-27205c7019e1)
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/cbdbc6fc-cf79-4013-ab5e-198f8af3b81a)
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/03aaa83c-4e0e-4fce-952b-45b262a7743a)
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/4c23bc5a-a1c3-4f8a-bf21-44b3658022ff)
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/25a8ae6a-0536-44f1-835d-80928cb27359)
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/706cbd1c-9f83-4340-b092-1982d58719c9)
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/1791b256-4927-49e5-970d-db07ead79c5a)   
*All rights and credits reserved to [Samsar4](https://github.com/Samsar4)*



## RegShot
RegShot is used to take a snapshot of the registry in Windows, a fundamental artifact for digital forensics on Windows. Double-check your network is disabled before running the RAT.
We will take a snapshot of the registry before running the RAT and then we will run the RAT and take another snapshot, and thus compare both snapshots using RegShot to see what has been changed.

- What registry keys changed?
  
- What was added?

- Does this appear to be for persistence, or something else?

- What clues (Indicators of Compromise) could someone look for in the registry to detect an NjRAT infection?

### File functionality of RegShot
RegShot allows you to take snapshots of directories as well. So then we will identify at least one file or directory created or altered by NjRAT when it runs. You may need to revert to your pre-RAT VM snapshot to check several directories to find a change.

- What files or directories did you see changed?
  > Just by iterating trough the directories, I found that it dropped a bunch of different files in Local C disk root directory.
  > ![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/6e97dd53-3f67-49c3-a311-f580248e9aab)
  
- Does this appear to be for persistence, or something else?
  > I noticed that on the startup apps, there were added a couple of executables that werent there before executing the malware. (this is mentioned at the end of the doc in Additional notes)
  > I assumed the malware did this for persistance whis refers to the ability of the malicious software to maintain its presence on an infected system over time, even after system reboots or attempts to remove it. Essentially, it's the malware's ability to "persist" or remain active on the compromised system to ensure continued control or access for the attacker. These mechanisms typically involve making changes to the system's configuration, startup routines, or other areas to ensure that the malware is executed automatically each time the system boots up or specific conditions are met.
- What clues (Indicators of Compromise) could someone look for in their filesystem to detect this NjRAT infection?

## FakeNet
FakeNet is an open-source tool primarily used for dynamic malware analysis and network traffic analysis. It is designed to simulate a network environment, allowing researchers and analysts to observe how malware interacts with the network without exposing real systems to potential harm.

You may need to set up a network interface on your VM. Most hypervisors will allow you to create a non-Internet-connected interface. FakeNet-NG will show a live feed of network activity when it is running properly, and you should take note of what Windows is already doing in the background.

After running FakeNet, I took a picture of some of the processes that were already running. I waited a couple of minutes before taking a snapshot in RegShot. I notice a couple of request to Microsoft Servers and then after tooking the snapshot of directories and registry I decided that it was time to run the malware.
- ***What did NjRAT do on the network?***
  > NjRAT started requesting a DNS server for the domain "zaaptoo.zapto.org" every 25 seconds. I could notice any other activity on the network besides this DNS request.
- What DNS name(s) did it look up?
  > The DNS was "zaaptoo.zapto.org"`
- Investigate that DNS name -- is this a known malicious domain, or an attacker abusing a legitimate service? Why do you think so?
  > zaaptoo.zapto.org appears to be a domain name registered with the "zapto.org" domain service. Zapto.org is a dynamic DNS service that allows users to create free subdomains under the "zapto.org" domain for remote access to their computers or services.
  > Dynamic DNS services like Zapto.org are commonly used for legitimate purposes, such as accessing home networks remotely or hosting personal websites on a dynamic IP address. However, they can also be abused by malware authors and cybercriminals to establish      > command-and-control (C2) infrastructure for malicious activities.
  > The domain and top-level domain zapto.org are perfectly fine but it has a bad reputition because of its use in illegal activities. I believe that an attacker is abusing this legitimate service to register their subdomain. After searching more about this subdomain and domain all together we get all kind of information related to the NjRAT.
- What indicators of compromise could a network administrator look for to identify if any of their machines are infected with this same malware?
  > Network administrators can look for the following indicators of compromise to identify if any of their machines are infected with the NjRAT malware:
  > - DNS Requests: Monitor network traffic for repeated DNS requests to the domain "zaaptoo.zapto.org" or any other suspicious domains associated with NjRAT. This request repeats every 25 seconds.
  > - Unusual Network Activity: Look for unusual or suspicious network activity, such as frequent outbound connections to unknown or suspicious IP addresses, especially if they occur at regular intervals.
  > - Outbound Connections: Analyze outbound connections from the infected machine to known NjRAT command-and-control (C2) servers or other malicious domains associated with NjRAT activity.
  > - Process Activity: Monitor process activity on the infected machine for any processes associated with NjRAT. This could include unusual or unauthorized processes running in the background, especially those with obfuscated or random names.
  > - Registry Modifications: Check for suspicious modifications to the Windows registry, such as the creation of new registry keys or entries related to NjRAT persistence mechanisms.
  > - File System Changes: Look for changes to the file system, such as the creation of new files or directories associated with NjRAT, especially in common locations used by malware for persistence, such as %APPDATA% or %TEMP%.
  > - Anti-Virus Alerts: Pay attention to any alerts or warnings from anti-virus or endpoint security software indicating the presence of NjRAT or related malware on the infected machine.
  > - Anomalous Behavior: Watch for any other anomalous behavior on the infected machine, such as unexpected system crashes, slowdowns, or unusual user activity, which could indicate the presence of malware.

  > By monitoring for these indicators of compromise, network administrators can detect and respond to NjRAT infections promptly, mitigating the potential damage and preventing further spread within their network. Additionally, implementing robust security measures, such as endpoint protection, network segmentation, and user education, can help prevent NjRAT infections and other malware threats.


## Aditional Notes
I decided to reboot the VM without restoring the snapshot to see how the malware behaves. Once the machine booted back on, I started FakeNet and I noticed it immediately started catching DNS request to zaaptoo.zapto.org as shown on the next picture:   
![PXL_20240409_072225489~2](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/1c73347d-6a6d-4d1a-b737-4a83f25f1dde)   

<br>

I went into the task manager but I couldnt find any suspicious processes, but when I went into the startup apps I found a executable with a strange name which appears to be md5 (just a supposition), and I also found windows.exe executables that should not be there. Searching in Google, I found that this is one of the things that this malware sets up.

![PXL_20240409_072506132](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/38a25399-018f-4574-8823-bfc37af6c46b)

