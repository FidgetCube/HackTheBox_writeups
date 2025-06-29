<a id="top"></a>
# HTB Sherlock - LockPick (Malware Analysis - Easy)

<details>
  <summary>Table of Contents</summary>
  
+ [Challenge Description](#challenge-description)
+ [Challenge Files](#challenge-files)
+ [Solution](#Solution)
  + [Goals](#goals)
  + [Reversing the Ransomware in with Ghidra](#reversing-the-ransomware-in-with-ghidra)
</details>

## Challenge Description

Forela needs your help! A whole portion of our UNIX servers have been hit with what we think is ransomware. We are refusing to pay the attackers and need you to find a way to recover the files provided.

>**Warning**  
*This is a warning that this Sherlock includes software that is going to interact with your computer and files. This software has been intentionally included for educational purposes and is NOT intended to be executed or used otherwise. Always handle such files in isolated, controlled, and secure environments.  
Once the Sherlock zip has been unzipped, you will find a DANGER.txt file. Please read this to proceed.*

---

[^top](#top)
## Challenge Files
+ [Download challenge file](https://challenges-cdn.hackthebox.com/sherlocks/easy/lockpick1.zip?u=117571&p=ep&e=1751099977&t=1751092777&h=440985e388efe61775c6f4eed605612f896a3d27b6a88b803143471abf7884f0)
+ Archive password = `hacktheblue`

---

[^top](#top)
## Solution

### Goals
Goals:
+ Reverse the ransomware binary
  + identify the encryption key
  + identify the encryption algorithm (and possible i/v)
  + answer some of the challenge questions based on ransomware behaviour
+ Decrypt the files using the identified encryption key
  + answer the rest of the questions requiring the decrypted files 

I started by downloading the challenge files and unzipping them. We are presented with a bunch of encrypted files located in a folder called `/forela-criticaldata`, with Forela being the name of the ficticious company in the challenge description. 

![image](https://github.com/user-attachments/assets/66326d47-ac7f-499e-af4f-56bf16abe094)

Next, read the file `DANGER.txt` for the password to unzip the actual ransomware so we can figure out how to reverse it and decrypt the files. A quick check of the unzipped ransomware binary info.

![image](https://github.com/user-attachments/assets/cd916b96-c6ee-47a8-9595-41f66f7a4fb0)

Load it up in Detect it Easy and see that it was compiled using GCC so i'll reverse it using Ghidra

![image](https://github.com/user-attachments/assets/96ef7795-62bd-411c-a705-9896a2a56140)

Worth noting is there are some intersting strings identified, including file extensions which we can assume the ransomware is searching for to encrypt, and another string that looks suspiciously like an encryption key but i'll wait to confirm this in Ghidra

![image](https://github.com/user-attachments/assets/dd34016b-fff0-4359-add5-124d2ea43b4f)

### Reversing the Ransomware in with Ghidra
Loading up Ghidra and decompiling main we see a function called `process_directory` which takes 2 arguments, the second being the suspicious string identified earlier which looks like an encryption key. Lets follow the `process_directory` function 

![image](https://github.com/user-attachments/assets/9b502bb7-181e-422c-8cc6-c3ba92e482cb)

This function performs a series of checks and actions with the high level summary as follows;
+ It attempts to open the object passed in at argument 1 (`/forela-criticaldata/`), as a directory, and if that doesn't fail, it then steps into further checks
+ The function then compares objects (files) against a hardcoded list of filetypes, if the object matches the file type, it then it is passed to another function called `encrypt_file`
+ `encrypt_file` takes 2 arguments, a file is passed in as argument 1 and argument 2 contains the suspicious string (suspected encryption key) identified before  

![image](https://github.com/user-attachments/assets/0f47dddd-2fc0-4b30-9da2-345a7e9ab19e)












