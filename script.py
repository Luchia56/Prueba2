import turtle as t, math as m, random as r

ESCALA = 100
s = t.Screen()
s.setup(600, 700)
s.bgcolor("black")
s.tracer(0)

p = t.Turtle()
p.hideturtle()
p.penup()

def corazon(u):
    x = 1.6 * (m.sin(u) ** 3)
    y = 1.3 * m.cos(u) - 0.5 * m.cos(2 * u) - 0.2 * m.cos(3 * u) - 0.1 * m.cos(4 * u)
    return x, y

N = 2000
rays = []
for i in range(N):
    u = r.uniform(0, 2 * m.pi)
    hx, hy = corazon(u)
    rays.append((hx, hy))

# Inicializamos el contador de pasos para la animación
step = 0

def color(f):
    f = max(0.0, min(1.0, f))
    r1, g1, b1 = 70, 0, 10
    r2, g2, b2 = 255, 30, 50
    return f"#{int(r1 + (r2 - r1) * f):02x}{int(g1 + (g2 - g1) * f):02x}{int(b1 + (b2 - b1) * f):02x}"

def loop():
    global step
    t_val = step * 0.05  # Controla la velocidad de avance de la animación
    
    p.clear()  # Limpia el fotograma anterior para que la animación fluya
    
    if t_val <= 1.6:
        head = min(1.0, t_val)
        tail = max(0.0, t_val - 0.35)
        fade = max(0, 1.0 - (t_val - 0.7)) if t_val > 0.7 else 1.0

        read_c = int(170 * fade)
        p.color(f"#{read_c:02x}001a")

        for hx, hy in rays:
            # Aplicamos la ESCALA para que tenga el tamaño correcto
            x1, y1 = hx * tail * ESCALA, hy * tail * ESCALA
            x2, y2 = hx * head * ESCALA, hy * head * ESCALA
            p.penup()
            p.goto(x1, y1)
            p.pendown()
            p.goto(x2, y2)

            if t_val < 0.9:
                p.penup()
                p.goto(x2, y2)
                p.color("#ff1a40")
                p.dot(1.8)
                p.color(f"#{read_c:02x}001a")
    else:
        step = 0  # Reinicia el bucle para que la animación se repita

    s.update()
    step += 1
    s.ontimer(loop, 25)

loop()
t.mainloop()