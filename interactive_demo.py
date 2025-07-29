#!/usr/bin/env python3
"""
Interactive demo for the SensoryAI system
Allows users to create custom sensory experiences
"""

from sensory_ai import SensoryAI
import json

def print_banner():
    """Print the demo banner"""
    print("=" * 60)
    print("🎭 SensoryAI Interactive Demo 🎭")
    print("Experience the world through AI senses!")
    print("=" * 60)

def print_menu():
    """Print the main menu"""
    print("\n📋 Available Options:")
    print("1. 🏠 Create a custom environment")
    print("2. 🎯 Use preset environments")
    print("3. 🧠 Adjust AI consciousness")
    print("4. 👁️ Set attention focus")
    print("5. 📊 View sensory statistics")
    print("6. 📚 View experience history")
    print("7. 🧪 Run quick experiments")
    print("8. 💤 Put AI to sleep")
    print("9. 🔄 Wake AI up")
    print("0. 🚪 Exit")
    print("-" * 40)

def get_user_input(prompt, default=""):
    """Get user input with optional default value"""
    if default:
        user_input = input(f"{prompt} (default: {default}): ").strip()
        return user_input if user_input else default
    else:
        return input(f"{prompt}: ").strip()

def create_custom_environment():
    """Create a custom environment with user input"""
    print("\n🎨 Creating Custom Environment")
    print("Describe what the AI should experience through each sense:")
    
    environment = {}
    
    # Get descriptions for each sense
    senses = {
        "vision": "What do you see? (colors, objects, shapes, etc.)",
        "hearing": "What do you hear? (sounds, music, voices, etc.)",
        "touch": "What do you feel? (textures, temperatures, pressure, etc.)",
        "smell": "What do you smell? (odors, scents, aromas, etc.)",
        "taste": "What do you taste? (flavors, tastes, etc.)"
    }
    
    for sense, prompt in senses.items():
        description = get_user_input(prompt)
        if description:
            environment[sense] = description
    
    return environment

def preset_environments():
    """Show preset environments"""
    presets = {
        "1": {
            "name": "🌅 Peaceful Sunrise",
            "environment": {
                "vision": "Golden sunrise over calm ocean, pink clouds, seagulls flying",
                "hearing": "Gentle ocean waves, distant seagull calls, soft wind",
                "touch": "Warm morning sun, cool ocean breeze, soft sand",
                "smell": "Fresh ocean air, salty breeze, morning dew",
                "taste": "Clean, fresh morning air"
            }
        },
        "2": {
            "name": "🏙️ Busy City Street",
            "environment": {
                "vision": "Tall skyscrapers, bright neon lights, busy traffic, people walking",
                "hearing": "Loud traffic, car horns, people talking, sirens",
                "touch": "Hard concrete sidewalk, warm city air, vibration from traffic",
                "smell": "Car exhaust, street food, city air",
                "taste": "Polluted air, street food aromas"
            }
        },
        "3": {
            "name": "🌲 Forest Adventure",
            "environment": {
                "vision": "Tall green trees, dappled sunlight, moss-covered rocks, wildlife",
                "hearing": "Rustling leaves, bird songs, flowing stream, animal sounds",
                "touch": "Rough tree bark, soft moss, cool shade, fresh air",
                "smell": "Pine trees, earth, fresh air, wildflowers",
                "taste": "Clean forest air, natural freshness"
            }
        },
        "4": {
            "name": "🏠 Cozy Home",
            "environment": {
                "vision": "Warm lighting, comfortable furniture, family photos, fireplace",
                "hearing": "Soft music, gentle conversation, crackling fire, quiet comfort",
                "touch": "Soft cushions, warm temperature, comfortable fabrics",
                "smell": "Home cooking, comfort, warmth, family",
                "taste": "Warm tea, home-cooked meal, comfort"
            }
        },
        "5": {
            "name": "🎵 Concert Hall",
            "environment": {
                "vision": "Bright stage lights, musicians, audience, elegant hall",
                "hearing": "Beautiful music, applause, instruments, acoustics",
                "touch": "Vibrating bass, warm crowd, excitement, elegant seating",
                "smell": "Perfume, excitement, venue air, anticipation",
                "taste": "Excitement, anticipation, elegant atmosphere"
            }
        }
    }
    
    print("\n🎭 Available Preset Environments:")
    for key, preset in presets.items():
        print(f"{key}. {preset['name']}")
    
    choice = get_user_input("\nSelect a preset (1-5) or '0' to cancel")
    
    if choice in presets:
        return presets[choice]["environment"], presets[choice]["name"]
    else:
        return None, None

def adjust_consciousness(ai):
    """Adjust AI consciousness level"""
    print("\n🧠 Adjusting AI Consciousness")
    print("Consciousness level affects how aware the AI is of its surroundings.")
    print("0.0 = Unconscious, 0.5 = Half-aware, 1.0 = Fully conscious")
    
    current_level = ai.brain.consciousness_level
    print(f"Current consciousness level: {current_level}")
    
    new_level = get_user_input("Enter new consciousness level (0.0-1.0)", str(current_level))
    
    try:
        level = float(new_level)
        if 0.0 <= level <= 1.0:
            ai.set_consciousness_level(level)
            print(f"✅ Consciousness level set to {level}")
        else:
            print("❌ Please enter a value between 0.0 and 1.0")
    except ValueError:
        print("❌ Please enter a valid number")

def set_attention_focus(ai):
    """Set AI attention focus"""
    print("\n👁️ Setting Attention Focus")
    print("Attention focus determines which senses the AI prioritizes.")
    
    current_focus = ai.brain.attention_focus
    print(f"Current attention focus: {current_focus}")
    
    print("\nAvailable focus options:")
    print("- general (all senses equal)")
    print("- visual (prioritize sight)")
    print("- auditory (prioritize hearing)")
    print("- tactile (prioritize touch)")
    print("- olfactory (prioritize smell)")
    print("- gustatory (prioritize taste)")
    print("- custom (enter your own)")
    
    focus = get_user_input("Enter attention focus", current_focus)
    ai.set_attention_focus(focus)
    print(f"✅ Attention focus set to '{focus}'")

def view_statistics(ai):
    """View sensory statistics"""
    print("\n📊 Sensory Statistics")
    print("-" * 30)
    
    stats = ai.get_sensory_stats()
    for key, value in stats.items():
        formatted_key = key.replace('_', ' ').title()
        print(f"{formatted_key}: {value}")

def view_history(ai):
    """View experience history"""
    print("\n📚 Experience History")
    print("-" * 30)
    
    history = ai.get_experience_history()
    
    if not history:
        print("No experiences recorded yet.")
        return
    
    for i, experience in enumerate(history, 1):
        print(f"\nExperience {i}:")
        print(f"  Timestamp: {experience['timestamp']}")
        print(f"  Environment: {list(experience['environment'].keys())}")
        
        # Show brief summary
        integrated = experience['experience']['integrated_experience']
        print(f"  Quality: {integrated['experience_quality']}")
        print(f"  Dominant Sense: {integrated['dominant_sense']}")
        print(f"  Overall Intensity: {integrated['overall_intensity']:.2f}")

def quick_experiments(ai):
    """Run quick experiments"""
    print("\n🧪 Quick Experiments")
    print("These experiments test different aspects of the AI's sensory processing.")
    
    experiments = {
        "1": {
            "name": "Intensity Test",
            "description": "Test how the AI responds to high-intensity stimuli",
            "environment": {
                "vision": "Bright flashing lights, rapid movement, intense colors",
                "hearing": "Loud explosions, screaming, thunder",
                "touch": "Intense pressure, extreme heat, sharp pain",
                "smell": "Strong chemicals, burning, intense odors",
                "taste": "Extremely bitter, extremely sour, intense flavors"
            }
        },
        "2": {
            "name": "Pleasant vs Unpleasant",
            "description": "Compare pleasant and unpleasant sensory inputs",
            "environment": {
                "vision": "Beautiful flowers and garbage dump",
                "hearing": "Beautiful music and loud noise",
                "touch": "Soft silk and rough sandpaper",
                "smell": "Fresh flowers and rotten food",
                "taste": "Sweet chocolate and bitter medicine"
            }
        },
        "3": {
            "name": "Single Sense Focus",
            "description": "Test with only one sense active",
            "environment": {
                "vision": "Complex visual scene with many colors and objects",
                "hearing": "",
                "touch": "",
                "smell": "",
                "taste": ""
            }
        }
    }
    
    print("\nAvailable experiments:")
    for key, exp in experiments.items():
        print(f"{key}. {exp['name']}: {exp['description']}")
    
    choice = get_user_input("\nSelect an experiment (1-3) or '0' to cancel")
    
    if choice in experiments:
        experiment = experiments[choice]
        print(f"\n🧪 Running: {experiment['name']}")
        print(f"Description: {experiment['description']}")
        
        # Filter out empty senses
        env = {k: v for k, v in experiment['environment'].items() if v}
        
        ai.experience(env)
    else:
        print("❌ Invalid choice")

def main():
    """Main interactive demo loop"""
    print_banner()
    
    # Create AI instance
    ai_name = get_user_input("Enter a name for your AI", "Alex")
    ai = SensoryAI(ai_name)
    ai.wake_up()
    
    print(f"\n🤖 {ai_name} is ready to experience the world!")
    
    while True:
        print_menu()
        choice = get_user_input("Enter your choice (0-9)")
        
        if choice == "0":
            print(f"\n👋 Goodbye! {ai_name} is going to sleep...")
            ai.sleep()
            break
        
        elif choice == "1":
            environment = create_custom_environment()
            if environment:
                print(f"\n🎭 {ai_name} is experiencing your custom environment...")
                ai.experience(environment)
            else:
                print("❌ No environment created")
        
        elif choice == "2":
            environment, name = preset_environments()
            if environment:
                print(f"\n🎭 {ai_name} is experiencing: {name}")
                ai.experience(environment)
        
        elif choice == "3":
            adjust_consciousness(ai)
        
        elif choice == "4":
            set_attention_focus(ai)
        
        elif choice == "5":
            view_statistics(ai)
        
        elif choice == "6":
            view_history(ai)
        
        elif choice == "7":
            quick_experiments(ai)
        
        elif choice == "8":
            ai.sleep()
        
        elif choice == "9":
            ai.wake_up()
        
        else:
            print("❌ Invalid choice. Please enter a number between 0-9.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Demo interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please restart the demo.") 