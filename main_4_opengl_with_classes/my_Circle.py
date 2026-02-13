import numpy as np
import ctypes
import math
from OpenGL.GL import *

class Circle:
    def __init__(self, cx = 0, cy = 0, raio = 1, nDiv = 32):
        self._create_geometry(cx, cy, raio, nDiv)
        self._setup_buffers()

    def _create_geometry(self, cx, cy, raio, nDiv):
        vertices = []

        deltaAngle = 2 * math.pi / nDiv

        for i in range(nDiv):
            angle = i * deltaAngle
            x = cx + raio * math.cos(angle)
            y = cy + raio * math.sin(angle)
            vertices.append([x, y, 1.0, 0.0, 0.0])

        self.vertices = np.array(vertices, dtype=np.float32)

        # For line loop, indices are sequential
        self.indices = np.array(
            list(range(nDiv)),
            dtype=np.uint32
        )

        self.qtdIndices = len(self.indices)


    def _setup_buffers(self):
        self._create_vao()
        self._bind_vao()
        self._upload_vertex_data()
        self._define_vertex_layout()
        self._upload_index_data()
        self._unbind_vao()


    def render(self):
        self._bind_vao()
        glDrawElements(GL_LINE_LOOP, self.qtdIndices, GL_UNSIGNED_INT, None)
        self._unbind_vao()


    def _create_vao(self):
        self.vaoId = glGenVertexArrays(1)


    def _bind_vao(self):
        glBindVertexArray(self.vaoId)


    def _upload_vertex_data(self):
        self.vboId = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vboId)
        glBufferData(
            GL_ARRAY_BUFFER,
            self.vertices.nbytes,
            self.vertices,
            GL_STATIC_DRAW
        )


    def _define_vertex_layout(self):
        stride = 5 * self.vertices.itemsize

        # Attribute 0 → position (x, y)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(
            0,                  # attribute location
            2,                  # number of floats (x, y)
            GL_FLOAT,
            GL_FALSE,
            stride,
            ctypes.c_void_p(0)  # offset 0
        )

        # Attribute 1 → color (r, g, b)
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(
            1,                                  # attribute location
            3,                                  # number of floats
            GL_FLOAT,
            GL_FALSE,
            stride,
            ctypes.c_void_p(2 * self.vertices.itemsize)  # offset after x,y
        )

    def _upload_index_data(self):
        self.eboId = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.eboId)
        glBufferData(
            GL_ELEMENT_ARRAY_BUFFER,
            self.indices.nbytes,
            self.indices,
            GL_STATIC_DRAW
        )

    def _unbind_vao(self):
        glBindVertexArray(0)

