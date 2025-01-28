from manim_slides import Slide
from manim import *

import numpy as np
import math

class LeyDeHooke(Slide):
    def construct(self):
        # Crear el texto "Ley de Hooke"
        titulo = Text("Ley de Hooke", font_size=72)

        # Animar el texto escribiéndolo en el centro
        self.play(Write(titulo))


        # NEXT SLIDE
        self.next_slide()


        # Animar una salida opcional (por ejemplo, desvanecimiento)
        self.play(FadeOut(titulo))
        
        # -----------------

        base_shift = 2 * UP  # Desplazamiento hacia arriba
        road = Line(start=7*LEFT+3*DOWN, end=7*RIGHT+3*DOWN, stroke_width=5).shift(base_shift)  # Base
        wall = Line(start=4*LEFT+3*DOWN, end=4*LEFT+UP, stroke_width=10).shift(base_shift)  # Pared
        block = Block(mass=1, side_length=1, fill_color=GREEN, fill_opacity=0.7, stroke_color=GREEN_A, z_index=-1).next_to(road, UP, buff=0)
        
        mola = always_redraw(lambda: DashedLine(
            start=wall.get_x()*RIGHT + (block.get_y()-0.25)*UP,
            end=block.get_x()*RIGHT + block.get_y()*UP + block.side_length*0.5*LEFT + 0.25*DOWN,
            stroke_color=GRAY, stroke_width=5))
        
        mola2 = always_redraw(lambda: DashedLine(
            start=wall.get_x()*RIGHT + (block.get_y()+0.25)*UP,
            end=block.get_x()*RIGHT + block.get_y()*UP + block.side_length*0.5*LEFT + 0.25*UP,
            stroke_color=GRAY, stroke_width=5))
        
        K: float = 0.5  # Constante del resorte
        self.play(Create(road), Create(wall), Create(block), Create(mola), Create(mola2))

        # Etiqueta de elongación y vector de fuerza
        dist = always_redraw(lambda: Distance(
            height=0.25, 
            start=(block.get_y()+0.75)*UP,
            end=(block.get_y()+0.75)*UP + block.get_x()*RIGHT))
        
        dist_label = always_redraw(lambda: MathTex(
            rf"\Delta x = {round(block.get_x(), 2)}").scale(0.5).next_to(dist, UP))
        
        force_vec = always_redraw(lambda: Vector(
            [-K * block.get_x(), 0], color=DARK_BLUE).shift((block.get_y()+0.1)*UP + block.get_x()*RIGHT))
        
        self.play(Create(dist), Write(dist_label), Create(force_vec))

        # NEXT SLIDE
        self.next_slide()


        # Desplazamiento inicial del bloque
        self.play(block.animate.shift(RIGHT * 2), run_time=1.5)  # Movimiento inicial hacia la derecha


        # NEXT SLIDE
        self.next_slide(loop=True)


        # Movimiento oscilante
        time = ValueTracker(0)
        vel_vec = always_redraw(lambda: Vector(
            [-2*0.5**0.5*np.sin(0.5**0.5 * time.get_value()), 0], 
            color=GOLD).shift((block.get_y()-0.1)*UP + block.get_x()*RIGHT))
        
        x_of_t = lambda box: box.set_x(2 * np.cos(time.get_value() * (K / block.mass)**0.5))
        block.add_updater(update_function=x_of_t)
        self.add(vel_vec)

        # Simulación del movimiento
        P = math.pi * 8 ** 0.5  # Periodo del movimiento
        self.play(time.animate.set_value(2*P), rate_func=rate_functions.linear, run_time=P)


        # NEXT SLIDE
        self.next_slide()


        self.play(
            Uncreate(block), Uncreate(mola), Uncreate(mola2),
            Uncreate(wall), Uncreate(road), Uncreate(dist), 
            Uncreate(dist_label), Uncreate(force_vec), Uncreate(vel_vec)
        )
        
        # ----------------------

        # Configuración del sistema de coordenadas con NumberPlane
        number_plane = NumberPlane(
            x_range=[-7, 7, 1],  # Rango de la elongación (x)
            y_range=[-7, 7, 1],  # Rango de la velocidad (v)
            axis_config={"color": WHITE},
            faded_line_ratio=3
        )

        # Etiquetas de los ejes
        axes_labels = number_plane.get_axis_labels(x_label="v", y_label="x")

        # Función que describe el campo vectorial del sistema masa-resorte
        def spring_field_func(pos):
            x, v = pos[:2]  # Elongación (x) y velocidad (v)
            magnitude = np.sqrt(v**2 + (-x)**2)  # Magnitud del vector
            if magnitude == 0:
                return np.array([0, 0, 0])
            return np.array([v, -x, 0]) / magnitude  # Normalización

        # Nueva escala de colores: Rojo > Naranja > Amarillo > Verde azulado > Azul claro
        def color_func_amplitude(pos):
            x = abs(pos[0])  # Usar solo la elongación (posición x)
            # Invertimos el orden de la interpolación para que el rojo sea el color para más elongación
            return interpolate_color(BLUE, interpolate_color(TEAL, interpolate_color(YELLOW, interpolate_color(ORANGE, RED, x / 7), x / 7), x / 7), x / 7)

        # Campo vectorial con vectores más pequeños y colores basados en amplitud
        vector_field = ArrowVectorField(
            spring_field_func,
            x_range=[-7, 7],  # Ampliamos el rango de la elongación (x)
            y_range=[-7, 7],  # Ampliamos el rango de la velocidad (v)
            length_func=lambda x: 0.5 * x,  # Reducir el tamaño de los vectores
        )
        for arrow in vector_field:
            pos = arrow.get_start()  # Obtener la posición del vector
            arrow.set_color(color_func_amplitude(pos))  # Asignar color

        # Líneas de corriente con colores dinámicos
        stream_lines = StreamLines(
            spring_field_func,
            x_range=[-7, 7],  # Ampliamos el rango de la elongación (x)
            y_range=[-7, 7],  # Ampliamos el rango de la velocidad (v)
            padding=1,
            stroke_width=2,
            max_anchors_per_line=100,
            dt=0.1,
            color=WHITE,  # Color inicial (se actualizará dinámicamente)
        )

        # Updater para cambiar dinámicamente el color de las líneas de corriente
        def update_streamline_color(stream):
            for line in stream:
                # Calcular el color basado en la posición promedio de la línea
                avg_pos = np.mean(line.get_points(), axis=0)
                line.set_color(color_func_amplitude(avg_pos))

        stream_lines.add_updater(update_streamline_color)

        # Animación paso a paso
        self.play(Write(number_plane), Write(axes_labels))  # Escribir el NumberPlane y las etiquetas de los ejes
        self.play(Write(vector_field))  # Escribir el campo vectorial

        self.add_foreground_mobject(stream_lines)
        # Aquí es donde iniciamos la animación de StreamLines
        stream_lines.start_animation(flow_speed=1.5)  # Iniciar la animación de las líneas de corriente
        self.wait(6)  # Esperar mientras las líneas fluyen

        # Detener la animación de las líneas de corriente al final
        self.play(stream_lines.end_animation())
        

        # NEXT SLIDE
        self.next_slide()


        # Crear el punto en el origen
        origin_point = Dot(color=WHITE).move_to(number_plane.c2p(0, 0))  # Punto en el origen
        origin_point.scale(1.5)
        self.play(Create(origin_point))


        # NEXT SLIDE
        self.next_slide()

        # Animación: sube dos unidades hacia arriba
        self.play(origin_point.animate.shift(DOWN * 2))  # Subir 2 unidades en el eje y


        # NEXT SLIDE
        self.next_slide(auto_next=True)


        b = TracedPath(origin_point.get_center, stroke_opacity=1)
        self.add(b)
        # Animación: rotar 360 grados alrededor del origen
        self.play(Rotate(
            origin_point,
            angle=-2*PI,
            about_point=ORIGIN,
            rate_func=linear
            ), run_time=1.5
        )


        # NEXT SLIDE
        self.next_slide(loop=True)


        self.play(Rotate(
            origin_point,
            angle=-2*PI,
            about_point=ORIGIN,
            rate_func=linear
            ), run_time=1.5
        )


        # NEXT SLIDE
        self.next_slide()


        self.play(FadeOut(VGroup(origin_point, b)))
        self.play(Unwrite(vector_field))
        self.play(Unwrite(axes_labels), Unwrite(number_plane))

        # --------------------

        creditoFin = Text("Práctica", font_size=72)

        # Animar el texto escribiéndolo en el centro
        self.play(Write(creditoFin))

class Distance(Line):
    def __init__(self, height=0.5, **kwargs):
        super().__init__(**kwargs)

        startL = super().get_start()
        endL = super().get_end()

        left_bound = Line(start=startL + 0.5 * height * DOWN, end=startL + 0.5 * height * UP)
        right_bound = Line(start=endL + 0.5 * height * DOWN, end=endL + 0.5 * height * UP)

        self.add(left_bound, right_bound)

class Block(Square):
    def __init__(self, mass: int, **kwargs):
        super().__init__(**kwargs)
        self.mass = mass