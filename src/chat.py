import json
import os
import re
from datetime import datetime
from typing import Dict, List

from src import config, helpers, llm, llm_prompts, yt_search


class Chat:
    def __init__(self) -> None:
        self.chathistory = []
        self.metadata = {
            "chat_id": helpers.generate_chat_id(datetime.now()),
            "start_time": datetime.now(),
        }

    @staticmethod
    def get_empty_chat_object() -> Dict[str, str]:
        return {"you": "", "prompt": "", "llm": "", "youtube": "", "command": ""}

    def load_chat(self, chat_id) -> None:
        if self.chathistory:
            raise ValueError("Can't Load a chat in ongoing chat")

        if not os.path.exists(config.CHAT_SAVE_PATH):
            raise ValueError("No chat to load from")

        if helpers.verfiy_chat_id(chat_id):
            raise ValueError("Please Enter a valid chat_id")

        if not os.path.exists(config.CHAT_SAVE_PATH / f"{chat_id}.json"):
            raise ValueError("Chat Id {chat_id} not found!!")

        with open(config.CHAT_SAVE_PATH / f"{chat_id}.json", "rb") as f:
            data = json.load(f)

        self.chathistory = data["history"]
        self.metadata = data["metadata"]

        return f"Sucessfully loaded previous chat {chat_id}"

    def save_chat(self) -> str:
        os.makedirs(config.CHAT_SAVE_PATH, exist_ok=True)

        if self.chathistory:
            raise ValueError("Please send at least one message to bot.!!")

        data = {"metadata": self.metadata, "history": self.chathistory}
        with open(config.CHAT_SAVE_PATH / f"{chat_id}.json", "wb") as f:
            json.dump(data, f)

        return self.metadata["chat_id"]

    def generate_prompt(
        self, message: str, yt_search_results: List[Dict[str, str]]
    ) -> str:
        return message + "\n" + yt_search_results

    def format_llm_output(self, llm_output: str) -> str:
        return llm_output.split("Output: ")[-1].strip()

    def get_response(self, message: str) -> str:

        self.chathistory.append(Chat.get_empty_chat_object())

        self.chathistory[-1]["you"] = message
        self.chathistory[-1]["command"] = "chat"

        self.chathistory[-1]["llm"] = self.format_llm_output(llm.get_llm_output(self.chathistory[-1]["you"]), llm.conversation_default)

        return self.chathistory[-1]["llm"]

    def is_valid_youtube_link(self, message : str) -> str:
        pattern = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})"
        match = re.search(pattern, message)
        if match:
            return match.group(1)

    def get_search(self, message: str) -> str:

        self.chathistory.append(Chat.get_empty_chat_object())
        self.chathistory[-1]["you"] = message
        self.chathistory[-1]["command"] = "search"

        self.chathistory[-1]["yt_results"] = list(map(helpers.format_yt_results, yt_search.make_search(self.chathistory[-1]["you"])))
        return self.chathistory[-1]["yt_results"]

    def get_summary(self, message: str) -> str:

        self.chathistory.append(Chat.get_empty_chat_object())
        self.chathistory[-1]["you"] = message
        self.chathistory[-1]["command"] = "summary"

        if valid_yt_link := self.is_valid_youtube_link(message):
            video_transcript = " ".join(list(map(helpers.format_transcript, yt_search.download_transcript(valid_yt_link))))
            self.chathistory[-1]["llm"] = self.format_llm_output(llm.get_transcript_summary_output(video_transcript))
        else:
            self.chathistory[-1]["llm"] = self.format_llm_output(llm.get_llm_output(message, llm.conversation_video_summary))

        return self.chathistory[-1]["llm"]