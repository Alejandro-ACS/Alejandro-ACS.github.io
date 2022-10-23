from math import cos, sin, tan
from pyclbr import Function
from manim import *
from manim_revealjs import PresentationScene


config.video_dir= "./videos"

class FirstScene(PresentationScene):
    def construct(self):
        # TODO find out why end_fragment has the t parameter
        rect = Text("Teodolito")
        subtitle = Text("Hecho por: Luis De Páramo, Cristina De Rojas,\nÁfrica Navarro y Alejandro Cutillas")
        self.play(Write(rect))
        self.end_fragment()

        self.play(rect.animate.shift(UP).rotate(PI / 3))
        self.end_fragment()

        self.play(rect.animate.shift(3*LEFT))
        self.end_fragment()

class SecondScene(PresentationScene):
    def construct(self):
        ax = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 2],
            tips=False
        )

        circ = Circle(radius=2)
        radius = Line([0, 0, 0], [2, 0, 0], color=RED_A)
        num1 = Tex('1').shift(radius.get_center()+0.3*UP)

        self.play(Create(ax))
        self.play(Create(circ))
        self.play(Create(radius), Write(num1))
        self.end_fragment()

        self.play(Rotate(VGroup(radius, num1), angle=PI/4, about_point=[0, 0, 0]))
        coseno = Line([0, 0, 0], [radius.get_end()[0], 0, 0], color=BLUE)
        seno = Line([radius.get_end()[0], 0, 0], [radius.get_end()[0], radius.get_end()[1], 0], color=TEAL)
        letrC = Tex('cos').shift(coseno.get_center()+0.3*DOWN)
        letrS = Tex('sen').shift(seno.get_center()+0.5*RIGHT)
        self.play(Create(coseno), Create(seno), Write(letrC), Write(letrS))
        self.end_fragment()

        self.play(Unwrite(letrS), Unwrite(letrC))
        pTgline = TangentLine(circ, alpha=0.125, length=4)
        tgline = Line(pTgline.get_center(), pTgline.get_start(), color=ORANGE)
        letrTg = Tex('tan').shift(tgline.get_center()+0.3*UP+0.3*RIGHT)
        letrS.z_index = 1
        tgline.z_index = 0
        self.play(Create(tgline), Write(letrTg))
        self.end_fragment()

        ctgline = Line(pTgline.get_center(), pTgline.get_end(), color=GOLD)
        scline = Line([0, 0, 0], pTgline.get_start(), color=YELLOW)
        cscline = Line([0, 0, 0], pTgline.get_end(), color=MAROON)
        letrCtg = Tex('cotan').shift(ctgline.get_center()+0.2*UP+0.7*RIGHT)
        letrSc = Tex('sec').shift(scline.get_center()+0.3*DOWN)
        letrCsc = Tex('cosec').shift(cscline.get_center()+0.7*LEFT)
        self.play(Unwrite(letrTg), Create(ctgline), Create(scline), Create(cscline), Write(letrCtg), Write(letrSc), Write(letrCsc))
        self.end_fragment()

class SineCosine_Curve(PresentationScene):
    def construct(self):
        self.show_axis()
        self.show_circle()
        self.move_dot_and_draw_curve()

        self.wait()

    def show_axis(self):
        x_start = np.array([-6,2,0])
        x_end = np.array([3,2,0])

        y_start = np.array([-4,-3,0])
        y_end = np.array([-4,3.5,0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)
        self.add_xy_labels()

        self.orgin_point = np.array([-4,2,0])
        self.curve_start = np.array([-3,2,0])

    def add_xy_labels(self):
        x_labels = [
            MathTex(r"\pi"), MathTex(r"2 \pi"),
            MathTex(r"3 \pi"), MathTex(r"4 \pi"),
        ]

        y_labels = [
            MathTex(r"\pi"), MathTex(r"2 \pi"),
            MathTex(r"3 \pi"), MathTex(r"4 \pi"),
        ]

        for i in range(len(x_labels)):  # -2 -1 0 1
            x_labels[i].scale(0.6)
            x_labels[i].next_to(np.array([-2+i,2,0]), DOWN )
            self.add(x_labels[i])

        for i in range(len(y_labels)):  # 1 0 -1 -2
            y_labels[i].scale(0.6)
            y_labels[i].rotate(-PI/2)
            y_labels[i].next_to(np.array([-4, 1-i,0]), LEFT )
            self.add(y_labels[i])

    def show_circle(self):
        circle = Circle(radius=1)
        circle.move_to(self.orgin_point)

        self.add(circle)
        self.circle = circle

    def move_dot_and_draw_curve(self):
        orbit = self.circle
        orgin_point = self.orgin_point

        dot = Dot(radius=0.08, color=YELLOW)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.5

        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            # print(self.t_offset)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_circle():
            return Line(orgin_point, dot.get_center(), color=BLUE)

        ### sine
        def get_line_to_sine():
            x = self.curve_start[0] + self.t_offset * 2
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )

        self.sine_curve = VGroup()
        self.sine_curve.add(Line(self.curve_start,self.curve_start))
        def get_sine_curve():
            last_line = self.sine_curve[-1]
            x = self.curve_start[0] + self.t_offset * 2
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=YELLOW_D)
            self.sine_curve.add(new_line)

            return self.sine_curve

        ### cosine
        def get_line_to_cosine():
            x = dot.get_center()[0]
            y = self.curve_start[1] - self.t_offset * 2
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )

        self.cosine_curve = VGroup()
        self.cosine_curve.add(Line(self.curve_start, self.curve_start))

        def get_cosine_curve():
            last_line = self.cosine_curve[-1]
            x = dot.get_center()[0]
            y = self.curve_start[1] - self.t_offset * 2
            new_line = Line(last_line.get_end(), np.array([x, y, 0]), color=YELLOW_D)
            self.cosine_curve.add(new_line)

            return self.cosine_curve


        dot.add_updater(go_around_circle) #move dot around the circle

        origin_to_circle_line = always_redraw(get_line_to_circle) # from circle origin to dot

        dot_to_sine_line = always_redraw(get_line_to_sine) # from dot to sine curve
        sine_curve_line = always_redraw(get_sine_curve) # sine curve

        dot_to_cosine_line = always_redraw(get_line_to_cosine)  # from dot to cosine curve
        cosine_curve_line = always_redraw(get_cosine_curve)  # cosine curve

        self.add(dot, orbit)
        self.add(origin_to_circle_line,
                 dot_to_sine_line, sine_curve_line,
                 dot_to_cosine_line, cosine_curve_line,
         )
        self.wait(5.51)
        dot.remove_updater(go_around_circle)
        self.end_fragment()

        sinCosEquality = MathTex(r'sen(x)=cos(x-\frac{\pi}{2})')
        self.play(Write(sinCosEquality))
        self.end_fragment()

        sine = MathTex(r'sen(x)=sen(x+2k\pi)').shift(sinCosEquality.get_center()+DOWN)
        cosine = MathTex(r'cos(x)=cos(x+2k\pi)').shift(sine.get_center()+DOWN)
        kN = MathTex(r'k\in \mathbb{Z}').shift(cosine.get_center()+DOWN)
        self.play(Write(sine), Write(cosine), Write(kN))
        self.end_fragment()

class FourthScene(PresentationScene):
    def construct(self):
        imagen = ImageMobject('img')
        self.play(FadeIn(imagen))
        catetoA = Line([-4.5, 0.9, 0], [2.7, 0.9, 0])
        catetoO = Line([2.7, 0.9, 0], [2.7, 3.7, 0])
        hip = Line([-4.5, 0.9, 0], [2.7, 3.7, 0])
        angle = Angle(catetoA, hip, radius=2)
        triangulo = VGroup(catetoA, catetoO, hip, angle)
        self.play(Create(triangulo))
        self.end_fragment()

        self.play(FadeOut(imagen))
        trianguloC = VGroup(triangulo)
        trianguloC.generate_target()
        trianguloC.target.shift(DOWN*2.5+RIGHT)
        self.play(MoveToTarget(trianguloC))
        value = DecimalNumber(25, unit="^{\circ}").next_to(angle)
        letrcatA = Tex('5 m').shift(catetoA.get_center()+0.3*DOWN)
        letrcatO = Tex('h-1.5 m').shift(catetoO.get_center()+1*RIGHT)
        self.play(Write(value), Write(letrcatA), Write(letrcatO))
        self.end_fragment()

        self.play(Uncreate(triangulo), Unwrite(letrcatO), Unwrite(letrcatA), Unwrite(value))
        equat1 = MathTex("tan( 25^{\circ} )", "=", "{{{h}} - {{1.5}} \over {{5}}}")
        self.play(Write(equat1))
        self.end_fragment()

        equat2 = MathTex("h", "=", "tan( 25^{\circ} )", r"\cdot", "5", "+", "1.5")
        self.play(TransformMatchingTex(equat1, equat2))
        self.end_fragment()

        equat3 = MathTex("h", "=", "tan( 25^{\circ} )", r"\cdot", "5", "+", "1.5", r"\approx", "3.83")
        self.play(TransformMatchingTex(equat2, equat3))
        self.end_fragment()