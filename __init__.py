from mycroft import MycroftSkill, intent_file_handler


class Bible(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('bible.intent')
    def handle_bible(self, message):
        self.speak_dialog('bible')


def create_skill():
    return Bible()

