
```
C:\Tools\Maldoc\Office\Tools\DidierStevensSuite\rtfdump.py Project_Outline.doc
  ```
![image](https://github.com/user-attachments/assets/47653943-74d1-41d4-8b7c-f61e455a73c0)

Object 4 contains object that looks like equation editor vulnerability exploit


View the object
```
C:\Tools\Maldoc\Office\Tools\DidierStevensSuite\rtfdump.py Project_Outline.doc -O
  ```
![image](https://github.com/user-attachments/assets/6fc9f1f2-5fea-4781-ada8-016c4cf66edd)


Confirmed equation editor exploit in object 4
```
C:\Tools\Maldoc\Office\Tools\DidierStevensSuite\rtfdump.py Project_Outline.doc -s 4 -H | more
  ```
![image](https://github.com/user-attachments/assets/f2c4119a-92a2-44d2-8708-5d6af4b0d7ca)



Investigate with format-bytes.py
```
C:\Tools\Maldoc\assessment>C:\Tools\Maldoc\Office\Tools\DidierStevensSuite\rtfdump.py Project_Outline.doc -s 4 -d | python C:\Tools\Maldoc\Office\Tools\DidierStevensSuite\format-bytes.py -f name=eqn1
  ```
+ `Start MTEF header` suggests that the analysis found a MathType Equation File (MTEF) header, which is commonly embedded in documents as part of mathematical equations
+ `<class 'bytes'>` indicates shellcode presence

![image](https://github.com/user-attachments/assets/d382c2ea-cf77-4ce8-b1b0-e0bbd834151f)




Dump out shellcode
```
C:\Tools\Maldoc\Office\Tools\DidierStevensSuite\rtfdump.py Project_Outline.doc -s 4 --hexdecode --dump > shellcode.sc
  ```

Use XORsearch.exe to identify shellcode entry point (GetEIP)
```
C:\Tools\Maldoc\Office\Tools\DidierStevensSuite\XORSearch.exe -W shellcode.sc
  ```
Entry point: 6F
![image](https://github.com/user-attachments/assets/1a92c979-2dfb-43ac-817a-d3a54e519275)




Emulate with scdb.exe
```
C:\Tools\Maldoc\Office\Tools\scdbg\scdbg.exe /f shellcode.sc /foff 6f
  ```

![image](https://github.com/user-attachments/assets/96971216-fb49-4e44-8cf6-4d2f5e4cfa24)



Q1 Analyse the shellcode embedded in Project_Outline.doc. Provide the IP addresses the shellcode attempts to communicate with  
ANSWER: `2.59.254.18`


Q2 In the same shellcode, what is the name of the file hosted at the remote server  
ANSWER: `lawzx.exe`


Q3 Identify the name of Windows API function that is used to execute the file %APPDATA%\lawserhgj5784.exe in the shellcode  
ANSWER: `CreateProcessW`





