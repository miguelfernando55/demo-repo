import numpy as np
import ctypes

from OpenGL.GL import *

class Triangle:
    def __init__(self):
        self._create_geometry()
        self._setup_buffers()

    def _create_geometry(self):
        self.vertices = np.array([
            [-0.5, -0.5, 1.0, 0.0, 0.0],
            [ 0.5, -0.5, 0.0, 1.0, 0.0],
            [ 0.0,  0.5, 0.0, 0.0, 1.0],
        ], dtype=np.float32)

        self.faces = np.array([[0, 1, 2]], dtype=np.uint32)

        self.qtdVertices = len(self.vertices)
        self.qtdIndices = self.faces.size

    def _setup_buffers(self):
        self.vaoId = glGenVertexArrays(1)
        glBindVertexArray(self.vaoId)

        self.vboId = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vboId)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        stride = 5 * self.vertices.itemsize

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(2 * self.vertices.itemsize))

        self.eboId = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.eboId)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.faces.nbytes, self.faces, GL_STATIC_DRAW)

        glBindVertexArray(0)

    def render(self):
        glBindVertexArray(self.vaoId)
        glDrawElements(GL_LINE_LOOP, self.qtdIndices, GL_UNSIGNED_INT, None)
        glBindVertexArray(0)
