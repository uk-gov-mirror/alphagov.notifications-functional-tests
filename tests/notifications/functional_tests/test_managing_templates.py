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
    go_to_templates_page,
    recordtime,
)


@recordtime
@pytest.mark.parametrize(
    "template_type, view_class_name",
    [("email", ViewEmailTemplatePage), ("sms", ViewSMSTemplatePage), ("letter", ViewLetterTemplatePage)],
)
def test_copying_an_existing_template(driver, login_seeded_user, template_type, view_class_name):
    go_to_templates_page(driver)
    content = "This is a test template"

    # Create a template
    template_name = f"Functional Tests - copy email template - {uuid.uuid4()}"
    create_email_template(driver, name=template_name, content=content)

    # Confirm template was created
    go_to_templates_page(driver)
    templates_page = ShowTemplatesPage(driver)
    assert templates_page.get_h1_text() == "Templates"
    assert template_name in templates_page.get_all_listed_templates()

    # Copy an existing template
    view_template_page = view_class_name(driver)
    templates_page.click_add_new_template()
    templates_page.select_copy_an_existing_template()
    choose_existing_template_page = ChooseExistingTemplatePage(driver)
    assert choose_existing_template_page.get_h1_text() == "Choose an existing template to copy"
    choose_existing_template_page.click_template_by_link_text(template_name)
    copy_existing_template_page = CopyExistingTemplatePage(driver)
    assert copy_existing_template_page.get_h1_text() == "Copy an existing template"
    new_template_name = f"Functional Tests - new copied {template_type} template - {uuid.uuid4()}"
    copy_existing_template_page.change_template_name(new_template_name)
    copy_existing_template_page.click_copy_this_template_button()
    assert view_template_page.get_h1_text() == new_template_name

    # Confirm new copy of the template was created
    go_to_templates_page(driver)
    assert templates_page.get_h1_text() == "Templates"
    assert new_template_name in templates_page.get_all_listed_templates()

    # Delete templates created during test run
    templates_page.click_template_by_link_text(new_template_name)
    delete_template_from_view_template_page(driver, new_template_name, view_template_page)
    templates_page.click_template_by_link_text(template_name)
    assert view_template_page.get_h1_text() == template_name
    delete_template_from_view_template_page(driver, template_name, view_template_page)
