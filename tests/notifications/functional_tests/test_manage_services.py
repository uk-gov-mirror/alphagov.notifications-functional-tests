import uuid

from config import config
from tests.pages import AddServicePage, DashboardPage, YourServicesPage
from tests.test_utils import delete_service, recordtime


@recordtime
def test_select_live_service_from_list(driver, login_seeded_user):
    your_services_page = YourServicesPage(driver)
    dashboard_page = DashboardPage(driver)

    your_services_page.get(url=your_services_page.base_url + "/your-services")

    target_service_name = config["service"]["name"]

    your_services_page.go_to_service(target_service_name)
    assert dashboard_page.get_service_name() == target_service_name


@recordtime
def test_create_and_select_trial_service_from_list(driver, login_seeded_user):
    your_services_page = YourServicesPage(driver)
    add_service_page = AddServicePage(driver)
    dashboard_page = DashboardPage(driver)

    your_services_page.get(url=your_services_page.base_url + "/your-services")
    your_services_page.add_new_service()

    add_service_page.wait_until_current()
    add_service_page.click_trial_page_continue__button()
    add_service_page.wait_until_name_service_page()

    trial_service_name = f"Trial Service {uuid.uuid4()}"
    add_service_page.add_service(trial_service_name)

    try:
        assert dashboard_page.get_service_name() == trial_service_name

        your_services_page.get(url=your_services_page.base_url + "/your-services")
        your_services_page.wait_until_current()

        your_services_page.go_to_service(trial_service_name)

        assert dashboard_page.get_service_name() == trial_service_name

    finally:
        delete_service(driver)
