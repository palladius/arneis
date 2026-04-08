#!/usr/bin/env uv run
# /// script
# dependencies = [
#   "rich",
#   "anthropic",
#   "pyyaml",
#   "python-dotenv",
# ]
# ///

import os
import sys
from rich.console import Console
from rich.panel import Panel
from constants import APP_NAME, VERSION, DEFAULT_FAST_MODEL

# We will start by wrapping s01 (the foundational loop) but using our Gemini model via LiteLLM or similar.
# For now, let's just make it a beautiful entry point that points to the baseline.

console = Console()

def main():
    console.print(Panel(f"[bold yellow]🦞🍾 {APP_NAME} v{VERSION}[/bold yellow]\n[italic]Your custom AI Harness powered by Gemini[/italic]", expand=False))
    
    console.print(f"⚡ [cyan]Mode:[/cyan] Fast (Gemini 3 Flash)")
    console.print(f"🤖 [cyan]Model:[/cyan] {DEFAULT_FAST_MODEL}\n")

    console.print("🚀 [bold green]Starting the Perception-Action Loop (s01)...[/bold green]")
    
    # We try to run s01_perception_action_loop.py
    try:
        import s01_perception_action_loop
        s01_perception_action_loop.main()
    except Exception as e:
        console.print(f"❌ [bold red]Error starting the loop:[/bold red] {e}")
        console.print("\n💡 [yellow]Note:[/yellow] The original code uses the Anthropic SDK. We need to patch 'core.py' to use Gemini API.")

if __name__ == "__main__":
    main()
