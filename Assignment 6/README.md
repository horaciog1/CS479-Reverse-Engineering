# Reverse Engineering Ransomware
### Note: These are instructor-created (not a malware risk).   

<br>

# [ransomware1.zip](https://github.com/tolvumadur/Reverse-Engineering-Class/blob/main/Spring23/Samples/binaries/ransomware1.zip)
## Report and Decryption process
The decryption process for files encrypted by ransomware1 involves XORing all the bytes in the encrypted file with the character '4'. After performing the XOR operation, the resulting bytes are written to a new file named "secret.txt". This file contains the decrypted data. The decryption script provided below automates this process. To use it, provide the path to the encrypted file as the input and specify the desired output filename. The script will then perform the decryption and save the decrypted content to the specified file.   

### Decryption program

To make decrypt.py executable, type:
```bash
chmod +x decrypt.py
```

decrypt.py
```python3
#!/usr/bin/env python3

import sys

if (len(sys.argv)!=3):
    print("Usage: decrypt.py INFILE OUTFILENAME")

infile = sys.argv[1]
outfile = sys.argv[2]
key = ord('4')

with open(infile, "rb") as inf:
    with open(outfile, "wb") as ouf:

        contents = inf.read()
        
        for b in contents:
            ouf.write((b ^ key).to_bytes(1, "big"))


````
