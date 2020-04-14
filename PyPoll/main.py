import pathlib
import csv
import collections

filepath = pathlib.Path("../Resources/election_data.csv")


# =========================================== open file and calculate statistics ============================================

with open(filepath, "r") as csvfile:
    election_data = csv.reader(csvfile, delimiter = ",")

    # skip header
    next(election_data)

    # initialize counter of votes, candidate list, candidate name
    total_votes = 0
    candidate_list = []
    unique_candidate = []
    

    # loop through the data to store candidate list and count number of votes
    for row in election_data:
        total_votes = total_votes +1
        candidate_list.append(row[2])

        # store unique candidate value
        if not row[2] in unique_candidate:
            unique_candidate.append(row[2])

    # create a counter object to count number of votes per candidate
    my_counter = collections.Counter(candidate_list)

# =================================================== print out results ====================================================

print(
f"""Election Results
============================
Total Votes: {total_votes}
============================
{unique_candidate[0]}: {round((my_counter[unique_candidate[0]]/total_votes)*100,3)}% ({my_counter[unique_candidate[0]]})
{unique_candidate[1]}: {round((my_counter[unique_candidate[1]]/total_votes)*100,3)}% ({my_counter[unique_candidate[1]]})
{unique_candidate[2]}: {round((my_counter[unique_candidate[2]]/total_votes)*100,3)}% ({my_counter[unique_candidate[2]]})
{unique_candidate[3]}: {round((my_counter[unique_candidate[3]]/total_votes)*100,3)}% ({my_counter[unique_candidate[3]]})
============================
Winner: {my_counter.most_common(1)[0][0]}
============================

""")

# ==================================================== export results =====================================================

analysis_text = open("Poll_Analysis.txt","w")
analysis_text.write(
f"""Election Results
============================
Total Votes: {total_votes}
============================
{unique_candidate[0]}: {round((my_counter[unique_candidate[0]]/total_votes)*100,3)}% ({my_counter[unique_candidate[0]]})
{unique_candidate[1]}: {round((my_counter[unique_candidate[1]]/total_votes)*100,3)}% ({my_counter[unique_candidate[1]]})
{unique_candidate[2]}: {round((my_counter[unique_candidate[2]]/total_votes)*100,3)}% ({my_counter[unique_candidate[2]]})
{unique_candidate[3]}: {round((my_counter[unique_candidate[3]]/total_votes)*100,3)}% ({my_counter[unique_candidate[3]]})
============================
Winner: {my_counter.most_common(1)[0][0]}
============================

""")


        



    













