import glfw
from OpenGL.GL import *

vertices = [
    [-0.8, -0.4],   #v0
    [-0.4, -0.8],   #v1
    [0.4, -0.8],    #v2
    [0.8, -0.4],    #v3
    [0.8, 0.4],     #v4
    [0.4, 0.8],     #v5
    [-0.4, 0.8],    #v6
    [-0.8, 0.4],    #v7
]

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glPointSize(10.0)
    glLineWidth(3.0)

def render():
    glClear(GL_COLOR_BUFFER_BIT)

    # pontos
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_POINTS)
    for v in vertices:
        glVertex2fv(v)
    glEnd()

    # lines
    # glBegin(GL_LINES)
    # for v in vertices:
    #     glVertex2fv(v)
    # glEnd()

    # line strip
    # glBegin(GL_LINE_STRIP)
    # for v in vertices:
    #     glVertex2fv(v)
    # glEnd()

    # line strip
    # glBegin(GL_LINE_LOOP)
    # for v in vertices:
    #     glVertex2fv(v)
    # glEnd()

    # polígono
    # glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    # glBegin(GL_TRIANGLES)
    # for v in vertices:
    #     glVertex2fv(v)
    # glEnd()

    # polígono com linhas
    # glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    # glColor3f(0.0, 0.0, 0.0)
    # glBegin(GL_TRIANGLES)
    # for v in vertices:
    #     glVertex2fv(v)
    # glEnd()

    # # triangle fan
    # glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    # glBegin(GL_TRIANGLE_FAN)
    # for v in vertices:
    #     glVertex2fv(v)
    # glEnd()

    # # triangle fan
    # glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    # glColor3f(0.0, 0.0, 0.0)
    # glBegin(GL_TRIANGLE_FAN)
    # for v in vertices:
    #     glVertex2fv(v)
    # glEnd()

    # triangle strip
    


def main():
    # inicializar a API glfw
    glfw.init()

    # criar a janela
    window = glfw.create_window(500, 500, "2 - Intro", None, None)

    # criar o contexto OpenGL na janela
    glfw.make_context_current(window)

    #inicializar a janela
    init()

    # enquanto a janela não é fechada
    while not glfw.window_should_close(window):
        # tratamento de eventos
        glfw.poll_events()

        # renderizar
        render()

        # troca de frame buffers
        glfw.swap_buffers(window)

    # terminar o API GLFW
    glfw.terminate()

if __name__ == "__main__":
    main()
    

