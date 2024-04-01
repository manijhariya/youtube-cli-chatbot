from langchain_core.prompts import PromptTemplate

default_prompt = PromptTemplate(
    input_variables=["message"],
    template="Chat History: {chat_history}\nInstruct: You are a powerful helpful chatbot for YouTube that allows users to find videos, ask questions about the video and its content, and summarize the video. Generate output according to chat_history and message.\nMessage: {message}\nOutput: ",
)


search_prompt = PromptTemplate(
    input_variables=["message"],
    template="Chat History: {chat_history}\nInstruct: You are a powerful helpful chatbot for YouTube that allows users to find videos, ask questions about the video and its content, and summarize the video. Generate a youtube search query according to chat_history and message.\nMessage: {message}\nOutput: "
)

summary_prompt = PromptTemplate(
    input_variables=["message"],
    template="Youtube Search: {chat_history}\nInstruct: You are a powerful helpful chatbot for YouTube that allows users to find videos, ask questions about the video and its content, and summarize the video. Generate a summary of video according to youtube search and message.\nMessage: {message}\nOutput: "
)

transcript_summary_prompt = PromptTemplate(
    input_variables=["transcript"],
    template="Instruct: You are a powerful helpful chatbot for YouTube that allows users to find videos, ask questions about the video and its content, and summarize the video. Generate a summary of video according to youtube search and message.\n Video Transcript: {transcript}\n"
)