# AlertValidationToolScripts
This is the set if scripts used for the AlertValidationToolScripts
All relevant scripts, configuration files, datasets, and output logs used in this research are available in the publicly accessible GitHub repository:
🔗 https://github.com/kaviya-creator/AlertValidationToolScripts
The repository contains the following materials organized by category:
A. Tool Configuration Files and Automation Scripts
•	nmap_test.py, sql_test.py, metasploit_test.py: Python scripts for automating Nmap, SQLmap, and Metasploit respectively.
•	validate_script.py: The central validation orchestration script integrating alert parsing, sandbox execution, and result logging.
•	docker-compose.yml: Docker Compose configuration used to set up the sandbox environment with predefined vulnerable services.
B. Alert Samples
•	Sample_Test.csv: Contains sample entries derived from the Microsoft Security Incident Prediction Dataset. These entries were used to simulate real-world alerts for testing and demonstration purposes.
C. Evaluation Logs and Output Files
•	output_nmap.txt: Captured Nmap results including open ports and service detection logs.
•	output_sql.txt: SQLmap output logs indicating injection testing outcomes.
•	output_metasploit.txt: Session logs and exploit outcomes from automated Metasploit runs.
