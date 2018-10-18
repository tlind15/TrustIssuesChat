
class MessageInput(object):

    @staticmethod
    def read_message():
        while True:
            try:
                message_text = str(input("Enter message: "))
                if message_text.strip() == "":
                    print("Not a valid message\n")
                else:
                    break

            except TypeError:
                print("Not a valid message\n")

        return message_text

    @staticmethod
    def read_user():
        pass

    @staticmethod
    def read_recipient():
        pass
