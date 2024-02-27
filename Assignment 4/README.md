# Binary Reverse Engineering with Crackmes
### Note: These are instructor-created (not a malware risk).   

## [ezcrackme1.zip](https://github.com/tolvumadur/Reverse-Engineering-Class/blob/main/Spring23/Samples/binaries/ezcrackme1.zip)
### Reverse Engineering Report
For this crack-me I used the `strings easy_crackme_1` command from linux to extract the strings from the executable. I usually use this command before starting to reverse engineer since there exists a posibility that I can get something useful from the output of the `strings`command. Scrapping trough the output I found a particular string `picklecucumberl337`. I also used `floss easy_crackme_1 --format sc64` to see if I could get the same output but on the Windows VM. And they were the same. After running the file with the string I found it turns out is the correct key.   
<br>
*Output of strings command*   
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/a1f3132e-d728-4404-be1d-9b00379f6137)     


*Entering password*   
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/fe238053-ae65-414e-83e4-c9b0de11a83b)   

### Keygen (python3)
````python
#!/usr/bin/env python3

import string

print("picklecucumberl337")
````
#### How to make run the keygen on Linux
To run the following keygen script you will need to make it an executable. To achieve that you will need the following command, where "nameOfTheScript" is the name that you put to the file:
```bash
chmod +x nameOfTheScript.py
```
To run the crackme with the keygen you will need:
```bash
./nameOfTheScript.py | ./easy_crackme_1  
```
If you want to see the output that the keygen generates, you can use:
```bash
./nameOfTheScript.py
```
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/31b24398-b992-4677-92cd-4b95e16318e1)

---   
<br>
  
## [ezcrackme2.zip](https://github.com/tolvumadur/Reverse-Engineering-Class/blob/main/Spring23/Samples/binaries/ezcrackme2.zip)
### Reverse Engineering Report
Also for this crack-me, the same method used in the past crack-me can be applied for `easy_crackme_2`. So then using the `strings easy_crackme_2` command we get `artificialtree`.
After running the file with the string I found it turns out is the correct key.   
<br>
*Output of strings command*   
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/7de75813-3c5e-45ea-a4e3-4d220db4323a)   


*Entering password*   
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/478f4bff-0ee0-40ed-8a5f-ceedbe283ec7)

### Keygen (python3)
````python
#!/usr/bin/env python3

import string

print("artificialtree")
````
#### How to make run the keygen on Linux
To run the following keygen script you will need to make it an executable. To achieve that you will need the following command, where "nameOfTheScript" is the name that you put to the file:
```bash
chmod +x nameOfTheScript.py
```
To run the crackme with the keygen you will need:
```bash
./nameOfTheScript.py | ./easy_crackme_2  
```
If you want to see the output that the keygen generates, you can use:
```bash
./nameOfTheScript.py
```
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/b7d66d29-e9a0-4a37-8d52-7c9c9de160b4)

---
<br>

## [ezcrackme3.zip](https://github.com/tolvumadur/Reverse-Engineering-Class/blob/main/Spring23/Samples/binaries/ezcrackme3.zip)

### Reverse Engineering Report

This crackme was a little more complicated because when I tried to use FLOSS or strings on it, it gave me two different suspicious strings: `strawberry` and `kiwi`. I tried using both strings as passwords, but none of them worked.

![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/b822cfc2-7969-440d-8c5d-9ac695a91a07)

After this, I decided to open the file in Ghidra. First, I scanned the code from bottom to top, and after inspecting the code for a little bit, I changed the variable names to more compelling names.

![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/b49a1418-fe7c-4cbc-bab3-d2a06fb3a0b5)

I noticed all variables were set to 0. I also noticed that the `getinput()` function was being called with two arguments that, after inspecting inside the function, I assumed were the input from the user (or password being used) and the size of the password. I got that idea from the fact that `getinput()` was using the library function `strlen()` for what I assumed was the size of the input.

![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/0d8e3ff4-8e86-45bc-8613-ab3268ee314c)

Then, going back to the main function, I noticed that lines 30 and 31 were using a library function called `strcat()`, which, according to the website Programiz.com, is used to concatenate two variables.

The function definition of `strcat()` is:

>char *strcat(char *destination, const char *source)

`local38` was null, so after the first `strcat()` function, it would be `strawberry`, and after the second call of the function, it would be `strawberrykiwi`.

![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/ea3dd0a5-86db-4d88-b0a8-c539e33d22f6)

Then, line 32 compares the input from the user with the string "kiwi", and if they are the same, variable `ifKIWI` is equal to 0; otherwise, it's another number. The same happens on line 33; the input from the user is compared with `local_38`, which is equal to "strawberrykiwi". If they are equal, the `strawberrykiwi` variable will be set to 0; otherwise, another number. Line 34 means that if variable `strawberrykiwi` is different than 0 (is not "strawberrykiwi"), then that is stored in a variable called `false`. Line 35 compares the password with the string "strawberry", and if they match, the variable `strawberrykiwi` will be set to 0; otherwise, another number.

If the password entered was "strawberrykiwi", then we will skip the if statement on line 36 since none of the arguments is true. We will end up on the else statement on line 40, meaning that we cracked the program.   

![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/119b747a-81c8-4306-9f3f-134bc5eb6bb3)


### Keygen (Python3)
```python
#!/usr/bin/env python3

import string

print("strawberrykiwi")
```

#### How to make run the keygen on Linux
To run the keygen script, you will need to make it executable. To achieve that, you will need the following command, where "nameOfTheScript" is the name that you put to the file:

```bash
chmod +x nameOfTheScript.py
```
To run the crackme with the keygen, you will need:

```bash
./nameOfTheScript.py | ./easy_crackme_3  
```
If you want to see the output that the keygen generates, you can use:
```bash
./nameOfTheScript.py
```

![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/b362327e-6a65-4367-97e2-f99f6be43415)

---   

<br>


## [controlflow1-1.zip](https://github.com/tolvumadur/Reverse-Engineering-Class/blob/main/Spring23/Samples/binaries/controlflow1-1.zip)
### Reverse Engineering Report
In order for a generated key to be accepted, it must adhere to specific rules to ensure its validity. The key must consist of 16 characters or more, with predetermined characters at specific positions. The 1st character is fixed as 'A', the 2nd character as '6', the 4th character as '2', the 8th character as '%', and the 16th character as '*'. The remaining characters are subject to randomness and can be any ASCII characters. This script generates unique 16-character passwords with each execution.

To summarize, the rules that the generated key must follow are the following:
- Password must be at least 16 characters long.
- Must contain a 'A' in the 1st position
- Must contain a '6' in the 2nd position
- Must contain a '2' in the 4th position
- Must contain a '%' in the 8th position
- Must contain a '*' in the 16th position

![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/9dc0081b-daf9-4ca0-86e4-054cdab1700c)   
*execution*   
  

### Example passwords generated by the script
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/a703e8db-943f-41b5-b245-331d61ac3e17)


### Keygen (Python3)
```python
#!/usr/bin/env python3

import random
import string

def generate_password():
    fixed_chars = ['A', '6', None, '2', None, None, None, '%', None, None, None, None, None, None, None, '*']

    # Fill in the random characters for the positions without fixed characters
    for i in range(len(fixed_chars)):
        if fixed_chars[i] is None:
            fixed_chars[i] = random.choice(string.ascii_letters + string.digits)

    # Convert the array to a string
    password = ''.join(fixed_chars)

    return password

print(generate_password())
```

#### How to make run the keygen on Linux
To run the keygen script, you will need to make it executable. To achieve that, you will need the following command, where "nameOfTheScript" is the name that you put to the file:

```bash
chmod +x nameOfTheScript.py
```
To run the crackme with the keygen, you will need:

```bash
./nameOfTheScript.py | xargs  ./control_flow_1
```
If you want to see the output that the keygen generates, you can use:
```bash
./nameOfTheScript.py
```   

![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/9be4e356-7d20-44cb-a129-9be7234373d9)   

---   

<br>

## [controlflow1-2.zip](https://github.com/tolvumadur/Reverse-Engineering-Class/blob/main/Spring23/Samples/binaries/controlflow2-1.zip)
### Reverse Engineering Report
In order for a generated key to be accepted, it must adhere to specific rules to ensure its validity. The key must consist of 16 characters or more, with predetermined characters at specific positions. The 7th character is fixed as 'Y', the 9th character as '#', the 11th character as 'A', the 12th character as '*', and the 14th character as '6'. The remaining characters are subject to randomness and can be any ASCII characters. This script generates unique 16-character passwords with each execution.

To summarize, the rules that the generated key must follow are the following:
- Password must be at least 16 characters long.
- Must contain a 'Y' in the 7st position
- Must contain a '#' in the 9nd position
- Must contain a 'A' in the 11th position
- Must contain a '*' in the 12th position
- Must contain a '6' in the 14th position

![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/271e70b1-cfb7-4ca0-b4a4-ab762db4a560)   
*execution*   
  

### Example passwords generated by the script
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/864dd4ec-2793-43d7-9d64-75f68a53671a)   


### Keygen (Python3)
```python
#!/usr/bin/env python3

import random
import string

def generate_password():
    fixed_chars = [None, None, None, None, None, None, 'Y', None, '#', None, 'A', '*', None, '6', None, None]

    # Fill in the random characters for the positions without fixed characters
    for i in range(len(fixed_chars)):
        if fixed_chars[i] is None:
            fixed_chars[i] = random.choice(string.ascii_letters + string.digits)

    # Convert the array to a string
    password = ''.join(fixed_chars)

    return password

print(generate_password())

```

#### How to make run the keygen on Linux
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
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/39fa88a8-e47f-4133-9a03-6710ed398377)
















