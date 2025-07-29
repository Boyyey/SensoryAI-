import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import json
from sensory_ai import SensoryAI

# Page configuration
st.set_page_config(
    page_title="SensoryAI - Five Senses Experience",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #ff7f0e;
        margin-bottom: 1rem;
    }
    .sensory-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .experience-output {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .metric-card {
        background-color: #f9f9f9;
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
        border: 1px solid #ddd;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'ai' not in st.session_state:
    st.session_state.ai = SensoryAI("StreamlitAI")
    st.session_state.ai.wake_up()
    st.session_state.experience_history = []

def create_sensory_input_form():
    """Create form for sensory input"""
    st.markdown("### 🎭 Create Your Environment")
    
    col1, col2 = st.columns(2)
    
    with col1:
        vision = st.text_area("👁️ What do you see?", 
                             placeholder="Describe the visual scene (colors, objects, shapes, etc.)",
                             height=100)
        
        hearing = st.text_area("👂 What do you hear?", 
                              placeholder="Describe the sounds (music, voices, nature, etc.)",
                              height=100)
        
        touch = st.text_area("🖐️ What do you feel?", 
                            placeholder="Describe tactile sensations (textures, temperatures, pressure, etc.)",
                            height=100)
    
    with col2:
        smell = st.text_area("👃 What do you smell?", 
                            placeholder="Describe the scents and odors",
                            height=100)
        
        taste = st.text_area("👅 What do you taste?", 
                            placeholder="Describe the flavors and tastes",
                            height=100)
    
    return {
        "vision": vision,
        "hearing": hearing,
        "touch": touch,
        "smell": smell,
        "taste": taste
    }

def display_experience_result(result):
    """Display the sensory experience result"""
    if not result:
        return
    
    integrated = result['integrated_experience']
    individual = result['individual_senses']
    
    st.markdown("### 🧠 Sensory Experience Analysis")
    
    # Main metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Consciousness Level", f"{integrated['consciousness_level']:.2f}")
    
    with col2:
        st.metric("Overall Intensity", f"{integrated['overall_intensity']:.2f}")
    
    with col3:
        st.metric("Dominant Sense", integrated['dominant_sense'].title())
    
    with col4:
        st.metric("Experience Quality", integrated['experience_quality'].title())
    
    # Individual sensory inputs
    st.markdown("#### Individual Sensory Inputs")
    
    sensory_data = []
    for sense, input_data in individual.items():
        sensory_data.append({
            'Sense': sense.title(),
            'Quality': input_data.quality,
            'Intensity': input_data.intensity,
            'Location': input_data.location
        })
    
    df = pd.DataFrame(sensory_data)
    
    # Create a bar chart for intensity
    fig_intensity = px.bar(df, x='Sense', y='Intensity', 
                          title="Sensory Intensity Levels",
                          color='Intensity',
                          color_continuous_scale='viridis')
    fig_intensity.update_layout(height=400)
    st.plotly_chart(fig_intensity, use_container_width=True)
    
    # Display sensory details
    for sense, input_data in individual.items():
        with st.expander(f"{sense.title()} - {input_data.quality}"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Intensity", f"{input_data.intensity:.2f}")
            with col2:
                st.metric("Quality", input_data.quality)
            with col3:
                st.metric("Location", input_data.location)

def display_preset_environments():
    """Display preset environment options"""
    presets = {
        "Peaceful Sunrise": {
            "vision": "Golden sunrise over calm ocean, pink clouds, seagulls flying",
            "hearing": "Gentle ocean waves, distant seagull calls, soft wind",
            "touch": "Warm morning sun, cool ocean breeze, soft sand",
            "smell": "Fresh ocean air, salty breeze, morning dew",
            "taste": "Clean, fresh morning air"
        },
        "Busy City Street": {
            "vision": "Tall skyscrapers, bright neon lights, busy traffic, people walking",
            "hearing": "Loud traffic, car horns, people talking, sirens",
            "touch": "Hard concrete sidewalk, warm city air, vibration from traffic",
            "smell": "Car exhaust, street food, city air",
            "taste": "Polluted air, street food aromas"
        },
        "Forest Adventure": {
            "vision": "Tall green trees, dappled sunlight, moss-covered rocks, wildlife",
            "hearing": "Rustling leaves, bird songs, flowing stream, animal sounds",
            "touch": "Rough tree bark, soft moss, cool shade, fresh air",
            "smell": "Pine trees, earth, fresh air, wildflowers",
            "taste": "Clean forest air, natural freshness"
        },
        "Cozy Home": {
            "vision": "Warm lighting, comfortable furniture, family photos, fireplace",
            "hearing": "Soft music, gentle conversation, crackling fire, quiet comfort",
            "touch": "Soft cushions, warm temperature, comfortable fabrics",
            "smell": "Home cooking, comfort, warmth, family",
            "taste": "Warm tea, home-cooked meal, comfort"
        },
        "Concert Hall": {
            "vision": "Bright stage lights, musicians, audience, elegant hall",
            "hearing": "Beautiful music, applause, instruments, acoustics",
            "touch": "Vibrating bass, warm crowd, excitement, elegant seating",
            "smell": "Perfume, excitement, venue air, anticipation",
            "taste": "Excitement, anticipation, elegant atmosphere"
        }
    }
    
    st.markdown("### 🎯 Preset Environments")
    
    selected_preset = st.selectbox(
        "Choose a preset environment:",
        list(presets.keys())
    )
    
    if selected_preset:
        preset_data = presets[selected_preset]
        
        # Display the preset description
        st.markdown(f"**{selected_preset}**")
        for sense, description in preset_data.items():
            st.markdown(f"**{sense.title()}**: {description}")
        
        if st.button(f"Experience {selected_preset}"):
            return preset_data
    
    return None

def display_ai_controls():
    """Display AI control options"""
    st.markdown("### 🧠 AI Controls")
    
    col1, col2 = st.columns(2)
    
    with col1:
        consciousness = st.slider(
            "Consciousness Level",
            min_value=0.0,
            max_value=1.0,
            value=st.session_state.ai.brain.consciousness_level,
            step=0.1,
            help="How aware the AI is of its surroundings"
        )
        
        if st.button("Set Consciousness Level"):
            st.session_state.ai.set_consciousness_level(consciousness)
            st.success(f"Consciousness level set to {consciousness}")
    
    with col2:
        attention_focus = st.selectbox(
            "Attention Focus",
            ["general", "visual", "auditory", "tactile", "olfactory", "gustatory"],
            index=0 if st.session_state.ai.brain.attention_focus == "general" else 
                  ["visual", "auditory", "tactile", "olfactory", "gustatory"].index(st.session_state.ai.brain.attention_focus) + 1
        )
        
        if st.button("Set Attention Focus"):
            st.session_state.ai.set_attention_focus(attention_focus)
            st.success(f"Attention focus set to {attention_focus}")
    
    # AI Status
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Wake Up AI"):
            st.session_state.ai.wake_up()
            st.success("AI is now awake!")
    
    with col2:
        if st.button("Put AI to Sleep"):
            st.session_state.ai.sleep()
            st.success("AI is now sleeping!")

def display_statistics():
    """Display AI statistics"""
    st.markdown("### 📊 AI Statistics")
    
    stats = st.session_state.ai.get_sensory_stats()
    
    # Create metrics display
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Visual Experiences", stats['total_visual_experiences'])
    
    with col2:
        st.metric("Auditory Experiences", stats['total_auditory_experiences'])
    
    with col3:
        st.metric("Tactile Experiences", stats['total_tactile_experiences'])
    
    with col4:
        st.metric("Total Experiences", stats['total_integrated_experiences'])
    
    # Create a pie chart of experiences
    experience_data = {
        'Vision': stats['total_visual_experiences'],
        'Hearing': stats['total_auditory_experiences'],
        'Touch': stats['total_tactile_experiences'],
        'Smell': stats['total_olfactory_experiences'],
        'Taste': stats['total_gustatory_experiences']
    }
    
    fig_pie = px.pie(
        values=list(experience_data.values()),
        names=list(experience_data.keys()),
        title="Sensory Experience Distribution"
    )
    st.plotly_chart(fig_pie, use_container_width=True)

def display_experience_history():
    """Display experience history"""
    st.markdown("### 📚 Experience History")
    
    history = st.session_state.ai.get_experience_history()
    
    if not history:
        st.info("No experiences recorded yet. Create your first experience!")
        return
    
    # Create a timeline of experiences
    timeline_data = []
    for i, exp in enumerate(history):
        integrated = exp['experience']['integrated_experience']
        timeline_data.append({
            'Experience': f"Experience {i+1}",
            'Timestamp': exp['timestamp'],
            'Quality': integrated['experience_quality'],
            'Intensity': integrated['overall_intensity'],
            'Dominant Sense': integrated['dominant_sense']
        })
    
    df_timeline = pd.DataFrame(timeline_data)
    
    # Display timeline
    for _, row in df_timeline.iterrows():
        with st.expander(f"{row['Experience']} - {row['Quality'].title()}"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Quality", row['Quality'].title())
            with col2:
                st.metric("Intensity", f"{row['Intensity']:.2f}")
            with col3:
                st.metric("Dominant Sense", row['Dominant Sense'].title())
            st.caption(f"Timestamp: {row['Timestamp']}")

def main():
    """Main Streamlit app"""
    
    # Header
    st.markdown('<h1 class="main-header">🧠 SensoryAI - Five Senses Experience</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem;">Experience the world through AI senses with our interactive web interface!</p>', unsafe_allow_html=True)
    
    # Sidebar
    st.sidebar.markdown("## 🎛️ Navigation")
    page = st.sidebar.selectbox(
        "Choose a page:",
        ["🏠 Create Experience", "🎯 Preset Environments", "🧠 AI Controls", "📊 Statistics", "📚 History"]
    )
    
    # AI Status in sidebar
    st.sidebar.markdown("## 🤖 AI Status")
    status = "🟢 Awake" if st.session_state.ai.is_awake else "🔴 Sleeping"
    st.sidebar.markdown(f"**Status**: {status}")
    st.sidebar.markdown(f"**Consciousness**: {st.session_state.ai.brain.consciousness_level:.2f}")
    st.sidebar.markdown(f"**Attention**: {st.session_state.ai.brain.attention_focus}")
    
    # Page routing
    if page == "🏠 Create Experience":
        st.markdown("## 🏠 Create Custom Experience")
        
        # Get sensory input
        environment = create_sensory_input_form()
        
        # Experience button
        if st.button("🎭 Experience Environment", type="primary"):
            # Filter out empty inputs
            filtered_env = {k: v for k, v in environment.items() if v.strip()}
            
            if filtered_env:
                with st.spinner("Processing sensory experience..."):
                    result = st.session_state.ai.experience(filtered_env)
                    st.session_state.experience_history.append(result)
                
                display_experience_result(result)
            else:
                st.warning("Please provide at least one sensory input!")
    
    elif page == "🎯 Preset Environments":
        st.markdown("## 🎯 Preset Environments")
        
        preset_result = display_preset_environments()
        if preset_result:
            with st.spinner("Processing preset environment..."):
                result = st.session_state.ai.experience(preset_result)
                st.session_state.experience_history.append(result)
            
            display_experience_result(result)
    
    elif page == "🧠 AI Controls":
        st.markdown("## 🧠 AI Controls")
        display_ai_controls()
    
    elif page == "📊 Statistics":
        st.markdown("## 📊 Statistics")
        display_statistics()
    
    elif page == "📚 History":
        st.markdown("## 📚 Experience History")
        display_experience_history()
    
    # Footer
    st.markdown("---")
    st.markdown(
        '<p style="text-align: center; color: #666;">🧠 SensoryAI - Experience the world through AI senses | '
        'Built with Streamlit and Python</p>',
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main() 