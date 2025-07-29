# SensoryAI - Five Senses Experience System 🤖👁️👂🖐️👃👅

An advanced AI system that simulates and experiences the world through all five human senses: **Vision**, **Hearing**, **Touch**, **Smell**, and **Taste**. This project demonstrates how AI can process and integrate multiple sensory inputs to create a coherent experience of the environment.

## 🌟 Features

### 🧠 **Central Sensory Brain**
- **Sensory Integration**: Combines all five senses into unified experiences
- **Consciousness Levels**: Adjustable awareness and attention focus
- **Memory Systems**: Each sense maintains its own memory bank
- **Experience Logging**: Complete history of all sensory experiences

### 👁️ **Vision System**
- **Color Perception**: RGB color mapping and recognition
- **Shape Recognition**: Circle, square, triangle, rectangle, oval detection
- **Object Recognition**: Person, car, tree, building, animal, book, phone identification
- **Scene Complexity Analysis**: Simple, moderate, or complex scene classification

### 👂 **Hearing System**
- **Sound Intensity Levels**: Loud, moderate, quiet sound classification
- **Frequency Analysis**: Low, medium, high frequency detection
- **Auditory Memory**: Recent sound experience storage

### 🖐️ **Touch System**
- **Texture Recognition**: Smooth, rough, soft, hard surface detection
- **Temperature Sensing**: Hot, warm, cool, cold temperature classification
- **Pressure Sensitivity**: Intensity based on pressure and contact

### 👃 **Smell System**
- **Scent Classification**: Pleasant, unpleasant, neutral, strong odor detection
- **Olfactory Memory**: Recent scent experience storage
- **Intensity Mapping**: Scent strength and quality assessment

### 👅 **Taste System**
- **Taste Categories**: Sweet, sour, salty, bitter, umami flavor recognition
- **Intensity Control**: Strong, mild, or neutral taste strength
- **Gustatory Memory**: Recent taste experience storage

## 🚀 How to Run This Project

### 📋 Prerequisites

Before running this project, make sure you have:

- **Python 3.7 or higher** installed on your system
- **pip** (Python package installer) available
- **Git** (optional, for cloning the repository)

### 🔧 Step-by-Step Setup

#### **Option 1: Using Git (Recommended)**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/sensory-ai.git
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

#### **Option 2: Manual Setup**

1. **Download the project files**:
   - Download all files from the repository
   - Extract them to a folder on your computer

2. **Open terminal/command prompt**:
   - Navigate to the project folder
   - Example: `cd C:\path\to\your\sensory-ai-folder`

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### 🎮 Running the Project

#### **Web App (Recommended)**
```bash
streamlit run streamlit_app.py
```
This opens a beautiful web interface in your browser where you can:
- Create custom environments with interactive forms
- Choose from preset scenarios
- Adjust AI consciousness levels in real-time
- View visual charts and statistics
- Browse experience history timeline
- **Windows users**: Double-click `run_streamlit.bat`

#### **Interactive Demo (Command Line)**
```bash
python interactive_demo.py
```
This provides a command-line interface where you can:
- Create custom environments
- Choose from preset scenarios
- Adjust AI consciousness levels
- View statistics and history

#### **Quick Start - Main Demo**
```bash
python sensory_ai.py
```
This runs the main demonstration with three different environments.

#### **Example Demonstrations**
```bash
python example_usage.py
```
This runs comprehensive examples showing different features and scenarios.

#### **Run Tests**
```bash
python test_sensory_ai.py
```
This runs the test suite to verify everything is working correctly.

### 🖥️ Platform-Specific Instructions

#### **Windows**
1. Open **Command Prompt** or **PowerShell**
2. Navigate to your project folder:
   ```cmd
   cd C:\path\to\your\sensory-ai-folder
   ```
3. Install dependencies:
   ```cmd
   pip install -r requirements.txt
   ```
4. Run the web app (recommended):
   ```cmd
   streamlit run streamlit_app.py
   ```
   **Or double-click `run_streamlit.bat`**
5. Or run the command-line version:
   ```cmd
   python sensory_ai.py
   ```

#### **macOS/Linux**
1. Open **Terminal**
2. Navigate to your project folder:
   ```bash
   cd /path/to/your/sensory-ai-folder
   ```
3. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```
4. Run the web app (recommended):
   ```bash
   streamlit run streamlit_app.py
   ```
   **Or run: `./run_streamlit.sh`**
5. Or run the command-line version:
   ```bash
   python3 sensory_ai.py
   ```

### 🐍 Python Environment Setup (Optional but Recommended)

#### **Using Virtual Environment**

1. **Create a virtual environment**:
   ```bash
   # Windows
   python -m venv sensory-ai-env
   
   # macOS/Linux
   python3 -m venv sensory-ai-env
   ```

2. **Activate the virtual environment**:
   ```bash
   # Windows
   sensory-ai-env\Scripts\activate
   
   # macOS/Linux
   source sensory-ai-env/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the project**:
   ```bash
   python sensory_ai.py
   ```

5. **Deactivate when done**:
   ```bash
   deactivate
   ```

### 🔍 Troubleshooting

#### **Common Issues and Solutions**

**Issue: "python is not recognized"**
- **Solution**: Make sure Python is installed and added to your system PATH
- **Alternative**: Try using `python3` instead of `python`

**Issue: "pip is not recognized"**
- **Solution**: Install pip or use `python -m pip` instead
- **Alternative**: Try using `pip3` instead of `pip`

**Issue: "ModuleNotFoundError"**
- **Solution**: Make sure you've installed the requirements:
  ```bash
  pip install -r requirements.txt
  ```

**Issue: "Permission denied" (Linux/macOS)**
- **Solution**: Use `sudo` or install Python packages for your user only:
  ```bash
  pip install --user -r requirements.txt
  ```

#### **Verifying Installation**

Run this command to verify everything is set up correctly:
```bash
python -c "from sensory_ai import SensoryAI; print('✅ SensoryAI is ready to use!')"
```

### 📱 Running on Different Systems

#### **Jupyter Notebook**
If you prefer using Jupyter Notebooks:
1. Install Jupyter: `pip install jupyter`
2. Start Jupyter: `jupyter notebook`
3. Create a new notebook and import the system:
   ```python
   from sensory_ai import SensoryAI
   ai = SensoryAI("NotebookAI")
   ai.wake_up()
   ```

#### **Google Colab**
You can also run this project in Google Colab:
1. Upload the `sensory_ai.py` file to Colab
2. Install dependencies: `!pip install numpy`
3. Import and use the system as shown above

### 🎯 First Run Experience

When you run the project for the first time, you should see:

```
=== SensoryAI - Five Senses Experience System ===

Alex is now awake and experiencing the world!

==================================================
EXPERIENCE 1: Pleasant Outdoor Environment
==================================================

Alex is experiencing the environment...

=== Alex's Sensory Experience ===
Consciousness Level: 1.0
Attention Focus: general
Overall Intensity: 0.40
Dominant Sense: smell
Experience Quality: neutral

Individual Sensory Inputs:
  Vision: simple scene (intensity: 0.30)
  Hearing: medium frequency (intensity: 0.50)
  Touch: warm neutral (intensity: 0.50)
  Smell: pleasant (intensity: 0.70)
  Taste: sweet (intensity: 0.60)
```

### 🚀 Next Steps

After successfully running the project:

1. **Try the interactive demo** to create your own environments
2. **Experiment with different consciousness levels**
3. **Create custom sensory experiences**
4. **Explore the code** to understand how it works
5. **Modify and extend** the system with new features

### 📞 Getting Help

If you encounter any issues:
1. Check the troubleshooting section above
2. Verify your Python version: `python --version`
3. Check if all dependencies are installed: `pip list`
4. Try running the test suite: `python test_sensory_ai.py`

## 📖 Usage

### Basic Usage

```python
from sensory_ai import SensoryAI

# Create a new AI instance
ai = SensoryAI("Alex")
ai.wake_up()

# Experience an environment
environment = {
    "vision": "A beautiful garden with colorful flowers and green trees",
    "hearing": "Gentle birds chirping and soft wind",
    "touch": "Warm sunlight on skin",
    "smell": "Fresh flowers and clean air",
    "taste": "Sweet taste of fresh air"
}

experience = ai.experience(environment)
```

### Advanced Usage

```python
# Set consciousness level (0.0 to 1.0)
ai.set_consciousness_level(0.8)

# Set attention focus
ai.set_attention_focus("visual")

# Get sensory statistics
stats = ai.get_sensory_stats()
print(stats)

# Get experience history
history = ai.get_experience_history()

# Put AI to sleep
ai.sleep()
```

## 🎯 Examples

### Example 1: Pleasant Outdoor Environment
```python
outdoor_environment = {
    "vision": "A beautiful garden with colorful flowers, green trees, and a clear blue sky",
    "hearing": "Gentle birds chirping and soft wind rustling through leaves",
    "touch": "Warm sunlight on skin and a gentle breeze",
    "smell": "Fresh flowers and clean air",
    "taste": "Sweet taste of fresh air"
}
```

### Example 2: Busy City Street
```python
city_environment = {
    "vision": "Tall buildings, cars, people walking, traffic lights",
    "hearing": "Loud traffic noise, car horns, and people talking",
    "touch": "Hard concrete sidewalk under feet",
    "smell": "Car exhaust and city air",
    "taste": "Neutral taste of city air"
}
```

### Example 3: Kitchen Environment
```python
kitchen_environment = {
    "vision": "Clean kitchen with cooking utensils and ingredients",
    "hearing": "Sizzling sounds of cooking and soft music",
    "touch": "Warm stove and smooth countertop",
    "smell": "Delicious food cooking and fresh herbs",
    "taste": "Sweet and savory flavors from cooking"
}
```

## 🏗️ Architecture

### Core Components

1. **SensoryInput**: Data structure for all sensory information
2. **Vision**: Processes visual information and maintains visual memory
3. **Hearing**: Processes auditory information and maintains auditory memory
4. **Touch**: Processes tactile information and maintains tactile memory
5. **Smell**: Processes olfactory information and maintains olfactory memory
6. **Taste**: Processes gustatory information and maintains gustatory memory
7. **SensoryBrain**: Central processor that integrates all sensory inputs
8. **SensoryAI**: Main AI class that manages the complete sensory experience

### Data Flow

```
Environment Description → Individual Senses → Sensory Brain → Integrated Experience
```

## 🔧 Customization

### Adding New Sensory Capabilities

You can extend the system by modifying the sensory classes:

```python
class Vision:
    def __init__(self):
        # Add new color perceptions
        self.color_perception['pink'] = (255, 192, 203)
        
        # Add new shapes
        self.shapes.append('hexagon')
        
        # Add new objects
        self.objects.append('computer')
```

### Custom Sensory Processing

```python
def custom_see(self, scene_description: str) -> SensoryInput:
    # Add your custom visual processing logic here
    custom_intensity = self.calculate_custom_intensity(scene_description)
    custom_quality = self.analyze_custom_quality(scene_description)
    
    return SensoryInput(
        sense_type="vision",
        intensity=custom_intensity,
        quality=custom_quality,
        location="custom visual field"
    )
```

## 📊 Output Format

The system provides detailed sensory analysis:

```
=== Alex's Sensory Experience ===
Consciousness Level: 1.0
Attention Focus: general
Overall Intensity: 0.65
Dominant Sense: vision
Experience Quality: pleasant

Individual Sensory Inputs:
  Vision: complex scene (intensity: 0.80)
  Hearing: medium frequency (intensity: 0.50)
  Touch: warm neutral (intensity: 0.50)
  Smell: pleasant (intensity: 0.70)
  Taste: sweet (intensity: 0.60)
```

## 🤝 Contributing

We welcome contributions! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by human sensory perception and cognitive science
- Built with modern Python practices and type hints
- Designed for educational and research purposes

## 🔮 Future Enhancements

- [ ] Real-time sensory processing
- [ ] Machine learning integration for improved recognition
- [ ] Virtual reality environment support
- [ ] Multi-agent sensory interaction
- [ ] Emotional response to sensory inputs
- [ ] Cross-modal sensory learning


**Made with ❤️ for the AI community**

*Experience the world through AI eyes, ears, hands, nose, and tongue!* 
