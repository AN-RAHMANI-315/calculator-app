#!/usr/bin/env python3
"""
Command Line Interface for Calculator App.
"""

import click
from calculator import Calculator


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """Calculator CLI - Perform mathematical operations from command line."""
    if ctx.invoked_subcommand is None:
        click.echo("Calculator CLI")
        click.echo("Use --help to see available commands")


@cli.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def add(a, b):
    """Add two numbers."""
    calc = Calculator()
    result = calc.add(a, b)
    click.echo(f"{a} + {b} = {result}")


@cli.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def subtract(a, b):
    """Subtract b from a."""
    calc = Calculator()
    result = calc.subtract(a, b)
    click.echo(f"{a} - {b} = {result}")


@cli.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def multiply(a, b):
    """Multiply two numbers."""
    calc = Calculator()
    result = calc.multiply(a, b)
    click.echo(f"{a} * {b} = {result}")


@cli.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def divide(a, b):
    """Divide a by b."""
    calc = Calculator()
    try:
        result = calc.divide(a, b)
        click.echo(f"{a} / {b} = {result}")
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)


@cli.command()
@click.argument('base', type=float)
@click.argument('exponent', type=float)
def power(base, exponent):
    """Raise base to the power of exponent."""
    calc = Calculator()
    result = calc.power(base, exponent)
    click.echo(f"{base} ^ {exponent} = {result}")


@cli.command()
@click.argument('number', type=float)
def sqrt(number):
    """Calculate square root of a number."""
    calc = Calculator()
    try:
        result = calc.square_root(number)
        click.echo(f"√{number} = {result}")
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)


@cli.command()
@click.argument('value', type=float)
@click.argument('percent', type=float)
def percentage(value, percent):
    """Calculate percentage of a value."""
    calc = Calculator()
    result = calc.percentage(value, percent)
    click.echo(f"{percent}% of {value} = {result}")


@cli.command()
@click.argument('n', type=int)
def factorial(n):
    """Calculate factorial of a number."""
    calc = Calculator()
    try:
        result = calc.factorial(n)
        click.echo(f"{n}! = {result}")
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)


@cli.command()
def interactive():
    """Start interactive calculator mode."""
    calc = Calculator()
    click.echo("Interactive Calculator Mode")
    click.echo("Type 'quit' to exit, 'history' to see history, 'clear' to clear history")
    click.echo()
    
    while True:
        try:
            command = click.prompt("Enter operation (e.g., '5 + 3', 'sqrt 16')", type=str)
            
            if command.lower() == 'quit':
                break
            elif command.lower() == 'history':
                history = calc.get_history()
                if history:
                    click.echo("Calculation History:")
                    for operation in history[-10:]:  # Show last 10
                        click.echo(f"  {operation}")
                else:
                    click.echo("No history available")
                continue
            elif command.lower() == 'clear':
                calc.clear_history()
                click.echo("History cleared")
                continue
            
            # Parse and execute command
            result = parse_and_execute(command, calc)
            if result is not None:
                click.echo(f"Result: {result}")
                
        except (ValueError, KeyboardInterrupt) as e:
            if isinstance(e, KeyboardInterrupt):
                click.echo("\nGoodbye!")
                break
            click.echo(f"Error: {e}")
        except Exception as e:
            click.echo(f"Unexpected error: {e}")


def parse_and_execute(command, calc):
    """Parse and execute a command string."""
    parts = command.strip().split()
    
    if len(parts) == 3:  # Binary operations
        try:
            a = float(parts[0])
            op = parts[1]
            b = float(parts[2])
            
            if op == '+':
                return calc.add(a, b)
            elif op == '-':
                return calc.subtract(a, b)
            elif op == '*':
                return calc.multiply(a, b)
            elif op == '/':
                return calc.divide(a, b)
            elif op == '^' or op == '**':
                return calc.power(a, b)
            elif op == '%':
                return calc.modulo(a, b)
            else:
                raise ValueError(f"Unknown operator: {op}")
        except ValueError as e:
            if "could not convert" in str(e):
                raise ValueError("Invalid number format")
            raise e
    
    elif len(parts) == 2:  # Unary operations
        op = parts[0].lower()
        try:
            value = float(parts[1])
            
            if op == 'sqrt':
                return calc.square_root(value)
            elif op == 'factorial':
                return calc.factorial(int(value))
            else:
                raise ValueError(f"Unknown operation: {op}")
        except ValueError as e:
            if "could not convert" in str(e):
                raise ValueError("Invalid number format")
            raise e
    
    else:
        raise ValueError("Invalid command format. Use: 'a op b' or 'op value'")


if __name__ == '__main__':
    cli()
