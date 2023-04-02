from ctypes import alignment
from pyclbr import Function
from manim import *
from manim_revealjs import PresentationScene, LOOP, NO_PAUSE


config.video_dir= "./videos"

class PrimeraDiapositiva(PresentationScene):
    def construct(self):
        # TODO find out why end_fragment has the t parameter
        titulo = Paragraph("Joseph Fourier", alignment="center").scale(1.2)
        self.play(Write(titulo))
        self.end_fragment()