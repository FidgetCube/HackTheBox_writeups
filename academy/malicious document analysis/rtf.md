# Malicious Document Analysis

## References
+ [Didier Stevens SANS blog - RTF Analysis](https://isc.sans.edu/diary/29174)

## RTF Analysis

Start the analysis by using Didier Stevens RTFdump Python tool.

```
C:\Tools\Maldoc\Office\Tools\DidierStevensSuite\rtfdump.py Project_Outline.doc
  ```
<p align="center"><img src="https://github.com/user-attachments/assets/47653943-74d1-41d4-8b7c-f61e455a73c0"/></p>

Object 4 contains an object that looks like equation editor vulnerability exploit, use `-O` argument to 


View the object
```
C:\Tools\Maldoc\Office\Tools\DidierStevensSuite\rtfdump.py Project_Outline.doc -O
  ```
<p align="center"><img src="https://github.com/user-attachments/assets/6fc9f1f2-5fea-4781-ada8-016c4cf66edd"/></p>


Confirmed equation editor exploit in object 4
```
C:\Tools\Maldoc\Office\Tools\DidierStevensSuite\rtfdump.py Project_Outline.doc -s 4 -H | more
  ```
<p align="center"><img src="https://github.com/user-attachments/assets/f2c4119a-92a2-44d2-8708-5d6af4b0d7ca"/></p>



Investigate with format-bytes.py
```
C:\Tools\Maldoc\assessment>C:\Tools\Maldoc\Office\Tools\DidierStevensSuite\rtfdump.py Project_Outline.doc -s 4 -d | python C:\Tools\Maldoc\Office\Tools\DidierStevensSuite\format-bytes.py -f name=eqn1
  ```
+ `Start MTEF header` suggests that the analysis found a MathType Equation File (MTEF) header, which is commonly embedded in documents as part of mathematical equations
+ `<class 'bytes'>` indicates shellcode presence

<p align="center"><img src="https://github.com/user-attachments/assets/d382c2ea-cf77-4ce8-b1b0-e0bbd834151f"/></p>




Dump out shellcode
```
C:\Tools\Maldoc\Office\Tools\DidierStevensSuite\rtfdump.py Project_Outline.doc -s 4 --hexdecode --dump > shellcode.sc
  ```

Use XORsearch.exe to identify shellcode entry point (GetEIP)
```
C:\Tools\Maldoc\Office\Tools\DidierStevensSuite\XORSearch.exe -W shellcode.sc
  ```
Entry point: 6F
<p align="center"><img src="https://github.com/user-attachments/assets/1a92c979-2dfb-43ac-817a-d3a54e519275"/></p>




Emulate with scdb.exe
```
C:\Tools\Maldoc\Office\Tools\scdbg\scdbg.exe /f shellcode.sc /foff 6f
  ```

<p align="center"><img src="https://github.com/user-attachments/assets/96971216-fb49-4e44-8cf6-4d2f5e4cfa24"/></p>



Q1 Analyse the shellcode embedded in Project_Outline.doc. Provide the IP addresses the shellcode attempts to communicate with  
ANSWER: `2.59.254.18`


Q2 In the same shellcode, what is the name of the file hosted at the remote server  
ANSWER: `lawzx.exe`


Q3 Identify the name of Windows API function that is used to execute the file %APPDATA%\lawserhgj5784.exe in the shellcode  
ANSWER: `CreateProcessW`

<p align="center"><img src="https://github.com/user-attachments/assets/df4aef80-1cb0-4145-bb1c-541cc2a2b68c"/></p>
