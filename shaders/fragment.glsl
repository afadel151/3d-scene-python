#version 330 core
out vec4 FragColor;

in vec3 FragPos;
in vec3 Normal;
in vec2 TexCoord;

void main()
{
    // Output a solid red color
    FragColor = vec4(1.0, 0.0, 0.0, 1.0);
} 