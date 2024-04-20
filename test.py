from stem import Signal
from stem.control import Controller

def test_new_identity():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password='your_plain_text_password')  # replace with your plain text password
            controller.signal(Signal.NEWNYM)
            print("Success: The Tor identity has been successfully changed.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_new_identity()