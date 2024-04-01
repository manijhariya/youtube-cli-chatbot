import cmd
import traceback

from src import chat, llm

yt_chat = chat.Chat()


class YTChatBot(cmd.Cmd):
    """Simple command YTChatBot interface."""

    intro = 'Welcome to the YTChatBot shell.   Type help or ? to list commands.\n'
    prompt = '(YTChatBot) '

    def do_You(self, message):
        if message:
            print(f"YT Bot: {yt_chat.get_response(message)}")
        else:
            print("Please enter some message")

    def do_Search(self, message):
        if message:
            search_results = yt_chat.get_search(message)
            print("YT Search Results:\n")
            for search_result in search_results:
                print(f"{search_result['title']} - {search_result['id']}")
                print(f"Publichsed Time : {search_result['publishedTime']}")
                print(f"Duration : {search_result['duration']}")
                print(f"Channel : {search_result['channel']}")
                print(f"Short Description : {search_result['description']}\n")

        else:
            print("Please enter some message")

    def do_Summarize(self, message):
        if message:
            print(f"YT Summarize: {yt_chat.get_summary(message)}")
        else:
            print("Please enter some message")

    def do_exit(self, message):
        print("Bye!")
        return self.do_EOF("")

    def do_load(self, chat_id):
        if not chat_id:
            print("Please enter a correct chat id")
            return
        print(chat_id)

    def help_Summarize(self):
        print(
            "\n".join(
                [
                    "Summarize [message]",
                    "Message YT Chat Bot to summarize a yt vidoe you can than talk to its content",
                ]
            )
        )

    def help_Search(self):
        print(
            "\n".join(
                [
                    "Search [message]",
                    "Message YT Chat Bot to search yt vidoes",
                ]
            )
        )

    def help_You(self):
        print(
            "\n".join(
                [
                    "You [message]",
                    "Message YT Chat Bot",
                ]
            )
        )

    def help_exit(self):
        print("Exit Chat")

    def do_EOF(self, line):
        return True

def main():
    try:
        YTChatBot().cmdloop()
    except Exception as e:
        traceback.print_exc()
    finally:
        llm.close_llm()
        exit(-1)

if __name__ == "__main__":
    main()
