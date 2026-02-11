import glfw
from OpenGL.GL import * 

vertices = [
    [-0.5,-0.5],
    [0.5,-0.5],
    [0.0, 0.5]
]

cores = [
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0],
]

# Função para configurações iniciais da minha aplicação
def init():
    glClearColor(1,1,1,1)


# Função para atualizar a renderização da cena
def render():
    glClear(GL_COLOR_BUFFER_BIT)

    # pintar ecrâ
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    for v, c in zip(vertices, cores):
        glColor3fv(c)
        glVertex2fv(v)
    glEnd()

# Função Principal
def main():
    # inicalizar a API GLFW
    glfw.init()

    # criar a janela
    window = glfw.create_window(500, 500, "01 - Intro", None, None)
    
    # criar o contexto OpenGL na janela
    glfw.make_context_current(window)

    # inicializar a janela
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
