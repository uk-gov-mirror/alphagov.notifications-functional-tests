import uuid

import pytest

from tests.pages import (
    ChooseExistingTemplatePage,
    CopyExistingTemplatePage,
    ShowTemplatesPage,
    ViewEmailTemplatePage,
    ViewLetterTemplatePage,
    ViewSMSTemplatePage,
    delete_template_from_view_template_page,
)
from tests.test_utils import (
    create_email_template,
    create_letter_template,
    create_sms_template,
    go_to_templates_page,
    recordtime,
)


@recordtime
@pytest.mark.xdist_group(name="copy-an-existing-template")
def test_copying_an_existing_email_template(driver, login_seeded_user):
    go_to_templates_page(driver)
    content = "This is a test template"

    # Create an email template
    template_name = f"Functional Tests - copy email template - {uuid.uuid4()}"
    create_email_template(driver, name=template_name, content=content)

    # Confirm email template was created
    go_to_templates_page(driver)
    templates_page = ShowTemplatesPage(driver)
    assert templates_page.get_h1_text() == "Templates"
    assert template_name in templates_page.get_all_listed_templates()

    # Copy existing template
    view_template_page = ViewEmailTemplatePage(driver)
    new_template_name = copy_an_existing_template(
        driver, template_name, templates_page, view_template_page, notification_type="email"
    )

    # Confirm new copy of email template was created
    go_to_templates_page(driver)
    assert templates_page.get_h1_text() == "Templates"
    assert new_template_name in templates_page.get_all_listed_templates()

    # Delete created email templates
    templates_page.click_template_by_link_text(new_template_name)
    delete_template_from_view_template_page(driver, new_template_name, view_template_page)
    templates_page.click_template_by_link_text(template_name)
    assert view_template_page.get_h1_text() == template_name
    delete_template_from_view_template_page(driver, template_name, view_template_page)


@recordtime
@pytest.mark.xdist_group(name="copy-an-existing-template")
def test_copying_an_existing_sms_template(driver, login_seeded_user):
    go_to_templates_page(driver)
    content = "This is a test template"

    # Create sms template
    template_name = f"Functional Tests - copy sms template - {uuid.uuid4()}"
    create_sms_template(driver, name=template_name, content=content)

    # Confirm sms template was created
    go_to_templates_page(driver)
    templates_page = ShowTemplatesPage(driver)
    assert templates_page.get_h1_text() == "Templates"
    assert template_name in templates_page.get_all_listed_templates()

    # Copy existing sms template
    view_template_page = ViewSMSTemplatePage(driver)
    new_template_name = copy_an_existing_template(
        driver, template_name, templates_page, view_template_page, notification_type="sms"
    )

    # Confirm new copy of sms template was created
    go_to_templates_page(driver)
    assert templates_page.get_h1_text() == "Templates"
    assert new_template_name in templates_page.get_all_listed_templates()

    # Delete created sms templates
    templates_page.click_template_by_link_text(new_template_name)
    delete_template_from_view_template_page(driver, new_template_name, view_template_page)
    templates_page.click_template_by_link_text(template_name)
    assert view_template_page.get_h1_text() == template_name
    delete_template_from_view_template_page(driver, template_name, view_template_page)


@recordtime
@pytest.mark.xdist_group(name="copy-an-existing-template")
def test_copying_an_existing_letter_template(driver, login_seeded_user):
    go_to_templates_page(driver)
    content = "This is a test template"

    # Create letter template
    template_name = f"Functional Tests - copy letter template - {uuid.uuid4()}"
    create_letter_template(driver, name=template_name, content=content)

    # Confirm letter template was created
    go_to_templates_page(driver)
    templates_page = ShowTemplatesPage(driver)
    assert templates_page.get_h1_text() == "Templates"
    assert template_name in templates_page.get_all_listed_templates()

    # Copy letter template
    view_template_page = ViewLetterTemplatePage(driver)
    new_template_name = copy_an_existing_template(
        driver, template_name, templates_page, view_template_page, notification_type="letter"
    )

    # Confirm new copy of letter template was created
    go_to_templates_page(driver)
    assert templates_page.get_h1_text() == "Templates"
    assert new_template_name in templates_page.get_all_listed_templates()

    # Delete created letter templates
    templates_page.click_template_by_link_text(new_template_name)
    delete_template_from_view_template_page(driver, new_template_name, view_template_page)
    templates_page.click_template_by_link_text(template_name)
    assert view_template_page.get_h1_text() == template_name
    delete_template_from_view_template_page(driver, template_name, view_template_page)


def copy_an_existing_template(driver, template_name, templates_page, view_template_page, notification_type):
    templates_page.click_add_new_template()
    templates_page.select_copy_an_existing_template()
    choose_existing_template_page = ChooseExistingTemplatePage(driver)
    assert choose_existing_template_page.get_h1_text() == "Choose an existing template to copy"
    choose_existing_template_page.click_template_by_link_text(template_name)
    copy_existing_template_page = CopyExistingTemplatePage(driver)
    assert copy_existing_template_page.get_h1_text() == "Copy an existing template"
    new_template_name = f"Functional Tests - new copied {notification_type} template - {uuid.uuid4()}"
    copy_existing_template_page.change_template_name(new_template_name)
    copy_existing_template_page.click_copy_this_template_button()
    assert view_template_page.get_h1_text() == new_template_name
    return new_template_name
