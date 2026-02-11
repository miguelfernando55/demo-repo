import glfw
from OpenGL.GL import *

vertices = [
    [-0.8, -0.4],
    [-0.8, 0.4],
    [-0.4, -0.8],
    [-0.4, 0.8],
    [0.4, -0.8],
    [0.4, 0.8],
    [0.8, -0.4],
    [0.8, 0.4],
]

# Função para configurar inicialimente
def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glPointSize(10.0)
    glLineWidth(3.0)

# Função para renderizar a cena
def renderizar():
    # limpar a cor
    glClear(GL_COLOR_BUFFER_BIT)

    # desenhar os pontos
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POINTS)
    for v in vertices:
        glVertex2fv(v)
    glEnd()

    # pintar as faces
    glColor3f(0.2,0.0,0.0)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glBegin(GL_TRIANGLE_STRIP)
    for v in vertices:
        glVertex2fv(v)
    glEnd()

    # desenhar triangles strip em modo de strip
    glColor3f(1.0,0.0,0.0)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_TRIANGLE_STRIP)
    for v in vertices:
        glVertex2fv(v)
    glEnd()



def main():
    # inicializar a API GLFW
    glfw.init()

    # criar a janela
    window = glfw.create_window(
        500, 500, "2-2-Primitivas",
        None, None,
    )

    # criar o contexto no OpenGL
    glfw.make_context_current(window)

    # inicializar configurações
    init()

    # enquanto não fechar no X corre programa
    while not glfw.window_should_close(window):
        # correr eventos
        glfw.poll_events()

        # renderizar
        renderizar()

        # trocar buffers
        glfw.swap_buffers(window)

    # se terminar janela fecha a API
    glfw.terminate()

if __name__ == "__main__":
    main()


