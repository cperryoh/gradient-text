# gradient_text.py
from rich.console import Console
from rich.text import Text
from rich.style import Style
import argparse

def gradient_color(start_color, end_color, steps):
    """Generate a gradient between two colors."""
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    r_step = (end_r - start_r) / steps
    g_step = (end_g - start_g) / steps
    b_step = (end_b - start_b) / steps

    gradient_colors = []
    for i in range(steps):
        r = int(start_r + r_step * i)
        g = int(start_g + g_step * i)
        b = int(start_b + b_step * i)
        gradient_colors.append((r, g, b))

    return gradient_colors

def main():
    parser = argparse.ArgumentParser(description="Print text with a gradient between two colors.")
    parser.add_argument("text", type=str, help="The text to display")
    parser.add_argument("--start-color", type=str, default="ff0000", help="Start color in hex (e.g., ff0000 for red)")
    parser.add_argument("--end-color", type=str, default="0000ff", help="End color in hex (e.g., 0000ff for blue)")
    parser.add_argument("--background", type=str, default=None, help="Background color in hex (e.g., 000000 for black)")
    args = parser.parse_args()

    # Convert hex colors to RGB tuples
    start_color = tuple(int(args.start_color[i:i+2], 16) for i in (0, 2, 4))
    end_color = tuple(int(args.end_color[i:i+2], 16) for i in (0, 2, 4))
    background_color = tuple(int(args.background[i:i+2], 16) for i in (0, 2, 4)) if args.background else None

    # Split the input text into lines
    input_text = args.text.split('\n')

    # Create a Rich Text object
    text = Text()
    for line in input_text:
        # Generate gradient colors for the current line
        gradient_colors = gradient_color(start_color, end_color, len(line))
        for i, char in enumerate(line):
            color = gradient_colors[i]
            style = Style(color=f"rgb({color[0]}, {color[1]}, {color[2]})")
            if background_color:
                style += Style(bgcolor=f"rgb({background_color[0]}, {background_color[1]}, {background_color[2]})")
            text.append(char, style=style)
        text.append('\n')  # Add a newline after each line

    # Print the text to the terminal
    console = Console()
    console.print(text)

if __name__ == "__main__":
    main()
