# Invite Link Checker

This script checks a list of Discord invite links for validity. It uses regular expressions to extract the invite code from the link, constructs the invite endpoint URL, and makes a GET request to it to check the response status code. Valid invite links are printed in green, invalid ones in red. The script also creates a folder called `Data` and two files inside it called `valid_links.txt` and `invalid_links.txt`, where the corresponding links are saved.

## How to Use

1. Clone or download the repository.
2. Install the required packages: `pip install -r requirements.txt`.
3. Prepare a text file with a list of Discord invite links, one per line.
4. Run the script: `python main.py`.
5. Enter the name of the input file when prompted.
6. Check the console for the results.
7. Check the `Data` folder for the saved links.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

