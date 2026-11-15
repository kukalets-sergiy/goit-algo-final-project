"""Task 6: greedy algorithm and dynamic programming."""

TASK_INSTRUCTIONS = (
    f"Input: a hardcoded meal dictionary and a hardcoded budget of 100.\n"
    f"Processing: compare the greedy algorithm with 0/1 dynamic programming.\n"
    f"Output: meal names selected by both algorithms."
)


def greedy_algorithm(items, budget):
    """Return meals selected by the calories-to-cost ratio."""
    # Check that the budget is not negative.
    if budget < 0:
        raise ValueError("Бюджет не може бути від'ємним.")
    # Discard meals with zero or negative cost.
    valid_items = [item for item in items.items() if item[1]["cost"] > 0]
    # Sort meals by decreasing calories per unit of cost.
    sorted_items = sorted(
        valid_items,
        key=lambda item: item[1]["calories"] / item[1]["cost"],
        reverse=True,
    )
    # Create the result and the spent-budget counter.
    selected = []
    spent = 0
    # Check meals in order of their value.
    for name, data in sorted_items:
        # Skip invalid or too expensive meals.
        if data["cost"] <= 0 or spent + data["cost"] > budget:
            continue
        # Add the meal and increase spending.
        selected.append(name)
        spent += data["cost"]
    # Return the names of selected meals.
    return selected


def dynamic_programming(items, budget):
    """Return a meal set with the maximum total calories."""
    # Check that the budget is not negative.
    if budget < 0:
        raise ValueError("Бюджет не може бути від'ємним.")
    # Keep only meals with a positive cost.
    valid_items = [
        (name, data) for name, data in items.items() if data["cost"] > 0
    ]
    # Create a table of maximum calories.
    table = [0] * (budget + 1)
    # Store the meal set for every budget.
    choices = [[] for _ in range(budget + 1)]
    # Process each meal once, as in the 0/1 knapsack problem.
    for name, data in valid_items:
        # Iterate through budgets in reverse order.
        for current_budget in range(budget, data["cost"] - 1, -1):
            # Calculate the calories of a set containing the current meal.
            candidate = table[current_budget - data["cost"]] + data["calories"]
            # Update the result if the candidate is better.
            if candidate > table[current_budget]:
                table[current_budget] = candidate
                choices[current_budget] = choices[current_budget - data["cost"]] + [name]
    # Return the optimal meal set.
    return choices[budget]


if __name__ == "__main__":
    # Print the task instructions.
    print(TASK_INSTRUCTIONS)
    # Define the available meals and their properties.
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }
    # Set the budget limit.
    budget = 100
    # Run the greedy algorithm.
    greedy_result = greedy_algorithm(items, budget)
    # Run the dynamic programming algorithm.
    dynamic_result = dynamic_programming(items, budget)
    # Print the greedy result using an f-string.
    print(f"Greedy algorithm: {greedy_result}")
    # Print the optimal result using an f-string.
    print(f"Dynamic programming: {dynamic_result}")


