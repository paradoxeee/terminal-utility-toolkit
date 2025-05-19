import argparse
from port_scanner import port_scanner as pt
from sysinfo import systemInformation as si
from  markdow import print_readme as rm
from graphic_display import mainDisplay


def main():
    parser = argparse.ArgumentParser(description="Mon programme Python")
    parser.add_argument('--pt', action='store_true', help="Exécuter port_scanner")
    parser.add_argument('--si', action='store_true', help="Exécuter systemInformation")
    parser.add_argument('--rm', action='store_true', help="Exécuter print README")
    
    args = parser.parse_args()
    
    if args.pt:
        pt()
    elif args.si:
        si()
    elif args.rm:
        rm()
    else:
        mainDisplay()

if __name__ == "__main__":
    main()