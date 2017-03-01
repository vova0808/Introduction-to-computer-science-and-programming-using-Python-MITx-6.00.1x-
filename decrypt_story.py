from ps6 import *
def decrypt_story():
    story = get_story_string()
    message = CiphertextMessage(story)
    return message.decrypt_message()
