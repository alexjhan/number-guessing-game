import time
from rich.console import Console
from rich.panel import Panel
from jugar import elegir_amplitud_y_intentos
console = Console()

def main():
    while True:
        # Encabezado del menú con animación
        console.print("\n", Panel("🎰 [bold magenta]¡Bienvenido al Menú del Casino![/bold magenta] 🎰", expand=False, style="bright_yellow"))
        time.sleep(0.5)
        
        # Mostrar opciones con colores y animación
        console.print("[bold cyan]Opciones disponibles:[/bold cyan]")
        console.print("[bold green]1.[/bold green] [bold yellow]🎮 Jugar[/bold yellow]")
        time.sleep(0.3)
        console.print("[bold green]2.[/bold green] [bold yellow]📜 Ver reglas[/bold yellow]")
        time.sleep(0.3)
        console.print("[bold green]3.[/bold green] [bold yellow]🚪 Salir[/bold yellow]")
        
        # Línea decorativa
        console.print("[bold magenta]──────────────────────────────[/bold magenta]")
        
        # Capturar la opción del usuario
        option = console.input("[bold cyan]Elige una opción [dim](1-3)[/dim]: [/bold cyan]")
        
        # Procesar la opción ingresada
        if option == "1":
            console.print(Panel("🎮 [bold cyan]¡A jugar![/bold cyan] [bold green]Prepárate para la aventura...[/bold green]", style="green"))
            elegir_amplitud_y_intentos()
        elif option == "2":
            console.print(Panel("📜 [bold yellow]Reglas:[/bold yellow] [italic]Disfruta, apuesta responsablemente y diviértete.[/italic]", style="blue"))
        elif option == "3":
            console.print(Panel("🚪 [bold red]Saliendo del programa...[/bold red] [bold yellow]¡Hasta la próxima![/bold yellow]", style="red"))
            break
        else:
            console.print(Panel("[bold red]❌ Opción no válida[/bold red]. Intenta nuevamente.", style="bright_red"))
        
        # Agregar una pausa antes de mostrar el menú nuevamente
        time.sleep(0.5)
        console.input("[dim]Presiona Enter para regresar al menú principal...[/dim]")
        console.clear()  # Limpia la consola para una experiencia fresca cada vez

if __name__ == "__main__":
    main()
