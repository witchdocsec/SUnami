# SUnami
 Struggling with linux priveledge escelation? well then its time to cheese it with SUnami.
 0 interaction privesc is always recommended but not always achievable. For this reason we have created a tool for the most trivial priv esc in history (with a few drawbacks).
 This is not an exploit just a cheap but effective trick. The usecase is when you have a shell on a sudoers account but no sudo cred.
 It works by manipulating sudo via aliasing in their .bashrc file to prepend a malicious attacker specified command first in the background.
 This does mean you will need to wait for sudo to be executed.
  
  
