from base.base_driver import init_driver
from page.contact_list_page import ContactListPage
from page.new_contact_page import NewContactPage
from page.saved_page import SavedPage


class TestContact:

    def setup(self):
        self.driver = init_driver()

        self.contact_list_page = ContactListPage(self.driver)
        self.new_contact_page = NewContactPage(self.driver)
        self.saved_page = SavedPage(self.driver)

    def teardown(self):
        self.driver.quit()

    # name, phone
    # xiaoming, 188
    # xiaohong, 177
    # xiaoqiang, 166
    def test_new_contact(self):
        name = "xiaoming"
        self.contact_list_page.click_new_contact()
        self.new_contact_page.click_local_save()
        self.new_contact_page.input_name(name)
        self.new_contact_page.input_phone("1888")
        self.new_contact_page.click_back()

        assert name == self.saved_page.get_large_title_text()
