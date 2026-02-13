import glfw
from OpenGL.GL import *
from my_shader import *
import my_triangle
import my_Circle

def main():

    # inicializar a API do GLFW
    glfw.init()

    # criar a janela
    window = glfw.create_window(
        500, 500,
        "4 - OpenGL with Class",
        None, None
    )
    glfw.make_context_current(window)

    #
    glfw.set_key_callback(window, keyboard)

    # limpar a tela
    glClearColor(1.0,1.0,1.0,1.0)

    #############################
    # configurações de entrada

    # criar o objecto
    cx = 0
    cy = 0.4
    raio = 0.5
    nDiv = 32
    obj = my_Circle.Circle(cx, cy, raio, nDiv)

    # criar shader
    myshader = Shader(
        "./main_4_opengl_with_classes/vertex_shader.glsl",
        "./main_4_opengl_with_classes/fragment_shader.glsl"
    )

    # ciclo principal
    while not glfw.window_should_close(window):
        # correr eventos
        glfw.poll_events()

        # renderizar a tela
        glClear(GL_COLOR_BUFFER_BIT)

        # usar o programa
        myshader.bind()

        # renderizar o objeto
        obj.render()

        # parar o programa
        myshader.unbind()

        # trocar buffers
        glfw.swap_buffers(window)

    # terminar a API
    glfw.terminate()

# Função para gestão de eventos de teclado
def keyboard(window, key, scancode, action, mods):
    if action == glfw.PRESS:
        if key == glfw.KEY_ESCAPE : glfw.set_window_should_close(window, True)


if __name__ == "__main__":
    main()