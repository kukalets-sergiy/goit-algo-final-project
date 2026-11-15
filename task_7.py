"""Task 7: the Monte Carlo method for sums of two dice."""

f"Libraries required: matplotlib. Install it with: pip install -r requirements.txt"

TASK_INSTRUCTIONS = (
    f"Input: hardcoded values of 100000 rolls and random seed 42.\n"
    f"Processing: simulate two dice, count sums, and compare probabilities.\n"
    f"Output: a probability table, maximum deviation, and a comparison plot."
)

import random
from collections import Counter

import matplotlib.pyplot as plt


ANALYTICAL = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36,
}


def simulate_dice(rolls=100_000, seed=None):
    """Return occurrence counts for sums from 2 to 12."""
    # Validate the number of rolls.
    if rolls <= 0:
        raise ValueError("Кількість кидків має бути додатною.")
    # Create a separate generator for reproducible results.
    generator = random.Random(seed)
    # Simulate rolls of two dice.
    sums = [generator.randint(1, 6) + generator.randint(1, 6) for _ in range(rolls)]
    # Count all sums in one pass.
    counter = Counter(sums)
    # Return all possible sums, including zero-count results.
    return Counter({total: counter[total] for total in range(2, 13)})


def probabilities(counts):
    """Convert roll counts into probabilities."""
    # Calculate the total number of rolls.
    total = sum(counts.values())
    # Prevent division by zero.
    if total == 0:
        raise ValueError("Словник кількостей не може бути порожнім.")
    # Calculate the probability for every sum.
    return {total_value: count / total for total_value, count in counts.items()}


def plot_results(probability_values, show=True):
    """Plot a comparison of Monte Carlo and analytical probabilities."""
    # Get the sums in the correct order.
    totals = list(range(2, 13))
    # Create the figure and axes.
    figure, axis = plt.subplots(figsize=(10, 6))
    # Plot the simulated probabilities.
    axis.plot(totals, [probability_values[total] for total in totals], "o-", label="Монте-Карло")
    # Plot the exact analytical probabilities.
    axis.plot(totals, [ANALYTICAL[total] for total in totals], "s--", label="Аналітичні")
    # Label the axes and add a title.
    axis.set_xlabel("Сума на двох кубиках")
    axis.set_ylabel("Ймовірність")
    axis.set_title("Порівняння ймовірностей сум двох кубиків")
    # Add a grid and a legend.
    axis.grid(True, alpha=0.3)
    axis.legend()
    # Show the plot only when requested.
    if show:
        plt.show()
    # Return the figure for testing or saving.
    return figure


if __name__ == "__main__":
    # Print the task instructions.
    print(TASK_INSTRUCTIONS)
    # Run the simulation with a fixed seed for reproducibility.
    counts = simulate_dice(100_000, seed=42)
    # Convert counts into probabilities.
    result = probabilities(counts)
    # Print the table using f-strings.
    for total, probability in result.items():
        # Display the count and simulated probability.
        print(f"Sum {total:2d}: {counts[total]:6d} rolls, {probability:.2%}")
    # Calculate the maximum deviation from the analytical result.
    error = max(abs(result[total] - ANALYTICAL[total]) for total in ANALYTICAL)
    # Print a conclusion about the simulation accuracy.
    print(f"Maximum deviation from the analytical probability: {error:.4%}")
    # Visualize the results.
    plot_results(result)


