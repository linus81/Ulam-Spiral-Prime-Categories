import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Window settings
size = 600
screen = pygame.display.set_mode((size, size))
pygame.display.set_caption("Ulam Spiral with Prime Number Categories")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLORS = {
    "default": WHITE,
    "quadratic": GREEN,
    "twin": RED,
    "safe": BLUE
}

# Function to check if a number is prime
def is_prime1(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Optimized function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Function to categorize prime numbers
def prime_category(number):
    # Quadratic primes: numbers of the form n^2 + n + 41
    max_n = int(number**0.5) + 1  # Limit based on the square root of the number
    for n in range(max_n):
        if number == n**2 + n + 41:
            return "quadratic"
    
    # Twin primes: check if the number is part of a twin prime pair
    if is_prime(number) and (is_prime(number + 2) or is_prime(number - 2)):
        return "twin"

    # Safe primes: primes of the form 2p + 1, where p is also prime
    if number > 1 and (number - 1) % 2 == 0:  # Ensure that number - 1 is even
        if is_prime((number - 1) // 2):
            return "safe"
    
    # Default color for other primes
    return "default"

# Function to draw the Ulam spiral
def draw_spiral():
    # Initialize variables
    center = (size // 2, size // 2)  # Center of the window
    x, y = center  # Start at the center
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # Directions: right, up, left, down
    direction_index = 0  # Index to manage the current direction
    step = 1  # Initial number of steps for each direction
    steps_in_current_direction = 0  # Count steps in the current direction
    current_number = 1  # Start from number 1
    side_length_counter = 0  # Count completed sides to increase step length

    spacing = 3  # Spacing between points

    # Loop to draw the spiral
    while current_number <= (size * size):

        # Handle events during the drawing loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Draw the point only if the number is prime
        if is_prime(current_number):
           # Get the category of the prime number
            category = prime_category(current_number)
            color = COLORS[category]
            pygame.draw.circle(screen, color, (x, y), 2)

        # Increment the number for the next point
        current_number += 1

        # Update coordinates based on the current direction
        dx, dy = directions[direction_index]
        x += dx * spacing
        y += dy * spacing

        # Increment the step counter for the current direction
        steps_in_current_direction += 1

        # Check if it's time to change direction
        if steps_in_current_direction == step:
            # Change direction counterclockwise
            direction_index = (direction_index + 1) % 4
            steps_in_current_direction = 0  # Reset steps in the new direction
            side_length_counter += 1  # Increase the completed side counter

            # Every two sides, increase the number of steps (to maintain the spiral symmetry)
            if side_length_counter % 2 == 0:
                step += 1

        # Update the display
        pygame.display.update()

# Main function
def main():
    screen.fill(BLACK)
    draw_spiral()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Run the application
main()
