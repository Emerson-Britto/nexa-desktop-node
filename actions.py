import vlc


def play_audio(manager, data):
	print("executing play_sound method.")
	if not manager.get("vlcInstance"):
		manager.set("vlcInstance", vlc.Instance())
		manager.set("player", vlcInstance.media_player_new())
	media = vlcInstance.media_new(data)
	player = manager.get("player")
	player.set_media(media)
	player.play()	

def stop_audio(manager, data):
	if player: player.stop()


def pause_audio(manager, data):
	if player: player.pause()


def resume_audio(manager, data):
	if player: player.play()
