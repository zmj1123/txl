from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SavedPage(BaseAction):
    large_title_feature = By.ID, "com.android.contacts:id/large_title"

    def get_large_title_text(self):
        return self.get_text(self.large_title_feature)
