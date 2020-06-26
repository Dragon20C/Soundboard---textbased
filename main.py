import keyboard, simpleaudio as sa

while True:
    if keyboard.is_pressed("1"):
        wave_obj = sa.WaveObject.from_wave_file("sound effects/creeperexplosion.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()

    if keyboard.is_pressed("2"):
        wave_obj = sa.WaveObject.from_wave_file("sound effects/bruh.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()

    if keyboard.is_pressed("3"):
        wave_obj = sa.WaveObject.from_wave_file("sound effects/alert.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()

    if keyboard.is_pressed("4"):
        wave_obj = sa.WaveObject.from_wave_file("sound effects/fail.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()
