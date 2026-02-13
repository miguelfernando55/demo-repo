import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders as gls
import numpy as np
import ctypes
from my_shader import *

vertices = [
    [-0.8, -0.8, 1.0, 0.0, 0.0],   #v1
    [ 0.0, -0.8, 1.0, 1.0, 0.0],   #v2
    [ 0.8, -0.8, 1.0, 0.0, 1.0],   #v3
    [-0.4,  0.0, 0.0, 0.0, 1.0],   #v4
    [ 0.4,  0.0, 1.0, 1.0, 0.0],   #v5
    [ 0.0,  0.8, 0.0, 0.0, 1.0],   #v6
]

faces = [
    [0, 1, 3], # face inferior esquerda
    [1, 2, 4], # face inferior direita
    [3, 4, 5], # face superior
]

colors = [
    [1, 0, 0], # vermelho
    [0, 1, 0], # verde
    [0, 0, 1], # azul
    [1, 1, 0], # amarelo
    [1, 0, 1], # magenta
    [0, 1, 1], # ciano
]
colorActive = 0

qtdVertices = len(vertices)
qtdFaces = len(faces)

vaoId = 0

shaderId = 0

myshader = None

def init():
    # utilizar a variável de fora
    global vertices, faces, vaoId, shaderId, myshader
    
    # limpo a tela
    glClearColor(1.0,1.0,1.0,1.0)

    # criar vaoID
    vaoId = glGenVertexArrays(1)
    # ativar vao
    glBindVertexArray(vaoId)

    # transformo os vertices em 4 bytes de memoria
    vertices = np.array(vertices, dtype=np.float32)

    # criar o vbo - vertex buffer object
    vboId = glGenBuffers(1)

    # ativar o vbo
    glBindBuffer(GL_ARRAY_BUFFER, vboId)

    # enviar os dados para esse vbo  
    glBufferData(
        GL_ARRAY_BUFFER,
        vertices.nbytes,
        vertices,
        GL_STATIC_DRAW
    )

    # descrever como estão organizados os dados
    glVertexAttribPointer(
        0, # codigo do atributo ( posição )
        2,  # 2 posições
        GL_FLOAT, # tipo de dado
        GL_FALSE, # não normaliza
        5 * 4, # salto em bytes
        ctypes.c_void_p(0), # inicio do buffer
    )

    # descrever como estão organizados os dados
    glVertexAttribPointer(
        1, # codigo do atributo ( cor )
        3,  # 3 posições
        GL_FLOAT, # tipo de dado
        GL_FALSE, # não normaliza
        5 * 4, # salto em bytes
        ctypes.c_void_p(2 * 4), # inicio do buffer
    )

    # habilitar a posição
    glEnableVertexAttribArray(0)

    # habilitar a cor
    glEnableVertexAttribArray(1)

    # criando ebo
    faces = np.array(faces, dtype=np.uint32)
    eboId = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, eboId)
    glBufferData(
        GL_ELEMENT_ARRAY_BUFFER, 
        faces.nbytes,
        faces, 
        GL_STATIC_DRAW)

    # desativar o vbo
    glBindBuffer(GL_ARRAY_BUFFER, 0)

    # desativar o vaoID
    glBindVertexArray(0)

    # criar shader
    myshader = Shader(
        "vertex_shader.glsl",
        "fragment_shader.glsl"
    )
    
def renderizar():
    # limpar a tela
    glClear(GL_COLOR_BUFFER_BIT)

    # usar programa
    myshader.bind()

    # enviar o uniform das cores
    myshader.setUniformv("color", colors[colorActive])

    # ativar o vertex array
    glBindVertexArray(vaoId)
    glDrawElements(
        GL_TRIANGLES, # primitiva
        3 * qtdFaces,  # quantidade de faces
        GL_UNSIGNED_INT,
        None
    )

    # desativar o vertex array
    glBindVertexArray(0)

    # parar programa
    myshader.unbind()

def keyboard(window, key, scancode, action, mods):
    global colorActive

    if action == glfw.PRESS:
        if key == glfw.KEY_ESCAPE : glfw.set_window_should_close(window, True)
        if key == glfw.KEY_SPACE : colorActive = (colorActive + 1) % len(colors)

def main():
    # inicializar a API do GLFW
    glfw.init()

    # criar janela
    window = glfw.create_window(
        500, 500,
        "3 - OpenGL Moderno",
        None, None,
    )
    glfw.make_context_current(window)

    #
    glfw.set_key_callback(window, keyboard)

    # inicializar configurações iniciais
    init()

    # ciclo principal
    while not glfw.window_should_close(window):
        # correr eventos
        glfw.poll_events()

        # renderizar a tela
        renderizar()

        # trocar buffers
        glfw.swap_buffers(window)

    # terminar a API
    glfw.terminate()

if __name__ == "__main__":
    main()