# Program 2: Install a C compiler in the virtual machine and execute a simple program


## Aim
To install a C compiler in the virtual machine created using VirtualBox and execute a simple C program.

## Prerequisites
- VirtualBox with an Ubuntu VM (import `ubuntu_gt6.ova`: *File > Import Appliance*, set USB 1.1, start the VM)
- `gcc` inside the VM

## Repository contents
```
02-c-program-in-vm/
├── .gitignore
├── README.md
├── code.txt
├── output/output_screenshot.png
├── src/first.c
├── src/run_commands.txt
```
`code.txt` contains every program/command used, in one plain-text file.

## Procedure
1. Open the terminal in the Ubuntu VM.
2. Create the program: `gedit first.c` and type the code from `src/first.c`.
3. Compile: `gcc first.c -o first`
4. Run: `./first` and enter a number.

## Expected output
The program tells whether the entered number is even or odd



## Result
The C program was compiled and executed successfully inside the virtual machine.


