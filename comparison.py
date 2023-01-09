import pandas as pd

# Load the perfect matches into a dataframe
perfect_matches = pd.read_csv("data/abc.csv")
# half = pd.read_csv("data/abchalf.csv")
# Load the ground truths into a dataframe
ground_truths = pd.read_csv("data/DBLP-ACM_perfectMapping.csv")

ground_truths['idACM'] = ground_truths['idACM'].astype(object)
# ground_truths = ground_truths.sort_values(by=['idACM', 'idDBLP'])
# perfect_matches= perfect_matches.sort_values(by=['idACM', 'idDBLP'])
# # df1 = ground_truths.iloc[:, :1112]
# # print(perfect_matches[])
# print(ground_truths.size)
# merged = pd.merge(half, perfect_matches, on=["idDBLP", "idACM"], how="inner")
#
# # ground_truths['idDBLP'] = ground_truths['idDBLP'].strip()
# # ground_truths['idACM'] = ground_truths['idACM'].str.strip()
# # perfect_matches['idDBLP'] = perfect_matches['idDBLP'].str.strip()
# # perfect_matches['idACM'] = perfect_matches['idACM'].str.strip()
# # perfect_matches = perfect_matches.strip()
# # merged = pd.merge(perfect_matches, ground_truths,  how="inner")
# print(merged.head())
# # merged1 = pd.merge(ground_truths, perfect_matches, on=["idDBLP", "idACM"], how="inner")
# # print(merged1.head())
# # Calculate the accuracy as the number of true matches divided by the total number of matches
# num_matches = len(perfect_matches)
# num_true_matches = len(merged)
# accuracy = num_true_matches / num_matches
#
# # Print the accuracy
# print(f"Accuracy: {accuracy:.2f}")


# Initialize a counter for the number of true matches
num_true_matches = 0

# Iterate over the rows in the perfect_matches dataframe
for i, row in perfect_matches.iterrows():
    # Check if the row is present in the ground_truths dataframe
    if row['idDBLP'] in ground_truths['idDBLP'].values and row['idACM'] in ground_truths['idACM'].values:
        # If the row is present, increment the counter
        num_true_matches += 1

# Calculate the accuracy as the number of true matches divided by the total number of matches
num_matches = len(ground_truths)
accuracy = num_true_matches / num_matches

# Print the accuracy
print(f"Accuracy: {accuracy:.2f}")