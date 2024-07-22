import sys
from pathlib import Path
from colorama import init, Fore, Style

def visualize_directory(path):
    def recursive_display(current_path, indent=""):
        for item in current_path.iterdir():
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{item.name}{Style.RESET_ALL}/")
                recursive_display(item, indent + "    ")
            else:
                print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")

    # init(autoreset=True)
    directory_path = Path(path)

    if not directory_path.exists():
        print(f"{Fore.RED}Error: Path '{path}' does not exist.{Style.RESET_ALL}")
        return
    if not directory_path.is_dir():
        print(f"{Fore.RED}Error: Path '{path}' is not a directory.{Style.RESET_ALL}")
        return

    print(f"Directory structure for: {Fore.YELLOW}{directory_path}{Style.RESET_ALL}")
    recursive_display(directory_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Usage: python {sys.argv[0]} <directory_path>{Style.RESET_ALL}")
    else:
        visualize_directory(sys.argv[1])