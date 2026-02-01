import streamlit as st
from groq import Groq   #Ai brian

st.set_page_config(
    page_title="My App",
    layout="centered"
)

api_key = "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" 

try:
    client = Groq(api_key=api_key)  #AI Connection

except Exception as e:
    st.error("Api key error... Please check the key")

st.title("Boom AI")
st.markdown("--------")

st.write("Enter your prompt and get your post")
topic = st.text_area("What is your post about?", placeholder= "Ex: Nature")
language = st.selectbox(
        "Select Language :", 
        ["English", "Tamil", "Telugu", "Tanglish"]
    )

col1, col2, col3 = st.columns([1,2,1])
with col2:
    generate_btn = st.button("Generate AI Post", type="primary")

if generate_btn:
    if not  topic.strip():
        st.warning("Please enter a topic")

    else:
        with st.spinner("AI is Thinking"):

            prompt = f"""
            Act as professional social media influencer 
            write an engaging, viral linkedin/instagram post about: '{topic}'

            Strict requirement: Write the post in **{language}**

            Rules:
            1. Start with a catchy Hook/Headline
            2. Use Bullet Points
            3. Add 5 hashtags
            4. Keep the post under 800 words
            5. Avoid generic phrases like "In today’s world"
            6. Make the tone inspiring and confident
            7. End with a strong Call-To-Action (question or opinion)
            8. Use line breaks for better readability
            9. Add 1 relevant emoji per bullet point
            10. Do not mention that you are an AI
            11. Output ONLY the post content


            """

    try: 
        client_completion = client.chat.completions.create(
            messages=[
                {"role":"user", "content": prompt}
            ],

            model = "llama-3.3-70b-versatile"
        )

        ai_response = client_completion.choices[0].message.content


        st.balloons()
        st.success("Your caption for the post is ready !")

        st.markdown(ai_response)
        st.info("Post it on any Social Media :) ")


    except Exception as e:
        st.error(f"error : {e}")

