# ROM CLEANUP

![RomCleanupTitle x](https://github.com/j0npq/rom_cleanup/assets/157430728/92389430-2708-49bc-816c-df7b9cc85b0f)


ROM CLEANUP is a Python script designed and crafted by JonPQ in January 2024, aiming to streamline the organization of game ROMs with multiple versions. This tool provides a user-friendly interface to assist users in managing and selecting specific versions of games stored in a designated folder.

## Features:

1. **Folder Analysis:**
   - Users are prompted to input the path to the folder containing game ROMs.
   - The script analyzes the contents of the specified folder, identifying games with multiple versions based on the usual naming conventions.

2. **User Interaction:**
   - For each game with multiple versions, the script displays a prompt with the game's simple name and a numbered list of different versions found.
   - Users can choose to keep all versions, archive all versions, or manually select versions to keep.

3. **Version Selection:**
   - Users can input their selection based on the provided prompt.
   - Options include keeping all versions, archiving all versions, or manually entering specific version numbers.

4. **Organizing Versions:**
   - Selected versions are kept in the original folder, untouched.
   - Unselected versions are archived in a subfolder named "Other Versions" (created if it doesn't exist).

5. **Stopping the Script:**
   - Users can type 'stop' at any time to halt the script's execution.

6. **User Guidance:**
   - Throughout the process, the script provides clear instructions and messages to guide the user.
   - The script stops gracefully when the user decides to end the process.

## How to Use:

1. **Initiate the Script:**
   - Run the script.

2. **Provide Folder Path:**
   - Enter the path of the folder containing game files when prompted.
   - Type 'stop' to end the script at any time.

3. **Review and Select Versions:**
   - Examine the displayed information for each game with multiple versions.
   - Choose the desired option: '(blank)', 'None', or manually input specific version numbers.

4. **Completion Message:**
   - Once all games are processed, the script informs the user that no more games with multiple versions were identified.

This tool is extremely simple and is still being developed. Any feedback or support will be deeply appreciated!!

Thank you!
JonPQ | [linktr.ee/jon.pq](https://linktr.ee/jon.pq)

## Getting Started

### Prerequisites
- Python 3.x

### Installation
1. Clone the repository: `git clone https://github.com/your_username/rom-cleanup.git`
2. Navigate to the project directory: `cd rom-cleanup`

### Usage
1. Run the script: `python rom_cleanup.py`
2. Follow the on-screen prompts to organize your ROMs.

## License
This project is licensed under the [GNU GPLv3 license].

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Acknowledgments
- Mention any acknowledgments or credits for third-party libraries or tools used.

## Support
For any issues or feedback, please [open an issue](https://github.com/your_username/rom-cleanup/issues).
