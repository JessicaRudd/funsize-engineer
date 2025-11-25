import os
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.style import Style

def main():
    console = Console()
    
    # Load ASCII Art
    asset_path = os.path.join(os.path.dirname(__file__), 'assets', 'ascii-arti.txt')
    try:
        with open(asset_path, 'r') as f:
            ascii_art = f.read()
    except FileNotFoundError:
        ascii_art = "Image not found."

    # Define Colors (FanDuel inspired)
    FD_BLUE = "#1493FF" # FanDuel Blue
    FD_DARK = "#1F2A37" # Dark Background
    
    # Create Layout
    layout = Layout()
    layout.split_row(
        Layout(name="art", ratio=1),
        Layout(name="info", ratio=2)
    )

    # Art Panel
    art_text = Text(ascii_art, style=f"bold {FD_BLUE}")
    layout["art"].update(
        Panel(
            Align.center(art_text, vertical="middle"),
            border_style=FD_BLUE,
            padding=(1, 1)
        )
    )

    # Info Panel
    info_text = Text()
    info_text.append("Jessica Rudd\n", style="bold white on #1493FF")
    info_text.append("Staff Data Engineer\n", style="bold white")
    info_text.append("Analytics Engineering Team @ FanDuel\n\n", style="italic white")
    
    info_text.append("GitHub: ", style="bold cyan")
    info_text.append("https://github.com/JessicaRudd\n", style="underline blue")
    
    info_text.append("Email: ", style="bold cyan")
    info_text.append("jessica.rudd@fanduel.com\n", style="underline blue")
    
    info_text.append("LinkedIn: ", style="bold cyan")
    info_text.append("https://www.linkedin.com/in/jmrudd/\n", style="underline blue")
    
    info_text.append("Substack: ", style="bold cyan")
    info_text.append("https://funsizedatabytes.substack.com/\n", style="underline blue")

    layout["info"].update(
        Panel(
            Align.center(info_text, vertical="middle"),
            title="[bold white]Contact Info[/]",
            border_style="white",
            padding=(1, 2)
        )
    )

    # Main Display
    console.print(
        Panel(
            layout,
            title="[bold white]funsize-engineer[/]",
            subtitle="[italic]pip install funsize-engineer[/]",
            border_style=FD_BLUE,
            padding=(1, 1),
            width=100
        )
    )

if __name__ == "__main__":
    main()
