import ctypes
import os
import shutil
import time
import re
import win32gui

def set_window_size(width, height):
    hwnd = win32gui.GetForegroundWindow()
    win32gui.MoveWindow(hwnd, 337, 162, width, height, True)

# Recognized ROM extensions
ROM_EXTENSIONS = ['.zip', '.nes', '.smd', '.bin', '.gba', '.gbc', '.gb', '.n64', '.iso', '.cue', '.pce', '.tg16', '.md', '.gen', '.gg', '.cdi', '.iso', '.mame', '.chd', '.a26', '.ws', '.wsc', '.ngp', '.ngc', '.fds', '.psx', '.nintendods', '.ps2', '.3ds', '.wii', '.p64', '.pkm', '.vb', '.sms', '.tgc', '.x68k', '.a78', '.lynx', '.neo', '.dc', '.sat', '.vb', '.smc', '.sfc', '.fig', '.swc', '.c64', '.d64', '.xex', '.prg', '.tap', '.atr', '.xex', '.st', '.msa', '.rom']

def print_title_card():



    # Line above the title card
    print("\n" + " " * 4 + "-" * 120)

    title_card = """
 

    8888888b.   .d88888b.  888b     d888       .d8888b.  888      8888888888        d8888 888b    888 888     888 8888888b.
    888   Y88b d88P" "Y88b 8888b   d8888      d88P  Y88b 888      888              d88888 8888b   888 888     888 888   Y88b
    888    888 888     888 88888b.d88888      888    888 888      888             d88P888 88888b  888 888     888 888    888
    888   d88P 888     888 888Y88888P888      888        888      8888888        d88P 888 888Y88b 888 888     888 888   d88P
    8888888P"  888     888 888 Y888P 888      888        888      888           d88P  888 888 Y88b888 888     888 8888888P"
    888 T88b   888     888 888  Y8P  888      888    888 888      888          d88P   888 888  Y88888 888     888 888
    888  T88b  Y88b. .d88P 888   "   888      Y88b  d88P 888      888         d8888888888 888   Y8888 Y88b. .d88P 888
    888   T88b  "Y88888P"  888       888       "Y8888P"  88888888 8888888888 d88P     888 888    Y888  "Y88888P"  888   v1.0

 
    """

    print(title_card.center(120))

    # Line below the title card
    print(" " * 4 + "-" * 120)

    created_by_info = "Created by JonPQ | linktr.ee/jon.pq"
    print(created_by_info.center(120))

    additional_info = """
    A tool designed to help you organize your ROMs, letting you choose which versions you want to keep.

    JonPQ 2024
    """

    print(additional_info)

def extract_game_name(filename):
    # Remove known extensions
    for ext in ROM_EXTENSIONS:
        if filename.endswith(ext):
            filename = filename[:-len(ext)]

    # Use regular expressions to extract the base game name
    match = re.match(r'^(.*?)\s*[\[\(].*?[\]\)]', filename)
    if match:
        return match.group(1).strip().lower()
    else:
        return filename.strip().lower()

def list_games_with_versions(folder_path):
    games = {}

    for filename in os.listdir(folder_path):
        if any(filename.endswith(ext) for ext in ROM_EXTENSIONS):
            game_name = extract_game_name(filename)

            if game_name in games:
                games[game_name].append(filename)
            else:
                games[game_name] = [filename]

    return games

def display_game_header(game_name):
    print(f"\nGame {game_name.upper()} found!")

def display_game_versions(game_name, versions):
    print(f"\nYou have {len(versions):02d} versions of this game:\n")

    for i, version in enumerate(versions, start=1):
        print(f"{i}- {version}")
        time.sleep(0.05)  # Adjust the sleep duration as needed

def display_discarded_versions_header(game_name):
    print(f"\n- - - DONE MOVING DISCARDED VERSIONS OF {game_name.upper()}!!! - - -\n")
    time.sleep(0.5)  # Adjust the sleep duration as needed

def prompt_user(game_name, versions):
    if len(versions) == 1:
        return [1]  # If only one version, no need to ask the user

    while True:
        display_game_header(game_name)
        display_game_versions(game_name, versions)

        print("\nPlease enter the number(s) of the version(s) to keep (separated by a comma, if more than one);")
        print("Type 'none' to move all versions;")
        print("Type 'stop' to stop the script.\n")

        user_input = input(f"Which versions should I keep for {game_name.upper()}?: ")

        if user_input.lower() == 'stop':
            exit_program()

        if not user_input:
            print("\nKeeping all versions...\n")
            return list(range(1, len(versions) + 1))

        if user_input.lower() == 'none':
            return []

        try:
            selected_versions = [int(v.strip()) for v in user_input.split(',')]

            if all(1 <= v <= len(versions) for v in selected_versions):
                return selected_versions
            else:
                print("\nInvalid option(s). Please enter valid option(s).\n")
        except ValueError:
            print("\nInvalid input. Please enter valid option(s).\n")

def move_files(source_path, destination_path):
    filename = os.path.basename(source_path)
    print(f"\nMoving {filename} to 'Other Versions' folder...")
    time.sleep(0.1)  # Adjust the sleep duration as needed

    try:
        shutil.move(source_path, destination_path)
        print(f"{filename} moved to 'Other Versions' folder.\n")
        return True
    except FileNotFoundError:
        print(f"Error: {filename} not found in the source location.\n")
        return False

def organize_versions(folder_path, games):
    for game_name, versions in games.items():
        selected_versions = prompt_user(game_name, versions)

        if selected_versions is not None:
            versions_to_move = []

            for i, version in enumerate(versions, start=1):
                source_path = os.path.join(folder_path, version)

                if not selected_versions or i not in selected_versions:
                    versions_to_move.append(source_path)

            for source_path in versions_to_move:
                destination_folder = os.path.join(folder_path, "Other Versions")
                destination_path = os.path.join(destination_folder, os.path.basename(source_path))

                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                move_files(source_path, destination_path)

            if versions_to_move:
                display_discarded_versions_header(game_name)

def exit_program():
    print("Exiting the program.")
    exit()

def main():
    set_window_size(1070, 800)  # Define o tamanho da janela conforme necessário
    print_title_card()  # Chama a função para imprimir o título

    while True:
        folder_path = input("\nEnter the folder path where the files are located: ")

        if not os.path.exists(folder_path):
            print("Error: The specified folder does not exist.")
            continue

        games = list_games_with_versions(folder_path)

        if not games:
            print("No games with multiple versions found in the specified folder.")
            continue

        break  # Break out of the loop if a valid folder with games is found

    for game_name, versions in games.items():
        organize_versions(folder_path, {game_name: versions})

    print("\nOrganizing completed. No more games with multiple versions identified.")

    # Display title card and creator info at the end
    print_title_card()

if __name__ == "__main__":
    main()