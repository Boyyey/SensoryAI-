#!/usr/bin/env python3
"""
Test suite for the SensoryAI system
Verifies all core functionality
"""

import unittest
from sensory_ai import SensoryAI, SensoryInput, Vision, Hearing, Touch, Smell, Taste

class TestSensoryAI(unittest.TestCase):
    """Test cases for the SensoryAI system"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.ai = SensoryAI("TestAI")
    
    def test_ai_creation(self):
        """Test AI creation and basic properties"""
        self.assertEqual(self.ai.name, "TestAI")
        self.assertTrue(self.ai.is_awake)
        self.assertEqual(len(self.ai.experience_log), 0)
    
    def test_wake_sleep(self):
        """Test wake up and sleep functionality"""
        self.ai.sleep()
        self.assertFalse(self.ai.is_awake)
        
        self.ai.wake_up()
        self.assertTrue(self.ai.is_awake)
    
    def test_vision_system(self):
        """Test vision system functionality"""
        vision = Vision()
        
        # Test color perception
        self.assertIn('red', vision.color_perception)
        self.assertEqual(vision.color_perception['red'], (255, 0, 0))
        
        # Test shape recognition
        self.assertIn('circle', vision.shapes)
        self.assertIn('square', vision.shapes)
        
        # Test object recognition
        self.assertIn('person', vision.objects)
        self.assertIn('car', vision.objects)
        
        # Test visual processing
        visual_input = vision.see("A red car and blue sky")
        self.assertEqual(visual_input.sense_type, "vision")
        self.assertGreater(visual_input.intensity, 0)
        self.assertIsInstance(visual_input.quality, str)
    
    def test_hearing_system(self):
        """Test hearing system functionality"""
        hearing = Hearing()
        
        # Test sound classification
        self.assertIn('loud', hearing.sounds)
        self.assertIn('moderate', hearing.sounds)
        self.assertIn('quiet', hearing.sounds)
        
        # Test frequency classification
        self.assertIn('low', hearing.frequencies)
        self.assertIn('medium', hearing.frequencies)
        self.assertIn('high', hearing.frequencies)
        
        # Test auditory processing
        auditory_input = hearing.hear("Loud thunder and music")
        self.assertEqual(auditory_input.sense_type, "hearing")
        self.assertGreater(auditory_input.intensity, 0)
        self.assertIsInstance(auditory_input.quality, str)
    
    def test_touch_system(self):
        """Test touch system functionality"""
        touch = Touch()
        
        # Test texture classification
        self.assertIn('smooth', touch.textures)
        self.assertIn('rough', touch.textures)
        self.assertIn('soft', touch.textures)
        self.assertIn('hard', touch.textures)
        
        # Test temperature classification
        self.assertIn('hot', touch.temperatures)
        self.assertIn('warm', touch.temperatures)
        self.assertIn('cool', touch.temperatures)
        self.assertIn('cold', touch.temperatures)
        
        # Test tactile processing
        tactile_input = touch.feel("Smooth glass and hot metal")
        self.assertEqual(tactile_input.sense_type, "touch")
        self.assertGreater(tactile_input.intensity, 0)
        self.assertIsInstance(tactile_input.quality, str)
    
    def test_smell_system(self):
        """Test smell system functionality"""
        smell = Smell()
        
        # Test scent classification
        self.assertIn('pleasant', smell.scents)
        self.assertIn('unpleasant', smell.scents)
        self.assertIn('neutral', smell.scents)
        self.assertIn('strong', smell.scents)
        
        # Test olfactory processing
        olfactory_input = smell.smell("Fresh flowers and coffee")
        self.assertEqual(olfactory_input.sense_type, "smell")
        self.assertGreater(olfactory_input.intensity, 0)
        self.assertIsInstance(olfactory_input.quality, str)
    
    def test_taste_system(self):
        """Test taste system functionality"""
        taste = Taste()
        
        # Test taste classification
        self.assertIn('sweet', taste.tastes)
        self.assertIn('sour', taste.tastes)
        self.assertIn('salty', taste.tastes)
        self.assertIn('bitter', taste.tastes)
        self.assertIn('umami', taste.tastes)
        
        # Test gustatory processing
        gustatory_input = taste.taste("Sweet chocolate and salty chips")
        self.assertEqual(gustatory_input.sense_type, "taste")
        self.assertGreater(gustatory_input.intensity, 0)
        self.assertIsInstance(gustatory_input.quality, str)
    
    def test_sensory_integration(self):
        """Test sensory integration functionality"""
        self.ai.wake_up()
        
        # Create a test environment
        test_env = {
            "vision": "Red car and blue sky",
            "hearing": "Loud music and conversation",
            "touch": "Smooth glass and hot metal",
            "smell": "Fresh flowers and coffee",
            "taste": "Sweet chocolate and salty chips"
        }
        
        # Experience the environment
        result = self.ai.experience(test_env)
        
        # Verify result structure
        self.assertIn('individual_senses', result)
        self.assertIn('integrated_experience', result)
        
        # Verify individual senses
        individual_senses = result['individual_senses']
        self.assertIn('vision', individual_senses)
        self.assertIn('hearing', individual_senses)
        self.assertIn('touch', individual_senses)
        self.assertIn('smell', individual_senses)
        self.assertIn('taste', individual_senses)
        
        # Verify integrated experience
        integrated = result['integrated_experience']
        self.assertIn('timestamp', integrated)
        self.assertIn('consciousness_level', integrated)
        self.assertIn('attention_focus', integrated)
        self.assertIn('overall_intensity', integrated)
        self.assertIn('dominant_sense', integrated)
        self.assertIn('experience_quality', integrated)
    
    def test_consciousness_levels(self):
        """Test consciousness level setting"""
        self.ai.set_consciousness_level(0.5)
        self.assertEqual(self.ai.brain.consciousness_level, 0.5)
        
        # Test bounds
        self.ai.set_consciousness_level(1.5)  # Should be clamped to 1.0
        self.assertEqual(self.ai.brain.consciousness_level, 1.0)
        
        self.ai.set_consciousness_level(-0.5)  # Should be clamped to 0.0
        self.assertEqual(self.ai.brain.consciousness_level, 0.0)
    
    def test_attention_focus(self):
        """Test attention focus setting"""
        self.ai.set_attention_focus("visual")
        self.assertEqual(self.ai.brain.attention_focus, "visual")
        
        self.ai.set_attention_focus("auditory")
        self.assertEqual(self.ai.brain.attention_focus, "auditory")
    
    def test_experience_history(self):
        """Test experience history tracking"""
        self.ai.wake_up()
        
        # Create multiple experiences
        env1 = {"vision": "Test scene 1", "hearing": "Test sound 1", 
                "touch": "Test touch 1", "smell": "Test smell 1", "taste": "Test taste 1"}
        env2 = {"vision": "Test scene 2", "hearing": "Test sound 2", 
                "touch": "Test touch 2", "smell": "Test smell 2", "taste": "Test taste 2"}
        
        self.ai.experience(env1)
        self.ai.experience(env2)
        
        # Verify history
        history = self.ai.get_experience_history()
        self.assertEqual(len(history), 2)
        self.assertIn('timestamp', history[0])
        self.assertIn('environment', history[0])
        self.assertIn('experience', history[0])
    
    def test_sensory_stats(self):
        """Test sensory statistics"""
        self.ai.wake_up()
        
        # Create an experience
        test_env = {
            "vision": "Test scene",
            "hearing": "Test sound",
            "touch": "Test touch",
            "smell": "Test smell",
            "taste": "Test taste"
        }
        
        self.ai.experience(test_env)
        
        # Get statistics
        stats = self.ai.get_sensory_stats()
        
        # Verify statistics structure
        expected_keys = [
            'total_visual_experiences',
            'total_auditory_experiences',
            'total_tactile_experiences',
            'total_olfactory_experiences',
            'total_gustatory_experiences',
            'total_integrated_experiences',
            'consciousness_level',
            'attention_focus'
        ]
        
        for key in expected_keys:
            self.assertIn(key, stats)
    
    def test_sensory_input_structure(self):
        """Test SensoryInput data structure"""
        input_data = SensoryInput(
            sense_type="test",
            intensity=0.5,
            quality="test quality",
            location="test location"
        )
        
        self.assertEqual(input_data.sense_type, "test")
        self.assertEqual(input_data.intensity, 0.5)
        self.assertEqual(input_data.quality, "test quality")
        self.assertEqual(input_data.location, "test location")
        self.assertIsNotNone(input_data.timestamp)

def run_tests():
    """Run all tests"""
    print("Running SensoryAI Test Suite...")
    print("=" * 50)
    
    # Create test suite
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestSensoryAI)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Print summary
    print("\n" + "=" * 50)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print("\nFailures:")
        for test, traceback in result.failures:
            print(f"  {test}: {traceback}")
    
    if result.errors:
        print("\nErrors:")
        for test, traceback in result.errors:
            print(f"  {test}: {traceback}")
    
    if result.wasSuccessful():
        print("\n✅ All tests passed!")
    else:
        print("\n❌ Some tests failed!")
    
    return result.wasSuccessful()

if __name__ == "__main__":
    run_tests() 