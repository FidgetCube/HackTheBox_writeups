<a id="top"></a>
<p align="center"><img src="https://github.com/user-attachments/assets/44436ad5-2eed-42cd-afa9-1ad35a6ebae9"/></p>

# HTB Sherlock - ElectricBreeze-2 (Malware-Analysis - Easy)

<details>
  <summary>Table of Contents</summary>
  
+ [Challenge Description](#challenge-description)
+ [Challenge Files](#challenge-files)
+ [References](#references)
+ [Solution](#Solution)
</details>

## Challenge Description

This challenge is reversing a piece of malware called VersaMem, deployed by Volt Typhoon in late 2024. The malware exploits CVE-2024-39717 in Versa Director Servers, to deploy a webshell and keylogger functionality. The file itself is a .jar archive containing numerous *.class files.

>Your boss is concerned about Volt Typhoon and some of their malware developments. He has requested that you obtain a copy of the associated malware and conduct a static analysis to identify any useful information. Please report back with your findings.

---

[^top](#top)
## Challenge Files

Downloading the sample is actually part of [Question 1](#question-1) and can found in the solution section

---

[^top](#top)
## References
+ [Lumen - Technical analysis of VersaMem](https://blog.lumen.com/uncovering-the-versa-director-zero-day-exploitation/)

---

[^top](#top)
## Solution

### QUESTION 1
Use MalwareBazaar to download a copy of the file with the hash '4bcedac20a75e8f8833f4725adfc87577c32990c3783bf6c743f14599a176c37'. What is the URL to do this?

Visit: https://bazaar.abuse.ch/download/4bcedac20a75e8f8833f4725adfc87577c32990c3783bf6c743f14599a176c37/

Answer: `https://bazaar.abuse.ch/download/4bcedac20a75e8f8833f4725adfc87577c32990c3783bf6c743f14599a176c37/`



### QUESTION 2
What is the password to unlock the zip?

<p align="center"><img src="https://github.com/user-attachments/assets/8e124ea4-2695-4d27-aa78-7920029b8261"/></p>

Answer: `infected`





### QUESTION 3
What is the extension of the file once unzipping?

<p align="center"><img src="https://github.com/user-attachments/assets/c5eea26f-4735-4b74-ad85-9b4a9ed99e7d"/></p>

Answer: `.jar`





### QUESTION 4
What is a suspicious directory in META-INF?

<p align="center"><img src="https://github.com/user-attachments/assets/f8808fad-35c7-4417-842e-0dc0663d0dfe"/></p>

Answer: `Director_tomcat_memShell`





### QUESTION 5
One of the files in this directory may give some insight into the threat actor's origin. What is the file?

```

  ```

<p align="center"><img src="https://github.com/user-attachments/assets/xx"/></p>

Answer: `pom.xml`






### QUESTION 6
According to Google Translate, what language is the suspicious text?

<p align="center"><img src="https://github.com/user-attachments/assets/xx"/></p>

Answer: `Chinese`





### QUESTION 7
What is the translation in English?

<p align="center"><img src="https://github.com/user-attachments/assets/xx"/></p>

Answer: `Check for the latest version`






### QUESTION 8
According to this file, what is the application's name?

<p align="center"><img src="https://github.com/user-attachments/assets/xx"/></p>

Answer: `VersaTest`






### QUESTION 9
The VersaMem web shell works by hooking Tomcat. Which file holds the functionality to accomplish this?



```

  ```

<p align="center"><img src="https://github.com/user-attachments/assets/xx"/></p>

Answer: `com/versa/vnms/ui/TestMain.class`





### QUESTION 10
There is a command that determines the PID for the hook. What is the program used in this line of code?

```

  ```

<p align="center"><img src="https://github.com/user-attachments/assets/xx"/></p>

Answer: `pgrep`






### QUESTION 11
The functionality for the webshell is in a different file. What is its name?

```

  ```

<p align="center"><img src="https://github.com/user-attachments/assets/xx"/></p>

Answer: `com/versa/vnms/ui/init/WriteTestTransformer.class`





### QUESTION 12
What is the name of the function that deals with authentication into the webshell?

```

  ```

<p align="center"><img src="https://github.com/user-attachments/assets/xx"/></p>

Answer: `getinsertcode`








### QUESTION 13
What request parameter must be present to activate the webshell logic?

```

  ```

<p align="center"><img src="https://github.com/user-attachments/assets/xx"/></p>

Answer: `p`







### QUESTION 14
What is the hardcoded access password used to validate incoming webshell requests?

```

  ```

<p align="center"><img src="https://github.com/user-attachments/assets/xx"/></p>

Answer: `5ea23db511e1ac4a806e002def3b74a1`






### QUESTION 15
What type of encryption is used?

```

  ```

<p align="center"><img src="https://github.com/user-attachments/assets/xx"/></p>

Answer: `AES`



### QUESTION 16
What cipher mode is used to encrypt the credentials?

```

  ```

<p align="center"><img src="https://github.com/user-attachments/assets/xx"/></p>

Answer: `ecb`


### QUESTION 17
What is the key?

```

  ```

<p align="center"><img src="https://github.com/user-attachments/assets/xx"/></p>

Answer: `56, 50, 97, 100, 52, 50, 99, 50, 102, 100, 101, 56, 55, 52, 99, 53, 54, 101, 101, 50, 49, 52, 48, 55, 101, 57, 48, 57, 48, 52, 97, 97`


### QUESTION 18
What is the value of the key after decoding?

```

  ```

<p align="center"><img src="https://github.com/user-attachments/assets/xx"/></p>

Answer: `82ad42c2fde874c56ee21407e90904aa`


### QUESTION 19
To avoid static detection, the method name is constructed at runtime and passed to java.lang.reflect.Method, what is the decimal byte array used to construct the string name?

```

  ```

<p align="center"><img src="https://github.com/user-attachments/assets/xx"/></p>

Answer: `100, 101, 102, 105, 110, 101, 67, 108, 97, 115, 115`


### QUESTION 20
What is the Base64-encoded string that is returned to the client if the class is successfully defined?

```

  ```

<p align="center"><img src="https://github.com/user-attachments/assets/xx"/></p>

Answer: `R2qBFRx0KAZceVi+MWP6FGGs8MMoJRV5M3KY/GBiOn8=`


### QUESTION 21
What is the decrypted string?

Take the base64 encoded string `R2qBFRx0KAZceVi+MWP6FGGs8MMoJRV5M3KY/GBiOn8=` and AES decrypt in ECB mode with the raw byte string of the key `56 50 97 100 52 50 99 50 102 100 101 56 55 52 99 53 54 101 101 50 49 52 48 55 101 57 48 57 48 52 97 97`.

**Note:** Electronic Code Book (ECB) doesn't require an Initialisation Vector (i/v).

I wrote a python script to perform this which [decrypt_VersaMem.py](https://github.com/FidgetCube/HackTheBox_writeups/blob/main/sherlocks/electricBreeze-2/decrypt_VersaMem.py)

<p align="center"><img src="https://github.com/user-attachments/assets/170c8249-0124-4d06-8e37-00d5babf93da"/></p>

Answer: `classDefine by clzd`


### QUESTION 22
There is another class to log passwords for exfiltration. What is this file?

```

  ```

<p align="center"><img src="https://github.com/user-attachments/assets/xx"/></p>

Answer: `com/versa/vnms/ui/init/capturepasstransformer.class`


### QUESTION 23
What is the main malicious function in this class?

```

  ```

<p align="center"><img src="https://github.com/user-attachments/assets/xx"/></p>

Answer: `captureloginpasswordcode`


### QUESTION 24
The same AES key from the previous method is being used. What is the variable name it is being saved as in this function?

```

  ```

<p align="center"><img src="https://github.com/user-attachments/assets/xx"/></p>

Answer: `secretkey`


### QUESTION 25
What file is used to hold credentials before exfiltration?

```

  ```

<p align="center"><img src="https://github.com/user-attachments/assets/xx"/></p>

Answer: `/tmp/.temp.data`


Solve
<p align="center"><img src="https://github.com/user-attachments/assets/d76ce6ff-4df3-49b5-80a3-b4f8cd7f28dc"/></p>
