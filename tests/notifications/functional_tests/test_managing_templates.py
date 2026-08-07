import uuid

from tests.notifications.functional_tests.test_send_files_via_ui import delete_template_from_view_email_template_page
from tests.pages import ShowTemplatesPage, ChooseExistingTemplatePage, CopyExistingTemplatePage, ViewEmailTemplatePage
from tests.test_utils import recordtime, go_to_templates_page, create_email_template, create_sms_template, \
    create_letter_template, delete_template


@recordtime
def test_copying_an_existing_email_template(driver, login_seeded_user):
    go_to_templates_page(driver)
    content = "This is a test template"

    # Create an email template
    email_template_name = f"Functional Tests - copy email template - {uuid.uuid4()}"
    create_email_template(driver, name=email_template_name, content=content)

    # Confirm email template was created
    go_to_templates_page(driver)
    templates_page = ShowTemplatesPage(driver)
    assert templates_page.get_h1_text() == "Templates"
    assert email_template_name in templates_page.get_all_listed_templates()

    # Copy email template
    templates_page.click_add_new_template()
    templates_page.select_copy_an_existing_template()
    choose_existing_template_page = ChooseExistingTemplatePage(driver)
    assert choose_existing_template_page.get_h1_text() == "Choose an existing template to copy"
    choose_existing_template_page.click_template_by_link_text(email_template_name)
    copy_existing_template_page = CopyExistingTemplatePage(driver)
    assert copy_existing_template_page.get_h1_text() == "Copy an existing template"
    new_template_name = f"Functional Tests - new copied email template - {uuid.uuid4()}"
    copy_existing_template_page.change_template_name(new_template_name)
    copy_existing_template_page.click_copy_this_template_button()
    view_email_template_page = ViewEmailTemplatePage(driver)
    assert view_email_template_page.get_h1_text() == new_template_name

    # Delete created email templates
    delete_template_from_view_email_template_page(driver, new_template_name)
    templates_page.click_template_by_link_text(email_template_name)
    assert view_email_template_page.get_h1_text() == email_template_name
    delete_template_from_view_email_template_page(driver, email_template_name)
