from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
import random

class DiceLayout(BoxLayout):
    dice_source = StringProperty("dice1.png")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.roll_sound = SoundLoader.load("roll_sound.wav")
        self.anim_event = None
        self.anim_index = 0

    def roll_dice(self):
        if self.roll_sound:
            self.roll_sound.play()
        self.anim_index = 0
        self.anim_event = Clock.schedule_interval(self.animate_roll, 0.1)

    def animate_roll(self, dt):
        self.anim_index += 1
        number = random.randint(1, 6)
        self.dice_source = f"dice{number}.png"
        if self.anim_index >= 10:  # stop animation after 10 frames
            self.anim_event.cancel()

class DiceApp(App):
    def build(self):
        return DiceLayout()

if __name__ == "__main__":
    DiceApp().run()