import pjsua as pj
import threading
import Queue
import time

class MyCallCallback(pj.CallCallback):
    def __init__(self, call=None, account=None, call_queue=None):
        pj.CallCallback.__init__(self, call)
        self.timer = threading.Timer(30.0, self.on_no_answer)
        self.timer.start()
        self.account = account
        self.call_queue = call_queue

    def on_state(self):
        print("Call is ", self.call.info().state_text)
        if self.call.info().state == pj.CallState.CONFIRMED:
            print("Call is answered")
            self.timer.cancel()
        elif self.call.info().state == pj.CallState.DISCONNECTED:
            print("Call is disconnected, making a second call")
            self.call_queue.put("make_second_call")
        elif self.call.info().state == pj.CallState.NULL:
            self.timer.cancel()

    def on_no_answer(self):
        print("No answer, making a second call")
        self.call_queue.put("make_second_call")

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
    acc = lib.create_account(pj.AccountConfig("192.168.0.36", "1008", "BloeMenland2431a"))

    # Create a queue to communicate between threads
    call_queue = Queue.Queue()

    # Make the call
    call = acc.make_call("sip:1006@192.168.0.36", MyCallCallback(account=acc, call_queue=call_queue))

    # Check the queue in the main thread
    while True:
        try:
            msg = call_queue.get(timeout=1)
            if msg == "make_second_call":
                second_call = acc.make_call("sip:1006@192.168.0.36", MyCallCallback(account=acc, call_queue=call_queue))
        except Queue.Empty:
            pass

except pj.Error as e:
    print("Exception: " + str(e))
finally:
    # We're done, shutdown the library
    lib.destroy()
    lib = None