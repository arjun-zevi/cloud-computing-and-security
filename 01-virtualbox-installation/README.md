# Program 1: Install VirtualBox / VMware Workstation with different flavours of Linux or Windows OS

> Cloud Computing and Security (21CS71) - Lab Manual (2022 Scheme), Dept. of CSE, SCEM, Mangaluru

**Name:** ____________________  **USN:** ____________________  **Batch/Section:** __________

## Aim
To install VirtualBox / VMware Workstation and create virtual machines with different flavours of Linux or Windows.

## Prerequisites
- Windows 7/8 (or later) host with virtualization enabled in BIOS
- VirtualBox installer (.exe) from virtualbox.org

## Repository contents
```
01-virtualbox-installation/
├── .gitignore
├── README.md
├── code.txt
├── output/output_screenshot.png
├── src/verify_installation.txt
```
`code.txt` contains every program/command used, in one plain-text file.

## Procedure
1. Download the VirtualBox `.exe` and double-click it, then click **Next**.
2. Click **Next** on the custom-setup screen.
3. Click **Next** again, then **Yes** on the network-interfaces warning.
4. Click **Install** and wait for the installation to finish.
5. Finish - the VirtualBox icon appears on the desktop.
6. (Optional) Verify with the commands in `src/verify_installation.txt`.

## Expected output
VirtualBox installed and its icon is shown on the desktop.

![Output screenshot](output/output_screenshot.png)

*Screenshot is taken from the lab manual (your own).*

## Result
VirtualBox was installed successfully and is ready to host Linux/Windows virtual machines.
