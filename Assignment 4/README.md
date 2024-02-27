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

## [ezcrackme3.zip ](https://github.com/tolvumadur/Reverse-Engineering-Class/blob/main/Spring23/Samples/binaries/ezcrackme3.zip)
### Reverse Engineering Report
This crackme was a little bit more complicated because when I tried to use FLOSS or strings on it it gave me two different suspicious strings: `strawberry` and `kiwi`. I tried to use both strings as passwords but none of them worked.   

![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/b822cfc2-7969-440d-8c5d-9ac695a91a07)

<br>
After this, I decided to open the file in Ghidra. First, I scanned the code from bottom to top, and after inspecting the code for a little bit I changed the variable names to more compelling names.   

![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/b49a1418-fe7c-4cbc-bab3-d2a06fb3a0b5)   

I noticed all variables were set to 0. I also notice that the `getinput()` function was being called with two arguments that after inspecting inside the function, I assumed were the input from the user (or password being used) and the size of the password. I got that idea from the fact that `getinput()` was using the library function `strlen()` to what I assumed was the size of the input.   

![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/0d8e3ff4-8e86-45bc-8613-ab3268ee314c)   

Then going back to the main function, I notice that lines 30 and 31 were using a library function called `strcat()` which according to the website Programiz.com, it is used to concatenate two variables.

The function definition of `strcat()` is:
>char *strcat(char *destination, const char *source)

local38 was null, so then after the first `strcat()` function it will be `strawberry `, and after the second call of the function, it will be `strawberrykiwi`.   

![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/ea3dd0a5-86db-4d88-b0a8-c539e33d22f6)   



### Keygen (python3)
````python
#!/usr/bin/env python3

import string

print("strawberrykiwi")
````
#### How to make run the keygen on Linux
To run the following keygen script you will need to make it an executable. To achieve that you will need the following command, where "nameOfTheScript" is the name that you put to the file:
```bash
chmod +x nameOfTheScript.py
```
To run the crackme with the keygen you will need:
```bash
./nameOfTheScript.py | ./easy_crackme_3  
```
If you want to see the output that the keygen generates, you can use:
```bash
./nameOfTheScript.py
```





















