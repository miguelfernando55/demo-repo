import numpy as np
import ctypes

from OpenGL.GL import *

class Circle:
    def __init__(self):

        # raw data        
        self.vertices = [
            # posicoes      # cores
            [ -0.5, -0.5,   1.0, 0.0, 0.0],
            [  0.5, -0.5,   0.0, 1.0, 0.0],
            [  0.0,  0.5,   0.0, 0.0, 1.0],
        ]


        # number of vertices
        self.qtdVertices = len(self.vertices)
        self.vertices = np.array(
            self.vertices,
            dtype = np.float32
        )

        # ebo info
        self.faces = [
            [0, 1, 2], 
        ]
        self.qtdFaces = len(self.faces)
        self.faces = np.array(self.faces, dtype=np.uint32)

        # vao id - important to put the object on the graphic
        self.vaoId = glGenVertexArrays(1)
        # put the object on the graphic - this is just the id and pointer to the buffer
        glBindVertexArray(self.vaoId)

        # object is putted on the memory - buffer
        vboId = glGenBuffers(1)
        # the buffer is an array
        glBindBuffer(GL_ARRAY_BUFFER, vboId)
        # put the data on the array of the memory of the graphics
        glBufferData(
            GL_ARRAY_BUFFER, 
            self.vertices.nbytes,
            self.vertices,
            GL_STATIC_DRAW)
        #
        glEnableVertexAttribArray(0)
        #
        glVertexAttribPointer(0,
                              2,
                              GL_FLOAT,
                              GL_FALSE,
                              5 * 4,
                              ctypes.c_void_p(0))
        #
        glEnableVertexAttribArray(1)
        #
        glVertexAttribPointer(1,
                              3,
                              GL_FLOAT,
                              GL_FALSE,
                              5 * 4,
                              ctypes.c_void_p(2 * 4))
        #
        glBindBuffer(GL_ARRAY_BUFFER, 0)

        # unbind the vao Id
        glBindVertexArray(0)

    def render(self):
        # bind the vao
        glBindVertexArray(self.vaoId)
        
        # draw the line loop between vertices
        glDrawArrays(GL_LINE_LOOP, 0, self.qtdVertices)

        # unbind the vao
        glBindVertexArray(0)