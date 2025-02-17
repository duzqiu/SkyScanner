import requests

class SendBark:
    def __init__(self, key):
        self.key = key     

    def send_t_c(self, title, content):
        self.url = f"https://api.day.app/{self.key}/{title}/{content}"
        requests.get(self.url)

if __name__ == "__main__":
    key = "UZ9juRSNtAMpnzWEQokJYF"
    title = "Hello, World!"
    content = "This is a test message."
    bark = SendBark(key)
    bark.send_t_c(title, content)