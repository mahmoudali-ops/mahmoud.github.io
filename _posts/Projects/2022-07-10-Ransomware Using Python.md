---
title: Ransomware Using Python
classes: wide
header:
  teaser: https://user-images.githubusercontent.com/84356407/183726121-3c00cbbd-8a45-4609-94f9-4f5eb98e637b.jpg
ribbon: MidnightBlue
categories:
  - Projects
toc: true
---

> # Ransomware Using Python

Ransomware is a type of malicious software or malware that is intended to block users from accessing files and data on their computer until a ransom is paid. 
It encrypts your data.

here in my project (Ransomware) there are two parts :
1. Server (Attacker)
2. Client (Victim)

> ## Server (Attacker)
 
#### First, I connect by a port and an IP add
<img src="https://user-images.githubusercontent.com/84356407/183730069-f51faaff-5246-4b61-9207-944057766288.png"><br /><br />
#### Then,  Assigning a key for encrtypting Data but if I left the key like this it will be catched using Wireshare or any sniffing network tools, so i encrypted the key by RSA 

<img src="https://user-images.githubusercontent.com/84356407/183856667-e9a38b5b-d73c-41ea-8fcf-6db1df73f927.png" width="700"><br /><br />
#### Then, opening a socket to connect with the victim and send to it some command like (encrypt , decrypt, ..)

<img src="https://user-images.githubusercontent.com/84356407/183858152-23bb7fa1-20c0-417c-b4cb-ef9e43f9d4fe.png" width="700"><br /><br />

> ## Client (Victim)

#### First, It sniffs and checks whick OS you use (Windows or Linux)

<img src="https://user-images.githubusercontent.com/84356407/183868087-1b2b55bb-11fb-40a0-ac86-16bcb88b6d05.png" width="700"><br /><br />
#### Then, it lists the partitions on your device to encrypt Data in them 

<p float="left">
  <img src="https://user-images.githubusercontent.com/84356407/183868808-c571e095-d2f6-4bc0-966d-cbadc7c0a123.png" width="500" />
  <img src="https://user-images.githubusercontent.com/84356407/183868827-8ee036eb-f68a-4c24-a971-bee61fd6f16e.png" width="500" /> 
</p>

#### After That, it opens connction with the attacker through socket and recieves the key to encrypt Data

 <img src="https://user-images.githubusercontent.com/84356407/183870856-15eab503-06c8-474e-af72-457f7f996a7c.png" width="500" /> 
 
#### Then, It reads all files with thier extensions to encrypt them 
 
 <img src="https://user-images.githubusercontent.com/84356407/183871249-0e3f1da3-38bb-424a-9c06-ac3b465968b0.png" width="500" /> 


#### Then, It encrypts Data. Here, I reley on CTR mode for AES Algorithm, I read the file with block-size = 16 byte then encrypt it and change the extension with it by ".huss"

 <img src="https://user-images.githubusercontent.com/84356407/183872842-131d21eb-e20e-432f-961f-f5b10473adbb.png" width="500" /> 


### For decrypting data we call decryption_function. Here is the same as encryption_function- it releys on CTR mode for AES Algorithm and read the encrypted file as block-size = 16 byte then it decrypts it to the original file

<img src="https://user-images.githubusercontent.com/84356407/183873098-062eccca-e943-4866-a019-95cd23679028.png" width="500" /> 

#### To decrypt and encrypt the attacker send a command to the victim through socket to do that (encrypt, decrypt, exit)

<img src="https://user-images.githubusercontent.com/84356407/183874256-f3bcdaac-fcc2-4de1-83ec-1f0176da7906.png" width="500" /> 

## From Runnig Ransomware

<p float="left">
  <img src="https://user-images.githubusercontent.com/84356407/183876602-80583445-29e3-4d55-be07-5a45a492f462.png" width="700" /> 
  <img src="https://user-images.githubusercontent.com/84356407/183876612-0e3fe2fd-e28a-4a2b-b06e-6f64b70469b6.png" width="300" /> 
</p>


> # How to run this Ransomware

## Install python 
Download the latest version of python [python](https://www.python.org/downloads/)
## install libriries that we need
```
pip install pycryptodome
```
```
pip install crypto
```
```
pip install cryptography
```

# See it on GitHub(Code)
[Code](https://github.com/HusseinAdel7/Ransomeware)
