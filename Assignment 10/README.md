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


