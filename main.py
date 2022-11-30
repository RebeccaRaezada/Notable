def create_numbered_list(transcribed_text):
    
    # making input case consistent
    lowercase_transcribed_text = transcribed_text.lower()
    
    # initializing variables
    index_mapping = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    numbered_list_extract = {}
    counter = 1
    
    # capturing introductory text, before the numbered list
    pre_numbered_list_extract = lowercase_transcribed_text.split("number")[0][0].upper() + lowercase_transcribed_text.split("number")[0][1:]

    # capturing phrases and starting location for numbered list of phrases
    first_phrase = lowercase_transcribed_text.split("number")[1]
    next_phrases = lowercase_transcribed_text.split("number next")[1:]
    
    start_location = index_mapping[first_phrase.split(" ")[1]]
    first_line = ' '.join(first_phrase.split(" ")[2:])
    
    # getting numbered list
    numbered_list_extract[start_location] = (first_line[0].upper() + first_line[1:])
    for phrases in next_phrases:
        phrase = (' '.join(phrases.split(" ")[2:]))
        start_location += 1
        numbered_list_extract[start_location] = (phrase[0].upper() + phrase[1:])
        counter += 1

    return pre_numbered_list_extract, numbered_list_extract


test_input = "Patient presents today with several issues. " \
                "Number one BMI has increased by 10% since their " \
                "last visit number next patient reports experiencing " \
                "dizziness several times in the last two weeks. Number " \
                "next patient has a persistent cough that hasn’t improved " \
                "for last 4 weeks Number next patient is taking drug number " \
                "five several times a week."

pre_numbered_list_extract, result = create_numbered_list(test_input)
print(pre_numbered_list_extract)
for each_line in result:
    print(each_line, result[each_line])
