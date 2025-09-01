import json
import argparse

def extract_min_fitness(json_file_path):
    """
    Extract the smallest total fitness from a JSON file.

    Args:
        json_file_path (str): Path to the JSON file containing fitness data.

    Returns:
        dict: The entry with the smallest total fitness.
    """
    # Load the JSON data
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    # Find the entry with the smallest total fitness
    min_fitness_entry = None
    for entry in data:
        if 'total_fitness' not in entry:
            continue

        if min_fitness_entry is None or entry['total_fitness'] < min_fitness_entry['total_fitness']:
            min_fitness_entry = entry

    return min_fitness_entry

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Extract the smallest total fitness from a JSON file.')
    parser.add_argument('json_file', type=str, help='Path to the JSON file containing fitness data.')
    args = parser.parse_args()

    # Extract and print the smallest total fitness
    min_fitness_entry = extract_min_fitness(args.json_file)
    if min_fitness_entry:
        print("Entry with the smallest total fitness:", min_fitness_entry)
    else:
        print("No valid entries with 'total_fitness' found in the JSON file.")
