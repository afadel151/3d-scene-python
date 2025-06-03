# 🎮 Python 3D Rendering Engine

A modern OpenGL-based 3D rendering engine built with Python and PyOpenGL. This project demonstrates advanced 3D graphics programming concepts including shader-based rendering, lighting, texturing, and camera controls.

![3D Scene Preview](output/preview.png)

## ✨ Features

- **Modern OpenGL (3.3+)**
  - Shader-based rendering pipeline
  - Vertex and fragment shaders
  - VAO/VBO management
  - Texture mapping

- **Advanced Lighting**
  - Ambient lighting
  - Diffuse lighting
  - Specular highlights
  - Dynamic light positioning

- **Camera System**
  - First-person camera controls
  - WASD movement
  - Mouse look
  - Smooth camera transitions

- **Project Structure**
  - Modular and extensible architecture
  - Clean separation of concerns
  - Configuration management
  - Asset management

## 🛠️ Technical Stack

- **Python 3.10+**
- **PyOpenGL 3.1.7**
- **GLFW 2.5.9** (Window management)
- **NumPy 1.24.3** (Matrix operations)
- **Pillow 10.0.0** (Texture loading)
- **GLSL 330** (Shaders)

## 📁 Project Structure

```
python-3D-rendering/
├── main.py              # Main application entry point
├── config/             
│   └── settings.py      # Configuration parameters
├── core/               
│   └── camera.py       # Camera implementation
├── shaders/            
│   ├── vertex.glsl     # Vertex shader
│   └── fragment.glsl   # Fragment shader
├── utils/              
│   └── shader_loader.py # Shader management
├── assets/             
│   └── textures/       # Texture files
├── output/             # Rendered output directory
└── requirements.txt    # Python dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- OpenGL 3.3+ compatible graphics card
- Git
- pip (Python package installer)
- setuptools and wheel

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/python-3D-rendering.git
cd python-3D-rendering
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/MacOS
python -m venv .venv
source .venv/bin/activate
```

3. Upgrade pip and install build tools:
```bash
python -m pip install --upgrade pip
pip install --upgrade setuptools wheel
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

If you encounter any issues with PyOpenGL installation, try:
```bash
# Windows
pip install PyOpenGL PyOpenGL-accelerate --no-deps
pip install -r requirements.txt

# Linux/MacOS
pip install PyOpenGL PyOpenGL-accelerate
pip install -r requirements.txt
```

5. Add a texture:
   - Place a JPG image named `container.jpg` in `assets/textures/`
   - Or modify `config/settings.py` to use a different texture

### Running the Application

```bash
python main.py
```

## 🎮 Controls

- **W/A/S/D** - Move camera
- **Mouse** - Look around
- **ESC** - Exit application

## 🎨 Customization

### Configuration

Edit `config/settings.py` to modify:
- Window dimensions
- Camera settings
- Lighting parameters
- Rendering options

### Shaders

Modify shader files in `shaders/`:
- `vertex.glsl` - Vertex transformations
- `fragment.glsl` - Lighting and texturing

## 🧪 Development

### Adding New Features

1. **New Objects**
   - Add vertex data in `main.py`
   - Create new shader programs if needed

2. **New Effects**
   - Modify fragment shader
   - Add new uniforms in `main.py`

3. **New Controls**
   - Extend camera class in `core/camera.py`
   - Add input handling in `main.py`

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)
Project Link: [https://github.com/yourusername/python-3D-rendering](https://github.com/yourusername/python-3D-rendering)

## 🙏 Acknowledgments

- [LearnOpenGL](https://learnopengl.com/) for OpenGL tutorials
- [PyOpenGL](http://pyopengl.sourceforge.net/) documentation
- [GLFW](https://www.glfw.org/) for window management


