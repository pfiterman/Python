# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.

# <code>
import azure.cognitiveservices.speech as speechsdk
import os

# Environment variables named "SPEECH_KEY" and "SPEECH_ENDPOINT"
speech_key = os.getenv("SPEECH_KEY")
speech_region = os.getenv("SPEECH_REGION")
speech_endpoint = f"https://{speech_region}.api.cognitive.microsoft.com/"

# Creates an instance of a speech config with specified endpoint and subscription key.
speech_config = speechsdk.SpeechConfig(subscription=speech_key, endpoint=speech_endpoint)

# Set the voice name, refer to https://aka.ms/speech/voices/neural for full list.
male_voices = {
    "Andrew": "en-US-AndrewNeural",
    "Brian": "en-US-BrianNeural"
}

speech_config.speech_synthesis_voice_name = male_voices["Brian"]

# Set the output format to audio
audio_config = speechsdk.audio.AudioOutputConfig(filename="output.wav")

# Creates a speech synthesizer using the default speaker as audio output.
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# Receives a text from console input.
# print("Type some text that you want to speak...")
# text = input()

interview_answers = {
    "tell_me_about_yourself" :  "I'm a Full-Stack Developer with over 10 years of experience delivering robust web applications. I hold a diploma in Data Processing Technology — equivalent to a bachelor's degree in Computer Science — along with a specialization in Web Development." \
                                "Much of my experience has been in the Public Sector, working with Public Safety organizations in Brazil. At the Brazilian Federal Police Department, I developed a Web ERP Portal that automated key operational processes. I also worked with the Public Safety Secretariat, where I delivered enhancements to the online Police Report platform, improving accessibility and reducing in-person reporting. " \
                                "Currently, I’m working remotely as a Full-Stack Developer for a non-profit organization in Ottawa. I’m building and improving features for an Expense and Revenue Management System using React and TypeScript on the front end, and Node.js, Express, MySQL and Prisma ORM on the backend. I also led the deployment of the application to a new hosting server and implemented a CI/CD pipeline using GitHub Actions." \
                                "I'm now looking for a full-stack role where I can contribute to a modern engineering team, continue growing my technical skills, and deliver impactful solutions.",

    "why_change_roles" :  "The reason I’m currently looking for a new opportunity and am particularly interested in this role is that I’m keen to take on positions where I can leverage my experience in React and Node.js to create impactful and challenging solutions. I enjoy building applications that improve usability and user experience, ultimately delivering better service for clients." \
                          "I also love collaborating with different teams, sharing my knowledge, and learning from others’ expertise. This helps me enhance my skills and continue growing in my career as a Full-Stack Developer",

    "what_your_manage_would_say": "My manager is a great leader with strong communication skills, and I’ve spoken with him about my decision to leave in order to pursue professional growth in my career. We’ve often shared our goals and aspirations for the future. I’m confident he would say that I’ve been a valuable asset to the team, consistently contributing and helping achieve important milestones during the time we’ve worked together. " \
                                  "From my perspective, coworkers and managers become like a professional family—we often spend more time with them than with loved ones. That’s why I believe in building strong, respectful relationships and collaborating to grow together as a team",

    "what_do_you_see_yourself_five_years": "In five years, I see myself continuing to grow as a Full-Stack Developer, taking on more technical ownership of projects, mentoring junior developers, and contributing to architectural decisions. I want to be someone who not only writes high-quality code, but also improves processes, collaborates across teams, and helps the organization deliver impactful solutions to customers." \
                                           "I want to be someone who has grown within the company - someone who has taken on more responsibility, learned new technologies, and earned trust through consistent results. I’m not fixed on a title; I’m focused on development and becoming more valuable to the organization over time",

    "which_type_culture_you_thrive_in": "I thrive in a culture that values collaboration, continuous learning, and open communication. I do my best work in environments where people share knowledge, support each other, and prioritize solving problems as a team rather than individually. I also appreciate a culture that encourages initiative, ownership, trust and I enjoy working with teams that are focused on results and customer value.",
    "what_do_you_look_for_manager": "What I look for in a manager is someone who communicates clearly, provides guidance when needed, and trusts the team to take ownership of their work. I appreciate managers who give constructive feedback, support growth, and foster an environment where collaboration and openness are encouraged." \
                                    "I appreciate managers who act as mentors - someone who helps me develop my skills, challenges me in a positive way, and encourages professional growth. I value a manager who provides direction and expectations, but also gives the freedom to learn, experiment, and make decisions"                                    

}

                         
text = interview_answers["what_do_you_look_for_manager"]

# Synthesizes the received text to speech.
# The synthesized speech is expected to be heard on the speaker with this line executed.
result = speech_synthesizer.speak_text_async(text).get()

# Checks result.
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized to speaker for text [{}]".format(text))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
    print("Did you update the subscription info?")
# </code>