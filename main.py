from manimlib.imports import *
from pathlib import Path
import os
# ---------- FLAGS

RESOLUTION = ""
FLAGS = f"-pm {RESOLUTION}"
SCENE = "Test"


class Test(Scene):
    def construct(self):
        text = Text("Eai galera", color=TEAL)
        self.play(FadeIn(text))
        self.wait()


if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
