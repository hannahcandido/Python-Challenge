# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = []  # List to store candidate names
vote_count = {}  # Dictionary to track candidate names and their respective vote counts

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates:
            candidates.append(candidate_name)  # Add the candidate to the list
            vote_count[candidate_name] = 0  # Initialize their vote count

        # Add a vote to the candidate's count
        vote_count[candidate_name] += 1  # Increment the candidate's vote count

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {total_votes}")
    print("----------------------------")

    # Write the total vote count to the text file
    txt_file.write(
        f"Election Results\n"
        f"----------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"----------------------------\n"
        )

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidates:

        # Get the vote count and calculate the percentage
        votes = vote_count[candidate]
        vote_percentage = (votes / total_votes) * 100  # Calculate the percentage of votes

        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate  # Update the winning candidate

        # Print and save each candidate's vote count and percentage
        print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
        txt_file.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")

    # Generate and print the winning candidate summary
    winning_summary = (
        f"----------------------------\n"
        f"\nWinner: {winning_candidate}\n"
        f"----------------------------\n"
    )
    print(winning_summary)

    # Save the winning candidate summary to the text file
    txt_file.write(winning_summary)   