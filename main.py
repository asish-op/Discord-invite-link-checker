import os
import re
import time
import requests
from colorama import Fore, Style

print(Fore.GREEN + ''' 
░█████╗░░██████╗██╗░██████╗██╗░░██╗  ░█████╗░██████╗░
██╔══██╗██╔════╝██║██╔════╝██║░░██║  ██╔══██╗██╔══██╗
███████║╚█████╗░██║╚█████╗░███████║  ██║░░██║██████╔╝
██╔══██║░╚═══██╗██║░╚═══██╗██╔══██║  ██║░░██║██╔═══╝░
██║░░██║██████╔╝██║██████╔╝██║░░██║  ╚█████╔╝██║░░░░░
╚═╝░░╚═╝╚═════╝░╚═╝╚═════╝░╚═╝░░╚═╝  ░╚════╝░╚═╝░░░░░ ''' + Style.RESET_ALL)

# Prompt the user to enter the name of the input file.
input_file = input("Enter the name of the input file: ")

# Create a directory to store the output files.
output_dir = "Data"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Open the output files for writing.
valid_file = open(f"{output_dir}/valid_links.txt", "w")
invalid_file = open(f"{output_dir}/invalid_links.txt", "w")

# Open the input file and read the invite links.
with open(input_file, "r") as file:
    invite_links = file.readlines()

# Process each invite link.
for invite_link in invite_links:
    # Strip any leading or trailing whitespace from the invite link.
    invite_link = invite_link.strip()

    # Parse the invite code from the link.
    match = re.search(r"(discord\.gg|discordapp\.com/invite)/([a-zA-Z0-9]+)", invite_link)
    if not match:
        invalid_file.write(f"{invite_link}\n")
        print(Fore.RED + f"Invalid invite link: {invite_link}" + Style.RESET_ALL)
        continue

    # Construct the invite endpoint URL.
    invite_code = match.group(2)
    invite_url = f"https://discord.com/api/v9/invites/{invite_code}"

    # Make a GET request to the invite endpoint URL.
    response = requests.get(invite_url)

    # Check the response status code to determine if the invite is valid or not.
    if response.status_code == 200:
        valid_file.write(f"{invite_link}\n")
        print(Fore.GREEN + f"Valid invite link: {invite_link}" + Style.RESET_ALL)
    #introducing this check will remove false negatives from accuring
    elif response.status_code == 429:
        print("Rate limited retrying after one minute...")
        time.wait(70)
    else:
        invalid_file.write(f"{invite_link}\n")
        print(Fore.RED + f"Invalid invite link: {invite_link}" + Style.RESET_ALL)

# Close the output files.
valid_file.close()
invalid_file.close()

# Notify the user that the output files have been saved.
print(f"Valid invite links have been saved to {output_dir}/valid_links.txt")
print(f"Invalid invite links have been saved to {output_dir}/invalid_links.txt")
