import subprocess
import time

# Register a SIP account
sip_username = "your_sip_username"
sip_password = "your_sip_password"
sip_domain = "your_sip_domain"

# Make a call to a specific extension
call_extension = "1006"

# Start linphone in non-interactive mode, register and make a call
command = f'echo -e "register {sip_username} {sip_password} sip:{sip_domain}\ncall sip:{call_extension}@{sip_domain}\n" | linphonec'
subprocess.run(command, shell=True)

# Wait for the call to connect and then end it after a certain period of time
time.sleep(10)
subprocess.run('echo "terminate" | linphonec', shell=True)