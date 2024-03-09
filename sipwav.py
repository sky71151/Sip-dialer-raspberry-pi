import pjsua as pj
import threading

class MyCallCallback(pj.CallCallback):
    def __init__(self, call=None):
        pj.CallCallback.__init__(self, call)
        self.player_id = None

    def on_state(self):
        print("Call is ", self.call.info().state_text)
        if self.call.info().state == pj.CallState.CONFIRMED:
            print("Call is answered")
            # Play the WAV file
            self.player_id = pj.Lib.instance().create_player('/home/pi/StarWars60.wav', loop=False)
            player_slot = pj.Lib.instance().player_get_slot(self.player_id)
            call_slot = self.call.info().conf_slot
            pj.Lib.instance().conf_connect(player_slot, call_slot)
        elif self.call.info().state == pj.CallState.DISCONNECTED:
            print("Call is disconnected")
            if self.player_id is not None:
                pj.Lib.instance().player_destroy(self.player_id)



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
    print("Press ENTER to quit")
    input()

except pj.Error as e:
    print("Exception: " + str(e))
finally:
    # We're done, shutdown the library
    lib.destroy()
    lib = None