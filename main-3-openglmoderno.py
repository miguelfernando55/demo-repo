import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders as gls
import numpy as np
import ctypes

vertices = [
    [-0.8, -0.8],   #v1
    [ 0.0, -0.8],   #v2
    [-0.4,  0.0],   #v3
    [ 0.0, -0.8],   #v4
    [ 0.8, -0.8],   #v5
    [ 0.4,  0.0],   #v6
    [-0.4,  0.0],   #v7
    [ 0.4,  0.0],   #v8
    [ 0.0,  0.8],   #v9
]

qtdVertices = len(vertices)

vaoId = 0

shaderId = 0

def init():
    # utilizar a variável de fora
    global vertices, vaoId, shaderId
    
    # limpo a tela
    glClearColor(1.0,1.0,1.0,1.0)

    # criar vaoID
    vaoId = glGenVertexArrays(1)
    # ativar vao
    glBindVertexArray(vaoId)

    # transformo os vertices em 4 bytes de memoria
    vertices = np.array(vertices, np.dtype(np.float32))

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
        0, # posicao do atributo
        2,  # 2 posições
        GL_FLOAT, # tipo de dado
        GL_FALSE, # não normaliza
        2 * 4, # salto em bytes
        ctypes.c_void_p(0), # inicio do buffer
    )

    # habilitar 
    glEnableVertexAttribArray(0)

    # desativar o vbo
    glBindBuffer(GL_ARRAY_BUFFER, 0)

    # desativar o vaoID
    glBindVertexArray(0)

    # criar shader

    # codigo fonte dos shaders

    # ler o arquivo vertex shader
    with open("vertex_shader.glsl", "r") as file:
        vsSource = file.read()

    # ler o arquivo fragment shader
    with open("fragment_shader.glsl", "r") as file:
        fragSource = file.read()

    # criar o objeto vertex shader
    vsId = gls.compileShader(vsSource, GL_VERTEX_SHADER)

    # criar o objeto fragment shader
    fsId = gls.compileShader(fragSource, GL_FRAGMENT_SHADER)

    # criar um shader program
    shaderId = gls.compileProgram(vsId, fsId)

def renderizar():
    # limpar a tela
    glClear(GL_COLOR_BUFFER_BIT)

    # usar programa
    glUseProgram(shaderId)

    # ativar o vertex array
    glBindVertexArray(vaoId)
    glDrawArrays(
        GL_TRIANGLES,
        0,
        qtdVertices
    )

    # desativar o vertex array
    glBindVertexArray(0)

    # parar programa
    glUseProgram(0)

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