from playwright.sync_api import Page, expect
from configs.config import BASE_URL


class WebTablesPage:
    def __init__(self, page: Page):
        self.page = page

    ### ========== LOCATORS ==========
    def _add_btn(self):
        return self.page.get_by_role("button", name="Add")
    
    def _first_name_input(self):
        return self.page.get_by_role("textbox", name="First Name")
    
    def _last_name_input(self):
        return self.page.get_by_role("textbox", name="Last Name")
    
    def _email_input(self):
        return self.page.get_by_role("textbox", name="name@example.com")
    
    def _age_input(self):
        return self.page.get_by_role("textbox", name="Age")
    
    def _salary_input(self):
        return self.page.get_by_role("textbox", name="Salary")
    
    def _department_input(self):
        return self.page.get_by_role("textbox", name="Department")
    
    def _submit_btn(self):
        return self.page.get_by_role("button", name="Submit")
    
    def _edit_btn(self, employee_first_name):
        return self.page.get_by_role('rowgroup').filter(has_text=employee_first_name).get_by_title('Edit')

    def _delete_btn(self, employee_first_name):
        return self.page.get_by_role('rowgroup').filter(has_text=employee_first_name).get_by_title('Delete')
    
    def _email_cell(self, email_address):
        return self.page.get_by_role("gridcell", name=email_address)

    def _salary_cell(self, employee_first_name):
        return self.page.get_by_role('rowgroup').filter(has_text=employee_first_name).get_by_role('gridcell').locator('nth=4')
    

    ### ========== ACTIONS =============
    def goto(self):
        self.page.goto(f"{BASE_URL}/webtables")

    def add_record(self, employee):
        self._add_btn().click()
        self._first_name_input().fill(employee.first_name)
        self._last_name_input().fill(employee.last_name)
        self._email_input().fill(employee.email)
        self._age_input().fill(employee.age)
        self._salary_input().fill(employee.salary)
        self._department_input().fill(employee.department)
        self._submit_btn().click()

    def edit_record(self, employee):
        self._edit_btn(employee.first_name).click()
        self._salary_input().fill(employee.salary)
        self._submit_btn().click()

    def get_salary(self, employee_first_name):
        return self._salary_cell(employee_first_name).inner_text()

    def delete_record(self, employee_first_name):
        self._delete_btn(employee_first_name).click()


    ### ========== ASSERTIONS =============
    def is_email_cell_visible(self, email_address) -> bool:
        expect(self._email_cell(email_address)).to_be_visible()
        return True
    
    def is_record_deleted(self, email_address):
        expect(self._email_cell(email_address)).not_to_be_visible()
        return True
