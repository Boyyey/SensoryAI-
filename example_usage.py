#!/usr/bin/env python3
"""
Example usage of the SensoryAI system
Demonstrates various environments and scenarios
"""

from sensory_ai import SensoryAI
import time

def demo_basic_usage():
    """Demonstrate basic usage of the SensoryAI system"""
    print("=== Basic Usage Demo ===")
    
    # Create AI instance
    ai = SensoryAI("DemoAI")
    ai.wake_up()
    
    # Simple environment
    simple_env = {
        "vision": "A white wall with a red circle",
        "hearing": "Silence",
        "touch": "Smooth surface",
        "smell": "Clean air",
        "taste": "Neutral taste"
    }
    
    ai.experience(simple_env)
    ai.sleep()

def demo_environment_comparison():
    """Compare different environments"""
    print("\n=== Environment Comparison Demo ===")
    
    ai = SensoryAI("CompareAI")
    ai.wake_up()
    
    # Environment 1: Peaceful nature
    nature_env = {
        "vision": "Green forest with tall trees and blue sky",
        "hearing": "Soft wind and distant bird songs",
        "touch": "Cool breeze and soft grass under feet",
        "smell": "Fresh pine and earth",
        "taste": "Clean, fresh air"
    }
    
    print("\n--- Nature Environment ---")
    ai.experience(nature_env)
    
    # Environment 2: Urban chaos
    urban_env = {
        "vision": "Tall buildings, bright lights, moving cars",
        "hearing": "Loud traffic, horns, people talking",
        "touch": "Hard concrete, warm air",
        "smell": "Exhaust fumes and city smells",
        "taste": "Polluted air taste"
    }
    
    print("\n--- Urban Environment ---")
    ai.experience(urban_env)
    
    # Environment 3: Cozy home
    home_env = {
        "vision": "Warm lighting, comfortable furniture, family photos",
        "hearing": "Soft music, gentle conversation",
        "touch": "Soft cushions, warm temperature",
        "smell": "Home cooking and comfort",
        "taste": "Warm tea taste"
    }
    
    print("\n--- Home Environment ---")
    ai.experience(home_env)
    
    # Show statistics
    print("\n--- Final Statistics ---")
    stats = ai.get_sensory_stats()
    for key, value in stats.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    
    ai.sleep()

def demo_consciousness_levels():
    """Demonstrate different consciousness levels"""
    print("\n=== Consciousness Levels Demo ===")
    
    ai = SensoryAI("ConsciousAI")
    ai.wake_up()
    
    # Same environment with different consciousness levels
    test_env = {
        "vision": "Complex scene with many colors and objects",
        "hearing": "Multiple sounds at different volumes",
        "touch": "Various textures and temperatures",
        "smell": "Mixed pleasant and unpleasant odors",
        "taste": "Complex flavor profile"
    }
    
    # High consciousness
    ai.set_consciousness_level(1.0)
    ai.set_attention_focus("high awareness")
    print("\n--- High Consciousness (1.0) ---")
    ai.experience(test_env)
    
    # Medium consciousness
    ai.set_consciousness_level(0.5)
    ai.set_attention_focus("moderate awareness")
    print("\n--- Medium Consciousness (0.5) ---")
    ai.experience(test_env)
    
    # Low consciousness
    ai.set_consciousness_level(0.2)
    ai.set_attention_focus("low awareness")
    print("\n--- Low Consciousness (0.2) ---")
    ai.experience(test_env)
    
    ai.sleep()

def demo_sensory_focus():
    """Demonstrate focusing on specific senses"""
    print("\n=== Sensory Focus Demo ===")
    
    ai = SensoryAI("FocusAI")
    ai.wake_up()
    
    rich_env = {
        "vision": "Rainbow of colors, geometric shapes, moving objects",
        "hearing": "Symphony of sounds, music, nature, machines",
        "touch": "Smooth silk, rough sandpaper, hot metal, cold ice",
        "smell": "Fresh flowers, burning wood, salty ocean, sweet vanilla",
        "taste": "Sweet chocolate, sour lemon, salty chips, bitter coffee"
    }
    
    # Focus on vision
    ai.set_attention_focus("visual")
    print("\n--- Visual Focus ---")
    ai.experience(rich_env)
    
    # Focus on hearing
    ai.set_attention_focus("auditory")
    print("\n--- Auditory Focus ---")
    ai.experience(rich_env)
    
    # Focus on touch
    ai.set_attention_focus("tactile")
    print("\n--- Tactile Focus ---")
    ai.experience(rich_env)
    
    ai.sleep()

def demo_experience_history():
    """Demonstrate experience history tracking"""
    print("\n=== Experience History Demo ===")
    
    ai = SensoryAI("HistoryAI")
    ai.wake_up()
    
    # Create multiple experiences
    experiences = [
        {
            "vision": "Sunrise over mountains",
            "hearing": "Morning silence",
            "touch": "Cool morning air",
            "smell": "Fresh mountain air",
            "taste": "Clean morning taste"
        },
        {
            "vision": "Busy office environment",
            "hearing": "Typing, talking, phones ringing",
            "touch": "Office chair, keyboard",
            "smell": "Coffee, paper, office air",
            "taste": "Coffee taste"
        },
        {
            "vision": "Sunset at beach",
            "hearing": "Ocean waves, seagulls",
            "touch": "Warm sand, ocean breeze",
            "smell": "Salty ocean air",
            "taste": "Salty air taste"
        }
    ]
    
    # Experience each environment
    for i, env in enumerate(experiences, 1):
        print(f"\n--- Experience {i} ---")
        ai.experience(env)
        time.sleep(1)  # Brief pause between experiences
    
    # Show experience history
    print("\n--- Experience History ---")
    history = ai.get_experience_history()
    for i, exp in enumerate(history, 1):
        print(f"Experience {i}: {exp['timestamp']}")
        print(f"  Environment keys: {list(exp['environment'].keys())}")
    
    ai.sleep()

def demo_custom_scenarios():
    """Demonstrate custom scenarios"""
    print("\n=== Custom Scenarios Demo ===")
    
    ai = SensoryAI("CustomAI")
    ai.wake_up()
    
    # Scenario 1: Cooking in kitchen
    cooking_env = {
        "vision": "Kitchen with ingredients, pots, and cooking utensils",
        "hearing": "Sizzling oil, chopping sounds, bubbling water",
        "touch": "Warm stove, smooth knife handle, hot pan",
        "smell": "Garlic, onions, herbs, cooking oil",
        "taste": "Salty and savory cooking flavors"
    }
    
    print("\n--- Cooking Scenario ---")
    ai.experience(cooking_env)
    
    # Scenario 2: Library study session
    library_env = {
        "vision": "Rows of books, study tables, soft lighting",
        "hearing": "Pages turning, quiet whispers, pencil writing",
        "touch": "Smooth book covers, wooden table, paper",
        "smell": "Old books, paper, quiet air",
        "taste": "Neutral, focused taste"
    }
    
    print("\n--- Library Scenario ---")
    ai.experience(library_env)
    
    # Scenario 3: Concert experience
    concert_env = {
        "vision": "Bright stage lights, crowd, musicians",
        "hearing": "Loud music, cheering, instruments",
        "touch": "Vibrating bass, warm crowd, excitement",
        "smell": "Crowd, excitement, venue air",
        "taste": "Excitement in the air"
    }
    
    print("\n--- Concert Scenario ---")
    ai.experience(concert_env)
    
    ai.sleep()

def main():
    """Run all demonstrations"""
    print("SensoryAI System - Example Demonstrations")
    print("=" * 50)
    
    try:
        # Run all demos
        demo_basic_usage()
        demo_environment_comparison()
        demo_consciousness_levels()
        demo_sensory_focus()
        demo_experience_history()
        demo_custom_scenarios()
        
        print("\n" + "=" * 50)
        print("All demonstrations completed successfully!")
        print("The SensoryAI system is ready for your own experiments!")
        
    except Exception as e:
        print(f"Error during demonstration: {e}")

if __name__ == "__main__":
    main() 