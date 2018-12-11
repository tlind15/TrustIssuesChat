
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
    def read_recipient(rsa_config):
        print("Which of the following friends do you want to send the message to?")
        all_friends = rsa_config.friends_rsa
        # need to eventually check if friends with public keys is empty
        friends_with_rsa_public_keys = [friend for friend in all_friends if all_friends[friend] is not None and
                                        all_friends[friend].strip() != ""]
        for i in range(0, len(friends_with_rsa_public_keys)):
            print("(" + str(i+1) + ") " + friends_with_rsa_public_keys[i])

        selection = int(input("\nSelection: "))
        return friends_with_rsa_public_keys[selection-1]

