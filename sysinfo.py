import psutil
from rich.console import Console
from rich.table import Table

def get_cpu_usage():
    """Retourne l'utilisation du CPU en pourcentage"""
    cpu_usage = psutil.cpu_percent(interval=1)
    return f"[bright_cyan]🔥 CPU: [/bright_cyan]{cpu_usage}"

def get_local_ip():
    """Retourne l'adresse IP locale (non localhost)"""
    addrs = psutil.net_if_addrs()
    
    # Recherche dans les interfaces communes
    for interface in ['eth0', 'en0', 'wlan0', 'Wi-Fi', 'Ethernet']:
        if interface in addrs:
            for addr in addrs[interface]:
                if addr.family == 2 and not addr.address.startswith('127.'):  # AF_INET
                    return f"[bright_cyan]🌐 IP ADDRESS: [/bright_cyan]{addr.address}"
    
    # Recherche dans toutes les interfaces si pas trouvé
    for intf in addrs.values():
        for addr in intf:
            if addr.family == 2 and not addr.address.startswith('127.'):
                return f"[bright_cyan]🌐 IP ADDRESS: [/bright_cyan]{addr.address}"
    
    return "127.0.0.1"

def get_memory_stats():
    """Retourne les statistiques mémoire formatées"""
    mem = psutil.virtual_memory()
    
    # Conversion en Go avec arrondi à 2 décimales
    ram_used_gb = round(mem.used / (1024 ** 3), 2)
    ram_total_gb = round(mem.total / (1024 ** 3), 2)
    
    # Retourne une chaîne formatée au lieu d'imprimer
    return f"[bright_cyan]💾 RAM: [/bright_cyan]{ram_used_gb} GB / {ram_total_gb} GB"

def systemInformation():

    console = Console()

    # Création du tableau
    table = Table(title="System Information", show_header=True, 
                header_style="bold yellow", border_style="bold white")
    table.add_column("CPU USAGE", justify="center")
    table.add_column("RAM Used", justify="center")
    table.add_column("IP Address", justify="center")

    # Ajout des données
    table.add_row(
        f"{get_cpu_usage()}%", 
        get_memory_stats(),  # Pas besoin de f-string car la fonction retourne déjà une string
        get_local_ip()
    )

    console.print(table)