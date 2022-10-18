# experimental

from managers import Action_Manager
import actions
import socketio


action_Manager = Action_Manager()
action_Manager.extendModule(actions)
sio = socketio.Client()
sio.connect('http://127.0.0.1:3080')
print("connected to nexa server")


print("I need a room key, you can request it to me on telegram")
room_key = input("room key: ")
sio.emit("connect_to_room", room_key)



@sio.on('connected_to_room')
def connected_to_room(data):
	print(data)


@sio.on('room_key_error')
def room_key_error(data):
	print(data)
	room_key = input("room key: ")
	sio.emit("connect_to_room", room_key)


@sio.on('execute_order')
def execute_order(order):
	try:
		action_Manager.execute(order["label"], order.get("data"))
	except Exception as e:
		print("Error (execute_order)", e)