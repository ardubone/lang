from typing import List

from selenium.webdriver.remote.webelement import WebElement

from base.sileniumbase import SeleniumBase

class PageNav(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver        
        #self.__title: str = 'title'
        #self.TITLE_TEXT = 'oogl'
        
    #def get_title(self) -> List[WebElement]:
        return self.is_present('name', self.__title, 'title')
    
    #def get_title_text(self) -> str:
        title = self.get_title()
        title_text = self.get_attribute(title)
        return (title_text)