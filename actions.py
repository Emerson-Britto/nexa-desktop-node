import vlc


def play_audio(manager, data):
	print("executing play_sound method.")
	if not manager.get("vlcInstance"):
		manager.set("vlcInstance", vlc.Instance())
		vlcInstance = manager.get("vlcInstance")
		manager.set("player", vlcInstance.media_player_new())
	
	vlcInstance = manager.get("vlcInstance")
	media = vlcInstance.media_new(data)
	player = manager.get("player")
	player.set_media(media)
	player.play()	

def stop_audio(manager, data):
	player = manager.get("player")
	if player: player.stop()


def pause_audio(manager, data):
	player = manager.get("player")
	if player: player.pause()


def resume_audio(manager, data):
	player = manager.get("player")
	if player: player.play()
