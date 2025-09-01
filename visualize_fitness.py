import json
import matplotlib.pyplot as plt
import os

def visualize_fitness(json_file_path):
    """
    Visualize the total fitness from a JSON file.

    Args:
        json_file_path (str): Path to the JSON file containing fitness data.
    """
    # Load the JSON data
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    # Prepare data for plotting
    x_values = []
    y_values = []
    colors = []

    for entry in data:
        # Check if 'total_fitness' key exists
        if 'total_fitness' not in entry:
            print(f"Skipping entry without 'total_fitness': {entry}")
            continue

        index = entry['generation'] + entry['child'] / 50  # Normalize child index for better spacing
        total_fitness = entry['total_fitness']

        # Adjust fitness and determine color
        if total_fitness > 1:
            y_values.append((total_fitness - 1) / 2)
            colors.append('red')
        else:
            y_values.append(total_fitness / 2)
            colors.append('blue')

        x_values.append(index)

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.scatter(x_values, y_values, c=colors, alpha=0.7, edgecolors='w', s=50)
    plt.title('Total Fitness Visualization')
    plt.xlabel('Generation')
    plt.ylabel('Total Fitness (adjusted)')
    plt.yscale('log')  # Set y-axis to log scale
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()

    # Save the plot
    output_dir = os.path.dirname(json_file_path)
    output_path = os.path.join(output_dir, 'fitness_plot.png')
    plt.savefig(output_path)
    print(f"Plot saved to {output_path}")

    # Show the plot
    plt.show()

if __name__ == "__main__":
    import argparse

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Visualize fitness data from a JSON file.')
    parser.add_argument('json_file', type=str, help='Path to the JSON file containing fitness data.')
    args = parser.parse_args()

    # Run the visualization
    visualize_fitness(args.json_file)