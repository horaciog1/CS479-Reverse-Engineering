# Reverse Engineering Report (Static Analysis): Win32.KeyPass

## Summary:
The Win32.KeyPass ransomware is a malicious program initially designed for Windows 7 that has been used to create similar ransomwares. The analysis reveals its functionality as a combination of a virus, trojan, and ransomware, disguising itself as Windows system file and possible installed/downloaded from fake installers. It exhibits potential for manual control but does not attempt to create backdoors or similar, and its encryption scheme employs the AES-256 algorithm. The malware is designed for Windows compatibility, identified by the presence of the string "!This program cannot be run in DOS mode" within the binary, indicative of the Windows Portable Executable (PE) file format.


## Malware Analysis:
### Type of Malware:
- **Category:** Ransomware, Crypto Virus, Files locker
- **File Type:** Win32 EXE / PE32 Executable
- **Target OS:** Microsoft Windows 7; using the strings command and CFF we can find a string "!This program cannot be run in DOS mode." within the binary, this reveals a significant association with the Windows Portable Executable (PE) file format. This string is a standard marker present in the header of Windows executable (.exe) files, indicating compatibility with the Windows operating system. The utilization of the PE format implies that the malware is designed to operate within the Windows ecosystem, this gives us a clue about its target OS.
- **Functionality:** Propagated through fake installers, encrypts files with AES-256 algorithm, exhibits potential for manual control. This malware could be categorized as a combination of a virus, a trojan, and a ransomware, since it needs user execution, it comes disguised a normal program and encrypts files in the infected system.

### Signatures:
Cybercriminals can edit their extension file types and the name of their malware or even change small pieces of code within their malware to avoid antivirus detection. Malware signatures are like unique fingerprints that help antivirus programs recognize and stop known types of malicious software. These signatures are specific patterns or characteristics found in the code or behavior of malware. When security software scans files or monitors system activities, it compares these patterns with a database of known malware signatures.Signatures help people recognize if they have the same malware. If every byte is exactly the same, the result of a cryptographic hash like SHA-256 (or weaker hashes like MD5) will match. Some of these hashes will completely change when something changes in the code, but when you use SSDEEP, it can compare how similar the malware is to other malware.   

The following hashes were obtained using the following linux commands:  `md5sum Win32.KeyPass.bin`, `sha1sum Win32.KeyPass.bin`, `sha256sum Win32.KeyPass.bin`, and `ssdeep Win32.KeyPass.bin`
- **File Hash (MD5):** `6999c944d1c98b2739d015448c99a291`
- **File Hash (SHA1):** `d9beb50b51c30c02326ea761b5f1ab158c73b12c`
- **File Hash (SHA-256):** `35b067642173874bd2766da0d108401b4cf45d6e2a8b3971d95bf474be4f6282`
- **File Hash (SSDEEP):** `49152:0u1ImfQE5L1PtWHeHoQAOs1dKvHHg/o2S1pj798JGKCO8C/eZRwCr:dzV5JPtWHeHoIs1dGHHx2S1998JGKCOC`
- **YARA Rule:**
```yara
rule malwareAnalysis {

}
```

### Indicator of Compromise (IoC):
- **File/Registry Changes:** The malware creates a file in Desktop called "!!!DECRYPTION__KEYPASS__INFO!!!.txt", I assume the ransomware encrypts all the files within a directory, changes the extension of the files to .KEYPASS and ransom notes are created inside the directory.
- The malware only encrypts the forst 5 mb of each file.
- According to AnyRun.com, the malware writes to a desktop.ini file (may be used to cloak folders)
- **Network Activities:** Since this is a static analysis, we cannot run the file. But in case we could, I would use wireshark to capture the network packets to see if the ransomware contacts a particular IP address or hostname.
- Strings tool showed that the malware tries to do a DNS request to `http://kronus.pp.ua/upwinload/get.php`
- There is also empty HTTP get request that appear when I used the strings command.
- Ransom Note:
```text
Attention! 

All your files, documents, photos, databases and other important files are encrypted and have the extension: .KEYPASS

The only method of recovering files is to purchase an decrypt software and unique private key.

After purchase you will start decrypt software, enter your unique private key and it will decrypt all your data.

Only we can give you this key and only we can recover your files.

You need to contact us by e-mail BM-2cUMY51WfNRG8jGrWcMzTASeUGX84yX741@bitmessage.ch send us your personal ID and wait for further instructions.

For you to be sure, that we can decrypt your files - you can send us a 1-3 any not very big encrypted files and we will send you back it in a original form FREE.

Price for decryption $300. 

This price avaliable if you contact us first 72 hours.

E-mail address to contact us:

BM-2cUMY51WfNRG8jGrWcMzTASeUGX84yX741@bitmessage.ch

Reserve e-mail address to contact us:

keypassdecrypt@india.com

Your personal id:
6se9RaIxXF9m70zWmx7nL3bVRp691w4SNY8UCir0

BM-2cUMY51WfNRG8jGrWcMzTASeUGX84yX741@bitmessage.ch

keypassdecrypt@india.com
 ```

### Clues about Origin:
- **Similar Malware:** This type of ransomware has been replicated a lot of times. There are several ransomware that utilize the KEYPASS extension file and are variants of this malware. One of them is the "STOP Ransomware" which I suspect is the parent malware and Win32.KEYPASS is a variant and/or derivation of the STOP ransomware. 
- **File/Strings Similarities:** All of the Ransomware variants of this malware that have the KEYPASS extension use the same ransom note.
- **Geographical Clues:** The binary analysis did not yield specific details regarding the geographical origin of the malware. However, a subsequent Google search using the malware signatures revealed instances of files containing Russian text. Notably, these files employed Russian characters, which fall within the Unicode block known as Cyrillic in UTF-8 encoding. Furthermore, the dialog box associated with the malware exhibited subpar English, leading to the inference that the attacker likely originates from outside the United States.

### C2 Infraestructure:
- **Command and Control (C2):**

### Additional Insights:
- Bitcoin-related images were discovered in the Icons folder using CFF Explorer. These images varied in size and resolution, indicating a potential adaptation for optimal display on diverse screen resolutions across computers.
- 


## Conclusion:
The analyzed file Win32.KeyPass.exe is identified as a variant of the STOP ransomware. This ransomware is known for encrypting files on the infected system and demanding a ransom for decryption. The behavior analysis indicates malicious activities such as encrypting files, creating ransomware instruction files, and modifying system folders. The static analysis reveals the presence of characteristics consistent with ransomware.
