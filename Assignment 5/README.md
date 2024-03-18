# Reverse Engineering Ransomware
### Note: These are instructor-created (not a malware risk).   

<br>

# [ransomware1.zip](https://github.com/tolvumadur/Reverse-Engineering-Class/blob/main/Spring23/Samples/binaries/ransomware1.zip)
## Report and Decryption process
The decryption of the files encrypted by ransomware1 works by xoring all the bytes in the file with the char '4'. After the XOR operation, this new bytes are written to a new file called secret.txt and the file is finally decrypted.
### Decryption program
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
### secret.txt
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/9bf8fcd3-66b8-4277-8323-a39735d55bca)

### Screenshot of Ghidra inside decryption()
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/c13521ba-e254-4071-bce2-c9efba181b46)
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/969cb01e-5ddf-4925-9eae-54fa842037e3)



## [ransomware2.zip](https://github.com/tolvumadur/Reverse-Engineering-Class/blob/main/Spring23/Samples/binaries/ransomware2.zip)
## Report and Decryption process
The decryption of the files encrypted by ransomware1 works by xoring all the bytes in the file with the char '4'. After the XOR operation, this new bytes are written to a new file called secret.txt and the file is finally decrypted.
### Decryption program
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
### secret.txt
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/9bf8fcd3-66b8-4277-8323-a39735d55bca)

### Screenshot of Ghidra inside decryption()
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/c13521ba-e254-4071-bce2-c9efba181b46)
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/969cb01e-5ddf-4925-9eae-54fa842037e3)
