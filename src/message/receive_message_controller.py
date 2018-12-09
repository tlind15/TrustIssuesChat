from src.server.server_boundary import ServerBoundary
from src.server.server_command import CheckMessagesCommand
from src.json_data.json_deconstructor import JsonDeconstructor, ReceiveMessagesStrategy

class ReceiveMessageController(object):

    @staticmethod
    def get_messages(username, token):
        data = {"username": username}
        # response = ServerBoundary.send_request(CheckMessagesCommand(data, token)).json()
        response = {'data': [{'message': 'qmr7dGcDO5TnZ7qkG1cibw==', 'iv': 'GGM7uHY2zM+aS06jN7wu1A==', 'sender': 't2',
                          'key': 'Ex7pkNDJiRb3Ix4MdCjZxkghtzh+MaTSqUJ8ssRdAF4yNnGpJCKcqbhJIaG5YC6+EZicOPYIsma7kstsmI5gPgsYHJHwUnktoE2oJ12ASEee0se+7cci/6JQnKkJfBj0LGLBcwnlvN59ZJeW2H9lNOCQcYpZmhEZK7z456qqpt6tgbOElQ0I8bQRKe0PQae6B9aY6IwlSWKMcvbREvasEgZE8iqyXCSPsi5w8HAlU5wAv8vAKm3JLUsoC5OOarU8k7IGcLEuTgJGCO1uHTdjkC9XP7eY/ffsR/BNsjsqV2kBAOWwGZlco2DxvP1W3gtNBSrVXD+S2wE1Fx8zN3raZQ==',
                          'time': '2018-12-09 08:31:01', 'tag': '9nqX+uJRRi69/7sdmagPd/sWYxZNKcVRykGD+EAnN7Y='},
                         {'message': 'VgIL8F9tReBMZF2T0kMxGg==', 'iv': 'vMn/m2WzWA6HLoZAb1E4AA==', 'sender': 't2',
                          'key': 'RR4BjQ6X/Al7E0F5y2gXBaiXufujReB6mR5bCRTbaAz9V6NnbaEc15ZHWDdmuW0nl5UnU779ljyJPfz7RtzheC5o2HpyJfHpvtKbYOiXhHWtrBv4QF5O1O4VcLp7eT/HWUccPS52fTZnHL/J6eGj1oO5khwJj8ZOacA887UDt//4/RM0NBnOMVTzY7h9y8mHeDp0zF2nnfQeoeL2uEaj6iCeEPupfUzr2MdchmvM1m+P2WFapjeAr1Zwjdrf8jOEZjwL8F8kDKomTP0/tg6J087QRzaigpZh9KTozyCEeuQwWCNEvDNyfREEAc5DLuBcAboG1WcXgImVtk+dVOiFDQ==',
                          'time': '2018-12-09 08:31:21', 'tag': 'cNWtBt6IWw6YavFIYH7hHM0DNrioYYYGDV7O+3vfMdo='}],
                'status': 'Success'}
        return JsonDeconstructor.deconstruct_json(ReceiveMessagesStrategy(response))


