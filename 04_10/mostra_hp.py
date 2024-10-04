def display_hp_bar(current_hp, max_hp):
    
    hp_percentage = current_hp / max_hp
    bar_length = 20  # Length of the bar
    filled_length = int(bar_length * hp_percentage)

    # Determine color based on the percentage of HP left
    if hp_percentage > 0.6:
        color = "\033[92m"  # Green
    elif hp_percentage > 0.3:
        color = "\033[93m"  # Yellow
    else:
        color = "\033[91m"  # Red

    # Reset color
    reset_color = "\033[0m"

    # Create the bar
    hp_bar = "[" + "=" * filled_length + "-" * (bar_length - filled_length) + "]"

    # Print HP bar with color
    print(f"{color}HP: {hp_bar} {current_hp}/{max_hp}{reset_color}")