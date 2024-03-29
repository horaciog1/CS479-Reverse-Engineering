# Assignment 1 - Assembly Review

## Overview

In this assignment, we are tasked with writing a 64-bit x86 Linux shellcode to execute the Linux system call `execve`, which replaces the currently running process with a terminal shell (`/bin/sh`). The goal is to write compact and efficient shellcode that passes the provided testing program.

## Solution

```assembly
# Horacio Gonzalez
# CS 479 Reverse Engineering
# Assignment 1

.text
.global _start
_start:
	lea path(%rip), %rdi	# Load the address of the path ("/bin/sh\0") into rdi
	xor %rdx, %rdx		# rdx = 0
	xor %rsi, %rsi		# rsi = 0
	
	mov $0x3b, %al		# Set syscall number for execve, this is the same as 
				# mov $59, %rax   (either way works and same size) 
				# but in this case we just want to use the lower 8
				# bits of %rax to make the size smaller

	syscall			# execute execve
path:
	.string "/bin/sh"	# path to sh

```
## Explanation
```assembly
.text
.global _start
_start:
```
- The code begins with the standard setup. `_start` is the entry point, and we mark it as global. This part was given to us by Dr. Reynolds.
<br>
  

```assembly
    lea path(%rip), %rdi   # Load the address of the path ("/bin/sh\0") into rdi
```
- `lea path(%rip), %rdi`: This instruction uses the `lea` (load effective address) to compute the effective address of the path label (the address of the `"/bin/sh\0"` string) and loads it into the `rdi` register. `rip` is the instruction pointer, and `%rip` represents the address of the next instruction. This sets up `rdi` with the address of the string.
<br>

```assembly
    xor %rdx, %rdx         # rdx = 0
    xor %rsi, %rsi         # rsi = 0
```
- `xor %rdx, %rdx`: Clears the `rdx` register by XORing it with itself. This sets `rdx` to 0.
- `xor %rsi, %rsi`: Clears the `rsi` register by XORing it with itself. This sets `rsi` to 0.
<br>

```assembly
    mov $0x3b, %al         # Set syscall number for execve, this is the same as 
                           # mov $59, %rax   (either way works and same size) 
                           # but in this case, we just want to use the lower 8
                           # bits of %rax to make the size smaller

```
- `mov $0x3b, %al`: Loads the value `0x3b` into the lower 8 bits of the `al` register. This sets up the `syscall` number for `execve`. Alternatively, you could use `mov $59, %rax` to set the `syscall` number, but this would require more bytes.
<br>

```assembly
  syscall                # execute execve
```
- `syscall`: Initiates a system call. The values in `rdi`, `rsi`, and `rdx`, determine the parameters passed to the system call. In this case, `rdi` contains the address of the string ("/bin/sh\0"), `rsi` and `rdx` are set to 0, indicating no additional arguments or environment variables.
<br>

```assembly
path:
    .string "/bin/sh"      # path to sh
```
- This section declares the string "/bin/sh" and labels it as `path`. The `lea` instruction from earlier loads the address of this string.
<br>

## Size
My shellcode is **25 bytes long**. Here they are: `48 8D 3D 0A 00 00 00 48 31 D2 48 31 F6 B0 3B 0F 05 2F 62 69 6E 2F 73 68 00`

## Other approaches
This was the first code that could actually work. The size of the shellcode was 36, so I decided to try to reduce this number. 
I deleted the first two instructions and re-run the program, and the shellcode run perfectly. After that I thought that instead of using the whole `%rax` register I could use only the lower 8 bits `%al` to setup the execve number. I also deleted the `leave` instruction since I was not using the stack instructions from the beggining.
```assembly
.text
.global _start
_start:
	push %rbp
	mov %rsp, %rbp
	
	lea shellPath(%rip), %rdi
	mov $59, %rax
	xor %rsi, %rsi
	xor %rdx, %rdx

	syscall

	leave
	ret

shellPath:
	.string "/bin/sh"
```
