import subprocess
import os
import sys
import time  # Ensure file writing delay is handled

def run_nmap(target):
    output_file = "output_nmap.txt"  # Fixed output file
    print(f"Writing output to: {output_file}")  # Debugging info

    try:
        # Run Nmap scan and write output directly to output.txt
        cmd = f"nmap -sV --script=vuln {target} -oN {output_file}"
        print(f"Running command: {cmd}")  # Debugging info
        subprocess.run(cmd, shell=True, check=True)

        # Allow some time for Nmap to finish writing to the file
        time.sleep(1)

        # Check if the file exists
        if not os.path.exists(output_file):
            print(f"Error: Nmap output file {output_file} is missing.")
            return f"Error: Nmap output file {output_file} is missing."

        # Ensure the file is not empty
        if os.path.getsize(output_file) == 0:
            print(f"Error: Nmap output file {output_file} is empty. Try running with 'sudo' or scanning another target.")
            return f"Error: Nmap output file {output_file} is empty. Try running with 'sudo' or scanning another target."

        # Read the Nmap output from the file
        with open(output_file, "r") as file:
            result = file.read().lower()

        # Debugging: Print the scan results
        print("Nmap Output:\n", result)

        # Check for vulnerability indicators
        vulnerability_keywords = ["vulnerable", "vulnerability", "exploitable", "cve", "attack"]
        if any(keyword in result for keyword in vulnerability_keywords):
            # Print result
            return "✅ True Positive: nmap found vulnerable services"
        
        # Print result
        return "🚫 False Positive: nmap did not find vulnerable services"

    except subprocess.CalledProcessError as e:
        error_message = f"Error: {e.stderr.strip()}" if e.stderr else "Error: Nmap execution failed."
        print(error_message)  # Print the error
        return error_message
    except Exception as e:
        error_message = f"Error: {str(e)}"
        print(error_message)  # Print the error
        return error_message

# Check if script is run from CLI
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 filename.py <target>")
        sys.exit(1)
    
    target = sys.argv[1]  # Get target from command line
    print(run_nmap(target))  # Run scan and print result

