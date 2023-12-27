import streamlit as st  
from langchain.llms import VertexAI
from langchain.prompts import PromptTemplate

prompt_explain = PromptTemplate.from_template("Explain what the below code does. {entered_code}")
prompt_alternate = PromptTemplate.from_template("Can you rewrite the below function using python best practices? {entered_code}")
prompt_unittests = PromptTemplate.from_template("Create unit test code/cases for the below function. {entered_code}")



llm = VertexAI(model_name="gemini-pro", max_output_tokens=1024)

if 'button' not in st.session_state:
    st.session_state.button = False

def analyzeCode():
    st.session_state.button = not st.session_state.button


st.set_page_config(
    page_title="Code Advisor",
    layout="wide",
)

st.title("Code Advisor")

in1,in2=st.columns([1,2])

with in1:
    entered_code = st.text_area(label="Enter your code here", height=200)
    st.button("Submit", on_click=analyzeCode)

with in2:
    
    if st.session_state.button:
        tab1, tab2, tab3 = st.tabs(["Explain", "Alternates", "Unit Tests"])
        with tab1:
            st.header("Explain")
            codeExplanation=llm(prompt_explain.format(entered_code=entered_code))
            st.write(codeExplanation)

        with tab2:
            st.header("Alternates")
            alternateCode=llm(prompt_alternate.format(entered_code=entered_code))
            st.write(alternateCode)

        with tab3:
            st.header("Unit Tests")
            unitTests=llm(prompt_unittests.format(entered_code=entered_code))
            st.write(unitTests)