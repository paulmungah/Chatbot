import pandas as pd 

# load your data into a dataframe
df = pd.read_csv("health_data.csv")
# print(df)
print("Healthbot: Hello there, I am your Health assistance bot . Ask me about any symptoms.")


while True:
    # Get user input and store the same into  a variable
    user_text = input("\n You:").lower()

    # 2. Check if the users want to exit
    if user_text == "quit":
        print("Healthbot:Goodbye! Nice to have been of service to you")
        break

    # Create a variable eith will store the details structured in the csv file
    found_answer = False

    # come up with a loop through the enire data frame created before
    for index, row in df.iterrows():
        # clean up the keywords from the CSV row
        ketwords_list = str(row['Keywords']).split(',')

        # Check every keyword in that given row()

        for word in ketwords_list:
            clean_word = word.strip().lower()

            # if keyword is inside of the users sentence
            if clean_word in user_text:
                print("Healthboot:",row["Response"])
                found_answer = True
                break 

            if found_answer:
                break
            # Stop looking at otherr ansers  since we already found 
            #  match

            # 4. if we went through the entire CSV file and never found  a match of the keywords,
            # we need to display a message to tteh user

            if not found_answer :
                print("Healthbot : Sorry , i dont know that one.Try asking for somethinf else") 
     