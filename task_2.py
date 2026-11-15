"""Task 2: recursive construction of a Pythagoras tree fractal."""

TASK_INSTRUCTIONS = (
    f"Input: the user enters a recursion level from 1 to 12.\n"
    f"Processing: recursively draw the Pythagoras tree.\n"
    f"Output: a turtle window; branch angle 30 and initial length 160 are fixed."
)

import math
import turtle


def draw_tree(pen, length, level, angle=30):
    """Recursively draw the branches of a Pythagoras tree."""
    # Stop recursion after reaching the requested level.
    if level == 0:
        return
    # Draw the main branch of the current level.
    pen.forward(length)
    # Save the direction before drawing the left branch.
    pen.left(angle)
    # Draw the left branch with a shorter length.
    draw_tree(pen, length * math.cos(math.radians(angle)), level - 1, angle)
    # Return to the direction of the main branch.
    pen.right(2 * angle)
    # Draw the right branch with a shorter length.
    draw_tree(pen, length * math.cos(math.radians(angle)), level - 1, angle)
    # Return to the direction of the parent branch.
    pen.left(angle)
    # Move the cursor back to the beginning of the current branch.
    pen.backward(length)


def main():
    # Print the task instructions before requesting user input.
    print(TASK_INSTRUCTIONS)
    # Ask the user for the recursion level.
    level = int(input("Вкажіть рівень рекурсії від 1 до 12: "))
    # Validate the range for comfortable drawing.
    if not 1 <= level <= 12:
        raise ValueError("Рівень рекурсії має бути від 1 до 12.")
    # Create the turtle window.
    screen = turtle.Screen()
    # Configure the window size.
    screen.setup(width=1000, height=800)
    # Create the drawing pen.
    pen = turtle.Turtle()
    # Disable animation for faster drawing.
    screen.tracer(False)
    # Configure the branch color and width.
    pen.color("#B22222")
    pen.pensize(2)
    # Place the tree base at the bottom of the window.
    pen.left(90)
    pen.penup()
    pen.goto(0, -350)
    pen.pendown()
    # Draw the fractal with the selected recursion level.
    draw_tree(pen, 160, level)
    # Update the screen after recursion is complete.
    screen.update()
    # Print an explanation using an f-string.
    print(f"Pythagoras tree built for recursion level {level}.")
    # Keep the window open.
    screen.mainloop()


if __name__ == "__main__":
    # Run the program only when the file is executed directly.
    main()

