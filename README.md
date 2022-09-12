# Election-Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code 1.38.1

## Results
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The county results were:
    - Jefferson County had 10.5% of the vote and 38,855 number of votes.
    - Denver County had 82.8% of the vote and 306,055 number of votes.
    - Arapahoe County had 6.7% of the vote and 24,801 number of votes.
- The largest county of the election was:
    - Denver County, which had 82.8% of the vote and 306,055 number of votes.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes

## Summary
The script used to generate the congressional election results dynamically generates the County and Candidates from a CSV file. Any state can provide a simple comma seperated value file, and get their results by without modifying the script.

The script can be modified to provide state votes instead of county for the Presidential Popular Vote.

The Script can be modified to provide zip code vote instead of county for Mayoral Election votes.