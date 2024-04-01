from youtube_search import YoutubeSearch
from youtube_transcript_api import YouTubeTranscriptApi as Transcript


def make_search(query: str, limit = 10) -> str:
    return YoutubeSearch(query).to_dict()


def download_transcript(yt_video_id: str) -> str:
    return Transcript.get_transcript(yt_video_id)