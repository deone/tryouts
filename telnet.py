import telnetlib

timeout = 120

print("Connecting...")
try:
    session = telnetlib.Telnet("10.130.19.116", 3300, timeout)
except socket.timeout:
    print("Socket timeout")
else:
    print("Sending commands...")
    session.write("ls\n")

print(session.read_all())
