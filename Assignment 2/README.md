# Reverse Engineering Report (Static Analysis): Win32.KeyPass

## Summary:
Briefly summarize the key findings and actionable information.  

## Malware Analysis:
### Type of Malware:
- **Category:** Ransomware
- **File Type:** Win32 EXE / PE32 Executable
- **Target OS:** Microsoft Windows; using the strings command and CFF we can find a string "!This program cannot be run in DOS mode." within the binary, this reveals a significant association with the Windows Portable Executable (PE) file format. This string is a standard marker present in the header of Windows executable (.exe) files, indicating compatibility with the Windows operating system. The utilization of the PE format implies that the malware is designed to operate within the Windows ecosystem, this gives us a clue about its target OS.
- **Functionality:** Worm-like propagation, Crypto-ransomware

### Signatures:
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
- **File/Registry Changes:**
- **Network Activities:**

### Clues about Origin:
- **Similar Malware:**
- **File/Strings Similarities:**
- **Geographical Clues:**

### C2 Infraestructure:
- **Command and Control (C2):**

## Conclusion:
