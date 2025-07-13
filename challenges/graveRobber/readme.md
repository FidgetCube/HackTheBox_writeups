<a id="top"></a>
<p align="center"><img src="https://github.com/user-attachments/assets/cc793c1e-9b8a-404b-9765-8eeda72fe5df"/></p>

# HTB Challenge - Graverobber (Reversing - Very Easy)

<details>
  <summary>Table of Contents</summary>
  
+ [Challenge Description](#challenge-description)
+ [Challenge Files](#challenge-files)
+ [Solution](#Solution)
</details>

## Challenge Description

>We're breaking into the catacombs to find a rumoured great treasure - I hope there's no vengeful spirits down there...

---

[^top](#top)
## Challenge Files

[Download file link](graverobber.zip)

ZIP Password: hackthebox

---

[^top](#top)
## Solution

Proof script - check shell:
```
echo $SHELL
  ```

(zsh)
```
string='HTB{br34k1n9_d0wn_th3_sysc4ll5}'; d="$PWD"; for i in {1..${#string}}; do c="${string[i,i]}"; mkdir "$c"; cd "$c"; done; cd "$d" && ./robber
```

Force bash:

change shell:
```
chsh -s /bin/bash
  ```
or run in bash:
```
bash -c 'string="HTB{br34k1n9_d0wn_th3_sysc4ll5}"; d="$PWD"; for ((i=0;i<${#string};i++)); do c="${string:i:1}"; mkdir "$c"; cd "$c"; done; cd "$d" && ./robber'
  ```


Cleanup script:
```

  ```

Understand:  
+ `local_ec` goes from `0` to `31` (0x1f)
+ For each index:
  + It loads a single 4-byte value from `parts[i]`
  + Stores it in `local_58[2*i]`
  + Inserts `'/'` after each byte at `local_58[2*i + 1]`
  + Then uses `stat (local_58, &local_e8)` to check if the resulting path exists
+ If any `stat()` call fails `(iVar1 != 0)`, it prints: `"We took a wrong turning!"` and exits with error code 1

Parts[]
>*(undefined4 *)(parts + (long)(int)local_ec * 4)


So...
+ So, `parts` **is an array of 32 4-byte values**, which is the flag and likely initialized or hardcoded elsewhere in the binary



Application running
<img width="212" height="44" alt="image" src="https://github.com/user-attachments/assets/b052e40b-5679-4628-9131-d1996a78a5c9" />

Created folder `H/`
<img width="286" height="116" alt="image" src="https://github.com/user-attachments/assets/5d018143-dfb7-4aa2-baf3-f35b7e8c3df7" />

Folder Path `H/T/`
<img width="584" height="83" alt="image" src="https://github.com/user-attachments/assets/f3a84b6c-66e2-482e-b02e-8e83314c3ac5" />



Cyberchef solve
<img width="1062" height="477" alt="image" src="https://github.com/user-attachments/assets/03c7a5c6-194a-4896-ae66-f45acdd869a5" />


strace 1
<img width="717" height="185" alt="image" src="https://github.com/user-attachments/assets/3e743bbf-bb96-457c-9ea6-dcb0702b5bcd" />

strace 2
<img width="653" height="36" alt="image" src="https://github.com/user-attachments/assets/2eca496c-a5c2-412e-a774-52d0e230de9d" />

strace 3
<img width="731" height="58" alt="image" src="https://github.com/user-attachments/assets/9136ffdd-98a5-4056-9427-d3c90a76486a" />

Ghidra - parts[]
<img width="1033" height="689" alt="image" src="https://github.com/user-attachments/assets/0603e8dc-3f5a-4cc0-a097-6db240b0f901" />

Ghidra main()

>undefined8 main(void)  
{  
  int iVar1;  
  undefined8 uVar2;  
  long in_FS_OFFSET;  
  uint local_ec;  
  stat local_e8;  
  char local_58 [72];  
  long local_10;  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);  
  local_58[0] = '\0';  
  local_58[1] = '\0';  
  local_58[2] = '\0';  
  local_58[3] = '\0';  
  local_58[4] = '\0';  
  local_58[5] = '\0';  
  local_58[6] = '\0';  
  local_58[7] = '\0';  
  local_58[8] = '\0';  
  local_58[9] = '\0';  
  local_58[10] = '\0';  
  local_58[0xb] = '\0';  
  local_58[0xc] = '\0';  
  local_58[0xd] = '\0';  
  local_58[0xe] = '\0';  
  local_58[0xf] = '\0';  
  local_58[0x10] = '\0';  
  local_58[0x11] = '\0';  
  local_58[0x12] = '\0';  
  local_58[0x13] = '\0';  
  local_58[0x14] = '\0';  
  local_58[0x15] = '\0';  
  local_58[0x16] = '\0';  
  local_58[0x17] = '\0';  
  local_58[0x18] = '\0';  
  local_58[0x19] = '\0';  
  local_58[0x1a] = '\0';  
  local_58[0x1b] = '\0';  
  local_58[0x1c] = '\0';  
  local_58[0x1d] = '\0';  
  local_58[0x1e] = '\0';  
  local_58[0x1f] = '\0';  
  local_58[0x20] = '\0';  
  local_58[0x21] = '\0';  
  local_58[0x22] = '\0';  
  local_58[0x23] = '\0';  
  local_58[0x24] = '\0';  
  local_58[0x25] = '\0';  
  local_58[0x26] = '\0';  
  local_58[0x27] = '\0';  
  local_58[0x28] = '\0';  
  local_58[0x29] = '\0';  
  local_58[0x2a] = '\0';  
  local_58[0x2b] = '\0';  
  local_58[0x2c] = '\0';  
  local_58[0x2d] = '\0';  
  local_58[0x2e] = '\0';  
  local_58[0x2f] = '\0';  
  local_58[0x30] = '\0';  
  local_58[0x31] = '\0';  
  local_58[0x32] = '\0';  
  local_58[0x33] = '\0';  
  local_58[0x34] = '\0';  
  local_58[0x35] = '\0';  
  local_58[0x36] = '\0';  
  local_58[0x37] = '\0';  
  local_58[0x38] = '\0';  
  local_58[0x39] = '\0';  
  local_58[0x3a] = '\0';  
  local_58[0x3b] = '\0';  
  local_58[0x3c] = '\0';  
  local_58[0x3d] = '\0';  
  local_58[0x3e] = '\0';  
  local_58[0x3f] = '\0';  
  local_58[0x40] = '\0';  
  local_58[0x41] = '\0';  
  local_58[0x42] = '\0';  
  local_58[0x43] = '\0';  
  local_ec = 0;  
  do {  
    if (0x1f < local_ec) {  
      puts("We found the treasure! (I hope it\'s not cursed)");  
      uVar2 = 0;  
LAB_00101256:  
      if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {  
                    /* WARNING: Subroutine does not return */  
        __stack_chk_fail();  
      }  
      return uVar2;  
    }  
    local_58[(int)(local_ec * 2)] = (char)*(undefined4 *)(parts + (long)(int)local_ec * 4);  
    local_58[(int)(local_ec * 2 + 1)] = '/';  
    iVar1 = stat(local_58,&local_e8);  
    if (iVar1 != 0) {  
      puts("We took a wrong turning!");  
      uVar2 = 1;  
      goto LAB_00101256;  
    }  
    local_ec = local_ec + 1;  
  } while( true );  
}




main() - stat() & parts[]
<img width="669" height="165" alt="image" src="https://github.com/user-attachments/assets/02e82224-e3ee-44d0-b829-f16adf45afe9" />



main() - 
<img width="412" height="630" alt="image" src="https://github.com/user-attachments/assets/0591ebca-8076-49fb-aff8-fdf7b23f4be5" />






Solve proof bash & zsh

<img width="1028" height="175" alt="image" src="https://github.com/user-attachments/assets/e490fdd9-0c44-4007-9b8d-2099e37e36a1" />

Folder structure
<img width="521" height="50" alt="image" src="https://github.com/user-attachments/assets/15654d8c-2000-4a34-b1dc-d223c00ebcf5" />











