from page_objects import *


class TestsPage:

    def test_register_page_external(self, driver):
        """Тест только валидными данными - Регистрация нового пользователя"""
        register_page = RegisterPage(driver)
        register_page.open(register_page.PATH)
        register_page.register()
        result_text_success_register = register_page.page_creat_account()
        assert f'{result_text_success_register}' == 'Your Account Has Been Created!'

    def test_main_page(self, driver):
        """Переключение валют из верхнего меню опенкарта"""
        main_page = MainPage(driver)
        main_page.open(main_page.PATH)
        list_currency = ["$ US Dollar", "£ Pound Sterling", "€ Euro"]
        random_currency = main_page.choose_currency()
        assert random_currency in list_currency

    def test_add_new_product(self, driver):
        """Добавление нового товара в разделе администратора"""
        admin_page = AdminPage(driver)
        admin_page.open(admin_page.PATH)
        admin_page.login("user", 'bitnami')
        admin_page.choose_element_catalog_menu()
        product = admin_page.add_new_product()
        result_pr = admin_page.form_result()
        assert product in result_pr

    def test_del_new_product(self, driver):
        """Удаление товара из списка в разделе администартора"""
        admin_page = AdminPage(driver)
        admin_page.open(admin_page.PATH)
        admin_page.login("user", 'bitnami')
        admin_page.choose_element_catalog_menu()
        admin_page.serch_product('last iPhone')
        name_del_product = admin_page.del_product()
        assert name_del_product == "No results!"
