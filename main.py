import keyboard, simpleaudio as sa


while True:
    try:
        user = int(input("Please pick a number: "))
    except ValueError:
        print("This isn't a number")

    if user == 1:
        wave_obj = sa.WaveObject.from_wave_file("sound effects/creeperexplosion.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()
        user = 0
    if user == 2:
        wave_obj = sa.WaveObject.from_wave_file("sound effects/bruh.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()
        user = 0
    if user == 3:
        wave_obj = sa.WaveObject.from_wave_file("sound effects/alert.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()
        user = 0
    if user == 4:
        wave_obj = sa.WaveObject.from_wave_file("sound effects/fail.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()
        user = 0
    if keyboard.is_pressed("p"):
        print("key p was pressed")
