"""
    example of usage:

    ```python
    from scraper import Scraper

    scraper = Scraper()
    input: list[str] = scraper.getInput()
    print(input)
    ```
"""

import requests
from dotenv import load_dotenv
import os
from typing import Optional 
import datetime

class Scraper:
    def __init__(self, dayOfTheMonth: int = -1):
        """Create a new Scraper object,
        This object will scrape the input for the given day of the month

        Args:
            dayOfTheMonth (Optional[int], optional): The day of the month to download. if not set, it will chose the current day of the month.
        """
        load_dotenv() # Load the .env file that should contain the session cookie
        
        if dayOfTheMonth == -1:
            dayOfTheMonth = datetime.datetime.now().day
        
        self.dayOfTheMonth: int = dayOfTheMonth
        self.input = []
        self.saveInput(dayOfTheMonth)
    
    def getInput(self) -> list[str]:
        """get the input that was scraped

        Returns:
            list[str]: the scraped input
        """
        return self.input

    def saveInput(self, dayOfTheMonth: Optional[int] = -1) -> list[str]:
        """Scrape the input for the given day of the month
        
        Args:
            dayOfTheMonth (Optional[int], optional): The day of the month to download. if not set, it will chose the current day of the month.
        
        Returns:
            list[str]: the scraped input
        """
        if dayOfTheMonth == -1:
            dayOfTheMonth = self.dayOfTheMonth
        
        if not os.path.exists(f"day{dayOfTheMonth}"):
            os.makedirs(f"day{dayOfTheMonth}")

        with open(f"day{dayOfTheMonth}/test.py", "w") as file:
            print("import sys\n\ndef main():\n\tdata = sys.stdin.read().strip().split(\"\\n\")\n\n\nif __name__ == \"__main__\":\n\tmain()", file=file)
        
        if os.path.exists(f"day{dayOfTheMonth}/input.txt"):
            with open(f"day{dayOfTheMonth}/input.txt", "r") as file:
                self.input = file.read().split("\n")
                return self.input
        
        url = f"https://adventofcode.com/2024/day/{dayOfTheMonth}/input"
        cookies = {
            "session": os.getenv("SESSION_COOKIE")
        }
        
        response = requests.get(url, cookies=cookies) # type: ignore
        
        try: 
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(f"Error: {e}, {response.text}")
            return []
        
        with open(f"day{dayOfTheMonth}/input.txt", "w") as file:
            file.write(response.text)
        
        self.input = response.text.split("\n")
        return self.input

if __name__ == "__main__":
    scraper = Scraper()
    if scraper.getInput() != []:
        print("Input downloaded successfully!")
