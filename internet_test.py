import pjsua as pj

class MyCallCallback(pj.CallCallback):
    def __init__(self, call=None):
        pj.CallCallback.__init__(self, call)

    def on_state(self):
        print("Call is ", self.call.info().state_text)
        if self.call.info().state == pj.CallState.CONFIRMED:
            print("Call is answered")

# Create a library instance
lib = pj.Lib()

try:
    # Initialize the library
    lib.init()

    # Create a transport instance
    transport = lib.create_transport(pj.TransportType.UDP)

    # Start the library
    lib.start()

    # Create and register an account
    acc = lib.create_account(pj.AccountConfig("192.168.0.36", "1008", "Bloemenland2431a"))

    # Make the call
    call = acc.make_call("sip:1006@192.168.0.36", MyCallCallback())
        # Wait for ENTER before quitting
    print("Press ENTER to quit")
    input()

except pj.Error as e:
    print("Exception: " + str(e))
finally:
    # We're done, shutdown the library
    lib.destroy()
    lib = None