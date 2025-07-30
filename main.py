import numpy as np
from rich.console import Console
from rich.table import Table


def get_user_numbers():
    """Prompts the user to enter numbers and returns them as a list of floats."""
    while True:
        user_input = input("Enter a list of numbers separated by spaces: ")
        if not user_input:
            print("Please enter some numbers.")
            continue

        # Split the input string into a list of strings
        str_numbers = user_input.split()

        try:
            # Convert each string to a float
            numbers = [float(num) for num in str_numbers]
            return numbers
        except ValueError:
            print("Invalid input. Please enter only numbers separated by spaces.")


def calculate_stats(numbers):
    """Calculates basic statistics for a list of numbers using numpy."""
    # Convert the list to a numpy array for efficient calculation
    data_array = np.array(numbers)

    stats = {
        "Mean": np.mean(data_array),
        "Median": np.median(data_array),
        "Standard Deviation": np.std(data_array),
        "Minimum": np.min(data_array),
        "Maximum": np.max(data_array),
        "Sum": np.sum(data_array),
        "Count": len(data_array)
    }
    return stats


def display_results(stats):
    """Displays the calculated statistics in a formatted table."""
    # Initialize the rich console
    console = Console()

    table = Table(title="[bold cyan]Statistical Analysis[/bold cyan]")
    table.add_column("Statistic", justify="left", style="cyan", no_wrap=True)
    table.add_column("Value", justify="right", style="magenta")

    for key, value in stats.items():
        # Format floating point numbers to have 2 decimal places
        if isinstance(value, float):
            table.add_row(key, f"{value:.2f}")
        else:
            table.add_row(key, str(value))

    console.print(table)


def main():
    """Main function to run the stats calculator."""
    console = Console()
    console.print("[bold green]Welcome to the Basic Stats Calculator![/bold green]")

    # 1. Get input from the user
    numbers = get_user_numbers()

    # 2. Perform calculations
    console.print("\n[yellow]Calculating...[/yellow]")
    statistics = calculate_stats(numbers)

    # 3. Output the results
    display_results(statistics)


if __name__ == "__main__":
    main()