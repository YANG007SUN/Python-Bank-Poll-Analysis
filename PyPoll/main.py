import pathlib
import csv




filepath = pathlib.Path("../Resources/election_data.csv")


# ====================================== open file and calculate statistics =======================================
with open(filepath, "r") as csvfile:
    election_data = csv.reader(csvfile, delimiter = ",")

    # skip header
    next(election_data)

    # initialize counter of votes, candidate list, candidate name
    total_votes = 0
    candidate_list = []
    

    # loop through the data to store candidate list and count number of votes
    for row in election_data:
        total_votes = total_votes +1
        candidate_list.append(row[2])

    # use set compression to remove duplicates and convert to list
    candidate_set = set()
    candidate_set = {cand for cand in candidate_list}
    unique_candidate = list(candidate_set)

    # initialize number of vote 
    number_vote = [num for num in range(len(unique_candidate))] 

    # create dict to hold candidate name, number of votes
    my_dict = {u:n for u,n in zip(unique_candidate, number_vote)}

    for i in range(len(candidate_list)):
        my_dict[candidate_list[i]] = my_dict[candidate_list[i]]+1
       
    
    winner = max(my_dict, key = my_dict.get)

    




        



    print(winner)













