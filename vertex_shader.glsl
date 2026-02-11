// declarar a versão de GLSL
#version 330 core

// declarar entradas e saídas
layout(location = 0) in vec2 a_pos;

void main()
{
    gl_Position = vec4(a_pos, 0.0, 1.0);
}