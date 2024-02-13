# Reverse Engineering Report (Static Analysis): Win32.KeyPass

## Summary:
Briefly summarize the key findings and actionable information.  

## Malware Analysis:
### Type of Malware:
- **Category:** Ransomware
- **Target OS:** Microsoft Windows; using the strings command and CFF we can find a string "!This program cannot be run in DOS mode." within the binary, this reveals a significant association with the Windows Portable Executable (PE) file format. This string is a standard marker present in the header of Windows executable (.exe) files, indicating compatibility with the Windows operating system. The utilization of the PE format implies that the malware is designed to operate within the Windows ecosystem, this gives us a clue about its target OS.
- **Functionality:** Worm-like propagation, Crypto-ransomware

### Signatures:
- **File Hash (MD5):**
- **File Hash (SHA1):**
- **File Hash (SHA-256):**
- **YARA Rule:**
```yara
rule malwareAnalysis {

}
```

### Indicator of Compromise (IoC):
- **File/Registry Changes:**
- **Network Activities:**

### Clues about Origin:
- **Similar Malware:**
- **File/Strings Similarities:**
- **Geographical Clues:**

### C2 Infraestructure:
- **Command and Control (C2):**

## Conclusion:
