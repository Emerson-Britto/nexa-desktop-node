# experimental

from threading import Thread
import socketio
import vlc


sio = socketio.Client()
sio.connect('http://127.0.0.1:3080')
print("connected to nexa server")

vlcInstance = None
player = None


print("I need a room key, you can request it to me on telegram")
room_key = input("room key: ")
sio.emit("connect_to_room", room_key)


def play_sound(data):
	global vlcInstance, player
	if not vlcInstance:
		vlcInstance = vlc.Instance()
		player = vlcInstance.media_player_new()
	media = vlcInstance.media_new(data)
	player.set_media(media)
	player.play()


@sio.on('connected_to_room')
def connected_to_room(data):
	print(data)


@sio.on('room_key_error')
def room_key_error(data):
	print(data)
	room_key = input("room key: ")
	sio.emit("connect_to_room", room_key)


@sio.on('play_audio')
def play_audio(data):
	print("executing play_sound method.")
	play_sound(data)


@sio.on('stop_audio')
def stop_audio():
	if player: player.stop()


@sio.on('pause_audio')
def pause_audio():
	if player: player.pause()


@sio.on('resume_audio')
def resume_audio():
	if player: player.play()
