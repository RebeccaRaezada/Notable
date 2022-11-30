def create_numbered_list(transcribed_text):
    lowercase_transcribed_text = transcribed_text.lower()
    index_mapping = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    result = {}
    counter = 1
    pre_numbered_list_extract = lowercase_transcribed_text.split("number")[0][0].upper() + lowercase_transcribed_text.split("number")[0][1:]

    text_splits = lowercase_transcribed_text.split("number")[1]
    next_text_splits = lowercase_transcribed_text.split("number next")[1:]
    location = index_mapping[text_splits.split(" ")[1]]
    first_line = ' '.join(text_splits.split(" ")[2:])
    result[location] = (first_line[0].upper() + first_line[1:])
    for sentence_parts in next_text_splits:
        phrase = (' '.join(sentence_parts.split(" ")[2:]))
        location += 1
        result[location] = (phrase[0].upper() + phrase[1:])
        counter += 1

    return result, pre_numbered_list_extract


transcription = "Patient presents today with several issues. " \
                "Number one BMI has increased by 10% since their " \
                "last visit number next patient reports experiencing " \
                "dizziness several times in the last two weeks. Number " \
                "next patient has a persistent cough that hasn’t improved " \
                "for last 4 weeks Number next patient is taking drug number " \
                "five several times a week."

result, pre_numbered_list_extract = create_numbered_list(transcription)
print(pre_numbered_list_extract)
for each_line in result:
    print(each_line, result[each_line])
