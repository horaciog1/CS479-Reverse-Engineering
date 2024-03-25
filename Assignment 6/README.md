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
### Crackme 1 Solution ([download file](https://crackmes.dreamhosters.com/users/seveb/crackme05/download/crackme05.tar.gz)):

To solve this crackme, you need to __________________________.

My solution is ____________________________. (If the crackme asks for a program, include your source code in a code block)

keygen:
```python3
#!/usr/bin/env python3

import random
import string

def generate_serial():
    # Generate 11th and 9th characters satisfying condition
    while True:
        char_11 = random.choice(string.ascii_letters + string.digits)
        char_9 = random.choice(string.ascii_letters + string.digits)
        var1 = ord(char_11) ^ ord(char_9)
        if 0 <= var1 < 10:
            break

    # Generate 14th and 6th characters satisfying condition
    while True:
        char_14 = random.choice(string.ascii_letters + string.digits)
        char_6 = random.choice(string.ascii_letters + string.digits)
        var2 = ord(char_14) ^ ord(char_6)
        if 0 <= var2 < 10:
            break

    # Calculate characters based on conditions
    var1 += 48
    var2 += 48
    char_1 = chr(var2)
    char_4 = chr(var1)
    char_16 = chr(var1)
    char_19 = chr(var2)

    # Generate 2nd, 3rd, 17th, and 18th characters satisfying conditions
    while True:
        char_3 = random.choice(string.ascii_letters + string.digits)
        char_2 = random.choice(string.ascii_letters + string.digits)
        char_17 = random.choice(string.ascii_letters + string.digits)
        char_18 = random.choice(string.ascii_letters + string.digits)
        if (ord(char_3) + ord(char_2) >= 171) and \
           (ord(char_17) + ord(char_18) >= 171) and \
           ((ord(char_3) + ord(char_2)) != (ord(char_17) + ord(char_18))):
            break

    # Generate other characters
    char_5 = '-'
    char_7 = random.choice(string.ascii_letters + string.digits)
    char_8 = random.choice(string.ascii_letters + string.digits)
    char_10 = '-'
    char_12 = random.choice(string.ascii_letters + string.digits)
    char_13 = random.choice(string.ascii_letters + string.digits)
    char_15 = '-'

    # Construct the serial
    serial = char_1 + char_2 + char_3 + char_4 + char_5 + char_6 + char_7 + char_8 + char_9 + char_10 + \
             char_11 + char_12 + char_13 + char_14 + char_15 + char_16 + char_17 + char_18 + char_19

    return serial

# Generate and print a serial
print(generate_serial())

```


#### How to run the keygen on Linux
To run the keygen script, you will need to make it executable. To achieve that, you will need the following command, where "nameOfTheScript" is the name that you put to the file:

```bash
chmod +x nameOfTheScript.py
```
To run the crackme with the keygen, you will need:

```bash
./nameOfTheScript.py | xargs  ./control_flow_2
```
If you want to see the output that the keygen generates, you can use:
```bash
./nameOfTheScript.py
```


### How I did it using Ghidra (and any other tools you used like gdb):

1. I opened the crackme in Ghidra
2. I found the `main` function and noticed three function calls.
3. The first one called `________` does ________. I can tell because ___________________.
4. etc.
5. Screenshots in here would be a nice touch -- especially if something is hard to describe in words. But images don't replace the need to explain what you did in enough detail that someone else could reproduce what you did.
