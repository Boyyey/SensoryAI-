import time
import json
import threading
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from datetime import datetime
import random
import numpy as np

@dataclass
class SensoryInput:
    """Data structure for sensory input"""
    sense_type: str
    intensity: float  # 0.0 to 1.0
    quality: str
    location: Optional[str] = None
    timestamp: float = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = time.time()

class Vision:
    """Simulates the sense of sight"""
    
    def __init__(self):
        self.visual_memory = []
        self.color_perception = {
            'red': (255, 0, 0),
            'green': (0, 255, 0),
            'blue': (0, 0, 255),
            'yellow': (255, 255, 0),
            'purple': (128, 0, 128),
            'orange': (255, 165, 0),
            'black': (0, 0, 0),
            'white': (255, 255, 255)
        }
        self.shapes = ['circle', 'square', 'triangle', 'rectangle', 'oval']
        self.objects = ['person', 'car', 'tree', 'building', 'animal', 'book', 'phone']
    
    def see(self, scene_description: str) -> SensoryInput:
        """Process visual information"""
        # Simulate visual processing
        colors = [color for color in self.color_perception.keys() 
                 if color in scene_description.lower()]
        shapes = [shape for shape in self.shapes 
                 if shape in scene_description.lower()]
        objects = [obj for obj in self.objects 
                  if obj in scene_description.lower()]
        
        # Calculate visual intensity based on scene complexity
        intensity = min(1.0, (len(colors) + len(shapes) + len(objects)) / 10.0)
        
        # Determine visual quality
        if len(objects) > 3:
            quality = "complex scene"
        elif len(objects) > 1:
            quality = "moderate detail"
        else:
            quality = "simple scene"
        
        visual_input = SensoryInput(
            sense_type="vision",
            intensity=intensity,
            quality=quality,
            location="visual field"
        )
        
        self.visual_memory.append(visual_input)
        return visual_input
    
    def get_visual_memory(self) -> List[SensoryInput]:
        """Retrieve recent visual memories"""
        return self.visual_memory[-10:]  # Last 10 visual inputs

class Hearing:
    """Simulates the sense of hearing"""
    
    def __init__(self):
        self.auditory_memory = []
        self.sounds = {
            'loud': ['thunder', 'explosion', 'siren', 'shout'],
            'moderate': ['conversation', 'music', 'traffic', 'footsteps'],
            'quiet': ['whisper', 'rustling', 'breathing', 'clock tick']
        }
        self.frequencies = {
            'low': ['bass', 'rumble', 'thunder'],
            'medium': ['human voice', 'music', 'traffic'],
            'high': ['whistle', 'bird chirp', 'alarm']
        }
    
    def hear(self, sound_description: str) -> SensoryInput:
        """Process auditory information"""
        # Determine sound intensity
        intensity = 0.5  # Default moderate
        for level, sounds in self.sounds.items():
            if any(sound in sound_description.lower() for sound in sounds):
                intensity = {'loud': 0.9, 'moderate': 0.5, 'quiet': 0.2}[level]
                break
        
        # Determine frequency quality
        quality = "medium frequency"
        for freq, sounds in self.frequencies.items():
            if any(sound in sound_description.lower() for sound in sounds):
                quality = f"{freq} frequency"
                break
        
        auditory_input = SensoryInput(
            sense_type="hearing",
            intensity=intensity,
            quality=quality,
            location="auditory field"
        )
        
        self.auditory_memory.append(auditory_input)
        return auditory_input
    
    def get_auditory_memory(self) -> List[SensoryInput]:
        """Retrieve recent auditory memories"""
        return self.auditory_memory[-10:]  # Last 10 auditory inputs

class Touch:
    """Simulates the sense of touch"""
    
    def __init__(self):
        self.tactile_memory = []
        self.textures = {
            'smooth': ['glass', 'metal', 'plastic'],
            'rough': ['sandpaper', 'bark', 'stone'],
            'soft': ['fabric', 'fur', 'cotton'],
            'hard': ['wood', 'concrete', 'ice']
        }
        self.temperatures = {
            'hot': ['fire', 'steam', 'sun'],
            'warm': ['body heat', 'warm water'],
            'cool': ['breeze', 'shade'],
            'cold': ['ice', 'snow', 'cold metal']
        }
    
    def feel(self, touch_description: str) -> SensoryInput:
        """Process tactile information"""
        # Determine texture
        texture = "neutral"
        for text_type, items in self.textures.items():
            if any(item in touch_description.lower() for item in items):
                texture = text_type
                break
        
        # Determine temperature
        temperature = "neutral"
        for temp_type, items in self.temperatures.items():
            if any(item in touch_description.lower() for item in items):
                temperature = temp_type
                break
        
        # Calculate intensity based on pressure and temperature
        intensity = 0.5
        if 'pressure' in touch_description.lower():
            intensity = 0.8
        elif 'gentle' in touch_description.lower():
            intensity = 0.3
        
        quality = f"{texture} {temperature}"
        
        tactile_input = SensoryInput(
            sense_type="touch",
            intensity=intensity,
            quality=quality,
            location="tactile receptors"
        )
        
        self.tactile_memory.append(tactile_input)
        return tactile_input
    
    def get_tactile_memory(self) -> List[SensoryInput]:
        """Retrieve recent tactile memories"""
        return self.tactile_memory[-10:]  # Last 10 tactile inputs

class Smell:
    """Simulates the sense of smell"""
    
    def __init__(self):
        self.olfactory_memory = []
        self.scents = {
            'pleasant': ['flowers', 'baking', 'fresh air', 'coffee'],
            'unpleasant': ['rotten', 'smoke', 'chemicals', 'garbage'],
            'neutral': ['paper', 'wood', 'metal', 'water'],
            'strong': ['perfume', 'garlic', 'ammonia', 'gasoline']
        }
    
    def smell(self, scent_description: str) -> SensoryInput:
        """Process olfactory information"""
        # Determine scent category and intensity
        intensity = 0.5
        quality = "neutral"
        
        for scent_type, items in self.scents.items():
            if any(item in scent_description.lower() for item in items):
                quality = scent_type
                if scent_type == 'strong':
                    intensity = 0.9
                elif scent_type == 'pleasant':
                    intensity = 0.7
                elif scent_type == 'unpleasant':
                    intensity = 0.6
                break
        
        olfactory_input = SensoryInput(
            sense_type="smell",
            intensity=intensity,
            quality=quality,
            location="olfactory receptors"
        )
        
        self.olfactory_memory.append(olfactory_input)
        return olfactory_input
    
    def get_olfactory_memory(self) -> List[SensoryInput]:
        """Retrieve recent olfactory memories"""
        return self.olfactory_memory[-10:]  # Last 10 olfactory inputs

class Taste:
    """Simulates the sense of taste"""
    
    def __init__(self):
        self.gustatory_memory = []
        self.tastes = {
            'sweet': ['sugar', 'honey', 'fruit', 'chocolate'],
            'sour': ['lemon', 'vinegar', 'citrus', 'yogurt'],
            'salty': ['salt', 'chips', 'pretzels', 'olives'],
            'bitter': ['coffee', 'dark chocolate', 'grapefruit', 'beer'],
            'umami': ['meat', 'cheese', 'mushrooms', 'soy sauce']
        }
    
    def taste(self, taste_description: str) -> SensoryInput:
        """Process gustatory information"""
        # Determine taste type and intensity
        intensity = 0.5
        quality = "neutral"
        
        for taste_type, items in self.tastes.items():
            if any(item in taste_description.lower() for item in items):
                quality = taste_type
                # Adjust intensity based on taste strength
                if 'strong' in taste_description.lower():
                    intensity = 0.9
                elif 'mild' in taste_description.lower():
                    intensity = 0.3
                else:
                    intensity = 0.6
                break
        
        gustatory_input = SensoryInput(
            sense_type="taste",
            intensity=intensity,
            quality=quality,
            location="taste buds"
        )
        
        self.gustatory_memory.append(gustatory_input)
        return gustatory_input
    
    def get_gustatory_memory(self) -> List[SensoryInput]:
        """Retrieve recent gustatory memories"""
        return self.gustatory_memory[-10:]  # Last 10 gustatory inputs

class SensoryBrain:
    """Central processing unit that integrates all sensory inputs"""
    
    def __init__(self):
        self.vision = Vision()
        self.hearing = Hearing()
        self.touch = Touch()
        self.smell = Smell()
        self.taste = Taste()
        
        self.sensory_integration = []
        self.consciousness_level = 1.0
        self.attention_focus = "general"
        
    def process_sensory_input(self, sense_type: str, description: str) -> SensoryInput:
        """Process input from a specific sense"""
        if sense_type.lower() == "vision":
            return self.vision.see(description)
        elif sense_type.lower() == "hearing":
            return self.hearing.hear(description)
        elif sense_type.lower() == "touch":
            return self.touch.feel(description)
        elif sense_type.lower() == "smell":
            return self.smell.smell(description)
        elif sense_type.lower() == "taste":
            return self.taste.taste(description)
        else:
            raise ValueError(f"Unknown sense type: {sense_type}")
    
    def integrate_senses(self) -> Dict[str, Any]:
        """Integrate all sensory inputs into a coherent experience"""
        all_inputs = {
            'vision': self.vision.get_visual_memory(),
            'hearing': self.hearing.get_auditory_memory(),
            'touch': self.touch.get_tactile_memory(),
            'smell': self.smell.get_olfactory_memory(),
            'taste': self.taste.get_gustatory_memory()
        }
        
        # Calculate overall sensory intensity
        total_intensity = 0
        active_senses = 0
        
        for sense, inputs in all_inputs.items():
            if inputs:
                total_intensity += inputs[-1].intensity
                active_senses += 1
        
        avg_intensity = total_intensity / max(active_senses, 1)
        
        # Determine dominant sense
        dominant_sense = "none"
        max_intensity = 0
        
        for sense, inputs in all_inputs.items():
            if inputs and inputs[-1].intensity > max_intensity:
                max_intensity = inputs[-1].intensity
                dominant_sense = sense
        
        # Create integrated experience
        integrated_experience = {
            'timestamp': time.time(),
            'consciousness_level': self.consciousness_level,
            'attention_focus': self.attention_focus,
            'overall_intensity': avg_intensity,
            'dominant_sense': dominant_sense,
            'sensory_inputs': all_inputs,
            'experience_quality': self._determine_experience_quality(all_inputs)
        }
        
        self.sensory_integration.append(integrated_experience)
        return integrated_experience
    
    def _determine_experience_quality(self, all_inputs: Dict[str, List[SensoryInput]]) -> str:
        """Determine the overall quality of the sensory experience"""
        pleasant_count = 0
        unpleasant_count = 0
        total_inputs = 0
        
        for inputs in all_inputs.values():
            for input_data in inputs:
                total_inputs += 1
                if 'pleasant' in input_data.quality.lower():
                    pleasant_count += 1
                elif 'unpleasant' in input_data.quality.lower():
                    unpleasant_count += 1
        
        if total_inputs == 0:
            return "neutral"
        
        pleasant_ratio = pleasant_count / total_inputs
        unpleasant_ratio = unpleasant_count / total_inputs
        
        if pleasant_ratio > 0.5:
            return "pleasant"
        elif unpleasant_ratio > 0.5:
            return "unpleasant"
        else:
            return "neutral"
    
    def experience_environment(self, environment_description: Dict[str, str]) -> Dict[str, Any]:
        """Experience a complete environment with all senses"""
        sensory_inputs = {}
        
        # Process each sense
        for sense, description in environment_description.items():
            try:
                sensory_inputs[sense] = self.process_sensory_input(sense, description)
            except ValueError as e:
                print(f"Warning: {e}")
                continue
        
        # Integrate all senses
        integrated_experience = self.integrate_senses()
        
        return {
            'individual_senses': sensory_inputs,
            'integrated_experience': integrated_experience
        }
    
    def get_sensory_summary(self) -> Dict[str, Any]:
        """Get a summary of all sensory experiences"""
        return {
            'total_visual_experiences': len(self.vision.visual_memory),
            'total_auditory_experiences': len(self.hearing.auditory_memory),
            'total_tactile_experiences': len(self.touch.tactile_memory),
            'total_olfactory_experiences': len(self.smell.olfactory_memory),
            'total_gustatory_experiences': len(self.taste.gustatory_memory),
            'total_integrated_experiences': len(self.sensory_integration),
            'consciousness_level': self.consciousness_level,
            'attention_focus': self.attention_focus
        }

class SensoryAI:
    """Main AI class that experiences the world through five senses"""
    
    def __init__(self, name: str = "SensoryAI"):
        self.name = name
        self.brain = SensoryBrain()
        self.is_awake = True
        self.experience_log = []
        
    def wake_up(self):
        """Wake up the AI and start experiencing"""
        self.is_awake = True
        print(f"{self.name} is now awake and experiencing the world!")
    
    def sleep(self):
        """Put the AI to sleep"""
        self.is_awake = False
        print(f"{self.name} is now sleeping...")
    
    def experience(self, environment: Dict[str, str]) -> Dict[str, Any]:
        """Experience an environment through all senses"""
        if not self.is_awake:
            print(f"{self.name} is sleeping and cannot experience anything.")
            return {}
        
        print(f"\n{self.name} is experiencing the environment...")
        
        # Process the experience
        experience_result = self.brain.experience_environment(environment)
        
        # Log the experience
        self.experience_log.append({
            'timestamp': datetime.now().isoformat(),
            'environment': environment,
            'experience': experience_result
        })
        
        # Print experience summary
        self._print_experience_summary(experience_result)
        
        return experience_result
    
    def _print_experience_summary(self, experience_result: Dict[str, Any]):
        """Print a summary of the sensory experience"""
        integrated = experience_result['integrated_experience']
        
        print(f"\n=== {self.name}'s Sensory Experience ===")
        print(f"Consciousness Level: {integrated['consciousness_level']}")
        print(f"Attention Focus: {integrated['attention_focus']}")
        print(f"Overall Intensity: {integrated['overall_intensity']:.2f}")
        print(f"Dominant Sense: {integrated['dominant_sense']}")
        print(f"Experience Quality: {integrated['experience_quality']}")
        
        print("\nIndividual Sensory Inputs:")
        for sense, input_data in experience_result['individual_senses'].items():
            print(f"  {sense.capitalize()}: {input_data.quality} (intensity: {input_data.intensity:.2f})")
    
    def get_experience_history(self) -> List[Dict[str, Any]]:
        """Get the complete history of experiences"""
        return self.experience_log
    
    def get_sensory_stats(self) -> Dict[str, Any]:
        """Get statistics about sensory experiences"""
        return self.brain.get_sensory_summary()
    
    def set_consciousness_level(self, level: float):
        """Set the consciousness level (0.0 to 1.0)"""
        self.brain.consciousness_level = max(0.0, min(1.0, level))
        print(f"Consciousness level set to: {self.brain.consciousness_level}")
    
    def set_attention_focus(self, focus: str):
        """Set the attention focus"""
        self.brain.attention_focus = focus
        print(f"Attention focus set to: {focus}")

# Example usage and demonstration
def main():
    """Demonstrate the SensoryAI system"""
    print("=== SensoryAI - Five Senses Experience System ===\n")
    
    # Create the AI
    ai = SensoryAI("Alex")
    ai.wake_up()
    
    # Example 1: A pleasant outdoor experience
    print("\n" + "="*50)
    print("EXPERIENCE 1: Pleasant Outdoor Environment")
    print("="*50)
    
    outdoor_environment = {
        "vision": "A beautiful garden with colorful flowers, green trees, and a clear blue sky",
        "hearing": "Gentle birds chirping and soft wind rustling through leaves",
        "touch": "Warm sunlight on skin and a gentle breeze",
        "smell": "Fresh flowers and clean air",
        "taste": "Sweet taste of fresh air"
    }
    
    ai.experience(outdoor_environment)
    
    # Example 2: A busy city street
    print("\n" + "="*50)
    print("EXPERIENCE 2: Busy City Street")
    print("="*50)
    
    city_environment = {
        "vision": "Tall buildings, cars, people walking, traffic lights",
        "hearing": "Loud traffic noise, car horns, and people talking",
        "touch": "Hard concrete sidewalk under feet",
        "smell": "Car exhaust and city air",
        "taste": "Neutral taste of city air"
    }
    
    ai.experience(city_environment)
    
    # Example 3: A kitchen experience
    print("\n" + "="*50)
    print("EXPERIENCE 3: Kitchen Environment")
    print("="*50)
    
    kitchen_environment = {
        "vision": "Clean kitchen with cooking utensils and ingredients",
        "hearing": "Sizzling sounds of cooking and soft music",
        "touch": "Warm stove and smooth countertop",
        "smell": "Delicious food cooking and fresh herbs",
        "taste": "Sweet and savory flavors from cooking"
    }
    
    ai.experience(kitchen_environment)
    
    # Get statistics
    print("\n" + "="*50)
    print("SENSORY STATISTICS")
    print("="*50)
    
    stats = ai.get_sensory_stats()
    for key, value in stats.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    
    # Put AI to sleep
    ai.sleep()

if __name__ == "__main__":
    main() 