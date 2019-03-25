clone the john the ripper repo

use JohnTheRipper/run/pdf2john.pl to get the password hash

use hashcat with rockyou.txt to crack the password

``hashcat -m 10500 hash rockyou.txt``
