# More Advanced External Crackmes
### Note: Remember, in addition to being fun puzzles these may contain malware. If you are a grad student, you need to do any 3. Undergrads can complete any 2.

<br>

### Options:

The password to extract each of these is "crackmes.de"

[Crackme 1](https://crackmes.dreamhosters.com/users/seveb/crackme05/download/crackme05.tar.gz) (Make a program that can output valid serial numbers for crackme05, you get both a 32-bit and 64-bit version) 

[Crackme 2](https://crackmes.dreamhosters.com/users/adamziaja/crackme1/download/crackme1.tar.gz) (Make a program that can create valid username/password pairs to unlock the success response from crackme1) 

[Crackme 3](https://crackmes.dreamhosters.com/users/twistedtux/first_keygenme/download/keygenme.tgz) (Make a program to create valid passwords for keygenMe) 

[Crackme 4](https://crackmes.dreamhosters.com/users/hmx0101/decryptme_1/download/Decryptme%231.zip) (Figure out what key will decrypt the message in the pop-up box using DecryptMe -- This one runs in Windows) 

[Crackme 5](https://crackmes.dreamhosters.com/users/seveb/crackme04/download/crackme04.tar.gz) (Make a program that can output valid serial numbers for crackme04, you get both a 32-bit and 64-bit version. You don't need to change any of the other crackmes to solve them, but you do need to patch this one to get it past the self-destruct instructions so it will actually ask for a serial number) 

## Report and Decryption process
### Crackme 1 Solution (link/to/download/location):

To solve this crackme, you need to __________________________.

My solution is ____________________________. (If the crackme asks for a program, include your source code in a code block)

```
#!/usr/bin/env python3

print("This is the answer!")
```


### How I did it using Ghidra (and any other tools you used like gdb):

1. I opened the crackme in Ghidra
2. I found the `main` function and noticed three function calls.
3. The first one called `________` does ________. I can tell because ___________________.
4. etc.
5. Screenshots in here would be a nice touch -- especially if something is hard to describe in words. But images don't replace the need to explain what you did in enough detail that someone else could reproduce what you did.


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
