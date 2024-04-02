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


<br>

### Crackme 4 Solution ([download](https://crackmes.dreamhosters.com/users/hmx0101/decryptme_1/download/Decryptme%231.zip)):

To solve this crackme, you need to enter the right key to decrypt the message. A windows appears after you enter the key and outputs a message.
My solution is a bruteforce attack on the keys until the right message appears. After inputting keys by hand, I figured out that the message was most likely to be "Well Done!, Congratulations!!!". This was my hypothesis after entering keys that improve the output every time I tried a new key.
I decided it was going to take to much time to brute force the message by hand, so I decided to reverse engineer the decryptme to se if I could find the decryption process and ciphertext. After finding both, the ciphertext and decryption process, i made a python script to brute force and output the different messages with different keys. The ciphertext was 30 Bytes long which is the same size as the string. These are the bytes: `0x74, 0x66, 0x6f, 0x6f, 0xc3, 0x47, 0x6c, 0x6d, 0x66, 0xc2, 0xaf, 0xc3, 0x60, 0x6c, 0x6d, 0x64, 0x71, 0x82, 0x17, 0x16, 0x6f, 0x82, 0x17, 0x6a, 0x6c, 0x6d, 0x70, 0xc2, 0xc2, 0xc2`. Assuming each byte is a character, then for example 0x74 is a byte, which is the same as 8 bits, so to bruteforce it we would need 2^8 = 256 different keys. Thus we want to try using the numbers from 0 to 255 which are all the possible keys. The key that worked in that range are `126` and `254`, I noticed there are other numbers that yield the same result. The difference between 254 and 126 is 128; if you multiply every number by 128, the result of the multiplication will also serve as a key. For example `2x128 = 254`, `3x128 = 384`, `4x128 = 512`, `5x128 = 640`, `6x128 = 768`, and so on.

```python3
#!/usr/bin/env python3

ciphertext = [0x74, 0x66, 0x6f, 0x6f, 0xc3, 0x47, 0x6c, 0x6d, 0x66, 0xc2, 
              0xaf, 0xc3, 0x60, 0x6c, 0x6d, 0x64, 0x71, 0x82, 0x17, 0x16, 
              0x6f, 0x82, 0x17, 0x6a, 0x6c, 0x6d, 0x70, 0xc2, 0xc2, 0xc2]

# 2^8 possible keys
for keys in range(0,256):
    plaintext = ""
    for i in ciphertext: 
        chars =  (( (i - 0x2644) ^ 0x0dead) + 10) - keys
        chars ^= keys
        plaintext += chr(chars & 0xff)      # apply the bitwise AND, and concatenate characters 
    print("Key: %s" % (keys,))
    print("Text: %s\n\n" % (plaintext,))
```


### How I did it using Ghidra (and any other tools you used like gdb):

1. I opened the crackme in Ghidra and in IDA. IDA does a better job at recognizing the functions of programs and import them. So I used both, side-by-side, to analyze the crackme. I really like the pseudocode and interface from Ghidra, but IDA does a great job with the functions.
2. I found an "OK!" string which was associated with the windows, so I decided it was a good place to start. I use the flow diagram to analyze how the program was behaving.
3. I went inside all the functions until I found one subroutine that caught my attention because it had an interesting pattern with a lot of math operations that for me seem that someone was using obfuscation to hide something in there.
4. The subroutine with the math operations was at `0x00013E1C`. And after examining it for a long time, and seeing where was this subroutine/function called, I decided to name it `decryption`.
5. The ciphertext was passed to the decryption function using the eax register and it can be seen at 0x00014019.
6. Then the decryption occurs, where each character/byte is put into a series of operations:  `( ( (char - 0x2644) XOR 0x0dead) + 10) - key_Or_User_input`, then later all that is XOR with the key, and finally that whole number is bitwise AND with 0xFF and concatenated with an empty string that will start we will start filling with the other decrypted characters.
7. Unfortunately, my computer start crashing when I had important advances, and I could take a lot of pictures since a loose a big part of my unsaved progress.

![WhatsApp Image 2024-04-02 at 1 47 52 AM](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/57bede2d-9a7f-4805-819f-5e0bf783341b)






