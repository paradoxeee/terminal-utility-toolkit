from port_scanner import port_scanner
from sysinfo import systemInformation
from markdow import print_readme
from rich.console import Console
from rich.table import Table

def main_display_choice():
    console = Console()
    table = Table(show_header=True, header_style="bold yellow", show_lines=True)
    table.add_column("Choice",  justify="center")
    table.add_column("Script",  justify="left")
    table.add_row("1", "port scanner")
    table.add_row("2", "system information")
    table.add_row("3", "print README")
    table.add_row("4", "--option valid")
    table.add_row("5", "quit")
    console.print(table)


def user_choice():
    console = Console()
    console.print("Please choose an option : ", end='')
    choice = int(input())
    if choice == 1:
        print("\n")
        port_scanner()
    elif choice == 2:
        print("\n")
        systemInformation()
    elif choice ==3:
        print_readme()
    elif choice == 4:
        print("\n")
        console.print("To see the possible options \n\n python main [bold green]-h[/bold green] | python main [bold green]--help[/bold green]")
    elif choice== 5:
        quit
    else:
        print("\n")
        console.print("[bold red]Please chooce a valid option[/bold red]")


def mainDisplay():
    main_display_choice()
    user_choice()
  
