echo-my-ip
==========

echo ip for raspberry pi, and others

HOWTO:<br>
1) run the emi_broadcaster.py on raspberry pi or other OS (only test on macos, debian) <br>
2) run the emi_server.py on other machine, you will receive the message from 'emi_broadcaster'

NOTICE:<br>
emi_server.py accept input ip, then send the message 'OK'<br>
emi_broadcaster.py if receive message 'OK' or run in 15 min, will shutdown self<br>
