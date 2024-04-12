######################################################
#Rinchen Tshering
#First Year Electronics and communication Engineering (1ECE)
#02230104
######################################################
#Refrences 
#https://www.dataquest.io/blog/read-file-python/#:~:text=Python%20provides%20a%20built%2Din,we%20can%20manipulate%20its%20content
#https://youtu.be/qjrRf_pXWFQ?si=CLB8rvMkiTahGdi8 
#https://youtu.be/eMIPA6yL4BY?si=N39xA9ym-nC6u6yG 
#https://youtu.be/L-6thRrnyS0?si=7v3FsGp-Kwpbm-hU 
######################################################
#Solution
#solution score: 49524
#Put your number here: 4
######################################################

# Define a function to read the file
def read_input(file_path):
    # Open the file as read only
    with open(file_path, 'r') as f:
        # Read the file content
        content = f.read()
        # Split the content into lines
        lines = content.strip().split('\n')
        # Split each line into two parts (shape and outcome)
        rounds = [line.strip().split() for line in lines]
    # Return the list of rounds
    return rounds

# Define a function to calculate the scores
def calculate_score(rounds):
    # Create a dictionary to map each shape and outcome to a score
    score_map = {
        ("A", "X"): 3, ("A", "Y"): 4, ("A", "Z"): 8,
        ("B", "X"): 1, ("B", "Y"): 5, ("B", "Z"): 9,
        ("C", "X"): 2, ("C", "Y"): 6, ("C", "Z"): 7,
    }
    # Initialize the score to 0
    total_score = 0
    # Iterate over each rounds in the list of rounds
    for shape, outcome in rounds:
        # Check if the shape and outcome are valid
        if (shape, outcome) in score_map:
            # Add the score to the total score
            total_score += score_map[(shape, outcome)]
        # if the shape and outcomes are not in the score map
        else:
            #print an invalid message
            print("Invalid shape or outcome in the file.")
            return 0
    return total_score

# Specify the file path
file_path = "input_4_cap1.txt"
# Read the file in lines
rounds = read_input(file_path)
# Calculate the total scores based on the file content
total_score = calculate_score(rounds)
# Print the total score
print(f"the total score of the rock paper scissors game is: \n{total_score}")