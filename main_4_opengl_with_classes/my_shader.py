from OpenGL.GL import *
import OpenGL.GL.shaders as gls

class Shader:

    def __init__(
            self, 
            vertexShaderfileName, 
            fragmentShaderfileName):
        
        # filenames
        self.m_vertexShaderfileName = vertexShaderfileName
        print(self.m_vertexShaderfileName)
        self.m_fragmentShaderfileName = fragmentShaderfileName
        
        with open(self.m_vertexShaderfileName, "r") as file:
            vsSource = file.read()

        # ler o arquivo fragment shader
        with open(self.m_fragmentShaderfileName, "r") as file:
            fragSource = file.read()

        # criar o objeto vertex shader
        vsId = gls.compileShader(vsSource, GL_VERTEX_SHADER)

        # criar o objeto fragment shader
        fsId = gls.compileShader(fragSource, GL_FRAGMENT_SHADER)

        # criar um shader program
        self.shaderId = gls.compileProgram(vsId, fsId)

    def bind(self):
        glUseProgram(self.shaderId)

    def unbind(self):
        glUseProgram(0)

    def setUniform(
            self,
            name,
            x, y=None, z=None, w=None):
        name_loc = glGetUniformLocation(self.shaderId, name)
        if y == None: glUniform1f(name_loc, x)
        elif z == None: glUniform2f(name_loc, x, y)
        elif w == None: glUniform3f(name_loc, x, y, z)
        else: glUniform4f(name_loc, x, y, z, w)

    def setUniformv(
            self,
            name,
            values):
        name_loc = glGetUniformLocation(self.shaderId, name)
        if len(values) == 1:    glUniform1fv(name_loc, 1, values)
        elif len(values) == 2:  glUniform2fv(name_loc, 1, values)
        elif len(values) == 3:  glUniform3fv(name_loc, 1, values)
        else:                   glUniform4fv(name_loc, 1, values)
