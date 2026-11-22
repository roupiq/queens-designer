from colorama import Fore, Back, Style

# print(f"{Fore.LIGHTBLACK_EX}\n{Fore.RESET}")
# print(f"{Style.BRIGHT}\n{Style.RESET_ALL}")
# print("\x1b[2K")
print(chr(27) + "[2J")
# for color in [Back.RED, Back.MAGENTA, Back.BLUE, Back.CYAN, Back.GREEN, Back.BLACK, Back.RESET, Back.YELLOW]:
#     print(color)