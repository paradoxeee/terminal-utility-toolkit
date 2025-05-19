from rich.console import Console
from rich.markdown import Markdown

def print_readme():
    console = Console()
    with open("README.md") as readme:
        mardown = Markdown(readme.read())
    console.print(mardown)