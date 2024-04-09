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

According to [Any.run](https://any.run/malware-trends/njrat) this malware was formaly seen in 1 January, 2013 and last seen 9 April, 2024; being this one of the most popular malware in the world. Newer version of the malware are also refered as `Njw0rm`. Here are some of the places where it has been recently seen: ![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/e73c2379-c020-47ef-bf2c-d0bb06898223)


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
- Does this appear to be for persistence, or something else?
- What clues (Indicators of Compromise) could someone look for in their filesystem to detect this NjRAT infection?

## FakeNet
FakeNet is an open-source tool primarily used for dynamic malware analysis and network traffic analysis. It is designed to simulate a network environment, allowing researchers and analysts to observe how malware interacts with the network without exposing real systems to potential harm.

You may need to set up a network interface on your VM. Most hypervisors will allow you to create a non-Internet-connected interface. FakeNet-NG will show a live feed of network activity when it is running properly, and you should take note of what Windows is already doing in the background.

**Note in your report the answers to these questions:** 
- What did NjRAT do on the network?
- What DNS name(s) did it look up?
- Investigate that DNS name -- is this a known malicious domain, or an attacker abusing a legitimate service? Why do you think so?
- What indicators of compromise could a network administrator look for to identify if any of their machines are infected with this same malware?
