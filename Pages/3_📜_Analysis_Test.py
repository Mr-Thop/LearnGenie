import streamlit as st


def cognitive(Cognitive):
    st.header("Cognitive")
    if Cognitive == "High":
        st.write("- **Optimal Study Times**: Schedule your study sessions during times when you feel most alert and focused, such as early morning or evening.")
        st.write("- **Minimize Distractions**: Create a distraction-free study environment. Use tools like website blockers or noise-canceling headphones.")
        st.write("- **Short Breaks**: Incorporate short breaks (5-10 minutes) to maintain high levels of focus. Try techniques like the Pomodoro method (25 minutes study, 5 minutes break).")
    else:
        st.write("- **Identify Peak Times**: Experiment with different study times to identify when you are most alert.")
        st.write("- **Breaks and Movement**: Take regular breaks and include some physical activity to refresh your mind.")
        st.write("- **Active Study Techniques**: Use active study methods such as summarizing information, teaching others, or using flashcards to keep engaged.")

def ability(Cognitive):
    st.header("Ability")
    if Cognitive == "High":
        st.write("- **Advanced Material**: Challenge yourself with more complex materials or advanced topics to keep your interest and enhance your skills.")
        st.write("- **Teach Others**: Reinforce your learning by explaining concepts to peers or teaching others.")
        st.write("- **Frequent Self-Assessment**: Regularly test yourself to gauge your understanding and retention.")
    elif Cognitive == "Moderate":
        st.write("- **Consistent Revision**: Schedule regular revision sessions to reinforce learning.")
        st.write("- **Variety of Resources**: Use multiple resources (videos, books, practice problems) to understand concepts better.")
        st.write("- **Active Learning**: Engage in activities like group discussions, hands-on experiments, and interactive quizzes.")
    else:
        st.write("- **Structured Revision**: Create a structured revision timetable and stick to it.")
        st.write("- **Use Mnemonics**: Employ mnemonic devices to remember information better.")
        st.write("- **Break Down Information**: Break down complex information into smaller, manageable chunks.")
    
def style(Style):
    st.header("Style")
    if Style == "Visual":
        st.write("- **Visual Aids**: Use charts, diagrams, and color-coded notes to organize information.")
        st.write("- **Mind Maps**: Create mind maps to visualize connections between concepts.")
        st.write("- **Video Content**: Watch videos and animations related to your study topics.")
    elif Style == "Audio":
        st.write("- **Listen to Lectures**: Record lectures or discussions to listen to them later.")
        st.write("- **Discussion Groups**: Join study groups to discuss and hear different perspectives on the material.")
        st.write("- **Audio Notes**: Record yourself reading notes and listen to them during revision.")
    elif Style == "Kinesthetic":
        st.write("- **Hands-On Activities**: Engage in lab experiments, model building, or other hands-on activities.")
        st.write("- **Physical Movement**: Incorporate movement into your study sessions, such as studying while standing or walking.")
        st.write("- **Role-Playing**: Use role-playing techniques to simulate real-world applications of the material.")
    else:
        st.write("- **Detailed Notes**: Take detailed, written notes during lectures and readings.")
        st.write("- **Summarize**: Write summaries of each topic in your own words.")
        st.write("- **Practice Writing**: Practice writing essays or answers to potential exam questions.")
def intensity(Intensity):
    st.header("Intensity")
    if Intensity == "High":
        st.write("- **Avoid Burnout**: Ensure you are not overworking by scheduling regular, meaningful breaks.")
        st.write("- **Balanced Schedule**: Mix intense study sessions with lighter review periods to balance workload.")
        st.write("- **Relaxation Techniques**: Incorporate relaxation techniques such as meditation or deep breathing exercises.")
    elif Intensity == "Balanced":
        st.write("- **Maintain Routine**: Stick to a consistent study routine with balanced study and break periods.")
        st.write("- **Flexibility**: Allow some flexibility in your schedule to adapt to unexpected changes without stress.")
        st.write("- **Regular Review**: Regularly review material to reinforce learning without cramming.")
    else:
        st.write("- **Increase Engagement**: Increase study intensity by setting specific goals and deadlines.")
        st.write("- **Active Study Sessions**: Make study sessions more active and engaging to maintain interest.")
        st.write("- **Scheduled Study Time**: Designate specific times for study to ensure consistent learning without interruptions.")
def evaluate_answers(answers):
    cognitive_score = 0
    learning_ability_score = 0
    learning_style_score = 0
    learning_intensity_score = 0

    # Scoring for Cognitive Level
    cognitive_answers = answers[:7]
    cognitive_score = cognitive_answers.count('a') + cognitive_answers.count('d')

    # Scoring for Learning Ability
    learning_ability_answers = answers[7:13]
    learning_ability_score = learning_ability_answers.count('c') + learning_ability_answers.count('d')

    # Scoring for Learning Style
    learning_style_answers = answers[13:20]
    learning_style_score = max([learning_style_answers.count(option) for option in ['a', 'b', 'c', 'd']])

    # Scoring for Learning Intensity
    learning_intensity_answers = answers[20:]
    learning_intensity_score = max([learning_intensity_answers.count(option) for option in ['a', 'b', 'c', 'd']])

    return cognitive_score, learning_ability_score, learning_style_score, learning_intensity_score

if st.session_state["Login"] == "":
    st.error("Please Login to Continue")
else:
    name = st.session_state['Name']
    st.title('LearnGenie Student Analysis Questionnaire')
    st.write(f"Hello *{name}* Please answer the following questions to help us Understand you Better")

    questions = [
        "When do you feel most alert and ready to study?",
        "How long can you stay focused during a study session before needing a break?",
        "How often do you find yourself getting distracted while studying?",
        "What do you do when you notice your mind wandering during a study session?",
        "How well do you remember information after studying it for the first time?",
        "How often do you need to revise material to remember it?",
        "Do you find it easier to focus when studying alone or in a group?",
        "How do you typically handle new information when studying?",
        "How frequently do you take breaks during a typical study session?",
        "How do you feel after taking a short break (5-10 minutes) while studying?",
        "When learning something new, do you prefer to understand the big picture first or the details?",
        "How do you handle complex subjects that require deeper understanding?",
        "When studying, how often do you quiz yourself on the material?",
        "Which method helps you learn most effectively?",
        "When faced with a complex problem, how do you prefer to tackle it?",
        "How do you best remember information?",
        "What type of environment do you prefer for studying?",
        "How do you organize your study materials?",
        "When preparing for an exam, which technique do you find most helpful?",
        "Do you prefer structured schedules or flexible study times?",
        "How would you describe your current study schedule?",
        "How do you manage your study sessions when you have a lot to cover?",
        "If an unexpected event interrupts your study schedule, how do you react?",
        "How often do you review your study schedule and adjust it?",
        "Do you incorporate different types of activities in your study schedule?",
        "How do you balance study sessions with leisure activities?",
        "How do you feel after a long study session?",
        "How often do you use tools like the Pomodoro technique in your study sessions?",
        "What is your approach to handling difficult subjects or topics?",
        "How do you track your study progress?"
    ]

    options = [
        ['Early morning', 'Late morning', 'Afternoon', 'Evening'],
        ['Less than 15 minutes', '15-30 minutes', '30-45 minutes', 'More than 45 minutes'],
        ['Very often', 'Often', 'Sometimes', 'Rarely'],
        ['Continue trying to study', 'Take a short break', 'Switch to a different activity', 'Review what you\'ve just studied'],
        ['Very poorly', 'Poorly', 'Moderately well', 'Very well'],
        ['Frequently', 'Occasionally', 'Rarely', 'Almost never'],
        ['Alone', 'In a small group', 'In a large group', 'It varies depending on the subject'],
        ['I need to revise it multiple times before it sticks.', 'I can remember it after a couple of revisions.', 'I usually understand and remember it after the first read.', 'I almost always understand and remember it instantly.'],
        ['Every 10-15 minutes', 'Every 20-30 minutes', 'Every 40-60 minutes', 'I rarely take breaks.'],
        ['Still tired', 'Slightly refreshed', 'Quite refreshed', 'Fully recharged'],
        ['Big picture', 'Details', 'Both equally', 'Depends on the topic'],
        ['Break them down into smaller parts', 'Discuss with peers or teachers', 'Use additional resources like videos or tutorials', 'Rely on examples and applications'],
        ['Never', 'Rarely', 'Sometimes', 'Often'],
        ['Visual aids (charts, diagrams)', 'Listening to lectures or discussions', 'Hands-on activities or practical exercises', 'Reading and writing'],
        ['Drawing diagrams or mind maps', 'Discussing it with someone', 'Working through it step-by-step physically', 'Reading about similar problems and solutions'],
        ['By visualizing it', 'By hearing it explained', 'By doing something with it', 'By writing it down'],
        ['Quiet room', 'Background music or white noise', 'Library or study hall', 'Outdoors or variable locations'],
        ['Color-coded notes and diagrams', 'Audio recordings and discussions', 'Physical models or demonstrations', 'Written summaries and outlines'],
        ['Creating visual aids like charts and mind maps', 'Joining study groups or listening to lectures', 'Doing practice problems and hands-on activities', 'Reading and summarizing textbooks and notes'],
        ['Structured schedules', 'Flexible study times', 'A mix of both', 'Depends on my mood'],
        ['Very intense, with minimal breaks', 'Moderately intense, with regular breaks', 'Balanced, with ample time for breaks and revision', 'Relaxed, with frequent breaks and little pressure'],
        ['Study for long hours with few breaks', 'Study in shorter, focused sessions with regular breaks', 'Mix of long and short sessions depending on the material', 'Study at a relaxed pace, regardless of the amount'],
        ['I find it difficult to get back on track.', 'I adjust my timetable and continue.', 'I reschedule my study sessions for later.', 'I take it in stride and easily make up for lost time.'],
        ['Daily', 'Weekly', 'Monthly', 'Rarely'],
        ['Always', 'Often', 'Sometimes', 'Never'],
        ['I prioritize study over leisure', 'I have a strict balance between the two', 'I mostly study but allow for some leisure time', 'I prioritize leisure over study'],
        ['Exhausted', 'Tired but accomplished', 'Neutral', 'Energized and ready for more'],
        ['Always1', 'Often1', 'Sometimes1', 'Never1'],
        ['Spend extra time studying them', 'Seek help from teachers or tutors', 'Use a variety of resources (videos, books, etc.)', 'Focus on other subjects and come back later'],
        ['Detailed logs or journals', 'Regular self-assessments and quizzes', 'Feedback from teachers and peers', 'I don\'t track my progress specifically']
    ]

    answer = []
    answers = []
    for i, question in enumerate(questions):
        st.write(f"{i+1}. {question}")
        option = st.radio("", options[i])
        answer.append(option)

    for i in range(30):
        if answer[i] in options[i]:
            if answer[i] == options[i][0]:
                answers.append('a')
            elif answer[i] == options[i][1]:
                answers.append('b')
            elif answer[i] == options[i][2]:
                answers.append('c')
            elif answer[i] == options[i][3]:
                answers.append('d')
            

    if st.button('Submit'):
        cognitive_score, learning_ability_score, learning_style_score, learning_intensity_score = evaluate_answers(answers)
        if cognitive_score >= 6:
            st.session_state["Cognitive"] = "High"
        elif cognitive_score >= 4:
            st.session_state["Cognitive"] = "Moderate"
        else:
            st.session_state["Cognitive"] = "Low"

        if learning_ability_score >= 5:
            st.session_state["Ability"] = "High"
        elif learning_ability_score >= 3:
            st.session_state["Ability"] = "Moderate"
        else:
            st.session_state["Ability"] = "Low"

        learning_style_answers = answers[13:20]
        if learning_style_score == learning_style_answers.count('a'):
            st.session_state["Style"] = "Visual"
        elif learning_style_score == learning_style_answers.count('b'):
            st.session_state["Style"] = "Audio"
        elif learning_style_score == learning_style_answers.count('c'):
            st.session_state["Style"] = "Kinesthetic"
        else:
            st.session_state["Style"] = "LSRW"

        learning_intensity_answers = answers[20:]
        if learning_intensity_score == learning_intensity_answers.count('a'):
            st.session_state["Intensity"] = "High"
        elif learning_intensity_score == learning_intensity_answers.count('b') or learning_intensity_score == learning_intensity_answers.count('c'):
            st.session_state["Intensity"] = "Balanced"
        else:
            st.session_state["Intensity"] = "Low"

        
        Cognitive = st.session_state["Cognitive"]
        Ability = st.session_state["Ability"]
        Style = st.session_state["Style"]
        Intensity = st.session_state["Intensity"]
        Name = st.session_state["Name"]

        st.write(f"Hello *{Name}*")
        st.write(f"""According to your responses, you have a *{Cognitive}* cognitive ability, \na *{Style}* learning style, a *{Intensity}* learning intensity, and a *{Ability}* learning ability.""")

        st.write("**The Resources that we Recommend using to you are as follows**")
        cognitive(Cognitive)
        ability(Ability)
        style(Style)
        intensity(Intensity)

    
