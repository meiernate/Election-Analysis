import csv
import os

# Set file locations
file_to_load = os.path.join('Resources', 'election_results.csv')
file_to_save = os.path.join('Analysis', 'election_analysis.txt')

# Initialize a total vote counter
total_votes = 0

# Candidate Options and Votes
candidate_options = []
candidate_votes = {}
candidate_results = ''

# Winning Candidate and Count Tracking
winning_candidate = ''
winning_count = 0
winning_percentage = 0

# Open file and read contents
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    # Read and print the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:

        # Add to the total vote count
        total_votes += 1

        # Set the cadidate name 
        candidate_name = row[2]

        # If candidate is not in the candidate list 
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Begin tracking the candidate's vote count
            candidate_votes[candidate_name] = 0
        
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file
with open(file_to_save, 'w') as txt_file:
    
    # Print the final vote count to the terminal.
    election_results = (
        f'\nElection Results\n'
        f'-------------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'-------------------------\n')
    print(election_results, end='')
    
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Iterate through candidate list for results
    for candidate_name in candidate_votes:
        
        # Retrieve vote count of a candidate 
        votes = candidate_votes[candidate_name]

        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # Set winning count
            winning_count = votes

            # Set winning percentage
            winning_percentage = vote_percentage

            # Set winning cadidate
            winning_candidate = candidate_name
        
        # Set candidate, vote count, and percentage to var
        candidate_results = (f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
        
        # Print each candidate, their voter count, and percentage to the terminal
        print(candidate_results)

        # Save the candidate results to the text file
        txt_file.write(candidate_results)

    # print(winning_candidate_summary)
    winning_candidate_summary = (
        f'-------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'-------------------------\n')
    
    # Print winning candidate results to the terminal
    print(winning_candidate_summary)

    # Save the winning candidate results to the text file
    txt_file.write(winning_candidate_summary)

