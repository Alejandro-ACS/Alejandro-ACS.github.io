from ctypes import alignment
from math import cos, sin, tan
from pyclbr import Function
from manim import *
from manim_revealjs import PresentationScene


config.video_dir= "./videos"

class PrimeraDiapositiva(PresentationScene):
    def construct(self):
        # TODO find out why end_fragment has the t parameter
        titulo = Paragraph("LOS PLANETAS DEL\nSISTEMA SOLAR", alignment="center").scale(1.2)
        subtitulo = Paragraph("Hecho por: Alejandro Cutillas, Jaime Torres,\nJavier Soler y Pepe Ponce", alignment="center").next_to(titulo, DOWN).scale(0.5)
        self.add(titulo, subtitulo)
        self.end_fragment()

class SegundaDiapositiva(PresentationScene):
    def construct(self):
        plano = NumberPlane()
        vector_1 = Vector([3, 1], color="yellow")
        label_vector_1 = vector_1.coordinate_label("yellow")
        name_vector_1 = MathTex(r"\vec{v}").shift(vector_1.get_center()+0.4*UP)
        self.play(Write(plano))
        self.play(Write(vector_1), Write(label_vector_1), Write(name_vector_1))
        self.end_fragment()

        vector_1.generate_target()
        vector_1.target.move_to(4*LEFT)
        name_vector_1.generate_target()
        name_vector_1.target.move_to(0)
        label_vector_1.generate_target()
        label_vector_1.target.move_to(4*RIGHT)

        self.play(Unwrite(plano), run_time=1.5)
        self.play(MoveToTarget(vector_1), MoveToTarget(name_vector_1), MoveToTarget(label_vector_1))
        self.end_fragment()

        text_vector = Tex('Físico').move_to(4*LEFT + 1.5*UP)
        self.play(Write(text_vector))
        self.end_fragment()

        text_label = Tex('Programador').move_to(4*RIGHT + 1.5*UP)
        self.play(Write(text_label))
        self.end_fragment()

        text_name = Tex('Matemático').move_to(1.5*UP)
        self.play(Write(text_name))
        self.end_fragment()

        self.play(Unwrite(VGroup(vector_1, name_vector_1, label_vector_1, text_vector, text_label, text_name)))
        self.end_fragment()

class TerceraDiapositiva(PresentationScene):
    def construct(self):
        plano_2 = NumberPlane(
            background_line_style={
                "stroke_color": GREY_D,
                "stroke_width": 2,
                "stroke_opacity": 0.4
            },
            axis_config={
                "stroke_color": GREY_D,
                "stroke_width": 2.5,
                "stroke_opacity": 0.6
            }
        )
        plano = NumberPlane()
        vector_1 = Vector([3, 1], color="yellow")
        name_vector_1 = MathTex(r"\vec{v}").shift(vector_1.get_center()+0.4*UP)
        self.play(Write(plano_2), Write(plano))
        self.play(Write(vector_1), Write(name_vector_1))
        self.end_fragment()

        vector_1_decolored = Vector([3, 1], color=GREY_D)
        vector_1_2 = Vector([6, 2], color="yellow")
        name_vector_1_2 = MathTex("2", r"\vec{v}").shift(vector_1_2.get_center()+0.4*UP)
        self.play(TransformMatchingTex(name_vector_1, name_vector_1_2), TransformFromCopy(vector_1, vector_1_2), Transform(vector_1, vector_1_decolored))
        self.end_fragment()

        vector_1_3 = Vector([1, 1/3], color="yellow")
        name_vector_1_3 = MathTex(r"\frac{1}{3}", r"\vec{v}").shift(vector_1_3.get_center()+0.5*UP)
        self.play(TransformMatchingTex(name_vector_1_2, name_vector_1_3), Transform(vector_1_2, vector_1_3))
        self.end_fragment()
        
        self.play(Unwrite(vector_1_2), Unwrite(vector_1), Unwrite(name_vector_1_3))
        self.end_fragment()

        vector_i = Vector([1, 0], color=GREEN_E)
        label_i = MathTex("\hat{\imath}", color=GREEN_E).shift(vector_i.get_center()+0.4*DOWN)
        vector_j = Vector([0, 1], color=RED_E)
        label_j = MathTex("\hat{\jmath}", color=RED_E).shift(vector_j.get_center()+0.4*LEFT)
        self.play(Write(vector_i), Write(vector_j), Write(label_i), Write(label_j))
        self.end_fragment()

        matrix_text = Matrix([[1, 0],
                              [0, 1]]).set_column_colors(GREEN_E, RED_E)
        matrix_text.to_corner(UP+LEFT)
        self.play(Write(matrix_text))
        self.end_fragment()

        matrix_text_2 = Matrix([[1, 1],
                                [0, 1]]).set_column_colors(GREEN_E, RED_E)
        matrix_text_2.to_corner(UP+LEFT)
        self.play(ApplyMatrix([[1, 1],
                               [0, 1]], VGroup(plano, vector_j, label_j, vector_i, label_i)), Transform(matrix_text, matrix_text_2))
        self.end_fragment()

        matrix_text_3 = Matrix([[1, 0],
                                [0, 1]]).set_column_colors(GREEN_E, RED_E)
        matrix_text_3.to_corner(UP+LEFT)
        self.play(ApplyMatrix([[1, -1],
                               [0, 1]], VGroup(plano, vector_j, label_j, vector_i, label_i)), Transform(matrix_text, matrix_text_3))
        self.end_fragment()

        matrix_text_4 = Matrix([[1, 1],
                                [-1, 1]]).set_column_colors(GREEN_E, RED_E)
        matrix_text_4.to_corner(UP+LEFT)
        self.play(ApplyMatrix([[1, -1],
                               [1, 1]], VGroup(plano, vector_j, label_j, vector_i, label_i)), Transform(matrix_text, matrix_text_4))
        self.end_fragment()

        self.play(Unwrite(VGroup(plano, vector_j, label_j, vector_i, label_i, plano_2, matrix_text)))
        self.end_fragment()

class CuartaDiapositiva(PresentationScene):
    def construct(self):
        mruV = MathTex("{{v}}", "=", "{{{x}} \over {{t}}}")
        self.play(Write(mruV))
        self.end_fragment()

        mruT = MathTex("{{t}}", "=", "{{{x}} \over {{v}}}")
        self.play(TransformMatchingTex(mruV, mruT))
        self.end_fragment()

        mruT.generate_target()
        mruT.target.to_edge(UP)
        self.play(MoveToTarget(mruT))
        self.end_fragment()

        ax = Axes(
            x_range=[-2, 8, 1],
            y_range=[-2, 6, 1],
            tips=False,
            axis_config={"include_numbers": True},
        )

        ax_labels = ax.get_axis_labels(x_label='v', y_label='t')
        graph_1 = ax.plot(lambda x: 1/x, x_range=[1/6, 8], use_smoothing=False, color=BLUE_C)
        graph_1_2 = ax.plot(lambda x: 1/x, x_range=[-2, -1/6], use_smoothing=False, color=BLUE_C)
        self.play(Write(ax), Write(ax_labels))
        self.play(Write(graph_1_2))
        self.play(Write(graph_1))
        self.end_fragment()

        self.play(Unwrite(graph_1), Unwrite(graph_1_2), Unwrite(ax_labels), Unwrite(ax), Unwrite(mruT))
        self.end_fragment()

class QuintaDiapositiva(PresentationScene):
    def construct(self):
        v_text = MathTex('v', '=', '28000', '\ km/h')
        self.play(Write(v_text))
        self.end_fragment()

        v_text.generate_target()
        v_text.target.to_edge(UP)

        mercurio_text = Text('Mercurio')
        mercurio_text.scale(0.5)
        mercurio_text.to_corner(UP+LEFT).shift(0.5*DOWN)
        mercurio_img = ImageMobject('img/mercurio')
        mercurio_img.height = 1
        mercurio_img.next_to(mercurio_text, DOWN)
        mercurio_v = MathTex('t', '=', r'\frac{91.7 \cdot 10^{6}}{28000}', '=', '3275', '\ h', '\sim', '136.45', '\ d')
        mercurio_v.scale(0.5).next_to(mercurio_img, RIGHT)

        venus_text = Text('Venus')
        venus_text.scale(0.5)
        venus_text.next_to(mercurio_img, DOWN)
        venus_img = ImageMobject('img/venus')
        venus_img.height = 1
        venus_img.next_to(venus_text, DOWN)
        venus_v = MathTex('t', '=', r'\frac{42.4 \cdot 10^{6}}{28000}', '=', '1514.28', '\ h', '\sim', '63.09', '\ d')
        venus_v.scale(0.5).next_to(venus_img, RIGHT)

        marte_text = Text('Marte')
        marte_text.scale(0.5)
        marte_text.next_to(venus_img, DOWN)
        marte_img = ImageMobject('img/marte')
        marte_img.height = 1
        marte_img.next_to(marte_text, DOWN)
        marte_v = MathTex('t', '=', r'\frac{78.3 \cdot 10^{6}}{28000}', '=', '2796.42', '\ h', '\sim', '116.51', '\ d')
        marte_v.scale(0.5).next_to(marte_img, RIGHT)

        jupiter_text = Text('Jupiter')
        jupiter_text.scale(0.5).next_to(marte_img, DOWN)
        jupiter_img = ImageMobject('img/jupiter')
        jupiter_img.height = 1
        jupiter_img.next_to(jupiter_text, DOWN)
        jupiter_v = MathTex('t', '=', r'\frac{628.9 \cdot 10^{6}}{28000}', '=', '22460.71', '\ h', '\sim', '935.86', '\ d')
        jupiter_v.scale(0.5).next_to(jupiter_img, RIGHT)

        saturno_text = Text('Saturno')
        saturno_text.scale(0.5).to_corner(UP+RIGHT).shift(0.5*DOWN)
        saturno_img = ImageMobject('img/saturno')
        saturno_img.height = 1
        saturno_img.to_edge(UP).shift(DOWN+0.5*RIGHT)
        saturno_v = MathTex('t', '=', r'\frac{1284.4 \cdot 10^{6}}{28000}', '=', '45871.42', '\ h', '\sim', '1911.3', '\ d')
        saturno_v.scale(0.5).next_to(saturno_img, RIGHT)

        urano_text = Text('Urano')
        urano_text.scale(0.5).next_to(saturno_text, 6*DOWN)
        urano_img = ImageMobject('img/urano')
        urano_img.height = 1
        urano_img.next_to(saturno_img, 3*DOWN)
        urano_v = MathTex('t', '=', r'\frac{2721.4 \cdot 10^{6}}{28000}', '=', '97192.85', '\ h', '\sim', '4049.7', '\ d')
        urano_v.scale(0.5).next_to(urano_img, RIGHT)

        neptuno_text = Text('Neptuno')
        neptuno_text.scale(0.5).next_to(urano_text, 6*DOWN)
        neptuno_img = ImageMobject('img/neptuno')
        neptuno_img.height = 1
        neptuno_img.next_to(urano_img, 3*DOWN)
        neptuno_v = MathTex('t', '=', r'\frac{4345.4 \cdot 10^{6}}{28000}', '=', '155192.85', '\ h', '\sim', '6466.36', '\ d')
        neptuno_v.scale(0.5).next_to(neptuno_img, RIGHT)

        self.play(MoveToTarget(v_text))
        self.play(Write(VGroup(mercurio_text, mercurio_v, venus_text, venus_v, marte_text, marte_v, jupiter_text, jupiter_v, saturno_text, saturno_v, urano_text, urano_v, neptuno_text, neptuno_v)), FadeIn(mercurio_img), FadeIn(venus_img), FadeIn(marte_img), FadeIn(jupiter_img), FadeIn(saturno_img), FadeIn(urano_img), FadeIn(neptuno_img))
        self.end_fragment()

        self.play(Unwrite(VGroup(v_text, mercurio_text, mercurio_v, venus_text, venus_v, marte_text, marte_v, jupiter_text, jupiter_v, saturno_text, saturno_v, urano_text, urano_v, neptuno_text, neptuno_v)), FadeOut(mercurio_img), FadeOut(venus_img), FadeOut(marte_img), FadeOut(jupiter_img), FadeOut(saturno_img), FadeOut(urano_img), FadeOut(neptuno_img))
        self.end_fragment()

class SextaDiapositiva(PresentationScene):
    def construct(self):
        plane = NumberPlane(
            x_range=[0, 12, 3],
            y_range=[0, 4, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_numbers": True},
            x_axis_config={
                "decimal_number_config": {
                    "unit": "\cdot 10^{8}m",
                    "num_decimal_places": 0
                },
                "numbers_to_exclude": [12]
            },
            y_axis_config={
                "decimal_number_config": {
                    "unit": "s",
                    "num_decimal_places": 0
                },
                "numbers_to_exclude": [4]
            }
        )


        vector_yo = Vector([0, 6], color=YELLOW_E)
        vector_yo.shift(3*DOWN+3*LEFT)

        vector_ella = Vector([3, 6], color=BLUE)
        vector_ella.shift(3*DOWN+3*LEFT)

        vector_la_otra = Vector([3, 6], color=GREEN)
        vector_la_otra.shift(3*DOWN+1.5*LEFT)

        vector_yo_luz = Vector([6, 6], color=PURPLE)
        vector_yo_luz.shift(3*DOWN+3*LEFT)

        plane_labels = plane.get_axis_labels(x_label='x', y_label='t')
        grupo = VGroup(vector_yo, plane, vector_ella, vector_la_otra, vector_yo_luz, plane_labels)
        grupo.to_edge(LEFT).shift(RIGHT)
        self.play(Write(plane), Write(plane_labels))
        self.end_fragment()


        monigote = ImageMobject('img/monigote')
        monigote.scale(0.2).to_corner(UP+RIGHT).shift(2*LEFT)

        linterna = ImageMobject('img/linterna_morada')
        linterna.scale(0.2).next_to(monigote, RIGHT).shift(0.4*LEFT)

        cohete = ImageMobject('img/cohete')
        cohete.scale(0.4).next_to(monigote, DOWN)

        cohete_verde = ImageMobject('img/cohete_verde')
        cohete_verde.scale(0.4).next_to(cohete, DOWN)

        self.play(FadeIn(monigote), Write(vector_yo))
        self.end_fragment()


        self.play(FadeIn(cohete), Write(vector_ella))
        self.end_fragment()

        self.play(FadeIn(cohete_verde), Write(vector_la_otra))
        self.end_fragment()

        self.play(FadeIn(linterna), Write(vector_yo_luz))
        self.end_fragment()
        
        grupo.generate_target()
        grupo.target.move_to(0)
        self.play(FadeOut(linterna), FadeOut(monigote), FadeOut(cohete), FadeOut(cohete_verde), MoveToTarget(grupo))
        self.end_fragment()

        self.play(ApplyMatrix([[1, 0.5],
                               [0, 1]], plane, about_point=3*DOWN+3*LEFT))
        self.end_fragment()

        vector_ella_luz = Vector([9, 6], color=RED_E)
        vector_ella_luz.shift(3*DOWN+3*LEFT)
        self.play(Write(vector_ella_luz))
        self.end_fragment()

        self.play(ApplyMatrix([[1, -0.5],
                               [0, 1]], plane, about_point=3*DOWN+3*LEFT), Transform(vector_ella_luz, Vector([6, 4], color=RED_E).shift(3*DOWN+3*LEFT), run_time=2.5))
        self.end_fragment()

        grupo.add(vector_ella_luz)
        grupo.generate_target()
        grupo.target.to_edge(LEFT).shift(RIGHT)
        t_text = MathTex("t=t'")
        x_text = MathTex(r"x' = x - v \cdot t")
        t_text.to_edge(RIGHT).shift(UP*0.5+LEFT)
        x_text.to_edge(RIGHT).shift(DOWN*0.5+LEFT)
        self.play(MoveToTarget(grupo), Write(VGroup(t_text, x_text)))
        self.end_fragment()

        t_text_2 = MathTex(r'\text{¿}', "t=t'", '?').move_to(t_text.get_center())
        x_text_2 = MathTex(r'\text{¿}', r"x' = x - v \cdot t", '?').move_to(x_text.get_center())
        self.play(TransformMatchingTex(t_text, t_text_2), TransformMatchingTex(x_text, x_text_2))
        self.end_fragment()

        self.play(Unwrite(VGroup(grupo, t_text_2, x_text_2)))
        self.end_fragment()

class SeptimaDiapositiva(PresentationScene):
    def construct(self):
        eq_x_prima = MathTex("x'", '=', "x", '-', 'v', r'\cdot', 't')
        eq_x_prima.shift(UP)
        eq_x = MathTex('x', '=', "x'", '+', 'v', r'\cdot', "t'")
        eq_x.next_to(eq_x_prima, DOWN)
        self.play(Write(VGroup(eq_x_prima, eq_x)))
        self.end_fragment()

        eq_x_prima_2 = MathTex("x'", '=', r'\gamma', r'\cdot', '(', "x", '-', 'v', r'\cdot', 't', ')')
        eq_x_prima_2.shift(UP)
        eq_x_2 = MathTex('x', '=', r'\gamma', r'\cdot', '(', "x'", '+', 'v', r'\cdot', "t'", ')')
        eq_x_2.next_to(eq_x_prima_2, DOWN)
        self.play(TransformMatchingTex(eq_x_prima, eq_x_prima_2), TransformMatchingTex(eq_x, eq_x_2))
        self.end_fragment()

        eq_mult = MathTex("x'", r'\cdot', 'x', '=', r'\gamma^{2}', r'\cdot', '(', 'x', '-', 'v', r'\cdot', 't', ')', r'\cdot', '(', "x'", '+', 'v', r'\cdot', "t'", ')')
        self.play(TransformMatchingTex(VGroup(eq_x_prima_2, eq_x_2), eq_mult))
        self.end_fragment()

        eq_mult_2 = MathTex("ct'", r'\cdot', 'ct', '=', r'\gamma^{2}', r'\cdot', '(', "ct", '-', 'v', r'\cdot', 't', ')', r'\cdot', '(', "ct'", '+', 'v', r'\cdot', "t'", ')')
        self.play(TransformMatchingTex(eq_mult, eq_mult_2))
        self.end_fragment()

        eq_mult_3 = MathTex("c^{2}t't", '=', r'\gamma^{2}', r'\cdot', '(', "c^{2}tt'", '-', "vctt'", '+', "vctt'", '-', "v^{2}tt'", ')')
        self.play(TransformMatchingTex(eq_mult_2, eq_mult_3))
        self.end_fragment()

        eq_mult_4 = MathTex("c^{2}t't", '=', r'\gamma^{2}', r'\cdot', '(', "c^{2}tt'", '-', "v^{2}tt'", ')')
        self.play(TransformMatchingTex(eq_mult_3, eq_mult_4))
        
        eq_mult_5 = MathTex("c^{2}", '=', r'\gamma^{2}', r'\cdot', '(', "c^{2}", '-', "v^{2}", ')')
        self.play(TransformMatchingTex(eq_mult_4, eq_mult_5))
        self.end_fragment()

        eq_mult_6 = MathTex(r'\gamma^{2}', '=', '{', 'c^{2}', "\over", '{', 'c^{2}', '-', 'v^{2}', '}}')
        self.play(TransformMatchingTex(eq_mult_5, eq_mult_6))
        self.end_fragment()

        eq_mult_7 = MathTex(r'\gamma', '=', r'\sqrt{', 'c^{2}', "\over", '{', 'c^{2}', '-', 'v^{2}', '}}')
        self.play(TransformMatchingTex(eq_mult_6, eq_mult_7))
        self.end_fragment()

        eq_mult_8 = MathTex(r'\gamma', '=', '{', '1', "\over", r'\sqrt{', '1', '-', '{', 'v^{2}', r'\over', 'c^{2}', '}', '}}')
        self.play(TransformMatchingTex(eq_mult_7, eq_mult_8))
        self.end_fragment()

        eq_mult_8.generate_target()
        eq_mult_8.target.to_edge(UP)
        eq_x_2.move_to(0)
        self.play(MoveToTarget(eq_mult_8), Write(eq_x_2))
        self.end_fragment()

        eq_x_3 = MathTex("t'", '=', '{', 'x', r'\over', r'\gamma', 'v', '}', '-', '{', "x'", r'\over', 'v', '}')
        self.play(TransformMatchingTex(eq_x_2, eq_x_3))
        self.end_fragment()

        eq_x_4 = MathTex("t'", '=', '{', 'x', r'\over', r'\gamma', 'v', '}', '-', '{', r'\gamma', r'\cdot', '(', "x", '-', 'v', r'\cdot', 't', ')', r'\over', 'v', '}')
        self.play(TransformMatchingTex(eq_x_3, eq_x_4))
        self.end_fragment()

        eq_x_5 = MathTex("t'", '=', r'\gamma', r'\cdot', '(', '{', 'x', r'\over', r'\gamma^{2}', 'v', '}', '-', '{', "x", r'\over', 'v', '}', '+', '{', 'v', r'\cdot', 't', r'\over', 'v', '}', ')')
        self.play(TransformMatchingTex(eq_x_4, eq_x_5))
        self.end_fragment()

        eq_x_6 = MathTex("t'", '=', r'\gamma', r'\cdot', '(', 'x', r'\cdot', '(', '{', '1', r'\over', r'\gamma^{2}', 'v', '}', '-', '{', "1", r'\over', 'v', '}', ')', '+', '{', 'v', r'\cdot', 't', r'\over', 'v', '}', ')')
        self.play(TransformMatchingTex(eq_x_5, eq_x_6))
        self.end_fragment()

        eq_x_7 = MathTex("t'", '=', r'\gamma', r'\cdot', '(', 'x', r'\cdot', '(', '-', '{', 'v', r'\over', 'c^{2}', '}', ')', '+', 't', ')')
        self.play(TransformMatchingTex(eq_x_6, eq_x_7))
        self.end_fragment()

        eq_x_8 = MathTex("t'", '=', r'\gamma', r'\cdot', '(', 't', '-', 'x', r'\cdot', '{', 'v', r'\over', 'c^{2}', '}', ')')
        self.play(TransformMatchingTex(eq_x_7, eq_x_8))
        self.end_fragment()

        eq_x_prima_2.next_to(eq_x_8, DOWN)
        self.play(Write(eq_x_prima_2))
        self.end_fragment()

        self.play(Unwrite(VGroup(eq_x_prima_2, eq_mult_8, eq_x_8)))
        self.play(Write(Tex('Fin').scale(2.2)))
        self.end_fragment()