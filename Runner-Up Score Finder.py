def find_runner_up_score(scores):
    # Remove duplicates and sort in descending order
    unique_sorted_scores = sorted(set(scores), reverse=True)
    
    # Check if there is a runner-up score
    if len(unique_sorted_scores) > 1:
        return unique_sorted_scores[1]
    else:
        return "There is no runner-up score."

def main():
    try:
        # Prompt user for the number of participants
        n = int(input("Enter the number of participants: "))
        
        # Check if there are at least two participants
        if n < 2:
            print("Error: There should be at least two participants.")
            return

        # Prompt user for scores separated by spaces
        scores_input = input("Enter the scores separated by spaces: ")
        
        # Convert input string to a list of integers
        scores = list(map(int, scores_input.split()))

        # Check if the number of scores matches the number of participants
        if len(scores) != n:
            print("Error: Number of scores does not match the number of participants.")
            return

        # Find and print the runner-up score
        runner_up = find_runner_up_score(scores)
        print(f"The runner-up score is: {runner_up}")

    except ValueError:
        print("Error: Please enter valid numeric values.")


if __name__ == "__main__":
    main()
