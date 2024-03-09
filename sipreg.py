import pjsua as pj
import time


#pi register information
password = "Bloemenland2431a"
user = "1008"
domain = "192.168.0.36"

#to call information
to_user1 = "1006"
to_user2 = "1006"
to_domain = "192.168.0.36"


class MyAccountCallback(pj.AccountCallback):
    def __init__(self, account=None):
        pj.AccountCallback.__init__(self, account)

    def on_incoming_call(self, call):
        print("Incoming call from ", call.info().remote_uri)
        call.answer(200)
        print("Call is answered and hanging up!")
        call.hangup()

    def on_reg_state(self):
        if self.account.info().reg_status >= 200 and self.account.info().reg_status < 300:
            print("Registration successful")
        elif self.account.info().reg_status >= 400:
            print("Registration failed, retrying")
            time.sleep(10)
            self.lib.create_account(pj.AccountConfig(domain, user, password))

# Create a library instance
lib = pj.Lib()

def check_registration_status(account):
    status = account.info().reg_status
    if status >= 200 and status < 300:
        print("Account is registered")
    elif status >= 400:
        print("Account registration failed")
        acc = lib.create_account(pj.AccountConfig(domain, user, password))
        time.sleep(10)
    else:
        print("Account registration is in progress")


try:
    # Initialize the library
    lib.init()

    # Create a transport instance
    transport = lib.create_transport(pj.TransportType.UDP)

    # Start the library
    lib.start()

    # Create and register an account
    acc = lib.create_account(pj.AccountConfig(domain, user, password))
    acc.set_callback(MyAccountCallback(acc))


    

    # The account will stay registered until the program exits or the account is deleted
    while True:
        time.sleep(5)
        print("Checking registration status")
        check_registration_status(acc)

except pj.Error as e:
    print("Exception: " + str(e))
finally:
    # We're done, shutdown the library
    lib.destroy()
    lib = None