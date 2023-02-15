import pytest

from pom.page_title import PageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:
   
     def test_page(self):
         page_title = PageNav(self.driver)
         actual_title = page_title.get_title_text
         expected_title = page_title.TITLE_TEXT            
         assert expected_title in actual_title