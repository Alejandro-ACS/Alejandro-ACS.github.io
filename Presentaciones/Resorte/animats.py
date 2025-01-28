from manim import *

class PhaseSpaceSpring(Scene):
    def construct(self):
        # Configuración del tamaño de pantalla

        # Configuración del espacio fase, con un rango más amplio para adaptarse mejor a la pantalla
        axes = Axes(
            x_range=[-7, 7, 1],  # Ampliamos el rango de la elongación (x)
            y_range=[-7, 7, 1],  # Ampliamos el rango de la velocidad (v)
            x_length=16,  # Ajustado al ancho de la pantalla
            y_length=10,  # Ajustado a la altura de la pantalla
            tips=False,
        ).add_coordinates()
        axes_labels = axes.get_axis_labels(x_label="x", y_label="v")

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
            opacity=0.5,
            color=WHITE,  # Color inicial (se actualizará dinámicamente)
        )

        # Updater para cambiar dinámicamente el color de las líneas de corriente
        def update_streamline_color(stream):
            for line in stream:
                # Calcular el color basado en la posición promedio de la línea
                avg_pos = np.mean(line.get_points(), axis=0)
                line.set_color(color_func_amplitude(avg_pos))

        stream_lines.add_updater(update_streamline_color)

        # Animar las líneas de corriente
        self.add(axes, axes_labels, vector_field, stream_lines)
        stream_lines.start_animation(flow_speed=1.5)  # Animación continua
        self.wait(6)  # Esperar mientras las líneas fluyen
        self.play(stream_lines.end_animation())
