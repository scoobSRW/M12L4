class BrowsingHistory:
    def __init__(self):
        self.history = []

    def visit_page(self, url):
        """Adds a new page to the browsing history (to the top of the stack)."""
        self.history.append(url)
        print(f"Visited: {url}")

    def go_back(self):
        """Removes the most recent page from the browsing history (go back to the previous page)."""
        if not self.is_empty():
            removed_page = self.history.pop()
            print(f"Going back from: {removed_page}")
        else:
            print("No pages to go back to!")

    def check_history_count(self):
        """Checks how many pages have been visited in the current session."""
        print(f"Pages visited: {len(self.history)}")

    def is_empty(self):
        """Checks if the browsing history stack is empty."""
        return len(self.history) == 0

    def display_history(self):
        """Displays the current browsing history."""
        if self.is_empty():
            print("No pages visited.")
        else:
            print("Browsing history (Most recent to oldest):")
            for page in reversed(self.history):
                print(f"- {page}")

# Example usage
browsing_history = BrowsingHistory()

# Visiting some pages
browsing_history.visit_page("https://www.example.com")
browsing_history.visit_page("https://www.youtube.com")
browsing_history.visit_page("https://www.github.com")

# Checking the current history
browsing_history.check_history_count()
browsing_history.display_history()

# Going back (removes the most recent page)
browsing_history.go_back()

# Checking the history again
browsing_history.check_history_count()
browsing_history.display_history()

# Attempt to go back when there are no more pages
browsing_history.go_back()
