# Binary Reverse Engineering with Crackmes
### Note: These are instructor-created and so not a malware risk.   

## [ezcrackme1.zip](https://github.com/tolvumadur/Reverse-Engineering-Class/blob/main/Spring23/Samples/binaries/ezcrackme1.zip)
For this crack-me I used the `strings easy_crackme_1` command from linux to extract the strings from the executable. I usually use this command before starting to reverse engineer since there exists a posibility that I can get something useful from the output of the `strings`command. Scrapping trough the output I found a particular string `picklecucumberl337`. I also used `floss easy_crackme_1 --format sc64` to see if I could get the same output but on the Windows VM. And they were the same. After running the file with the string I found it turns out is the correct key.   
<br>
*Output of strings command*   
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/a1f3132e-d728-4404-be1d-9b00379f6137)     


*Entering password*   
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/fe238053-ae65-414e-83e4-c9b0de11a83b)   
  
## [ezcrackme2.zip](https://github.com/tolvumadur/Reverse-Engineering-Class/blob/main/Spring23/Samples/binaries/ezcrackme2.zip)
Also for this crack-me, the same method used in the past crack-me can be applied for `easy_crackme_2`. So then using the `strings easy_crackme_2` command we get `artificialtree`.
After running the file with the string I found it turns out is the correct key.   
<br>
*Output of strings command*   
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/7de75813-3c5e-45ea-a4e3-4d220db4323a)   


*Entering password*   
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/478f4bff-0ee0-40ed-8a5f-ceedbe283ec7)


## [ezcrackme3.zip ](https://github.com/tolvumadur/Reverse-Engineering-Class/blob/main/Spring23/Samples/binaries/ezcrackme3.zip)
