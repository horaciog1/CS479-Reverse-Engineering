# Dynamic Analysis
On this week's report, we will perform dynamic analysis of a RAT, a Remote Access Trojan. We will analyze its behavior to quickly identify indicators
of compromise that could be used to detect this malware in the wild. The The RAT we will be looking at will come from the ZOO library used in assignment 2.
It is called NjRAT. Watch out that there is a Win32.NjRAT version and a plain NjRAT version. We will use the latter.
`hxxps://github.com/ytisf/theZoo/archive/refs/heads/master.zip`   This link will automatically download the malware library so be careful. You only need to change
`hxxps` for `https`.

## OSINT Investigation
Start your report this week by summarizing what others have already written about NjRAT. A good place to start is [Wikipedia](https://en.wikipedia.org/wiki/NjRAT) and its reference list. Include at least a paragraph about when NjRAT first appeared, and where it has been seen or used since. Cite your sources by including a URL to them. 

Each fact you state must be cited. For this assignment, the Wikipedia page is not allowed as a source to encourage you to look further.

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
