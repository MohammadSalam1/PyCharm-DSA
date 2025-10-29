class BrowserHistory:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current_page = None

    def visit(self, url):
        if self.current_page is not None:
            self.back_stack.append(self.current_page)

        self.forward_stack.clear()

        self.current_page = url
        print(f"visited: {self.current_page}")

    def go_back(self):
        if not self.back_stack:
            print("Error, can't go back")

        self.forward_stack.append(self.current_page)

        self.current_page = self.back_stack.pop()
        print(f"Back to: {self.current_page}")

    def go_forward(self):
        if not self.forward_stack:
            print("Error, can't move forward")

        self.back_stack.append(self.current_page)

        self.current_page = self.forward_stack.pop()
        print(f"Forward to: {self.current_page}")


if __name__ == "__main__":
    browser = BrowserHistory()
    print()
    browser.visit("google.com")
    browser.visit("youtube.com")
    browser.visit("github.com")
    print()
    browser.go_back()  # goes from github → youtube
    browser.go_back()  # goes from youtube → google
    browser.go_forward()  # goes from google → youtube
