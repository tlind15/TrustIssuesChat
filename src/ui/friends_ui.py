from src.friends.friend_requests import SendFriendRequestController


class FriendRequestUI(object):

    @staticmethod
    def send_friend_request(session):
        recipient = input("Who would you like to send a friend request to? ")
        SendFriendRequestController.send_friend_request(session, recipient)
