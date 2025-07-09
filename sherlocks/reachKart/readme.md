<a href="#top">^top</a>
<p align="center"><img src="https://github.com/user-attachments/assets/5dc591af-471e-484a-bfdc-66bb295ace9c"/></p>

# ReachKart (HTB Sherlock)  (DFIR Medium) 

## Description

This is a crypto theft using  network traffic capture (PCAP) of the theft 

Challenge Description:

>ReachKart is an e-commerce website running on Ehtereum blockchain technology, to support rapid development without disrupting the live environment, the company implemented a "production mirror" strategy, creating an exact replica of the production environment for development and testing purposes. The mirror includes replicated databases, services and blockchain nodes, but it appears that customer data has not been anonymized. Customer support is now receiving emails from sellers complaining that their wallets are missing ether. You have to investigate and understand if and how an intrusion has occurred.

## Resources

[Download file link](https://challenges-cdn.hackthebox.com/sherlocks/medium/ReachKart.zip?u=117571&p=ep&e=1752029826&t=1752022626&h=13800cc36954856e8b0bc7f0c34db3d3e2b6ac023820697d556c184e836820a1)

ZIP Password: hacktheblue

## Solution

### QUESTION 1
What was the vulnerable endpoint that allowed the attacker to leak files?

Answer: `/user/getOrderBill`



### QUESTION 2
When was the first successful exploitation of the vulnerable endpoint by the attacker (time in UTC)?

Answer: `2025-03-01 04:09:22`




### QUESTION 3
Which version of Express is currently being used on the server?

Answer: `4.21.2`



### QUESTION 4
Which Ethereum compatible development smart contract network is running on the server? (Format: name@version)

Answer: `hardhat@2.22.18`



### QUESTION 5
What is the signing key used by the server to sign JSON Web Tokens (JWT)?

Answer: `SuperSecretPassword`



### QUESTION 6
The attacker was able to generate a JWT from the signing key and log in to the admin panel. What is the JWT value?

Answer: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiRGFydGggVmFkZXIiLCJlbWFpbCI6ImRhcnRodmFkZXJAZW1waXJlLmNvbSIsImFjY291bnRfdHlwZSI6ImFkbWluIiwiaWF0IjoxNzQwODAyNzM0LCJleHAiOjE3NDA4ODkxMzR9.RBmMEC7IYmkzz1LsT-kP_JkLCUb7-hsJKX4IdjE91TE`



### QUESTION 7
Decode the token and find the email used by the attacker to log in to the admin panel.

Answer: `darthvader@empire.com`



### QUESTION 8
The admin panel uses WebSocket to send and receive terminal input. What port is being used?

Answer: `8888`



### QUESTION 9
The attacker then was able to retrieve a sensitive file. When did the attacker get the file (UTC)?

Answer: `2025-03-01 04:22:01`



### QUESTION 10
What is the SHA-256 hash of the file that the attacker downloaded ?

Answer: `fabe3234bb709ee5e5c5c2789c891a9a49368ffa520b23d60f6be2f2ca81bac6`



### QUESTION 11
How manysellers are there in the e-commerce website?

Answer: `8`



### QUESTION 12
The attacker started sending Ether from all identified sellers' wallets. What is the hash of the first transaction?

Answer: `0x7b7ded2d51f0dcb1bf3fc5cc9598b81a7a622aac15d3841d377c548986e0a7c3`



### QUESTION 13
What was the total amount of Ether stolen by the attacker? (1 Eth = 10^18 wei)

Answer: `24.4`



### QUESTION 14
What is the block number of the last transaction in which Ether was stolen? (Decimal)

Answer: `18`



### QUESTION 15
After the attacker stole the Ether, what was the balance in their wallet? (Ignore the trailing zeros)

Answer: `24.40023`































<p align="center"><img src="_images/3dcode.png"></p>

<p align="center"><img src="_images/5solve.png"></p>


