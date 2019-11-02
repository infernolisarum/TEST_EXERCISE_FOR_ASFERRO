import random
import string


def create_random_string(string_size):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    result_string = ""
    for _ in range(string_size):
        result_string += random.choice(chars)
    return result_string


def character_counter(string_to_count):
    char_counter = 0
    for i in string_to_count:
        if i.isalpha():
            char_counter += 1
    return char_counter


def create_rusult_letter(dict_with_letters):
    result_text = ""
    for key, value in dict_with_letters.iteritems():
        char_counter = character_counter(value)
        report_message = "Received mail on theme '{0}' with message: '{1}'. It contains '{2}' letters " \
                         "and '{3}' numbers".format(key, value, char_counter, 10 - char_counter)
        result_text += (report_message + "\n")
    return result_text
