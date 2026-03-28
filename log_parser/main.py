import os

log_file_path="server.log"
output_file="error_report.txt"
keyword=str(input("Enter keyword:"))

total_lines=0
keyword_count=0

print("Scanning file...")

try:
    with open(log_file_path,"r") as log_file, open(output_file,"w") as output:
        for line in log_file:
            total_lines+=1

            if keyword in line:
                output.write(line)
                keyword_count+=1
    print("\n Scanning Complete!")
    print(f" Total lines checked: {total_lines}")
    print(f" Total errors found: {keyword_count}")
    print(f" Check your clean report here: {output}")

except FileNotFoundError:
    print("File not found")

except Exception as e:
    print("Error occured!")