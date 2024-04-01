import secrets
from typing import List, Dict

def verfiy_chat_id(chat_id: str) -> bool:
    return True

def generate_chat_id(info: str) -> str:
    return secrets.token_urlsafe(5)

def format_yt_results(yt_result : Dict[str, str]) -> Dict[str, str]:
    new_obj = {}
    new_obj["id"] = yt_result["id"]
    new_obj["title"] = yt_result["title"]
    new_obj["publishedTime"] =  yt_result["publish_time"]
    new_obj["duration"] = yt_result["duration"]
    new_obj["description"] = yt_result["long_desc"]
    new_obj["channel"] = yt_result["channel"]

    return new_obj


def format_transcript(transcript_result : Dict[str, str]) -> str:
    return transcript_result['text']