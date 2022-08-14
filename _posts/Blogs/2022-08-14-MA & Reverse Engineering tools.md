---
title: Malware analysis and Reverse Engineering tools
classes: wide
header:
  teaser: https://user-images.githubusercontent.com/84356407/184531985-13aa1764-334f-431e-890f-7802d9b17a31.jpg
ribbon: MidnightBlue
categories:
  - Blogs
toc: true
---

# Malware Analysis and Reverse Engineering Tools

Here, You can find Tools that can help you to analyze malware and do reverse engineering 
# Static Malware Analysis Tools
### 1- VirusTotal 
It's a website that can analyze malware and give you a report for that Also you can know How many antiviruses discover this file and identify it.
##### [VirusTotal](https://www.virustotal.com/gui/home/upload)

### 2- Die_Win32  &  Exeinfope  &  PEiD
Checking if the malware is packed or unpacked.
##### [Die_Win32](https://github.com/horsicq/DIE-engine/releases)
##### [Exeinfope](https://exeinfo-pe.ar.uptodown.com/windows)
##### [PEiD](https://softfamous.com/peid/)

### 3- PEStadio
Examining executable files in depth.(Strings, Imports , Exports , .....)
##### [PEStadio](https://pestudio.en.lo4d.com/windows)

### 4- Strings
 Scaning the file for UNICODE (or ASCII) strings of a default length of 3 or more UNICODE (or ASCII) characters.
##### [Strings](https://docs.microsoft.com/en-us/sysinternals/downloads/strings)

### 5- Resource Hacker
Examining resources, such as .exe and .res files, extract them, replace icons and bitmaps, and more.
##### [Resource Hacker](http://www.angusj.com/resourcehacker/#download)

# Dynamic Malware Analysis Tools
### 1- VirusTotal & Anyrun & Hybrid Analysis
Websites that give you a report of what the malware does in you device (Dynamic Analysis).
##### [VirusTotal](https://www.virustotal.com/gui/home/upload)
##### [Anyrun](https://app.any.run/)
##### [Hybrid Analysis](https://www.hybrid-analysis.com/)

### 2- Process Hacker & Process Monitor
 Monitoring system resources, debug software and detect malware. Viewing Runing processes
##### [Process Hacker](https://processhacker.sourceforge.io/)
##### [Process Monitor](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon)

### 3- ProcDot
Ingesting the output from ProcMon and automatically generating a graphical representation of the captured data.
##### [ProcDot](https://www.procdot.com/downloadprocdotbinaries.htm)

### 4- Autoruns
Displaying any installed software on a device that is set to launch when a machine is powered on.
##### [Autoruns](https://docs.microsoft.com/en-us/sysinternals/downloads/autoruns)

### 5- FileActivityWatch & FolderChangesView  
Displaying information about every read/write/delete operation of files occurs on your system.
##### [FileActivityWatch](https://www.nirsoft.net/utils/fileactivitywatch.zip)
##### [FolderChangesView](https://www.nirsoft.net/utils/folderchangesview.zip)

### 6- Regshot
Taking a snapshot of your registry and then compare it with a second one
##### [Regshot](https://sourceforge.net/projects/regshot/)

### 7- FakeDNS & ApateDNS & INetSim 
These tools for the Network (Faking and simulating)
##### [FakeDNS](https://github.com/0xbahaa/fakedns/releases)
##### [ApateDNS](https://fireeye.market/apps/211380)
##### [INetSim](https://www.inetsim.org/downloads.html)

# Advanced Static Malware Analysis Tools
### 7- IDA & Ghidra 
For analyzing the code 
##### [IDA](https://hex-rays.com/ida-free/)
##### [Ghidra](https://github.com/NationalSecurityAgency/ghidra/releases)

# Advanced Dynamic Malware Analysis Tools

### 7- ollydbg & X64dbg & Windbg
For analyzing the code and examining the CPU registers while the code executes
##### [ollydbg](https://www.ollydbg.de/version2.html)
##### [X64dbg](https://github.com/x64dbg/x64dbg/releases)
##### [Windbg](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/debugger-download-tools)



 
