
download + unzip

`chmod 755 -R catscale_out`

## QUESTION 1
When did attacker start enumerating the web server? Please input the time in UTC format

Unzip all the way down to:
`/home/kali/Documents/HTB/Sherlocks/GetLab-D/catscale_out/Logs/var/log/gitlab/nginx/gitlab_access.log.1`

Command to extract User-Agents
`cat gitlab_access.log.1 | cut -d '"' -f 6 | sort | uniq -c`

<p align="center"><img src="https://github.com/user-attachments/assets/1ba86918-97c9-4b3d-a8ad-ecc5c1ca37d5"></p>

Grab the first instance of gobuster
```
cat gitlab_access.log.1 | grep gobuster | head -n 1
  ```

line 34
`10.10.0.74 - - [07/Aug/2023:11:27:19 +0100] "GET / HTTP/1.1" 302 97 "" "gobuster/3.5" -`
Convert to UTC (-01:00)

<p align="center"><img src="https://github.com/user-attachments/assets/3bd73a9a-3438-44fa-9673-e05ce3d83e01"></p>

ANSWER: `07/08/2023 10:27:19`


## QUESTION 2
Which tool was being used by the attacker to enumerate the website? (Format tool/version)

See screenshot above

ANSWER: `gobuster/3.5`


## QUESTION 3
Can you confirm the IP address of the attacker?

See screenshot above

ANSWER: `10.10.0.74`


## QUESTION 4
Which CVE was exploited by the attacker to leak sensitive information from endpoint?

```
cat gitlab_access.log.1 | grep CVE
  ```

ANSWER: `CVE-2023-2825`


## QUESTION 5
How many nested groups are included in the exploit by the attacker?

Count the `MV4-x`

<p align="center"><img src="https://github.com/user-attachments/assets/9bd3aa2a-010b-45f5-a1e5-2e1c9f823837"></p>


ANSWER: `11`


## QUESTION 6
When did attacker first dump a sensitive file via the exploit? Please input in UTC format

timestamp from dumping id_rsa

```
cat gitlab_access.log.1 | grep -E "passwd|id_rsa"
  ```

<p align="center"><img src="https://github.com/user-attachments/assets/4453e44a-6276-493b-b395-ff8017142737"></p>


ANSWER: `07/08/2023 10:37:38`


## QUESTION 7
What's the full path of the file which allowed the attacker to remotely access the server?

URL decode the GET request to id_rsa which is the SSH private key, allowing access to the server

`GET //L7X-1/L7X-2/L7X-3/L7X-4/L7X-5/L7X-6/L7X-7/L7X-8/L7X-9/L7X-10/L7X-11/CVE-2023-2825/uploads/fd626fc98c506cf7229ea7d61797658b//..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fvar%2Fopt%2Fgitlab%2F.ssh%2Fid_rsa`
Decoded
`GET //L7X-1/L7X-2/L7X-3/L7X-4/L7X-5/L7X-6/L7X-7/L7X-8/L7X-9/L7X-10/L7X-11/CVE-2023-2825/uploads/fd626fc98c506cf7229ea7d61797658b//../../../../../../../../../../../../var/opt/gitlab/.ssh/id_rsa`

ANSWER: `/var/opt/gitlab/.ssh/id_rsa`


## QUESTION 8
At what time did the attacker remotely access the server? please input in UTC format


```

  ```
ANSWER: `07/08/2023 10:44:15`


## QUESTION 9
Attacker performed horizontal lateral movement to access another user on the system. For how many minutes did this session last?


```

  ```
ANSWER: `31`


## QUESTION 10
We got an alert about a possible malicious file named "syncautomation.sh". When was this file downloaded/created at the endpoint. Please input in UTC format.

Recursively grep for the filename (case insensitive) from the root folder and suppress errors
```
grep -ri "syncautomation.sh" / 2>/dev/null
  ```
Returns this result, the 4th timestamp is File Creation, which can be confirmed by opening the CSV and checking column headers
`/home/kali/Documents/HTB/Sherlocks/GetLab-D/catscale_out/Misc/getlab-20230808-0930-full-timeline.csv:322490,1,/home/sam/syncautomation.sh,2023-08-07 11:57:26.181608597 +0100,2023-08-07 11:56:46.717608724 +0100,2023-08-07 11:57:15.413608632 +0100,2023-08-07 11:56:45.905608726 +0100,sam,sam,-rwxr-xr-x,836755`

Convert to UTC

ANSWER: `07/08/2023 10:56:45`




## QUESTION 11
What was the size of this file in bytes?


```

  ```
ANSWER: `836755`




## QUESTION 12
Netflow data indicated that the attacker has dropped a persistence mechanism on the machine, please find the name and full path of the file used for persistence.


```

  ```
ANSWER: `/home/sam/cloudfetch.bin`




## QUESTION 13
What is the mitre technique ID for the persistence mechanism employed by the attacker?


```

  ```
ANSWER: `T1053.003`




## QUESTION 14
SOC team beleives that the threat actor wanted to exfiltrate data. We are not yet sure whether they were successful or not. Which tool was downloaded by the attacker? Please confirm the name and version of this tool.


```

  ```
ANSWER: `rclone/1.63.1`


