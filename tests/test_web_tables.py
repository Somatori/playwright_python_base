from pages.web_tables_page import WebTablesPage
from model.employee import Employee
from helpers.data_helper import generate_random_employee


def test_create_update_delete_record(page):
    web_tables = WebTablesPage(page)
    web_tables.goto()
    
    # create a record
    employee = generate_random_employee()
    web_tables.add_record(employee)
    assert web_tables.is_email_cell_visible(employee.email)

    # update a salary
    employee.salary = "105000"
    web_tables.edit_record(employee)
    assert employee.salary == web_tables.get_salary(employee.first_name)

    # delete the record
    web_tables.delete_record(employee.first_name)
    assert web_tables.is_record_deleted(employee.email)