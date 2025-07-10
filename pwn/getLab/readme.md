

## QUESTION 1
What is the name of the web server listening on port 80?

```
nmap -p 80 -A 10.129.252.245
  ```
![image](https://github.com/user-attachments/assets/2c1a7d11-bb17-4cac-8c59-e97f19b7d9c8)

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

curl command

append to curl for id_rsa
`var%2fopt%2fgitlab%2f.ssh%2fid_rsa`

`/var/opt/gitlab/.ssh/id_rsa`

`ssh -i id_rsa git@10.129.252.245`
incorrect perms on id_rsa, edit permissions
`chmod 600 id_rsa`


```
executed +1
  ```
ANSWER: `7`



## QUESTION 6
What is the home directory of the git user?


```

  ```
ANSWER: `/var/opt/gitlab`


## QUESTION 7 
What is the full path of the private SSH key of the git user?
```

  ```
ANSWER: `/var/opt/gitlab/.ssh/id_rsa`


## ROOT FLAG
Submit the flag located in the sam user's home directory

```

  ```
ANSWER: ``




## 

```

  ```
ANSWER: ``


