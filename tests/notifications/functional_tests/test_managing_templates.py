import uuid

import pytest

from tests.notifications.functional_tests.test_send_files_via_ui import delete_template_from_view_email_template_page, \
    delete_template_from_view_sms_template_page, delete_template_from_view_letter_template_page
from tests.pages import ShowTemplatesPage, ChooseExistingTemplatePage, CopyExistingTemplatePage, ViewEmailTemplatePage, \
    ViewSMSTemplatePage, ViewLetterTemplatePage
from tests.test_utils import recordtime, go_to_templates_page, create_email_template, create_sms_template, \
    create_letter_template, delete_template


@recordtime
@pytest.mark.xdist_group(name="copy-an-existing-template")
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


@recordtime
@pytest.mark.xdist_group(name="copy-an-existing-template")
def test_copying_an_existing_sms_template(driver, login_seeded_user):
    go_to_templates_page(driver)
    content = "This is a test template"

    # Create sms template
    sms_template_name = f"Functional Tests - copy sms template - {uuid.uuid4()}"
    create_sms_template(driver, name=sms_template_name, content=content)

    # Confirm sms template was created
    go_to_templates_page(driver)
    templates_page = ShowTemplatesPage(driver)
    assert templates_page.get_h1_text() == "Templates"
    assert sms_template_name in templates_page.get_all_listed_templates()

    # Copy sms template
    templates_page.click_add_new_template()
    templates_page.select_copy_an_existing_template()
    choose_existing_template_page = ChooseExistingTemplatePage(driver)
    assert choose_existing_template_page.get_h1_text() == "Choose an existing template to copy"
    choose_existing_template_page.click_template_by_link_text(sms_template_name)
    copy_existing_template_page = CopyExistingTemplatePage(driver)
    assert copy_existing_template_page.get_h1_text() == "Copy an existing template"
    new_template_name = f"Functional Tests - new copied sms template - {uuid.uuid4()}"
    copy_existing_template_page.change_template_name(new_template_name)
    copy_existing_template_page.click_copy_this_template_button()
    view_sms_template_page = ViewSMSTemplatePage(driver)
    assert view_sms_template_page.get_h1_text() == new_template_name

    # Delete created sms templates
    delete_template_from_view_sms_template_page(driver, new_template_name)
    templates_page.click_template_by_link_text(sms_template_name)
    assert view_sms_template_page.get_h1_text() == sms_template_name
    delete_template_from_view_sms_template_page(driver, sms_template_name)


@recordtime
@pytest.mark.xdist_group(name="copy-an-existing-template")
def test_copying_an_existing_letter_template(driver, login_seeded_user):
    go_to_templates_page(driver)
    content = "This is a test template"

    # Create letter template
    letter_template_name = f"Functional Tests - copy letter template - {uuid.uuid4()}"
    create_letter_template(driver, name=letter_template_name, content=content)

    # Confirm letter template was created
    go_to_templates_page(driver)
    templates_page = ShowTemplatesPage(driver)
    assert templates_page.get_h1_text() == "Templates"
    assert letter_template_name in templates_page.get_all_listed_templates()

    # Copy letter template
    templates_page.click_add_new_template()
    templates_page.select_copy_an_existing_template()
    choose_existing_template_page = ChooseExistingTemplatePage(driver)
    assert choose_existing_template_page.get_h1_text() == "Choose an existing template to copy"
    choose_existing_template_page.click_template_by_link_text(letter_template_name)
    copy_existing_template_page = CopyExistingTemplatePage(driver)
    assert copy_existing_template_page.get_h1_text() == "Copy an existing template"
    new_template_name = f"Functional Tests - new copied letter template - {uuid.uuid4()}"
    copy_existing_template_page.change_template_name(new_template_name)
    copy_existing_template_page.click_copy_this_template_button()
    view_letter_template_page = ViewLetterTemplatePage(driver)
    assert view_letter_template_page.get_h1_text() == new_template_name

    # Delete created letter templates
    delete_template_from_view_letter_template_page(driver, new_template_name)
    templates_page.click_template_by_link_text(letter_template_name)
    assert view_letter_template_page.get_h1_text() == letter_template_name
    delete_template_from_view_sms_template_page(driver, letter_template_name)
