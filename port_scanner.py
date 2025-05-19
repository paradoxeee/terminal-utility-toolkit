import socket
from datetime import datetime
import threading
import time
import sys
from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn
from rich.panel import Panel
from rich.table import Table

# Configuration Rich
console = Console()

# Paramètres du scan
MAX_THREADS = 100
SOCKET_TIMEOUT = 1.0

def get_target():
    while True:
        try:
            hostname = console.input("[bold cyan]Enter target hostname/IP: [/]").strip()
            if not hostname:
                continue
            ip = socket.gethostbyname(hostname)
            console.print(f"[green]Target resolved to:[/] [bold]{ip}[/]")
            return ip
        except socket.gaierror:
            console.print("[red]Invalid hostname/IP. Please try again.[/]")

def scan_port(target, port, results, progress, task):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(SOCKET_TIMEOUT)
            result = s.connect_ex((target, port))
            if result == 0:
                results.append(port)
                console.log(f"[green]Port {port} is [bold]OPEN[/][/]")
    except (socket.timeout, ConnectionRefusedError):
        pass
    except Exception as e:
        console.log(f"[red]Error scanning port {port}:[/] {str(e)}")
    finally:
        progress.update(task, advance=1)

def port_scanner():
    target = get_target()
    ports_to_scan = list(range(1, 1024))
    open_ports = []
    threads = []
    start_time = datetime.now()

    console.print(Panel.fit(f"[bold]Starting scan of[/] [cyan]{target}[/]", title="Port Scanner"))

    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        transient=True
    ) as progress:
        task = progress.add_task("[cyan]Scanning ports...", total=len(ports_to_scan))

        try:
            for port in ports_to_scan:
                while threading.active_count() > MAX_THREADS:
                    time.sleep(0.1)
                
                thread = threading.Thread(
                    target=scan_port,
                    args=(target, port, open_ports, progress, task)
                )
                thread.daemon = True
                thread.start()
                threads.append(thread)

            for thread in threads:
                thread.join()

        except KeyboardInterrupt:
            console.print("\n[red]Scan interrupted by user![/]")
            sys.exit(1)

    end_time = datetime.now()
    scan_duration = end_time - start_time


    # Affichage des résultats
    table = Table(title="Scan Results", show_header=True, header_style="bold magenta")
    table.add_column("Port", style="cyan")
    table.add_column("Status", style="green")
    
    for port in sorted(open_ports):
        table.add_row(str(port), "[bold green]OPEN[/]")
    
    console.print(table)
    console.print(f"\n[bold]Scan completed in[/] [cyan]{scan_duration.total_seconds():.2f} seconds[/]")

