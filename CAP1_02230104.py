######################################################
#Rinchen Tshering
#First Year Electronics and communication Engineering (1ECE)
#02230104
######################################################
#Refrences 
#https://www.dataquest.io/blog/read-file-python/#:~:text=Python%20provides%20a%20built%2Din,we%20can%20manipulate%20its%20content
#https://chat.openai.com/c/080cac69-fa41-4ff5-9923-f4aea9e14dee 
#https://youtu.be/qjrRf_pXWFQ?si=CLB8rvMkiTahGdi8 
#https://youtu.be/eMIPA6yL4BY?si=N39xA9ym-nC6u6yG 
######################################################
#Solution
#solution score: 49226
#49226
######################################################

# Define a function to read the contents of a file
def read_file(file_path):
    # Open the file in read mode
    with open(file_path, 'r') as f:
        # Read the lines of the file into a list
        contents = f.readlines()
    # Return the list of lines
    return contents

# Define a function to calculate the score based on the file contents
def calculate_score(lines):
    # Initialize the total score to 0
    total_score = 0
    # Iterate over each line in the list
    for i in lines:
        # Split the line into two parts (shape and outcome)
        shape, outcome = i.strip().split()
        # Determine the score for the shape
        shape_score = {'A': 1, 'B': 2, 'C': 3}[shape]
        # Determine the score for the outcome
        outcome_score = {'X': 0, 'Y': 3, 'Z': 6}[outcome]
        # Add the shape score and the outcome score to the total score
        total_score += shape_score + outcome_score
    # Return the total score
    return total_score

# Specify the file path
file_path = 'input_4_cap1.txt'
# Read the contents of the file
lines = read_file(file_path)
# Calculate the total score based on the file contents
total_score = calculate_score(lines)
# Print the total score
print(f'The total score of the rock paper scissors game is: \n{total_score}')