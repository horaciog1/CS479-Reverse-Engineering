# x86 Assembly Review Exercises, IDA and Ghidra

## Assembly Review Excercises
### Answer the following in complete sentences:

1. What is the difference between machine code and assembly?   
    `This is an answer`
2. If the ESP register is pointing to memory address 0x00000000001270A4 and I execute a pushq rax instruction, what address will rsp now be pointing to?   
    `This is an answer`
3. What is a stack frame?   
    `This is an answer`
4. What would you find in a data section?   
    `This is an answer`
5. What is the heap used for?   
    `This is an answer`
6. What is in the code section of a program's virtual memory space?   
    `This is an answer`
7. What does the inc instruction do, and how many operands does it take?   
    `The inc instruction increments the value of the specified operand by 1. It takes only one operand. For example, inc eax would increment the value in the eax register by 1.`
8. If I perform a div instruction, where would I find the remainder of the binary division (modulo)?   
    `According to the manual, after performing a div instruction, the remainder of the binary division would be stored in the RDX register on x86-64 architecture.`
9. How does jz decide whether to jump or not?   
    `This is an answer`
10. How does jne decide whether to jump or not?   
    `This is an answer`
11. What does a mov instruction do?   
    `This is an answer`
12. What does the TF flag do, and why is it useful for debugging?   
    `This is an answer`
13. Why would an attacker want to control the RIP register inside a program they want to take control of?   
    `This is an answer`
14. What is the ax register and how does it relate to rax?   
    `AX is the lower 16 bits of the RAX register. Similarly, AH represents the higher 8 bits, and AL represents the lower 8 bits. The RAX register is the 64-bit version, and then EAX (32 bits), AX (16 bits), AH (8 bits), and AL (8 bits). This distribution is better explained in the following image:`   
    <br>
    ![RAX](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/0a6377c1-c870-4dcb-bfca-681576f9369f)
 
16. What is the result of the instruction xor rax, rax and where is it stored?   
    `This is an answer`
17. What does the leave instruction do in terms of registers to leave a stack frame?   
    `This is an answer`
18. What pop instruction is retn equivalent to?   
    `This is an answer`
19. What is a stack overflow?   
    `This is an answer`
20. What is a segmentation fault (a.k.a. a segfault)?   
    `This is an answer`
21. What are the RSI and RDI registers for that gives them their name?   
    `This is an answer`

---
    
## Crackme

### Screenshots

### How you solved it, and what the solution was.

### Whether Ghidra or IDA was more helpful to you, and why.

  
