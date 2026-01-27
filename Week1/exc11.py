class spng:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist
    def __str__(self):
        return f"{self.title} - {self.artist}"

if _name_ == "_main_":
    master_library = [
        Song("Into the night", "Yasobi"),
        Song("Blinding Lights", "The Weeknd"),
        Song("Jo Tum Mere Ho", "Anuv Jain"),
        Song("Her", "JVKE"),
        Song("Mockingbird", "Eminem"),
        Song("Save Your Tears", "The Weekend"),
        Song("Line Without a Hook", "\Ricky Montgomery"),
        Song("Shivers", "Ed Sheeran"),
        Song("Butter", "BTS"),
        Song("Die For You", "The Weekend"),
        Song("Blue", "Yung Kai"),
        Song("Husn", "Anuv Jain"),
        Song("Rap God", "Eminem"),
        Song("Sahiba", "Aditya Rikhari"),
        Song("Save Your Tears", "The Weeknd"),
        Song("Gul", "Anuv Jain"),
        Song("Die With a Smile", "Bruno Mars"),
        Song("Heat Waves", "Glass Animals"),
        Song("Usseewa", "Ado"),
        Song("Fairytale", "Alexander Rybak")
    ]



    my_player = MusicPlayer()
    create_random_playlist(my_player, master_library)
    while True:
        print("\n" + "="*30)
        print("    PYTHON MUSIC PLAYER")
        print("="*30)
        print("1. Play")
        print("2. Pause")
        print("3. Resume")
        print("4. Next Song")
        print("5. Previous Song")
        print("6. Change Volume")
        print("7. Toggle Repeat")
        print("8. Shuffle (New Playlist)")
        print("0. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            my_player.play()
        elif choice == '2':
            my_player.pause()
        elif choice == '3':
            my_player.resume()
        elif choice == '4':
            my_player.next_song()
        elif choice == '5':
            my_player.prev_song()
        elif choice == '6':
            try:
                vol = int(input("Enter volume (0-100): "))
                my_player.change_volume(vol)
            except ValueError:
                print("Invalid number.")
        elif choice == '7':
            my_player.toggle_repeat()
        elif choice == '8':
            create_random_playlist(my_player, master_library)
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")