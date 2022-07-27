class Mystuff(object):
    def __init__(self):
        targline="hello"
        self.targline="the world is yours"
    def apple(self):
        print("this is all about apples")
a=Mystuff()
a.apple()
print(a.targline)
class song(object):
    def __init__(self,lyrics):
        self.lyrics=lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
heat_waves=song(["])
love_me=song(["Love me like you do, lo-lo-love me like you do",
        "Love me like you do, lo-lo-love me like you do",
        "Touch me like you do, to-to-touch me like you do",
        "What are you waiting for?"])
heat_waves.sing_me_a_song()
love_me.sing_me_a_song()


    