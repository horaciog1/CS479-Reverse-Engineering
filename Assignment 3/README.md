# x86 Assembly Review Exercises, IDA and Ghidra

## Assembly Review Excercises
### Answer the following in complete sentences:

1. What is the difference between machine code and assembly?   
        `The main difference between machine code and assembly, is that machine code is only understand by the computers and is very difficult to understand by the human beings, it is the low-level binary representation of instructions that a computer's CPU can directly execute. It is represented by 0s and 1s. Assembly language, on the other hand, is a human-readable, symbolic representation of machine code instructions. It uses mnemonics and symbols to represent operations and operands, making it easier for programmers to write and understand code. `
2. If the ESP register is pointing to memory address 0x00000000001270A4 and I execute a pushq rax instruction, what address will rsp now be pointing to?   
    `When you execute a pushq rax instruction in x86-64 assembly, it will push the value of the rax register onto the stack, and the stack pointer (rsp) will be adjusted accordingly. Since the pushq instruction pushes a quadword (64 bits) onto the stack, rsp will be decremented by 8 bytes. So, if ESP is initially pointing to memory address 0x00000000001270A4, after the pushq rax instruction, it will be pointing to 0x000000000012709C.`
3. What is a stack frame?   
    `A stack frame is a portion of a program's call stack that contains local variables, function parameters, and other information needed for a specific function's execution. It is created when a function is called and typically includes a return address, saved registers, and space for local variables. The stack frame is essential for maintaining the function's state and facilitating the return from the function. I like to think it like a temporary workspace for a function. When a function is called, the computer sets up this workspace in the computer's memory to keep things organized.`
4. What would you find in a data section?   
    `In a data section, you would find initialized static variables and constants. These variables have predetermined values specified by the programmer and are stored in the program's memory when it is loaded.f`
5. What is the heap used for?   
    `This is an answer`
6. What is in the code section of a program's virtual memory space?   
    `This is an answer`
7. What does the inc instruction do, and how many operands does it take?   
    `The inc instruction increments the value of the specified operand by 1. It takes only one operand. For example, inc eax would increment the value in the eax register by 1.`
8. If I perform a div instruction, where would I find the remainder of the binary division (modulo)?   
    `According to the manual, after performing a div instruction, the remainder of the binary division would be stored in the RDX register on x86-64 architecture.`
9. How does jz decide whether to jump or not?   
    `The jz (jump if zero) instruction checks the zero flag (ZF) in the processor's flags register. If the zero flag is set (indicating that the result of a previous operation was zero), the jz instruction will jump to the specified target address.`
10. How does jne decide whether to jump or not?   
    `The jne (jump if not equal) instruction checks the zero flag (ZF) in the processor's flags register. If the zero flag is not set (indicating that the result of a previous operation was not zero), the jne instruction will jump to the specified target address.`
11. What does a mov instruction do?   
    `The mov (move) instruction copies data from a source operand to a destination operand. It is used to transfer values between registers, memory locations, or immediate values.`
12. What does the TF flag do, and why is it useful for debugging?   
    `The TF (trap flag) is a flag in the processor's flags register. When the TF flag is set, the processor enters single-step mode, which causes it to generate a "trap" after the execution of each instruction. This is useful for debugging, because it allows programmers to execute the program one instruction at a time, inspecting the state of registers and memory at each step.`
13. Why would an attacker want to control the RIP register inside a program they want to take control of?   
    `The RIP (instruction pointer) register holds the address of the next instruction to be executed. If an attacker can control the RIP register, they can manipulate the program's control flow, asking it to execute certain instructions or code of their choice. This is a common goal in many types of attacks, such as buffer overflow exploits.`
14. What is the ax register and how does it relate to rax?   
    `AX is the lower 16 bits of the RAX register. AX is usually called accumulator register, most of arithmatical operations are done with AX. Similarly, AH represents the higher 8 bits, and AL represents the lower 8 bits. The RAX register is the 64-bit version, and then EAX (32 bits), AX (16 bits), AH (8 bits), and AL (8 bits). This distribution is better explained in the following image:`   
    <br>
    ![RAX](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/0a6377c1-c870-4dcb-bfca-681576f9369f)
 
15. What is the result of the instruction xor rax, rax and where is it stored?   
    `The xor %rax, %rax instruction sets the value of the rax register to 0. The result is stored in the rax register.`
16. What does the leave instruction do in terms of registers to leave a stack frame?   
    `The leave instruction is often used in function epilogues to clean up the stack frame. The leave instruction is used to clean up the stack frame by restoring the previous stack frame's state before returning from a function. It sets the stack pointer esp to the value stored in the base pointer ebp. This deallocates the local variables and other stack frame-related data. It is equivalent to:`   
    ![image](https://github.com/horaciog1/CS479-Reverse-Engineering/assets/111658514/9cfbd317-807c-411b-b8c8-85a1907fd31c)
17. What pop instruction is retn equivalent to?   
    `The instruction retn is equivalent to "pop %rip" or "pop %eip" depending on the operand size`
18. What is a stack overflow?   
    `This is an answer`
19. What is a segmentation fault (a.k.a. a segfault)?   
    `This is an answer`
20. What are the RSI and RDI registers for that gives them their name?   
    `This is an answer`

---
    
## Crackme

### Screenshots

### How you solved it, and what the solution was.

### Whether Ghidra or IDA was more helpful to you, and why.

  
