import gc

import torch
from langchain.chains import ConversationChain, LLMChain
from langchain.memory import ConversationBufferMemory, ConversationSummaryBufferMemory
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from transformers import pipeline

from src import llm_prompts

# torch.set_default_device("cuda")
torch.cuda.empty_cache()
MODEL_NAME = "microsoft/phi-2"
pipe = pipeline("text-generation", model=MODEL_NAME, max_new_tokens=200)

LOCAL_LLM = HuggingFacePipeline(pipeline=pipe)

memory = ConversationSummaryBufferMemory(
    llm=LOCAL_LLM, memory_key="chat_history", max_token_limit=450, input_key="message"
)
conversation_default = LLMChain(llm=LOCAL_LLM, prompt=llm_prompts.default_prompt, memory=memory)
conversation_search = LLMChain(llm=LOCAL_LLM, prompt=llm_prompts.search_prompt, memory=memory)
conversation_video_summary = LLMChain(llm=LOCAL_LLM, prompt=llm_prompts.summary_prompt, memory=memory)
conversation_transcrip_summary = LLMChain(llm=LOCAL_LLM, prompt=llm_prompts.transcript_summary_prompt,memory=memory)

def get_llm_output(message : str, conversation : LLMChain) -> str:
    return conversation({"message": message})["text"]

def get_transcript_summary_output(transcript : str) -> str:
    return conversation_transcrip_summary({"transcript" : transcript})

def close_llm():
    print("\nClosing LLM")
    global LOCAL_LLM
    del LOCAL_LLM
    gc.collect()
    torch.cuda.empty_cache()
