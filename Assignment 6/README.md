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

To solve this crackme, you need to generate a serial with the following requierements:
- Serial must be 19 characters long
- Serial can only have uppercase letters, lowercase letters, and numbers
- Character 5th must be '-'
- Character 10th must be '-'
- Character 15th must be '-'
- Characters 7th, 8th, 12th, 13th can be any ascii letter or digit
- 0 <= char_11 XOR char_9 < 10
- 0 <= char_14 XOR char_6 < 10
- Character 4th must be equal to the ascii char ( (char_11 XOR char_9) + 48 )
- Character 1st must be equal to the ascii char ( (char_14 XOR char_6) + 48 )
- Character 16th must be equal to the ascii char ( (char_11 XOR char_9) + 48 )
- Character 19th must be equal to the ascii char ( (char_14 XOR char_6) + 48 )
- Using the decimal numbers from the ascii chars: `(char_3 + char_2 >= 171)` and `(char_17 + char_18 >= 171)` but `(char_3 + char_2) !=  (char_17 + char_18)`


My solution is python script that can output different serials that follow the requierements of the crackme.

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
chmod +x serial_keygen.py
```
To run the crackme with the keygen, you will need:

```bash
./serial_keygen.py | xargs ./crackme05_64bit
```
If you want to see the output that the keygen generates, you can use:
```bash
./serial_keygen.py
```


### How I did it using Ghidra:

1. I opened the crackme in Ghidra
2. I found the `main` function and noticed five interesting function calls called: `rock`, `paper`, `scissors`, `cracker`, and `decraycray`. The first four functions called another function in case the requierements of the serial were not meet named `bomb` which prints a bomb and calls another function called `decraycray` which prints a phrase, and ends the program.
3. The first one called `rock` checks that the serial is 19 characters long, does not include other characters that are not letters or digits (with an exception of `-`). I can tell because of the if functions and the paramaters that they are checking. 
4. The second one, `paper`, checks the conditions for the 11th, 9th, 14th, 6th, 4th, 16th, 19th, and 1st characters. If these conditions arent met it calls bomb to end the program. I can tell that once again because of the if statements and the conditions those if statements are checking.
5. The third one, `scissors`, checks the conditions for the 3rd, 2nd, 18th, and 17th. If these conditions arent met it calls bomb to end the program. I can tell that once again because of the if statements and the conditions those if statements are checking.
6. The fourth one, `cracker`, checks the conditions for the 5th, 10th, and 15th characters, which makes sure those are `-`. If these conditions arent met it calls bomb to end the program. I can tell that once again because of the if statements and the conditions those if statements are checking.
7. 
main function   
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/bbdce8e6-c67a-43ec-98ae-eccbbe4f53bd)


rock function   
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/a4022d24-9fbb-4e32-8929-4042cf070ec7)    


paper function   
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/8481de00-67d5-4bc0-b13e-d2ff6b1f8a8e)    


scissors function    
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/adfddc94-586c-4752-9d9b-ac175067780e)   


cracker function    
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/c4a8c8e4-104e-41b3-943e-5d373399596e)    


decraycray function    
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/f4b87c80-6378-4035-a435-406e44f75382)    


bomb function    
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/0a90b17b-33f2-445f-ae99-6b4276acb3d5)   







