from OpenGL.GL import *
from OpenGL.GL import shaders
import os

class ShaderLoader:
    @staticmethod
    def load_shader(shader_path, shader_type):
        try:
            print(f"Loading shader from: {shader_path}")
            if not os.path.exists(shader_path):
                print(f"Error: Shader file not found at {shader_path}")
                return None

            with open(shader_path, 'r') as f:
                shader_source = f.read()
                print(f"Shader source loaded:\n{shader_source}")
            
            shader = glCreateShader(shader_type)
            glShaderSource(shader, shader_source)
            glCompileShader(shader)
            
            # Check for compilation errors
            if not glGetShaderiv(shader, GL_COMPILE_STATUS):
                error = glGetShaderInfoLog(shader)
                print(f"Shader compilation error: {error}")
                return None
            
            print(f"Shader compiled successfully")
            return shader
        except Exception as e:
            print(f"Error loading shader {shader_path}: {str(e)}")
            return None

    @staticmethod
    def create_program(vertex_path, fragment_path):
        try:
            print("\nCreating shader program...")
            vertex_shader = ShaderLoader.load_shader(vertex_path, GL_VERTEX_SHADER)
            if vertex_shader is None:
                print("Failed to load vertex shader")
                return None

            fragment_shader = ShaderLoader.load_shader(fragment_path, GL_FRAGMENT_SHADER)
            if fragment_shader is None:
                print("Failed to load fragment shader")
                return None
            
            program = glCreateProgram()
            glAttachShader(program, vertex_shader)
            glAttachShader(program, fragment_shader)
            glLinkProgram(program)
            
            # Check for linking errors
            if not glGetProgramiv(program, GL_LINK_STATUS):
                error = glGetProgramInfoLog(program)
                print(f"Shader program linking error: {error}")
                return None
            
            print("Shader program linked successfully")
            
            # Clean up
            glDeleteShader(vertex_shader)
            glDeleteShader(fragment_shader)
            
            return program
        except Exception as e:
            print(f"Error creating shader program: {str(e)}")
            return None 