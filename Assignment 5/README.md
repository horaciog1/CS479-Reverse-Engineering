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
### secret.txt
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/9bf8fcd3-66b8-4277-8323-a39735d55bca)

### Screenshot of Ghidra inside decryption()
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/c13521ba-e254-4071-bce2-c9efba181b46)
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/969cb01e-5ddf-4925-9eae-54fa842037e3)



## [ransomware2.zip](https://github.com/tolvumadur/Reverse-Engineering-Class/blob/main/Spring23/Samples/binaries/ransomware2.zip)
## Report and Decryption process
The decryption process for files encrypted by ransomware2 involves XORing each byte of the encrypted file with a corresponding character from the string "1337". This process is achieved by iterating through each byte of the encrypted file and performing an XOR operation with the character from the "1337" string that corresponds to the current position. After this XOR operation, the resulting bytes are written to a new file specified by the user. The decryption script provided below automates this process, enabling users to decrypt files encrypted by ransomware2. To use the script, users need to provide the path to the encrypted file as input and specify the desired output filename. Upon execution, the script decrypts the file and saves the decrypted content to the specified file.
Note the use of bytearray() to store the decrypted bytes before writing them to the output file. Also, ord() is used to get the ASCII value of each character in the key for XOR operation. Finally, the modulo operation (%) is used to loop over the key characters if the encrypted file is longer than the key.   


### Decryption program

To make decrypt.py executable, type:
```bash
chmod +x decrypt.py
```

decrypt.py
```python3
#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("Usage: decrypt.py INFILE OUTFILENAME")
    sys.exit(1)

infile = sys.argv[1]
outfile = sys.argv[2]
key = "1337"

with open(infile, "rb") as inf:
    with open(outfile, "wb") as ouf:
        contents = inf.read()
        decrypted_contents = bytearray()

        # XOR each byte with the corresponding character from the key
        for i in range(len(contents)):
            decrypted_byte = contents[i] ^ ord(key[i % len(key)])
            decrypted_contents.append(decrypted_byte)

        ouf.write(decrypted_contents)
````
### secret.txt
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/c4d21dc6-932d-43db-9f02-a73be7454a03)


### Screenshot of IDA inside decryption()
For this particular ransomware, I initially struggled to understand the decompilation process using Ghidra since there was a lot of unrecognized functions. To gain a better understanding, I decided to experiment with IDA. Upon decompiling the file with IDA, everything became clearer. Unlike Ghidra, IDA was proficient at recognizing the C library functions, which significantly streamlined the analysis process. Analyzing the ransomware became notably easier and more intuitive with IDA, allowing for a more comprehensive understanding of its inner workings.   

