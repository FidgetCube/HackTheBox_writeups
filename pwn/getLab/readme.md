<a id="top"></a>
<p align="center"><img src="https://github.com/user-attachments/assets/de41ac6e-ba70-41cf-bc13-d93fd788e35c"/></p>

# Getlab (Pwn - Very Easy)

<details>
  <summary>Table of Contents</summary>
  
+ [Challenge Description](#challenge-description)
+ [Solution](#Solution)
</details>

## Challenge Description

summary

>GetLab is a very easy Linux machine that showcases an unauthenticated directory traversal vulnerability in GitLab 16.0.0, labeled CVE-2023-2825. Although the vulnerability itself does not require authentication, specific conditions have to be met in order to trigger it. User self-registration is enabled on the GitLab instance running on the machine, which allows attackers to log in under a new account and create a repository matching the required conditions, from which they can then retrieve arbitrary files in the context of the git user (which is running the GitLab application) including a private SSH key, which grants access as both the git user and an unprivileged user named sam.

---

[^top](#top)
## Solution

## QUESTION 1
What is the name of the web server listening on port 80?

```
nmap -p 80 -A 10.129.252.245
  ```
<p align="center"><img src="https://github.com/user-attachments/assets/2c1a7d11-bb17-4cac-8c59-e97f19b7d9c8"/></p>

ANSWER: `nginx`


## QUESTION 2
What is the name of the application served on port 80?

output above

ANSWER: `Gitlab`


## QUESTION 3 
Which version of the application is installed on the target machine?

Visit the site and go to /help

ANSWER: `v16.0.0`


## QUESTION 4
What is the 2023 CVE ID assigned to a path traversal vulnerability that affects the installed application?

Register account on gitlab, pull down POC and point and shoot
tim:timtimtim

[CVE-2023-2825 PoC](https://github.com/Occamsec/CVE-2023-2825/blob/main/poc.py)

ANSWER: `CVE-2023-2825`





## QUESTION 5
If we wanted to traverse back 6 directories using CVE-2023-2825, how many nested groups in a repository would be required?

We need to go back the number of executed +1

ANSWER: `7`



## QUESTION 6
What is the home directory of the git user?

ANSWER: `/var/opt/gitlab`


## QUESTION 7 
What is the full path of the private SSH key of the git user?

ANSWER: `/var/opt/gitlab/.ssh/id_rsa`


## ROOT FLAG
Submit the flag located in the sam user's home directory

Edit the PoC script to show this path, replacing the 'etc' with the 'var' so it hits the right location  
`var%2fopt%2fgitlab%2f.ssh%2fid_rsa`

That will print the SSH private key, which we can use to pwn the box. Save it into a file called `id_rsa` in the same directory.

If you attempt to use the id_rsa key without changing permissions you will get an error, you must run this first
```
chmod 600 id_rsa
  ```

<p align="center"><img src="https://github.com/user-attachments/assets/76d56d70-e94d-45f7-acdf-ce5f8ac77b6c"/></p>


Then you can ssh into the box

```
ssh -i id_rsa sam@10.129.252.245
  ```

<p align="center"><img src="https://github.com/user-attachments/assets/2c81ed8a-4163-4fcf-8f20-28fb626de50e"/></p>

ANSWER: `a19d69891e1a4039816852072620b80e`


<p align="center"><img src="https://github.com/user-attachments/assets/cc1cc175-93a7-4d81-b42c-553e2ff2a91d"/></p>

