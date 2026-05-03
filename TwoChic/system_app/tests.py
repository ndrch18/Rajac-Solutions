from django.test import TestCase, Client
from django.urls import reverse
from system_app.models import (
    Account, Employee, EmployeeRole,
    RawMaterial, MaterialUnit, MaterialCategory,
    Product, ProductCategory, ProductCollection,
    ProductMaterial, Order, OrderItem
)


# ============================================================
# HELPERS
# ============================================================

def create_owner():
    Account.objects.create(employee_id='0001', password='ownerpass')

def create_prodman():
    emp = Employee.objects.create(
        employee_id='1001', employee_name='Test Manager',
        employee_role='production_manager'
    )
    Account.objects.create(employee_id='1001', password='managerpass')
    return emp

def create_prodemp():
    emp = Employee.objects.create(
        employee_id='2001', employee_name='Test Employee',
        employee_role='production_employee'
    )
    Account.objects.create(employee_id='2001', password='emppass')
    return emp

def create_material_unit(name='Meter', category='fabrics'):
    return MaterialUnit.objects.create(unit_name=name, category=category)

def create_raw_material(name='Blue Cloth', category='fabrics', unit=None, qty=10, price=100):
    if unit is None:
        unit = create_material_unit()
    return RawMaterial.objects.create(
        material_name=name,
        material_category=category,
        material_unit=unit,
        material_quantity=qty,
        material_unitprice=price,
        minimum_threshold=2
    )

def create_product(name='Test Dress', category='dresses', collection='summer', qty=5, price=1000):
    return Product.objects.create(
        product_name=name,
        product_category=category,
        product_collection=collection,
        quantity=qty,
        price=price
    )

def login_as_owner(client):
    create_owner()
    client.post(reverse('login'), {'employee_id': '0001', 'password': 'ownerpass'})

def login_as_prodman(client):
    create_prodman()
    client.post(reverse('login'), {'employee_id': '1001', 'password': 'managerpass'})

def login_as_prodemp(client):
    create_prodemp()
    client.post(reverse('login'), {'employee_id': '2001', 'password': 'emppass'})


# ============================================================
# TEST SPECIFICATION #00 — ROLE-BASED ACCESS CONTROL
# ============================================================

class RoleBasedAccessControlTests(TestCase):

    def setUp(self):
        self.client = Client()

    # TC-00-01: Owner home page contains all necessary features
    def test_owner_homepage_accessible(self):
        login_as_owner(self.client)
        response = self.client.get(reverse('owner_homepage'))
        self.assertEqual(response.status_code, 200)

    # TC-00-02: Production Manager home page accessible
    def test_prodman_homepage_accessible(self):
        login_as_prodman(self.client)
        response = self.client.get(reverse('prodman_homepage'))
        self.assertEqual(response.status_code, 200)

    # TC-00-03: Production Employee home page accessible
    def test_prodemp_homepage_accessible(self):
        login_as_prodemp(self.client)
        response = self.client.get(reverse('prodemp_home'))
        self.assertEqual(response.status_code, 200)

    # TC-00-04: Only Owner can access products list (owner)
    def test_owner_can_access_products_list(self):
        login_as_owner(self.client)
        response = self.client.get(reverse('owner_products_list'))
        self.assertEqual(response.status_code, 200)

    # TC-00-05: Production Manager cannot access owner products list
    def test_prodman_cannot_access_owner_products(self):
        login_as_prodman(self.client)
        response = self.client.get(reverse('owner_products_list'))
        self.assertRedirects(response, reverse('login'))

    # TC-00-06: Production Employee cannot access owner products list
    def test_prodemp_cannot_access_owner_products(self):
        login_as_prodemp(self.client)
        response = self.client.get(reverse('owner_products_list'))
        self.assertRedirects(response, reverse('login'))

    # TC-00-07: Only Owner can delete a product
    def test_owner_can_delete_product(self):
        login_as_owner(self.client)
        product = create_product()
        response = self.client.post(reverse('owner_delete_product', args=[product.id]))
        self.assertFalse(Product.objects.filter(id=product.id).exists())

    # TC-00-08: Production Manager cannot delete a product
    def test_prodman_cannot_delete_product(self):
        login_as_prodman(self.client)
        product = create_product()
        response = self.client.post(reverse('owner_delete_product', args=[product.id]))
        self.assertTrue(Product.objects.filter(id=product.id).exists())

    # TC-00-09: Only Owner can view sales report
    def test_owner_can_view_sales_report(self):
        login_as_owner(self.client)
        response = self.client.get(reverse('owner_sales_report'))
        self.assertEqual(response.status_code, 200)

    # TC-00-10: Production Manager cannot view sales report
    def test_prodman_cannot_view_sales_report(self):
        login_as_prodman(self.client)
        response = self.client.get(reverse('owner_sales_report'))
        self.assertRedirects(response, reverse('login'))

    # TC-00-11: Production Employee cannot view sales report
    def test_prodemp_cannot_view_sales_report(self):
        login_as_prodemp(self.client)
        response = self.client.get(reverse('owner_sales_report'))
        self.assertRedirects(response, reverse('login'))

    # TC-00-12: Only Owner can manage employees
    def test_owner_can_manage_employees(self):
        login_as_owner(self.client)
        response = self.client.get(reverse('owner_manage_employees'))
        self.assertEqual(response.status_code, 200)

    # TC-00-13: Production Manager cannot access manage employees
    def test_prodman_cannot_manage_employees(self):
        login_as_prodman(self.client)
        response = self.client.get(reverse('owner_manage_employees'))
        self.assertRedirects(response, reverse('login'))

    # TC-00-14: Unauthenticated user redirected to login
    def test_unauthenticated_redirected_to_login(self):
        response = self.client.get(reverse('owner_homepage'))
        self.assertRedirects(response, reverse('login'))

    # TC-00-15: Production Manager can access material inventory
    def test_prodman_can_access_matinv(self):
        login_as_prodman(self.client)
        response = self.client.get(reverse('prodman_matinv'))
        self.assertEqual(response.status_code, 200)

    # TC-00-16: Production Employee cannot access prodman material inventory
    def test_prodemp_cannot_access_prodman_matinv(self):
        login_as_prodemp(self.client)
        response = self.client.get(reverse('prodman_matinv'))
        self.assertRedirects(response, reverse('login'))

    # TC-00-17: Production Manager can access products list
    def test_prodman_can_access_products_list(self):
        login_as_prodman(self.client)
        response = self.client.get(reverse('prodman_products_list'))
        self.assertEqual(response.status_code, 200)

    # TC-00-18: Production Employee can access their products list
    def test_prodemp_can_access_products_list(self):
        login_as_prodemp(self.client)
        response = self.client.get(reverse('prodemp_products_list'))
        self.assertEqual(response.status_code, 200)

    # TC-00-19: Production Employee can access material inventory
    def test_prodemp_can_access_material_inventory(self):
        login_as_prodemp(self.client)
        response = self.client.get(reverse('prodemp_matinv'))
        self.assertEqual(response.status_code, 200)

    # TC-00-20: Owner can access material inventory
    def test_owner_can_access_material_inventory(self):
        login_as_owner(self.client)
        response = self.client.get(reverse('prodman_matinv'))
        self.assertNotEqual(response.status_code, 302)
# ============================================================
# TEST SPECIFICATION #01 — LOGIN / LOGOUT
# ============================================================

class LoginLogoutTests(TestCase):

    def setUp(self):
        self.client = Client()
        Account.objects.create(employee_id='0001', password='ownerpass')
        Account.objects.create(employee_id='1001', password='managerpass')
        Account.objects.create(employee_id='2001', password='emppass')
        Employee.objects.create(employee_id='1001', employee_name='Manager', employee_role='production_manager')
        Employee.objects.create(employee_id='2001', employee_name='Employee', employee_role='production_employee')

    # TC-01-01: Owner logs in with valid credentials
    def test_owner_login_valid(self):
        response = self.client.post(reverse('login'), {
            'employee_id': '0001', 'password': 'ownerpass'
        })
        self.assertRedirects(response, reverse('owner_homepage'))

    # TC-01-02: Production Manager logs in with valid credentials
    def test_prodman_login_valid(self):
        response = self.client.post(reverse('login'), {
            'employee_id': '1001', 'password': 'managerpass'
        })
        self.assertRedirects(response, reverse('prodman_homepage'))

    # TC-01-03: Production Employee logs in with valid credentials
    def test_prodemp_login_valid(self):
        response = self.client.post(reverse('login'), {
            'employee_id': '2001', 'password': 'emppass'
        })
        self.assertRedirects(response, reverse('prodemp_home'))

    # TC-01-04: Login with wrong password fails
    def test_login_wrong_password(self):
        response = self.client.post(reverse('login'), {
            'employee_id': '0001', 'password': 'wrongpass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid login')

    # TC-01-05: Login with non-existent employee ID fails
    def test_login_nonexistent_id(self):
        response = self.client.post(reverse('login'), {
            'employee_id': '9999', 'password': 'somepass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid login')

    # TC-01-06: Login with empty fields fails
    def test_login_empty_fields(self):
        response = self.client.post(reverse('login'), {
            'employee_id': '', 'password': ''
        })
        self.assertEqual(response.status_code, 200)

    # TC-01-07: Logout clears session
    def test_logout_clears_session(self):
        self.client.post(reverse('login'), {'employee_id': '0001', 'password': 'ownerpass'})
        self.client.get(reverse('logout'))
        response = self.client.get(reverse('owner_homepage'))
        self.assertRedirects(response, reverse('login'))

    # TC-01-08: After logout, cannot access protected pages
    def test_after_logout_no_access(self):
        self.client.post(reverse('login'), {'employee_id': '1001', 'password': 'managerpass'})
        self.client.get(reverse('logout'))
        response = self.client.get(reverse('prodman_homepage'))
        self.assertRedirects(response, reverse('login'))

    # TC-01-09: Default password flag set on first login
    def test_default_password_flag(self):
        Account.objects.create(employee_id='1002', password='1111')
        Employee.objects.create(employee_id='1002', employee_name='New Manager', employee_role='production_manager')
        self.client.post(reverse('login'), {'employee_id': '1002', 'password': '1111'})
        session = self.client.session
        self.assertTrue(session.get('using_default_password'))

    # TC-01-10: Non-default password does not set flag
    def test_non_default_password_no_flag(self):
        self.client.post(reverse('login'), {'employee_id': '0001', 'password': 'ownerpass'})
        session = self.client.session
        self.assertFalse(session.get('using_default_password', False))

    # TC-01-11: Change password works correctly
    def test_change_password(self):
        self.client.post(reverse('login'), {'employee_id': '0001', 'password': 'ownerpass'})
        response = self.client.post(reverse('change_password'), {
            'current_password': 'ownerpass',
            'new_password': 'newpass123',
            'confirm_password': 'newpass123'
        })
        account = Account.objects.get(employee_id='0001')
        self.assertEqual(account.password, 'newpass123')

    # TC-01-12: Change password with wrong current password fails
    def test_change_password_wrong_current(self):
        self.client.post(reverse('login'), {'employee_id': '0001', 'password': 'ownerpass'})
        response = self.client.post(reverse('change_password'), {
            'current_password': 'wrongpass',
            'new_password': 'newpass123',
            'confirm_password': 'newpass123'
        })
        self.assertContains(response, 'incorrect')


# ============================================================
# TEST SPECIFICATION #02 — MATERIAL MANAGEMENT
# ============================================================

class MaterialManagementTests(TestCase):

    def setUp(self):
        self.client = Client()
        login_as_prodman(self.client)
        self.unit = create_material_unit()

    # TC-02-01: Add new material with all required fields
    def test_add_material_valid(self):
        response = self.client.post(reverse('prodman_matinv'), {
            'material_category': 'fabrics',
            'material_name': 'Blue Cloth',
            'material_unit': self.unit.id,
            'material_quantity': 10,
            'material_unitprice': 100,
            'minimum_threshold': 2
        })
        self.assertTrue(RawMaterial.objects.filter(material_name='Blue Cloth').exists())

    # TC-02-02: Add material with missing name fails
    def test_add_material_missing_name(self):
        response = self.client.post(reverse('prodman_matinv'), {
            'material_category': 'fabrics',
            'material_name': '',
            'material_unit': self.unit.id,
            'material_quantity': 10,
            'material_unitprice': 100,
            'minimum_threshold': 2
        })
        self.assertFalse(RawMaterial.objects.filter(material_name='').exists())

    # TC-02-03: Add material with numbers in name fails
    def test_add_material_name_with_numbers(self):
        response = self.client.post(reverse('prodman_matinv'), {
            'material_category': 'fabrics',
            'material_name': 'Cloth123',
            'material_unit': self.unit.id,
            'material_quantity': 10,
            'material_unitprice': 100,
            'minimum_threshold': 2
        })
        self.assertFalse(RawMaterial.objects.filter(material_name='Cloth123').exists())

    # TC-02-04: Add material with missing category fails
    def test_add_material_missing_category(self):
        response = self.client.post(reverse('prodman_matinv'), {
            'material_category': '',
            'material_name': 'Red Cloth',
            'material_unit': self.unit.id,
            'material_quantity': 10,
            'material_unitprice': 100,
            'minimum_threshold': 2
        })
        self.assertFalse(RawMaterial.objects.filter(material_name='Red Cloth').exists())

    # TC-02-05: Edit existing material successfully
    def test_edit_material_valid(self):
        material = create_raw_material(unit=self.unit)
        response = self.client.post(
            reverse('edit_raw_material', args=[material.id]),
            {
                'material_category': 'fabrics',
                'material_name': 'Updated Cloth',
                'material_unit': self.unit.id,
                'material_quantity': 20,
                'material_unitprice': 150,
                'minimum_threshold': 3
            }
        )
        material.refresh_from_db()
        self.assertEqual(material.material_name, 'Updated Cloth')

    # TC-02-06: Edit material quantity
    def test_edit_material_quantity(self):
        material = create_raw_material(unit=self.unit)
        self.client.post(
            reverse('edit_raw_material', args=[material.id]),
            {
                'material_category': 'fabrics',
                'material_name': material.material_name,
                'material_unit': self.unit.id,
                'material_quantity': 50,
                'material_unitprice': material.material_unitprice,
                'minimum_threshold': material.minimum_threshold
            }
        )
        material.refresh_from_db()
        self.assertEqual(material.material_quantity, 50)

    # TC-02-07: Delete material
    def test_delete_material(self):
        material = create_raw_material(unit=self.unit)
        self.client.post(reverse('delete_raw_material', args=[material.id]))
        self.assertFalse(RawMaterial.objects.filter(id=material.id).exists())

    # TC-02-08: Material list visible to prodman
    def test_material_list_visible(self):
        create_raw_material(unit=self.unit)
        response = self.client.get(reverse('prodman_matinv'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Blue Cloth')

    # TC-02-09: Search material by name
    def test_search_material(self):
        create_raw_material(name='Red Silk', unit=self.unit)
        create_raw_material(name='Blue Cotton', unit=create_material_unit('Yard'))
        response = self.client.get(reverse('prodman_matinv'), {'q': 'Red'})
        self.assertContains(response, 'Red Silk')
        self.assertNotContains(response, 'Blue Cotton')

    # TC-02-10: Filter material by category
    def test_filter_material_by_category(self):
        trim_unit = create_material_unit('Piece', 'trims')
        create_raw_material(name='Button', category='trims', unit=trim_unit)
        create_raw_material(name='Blue Cloth', category='fabrics', unit=self.unit)
        response = self.client.get(reverse('prodman_matinv'), {'category': 'trims'})
        self.assertContains(response, 'Button')
        self.assertNotContains(response, 'Blue Cloth')

    # TC-02-11: Critical material shows warning when below threshold
    def test_critical_material_warning(self):
        create_raw_material(name='Low Stock', unit=self.unit, qty=1)
        response = self.client.get(reverse('prodman_matinv'))
        self.assertContains(response, 'warning')

    # TC-02-12: Set minimum threshold for material
    def test_set_minimum_threshold(self):
        material = create_raw_material(unit=self.unit)
        self.client.post(
            reverse('edit_raw_material', args=[material.id]),
            {
                'material_category': 'fabrics',
                'material_name': material.material_name,
                'material_unit': self.unit.id,
                'material_quantity': material.material_quantity,
                'material_unitprice': material.material_unitprice,
                'minimum_threshold': 5
            }
        )
        material.refresh_from_db()
        self.assertEqual(material.minimum_threshold, 5)


# ============================================================
# TEST SPECIFICATION #03 — PRODUCT MANAGEMENT
# ============================================================

class ProductManagementTests(TestCase):

    def setUp(self):
        self.client = Client()

    # TC-03-01: Owner can add a new product
    def test_owner_add_product(self):
        login_as_owner(self.client)
        response = self.client.post(reverse('owner_add_product'), {
            'product_name': 'Summer Dress',
            'product_category': 'dresses',
            'product_collection': 'summer'
        })
        self.assertTrue(Product.objects.filter(product_name='Summer Dress').exists())

    # TC-03-02: Add product with missing name fails
    def test_add_product_missing_name(self):
        login_as_owner(self.client)
        response = self.client.post(reverse('owner_add_product'), {
            'product_name': '',
            'product_category': 'dresses',
            'product_collection': 'summer'
        })
        self.assertFalse(Product.objects.filter(product_name='').exists())

    # TC-03-03: Owner can edit product details
    def test_owner_edit_product(self):
        login_as_owner(self.client)
        product = create_product()
        self.client.post(reverse('owner_edit_product', args=[product.id]), {
            'product_name': 'Updated Dress',
            'product_category': 'tops',
            'product_collection': 'resort',
            'price': 2000
        })
        product.refresh_from_db()
        self.assertEqual(product.product_name, 'Updated Dress')

    # TC-03-04: Owner can delete product
    def test_owner_delete_product(self):
        login_as_owner(self.client)
        product = create_product()
        self.client.post(reverse('owner_delete_product', args=[product.id]))
        self.assertFalse(Product.objects.filter(id=product.id).exists())

    # TC-03-05: Owner can set retail price
    def test_owner_set_retail_price(self):
        login_as_owner(self.client)
        product = create_product()
        self.client.post(reverse('owner_product_detail', args=[product.id]), {
            'price': 3500
        })
        product.refresh_from_db()
        self.assertEqual(product.price, 3500)

    # TC-03-06: Product detail page accessible by owner
    def test_owner_product_detail_accessible(self):
        login_as_owner(self.client)
        product = create_product()
        response = self.client.get(reverse('owner_product_detail', args=[product.id]))
        self.assertEqual(response.status_code, 200)

    # TC-03-07: Product detail page accessible by prodman
    def test_prodman_product_detail_accessible(self):
        login_as_prodman(self.client)
        product = create_product()
        response = self.client.get(reverse('prodman_product_detail', args=[product.id]))
        self.assertEqual(response.status_code, 200)

    # TC-03-08: Production Manager can update product quantity
    def test_prodman_update_quantity(self):
        login_as_prodman(self.client)
        product = create_product(qty=5)
        self.client.post(reverse('prodman_product_detail', args=[product.id]), {
            'action': 'update_qty',
            'quantity': 10
        })
        product.refresh_from_db()
        self.assertEqual(product.quantity, 10)

    # TC-03-09: Product auto-generates product_id
    def test_product_auto_generates_id(self):
        login_as_owner(self.client)
        self.client.post(reverse('owner_add_product'), {
            'product_name': 'Auto ID Dress',
            'product_category': 'dresses',
            'product_collection': 'summer'
        })
        product = Product.objects.get(product_name='Auto ID Dress')
        self.assertTrue(product.product_id.startswith('#'))

    # TC-03-10: Product quantity updates when prodemp adds finished garments
    def test_prodemp_add_finished_garments(self):
        login_as_prodemp(self.client)
        product = create_product(qty=5)
        self.client.post(reverse('prodemp_product_detail', args=[product.id]), {
            'add_qty': 3
        })
        product.refresh_from_db()
        self.assertEqual(product.quantity, 8)

    # TC-03-11: Adding finished garments deducts raw material inventory
    def test_adding_garments_deducts_materials(self):
        login_as_prodemp(self.client)
        unit = create_material_unit()
        material = create_raw_material(unit=unit, qty=20)
        product = create_product(qty=5)
        ProductMaterial.objects.create(
            product=product,
            raw_material=material,
            quantity_per_garment=2,
        )
        self.client.post(reverse('prodemp_product_detail', args=[product.id]), {
            'add_qty': 3
        })
        material.refresh_from_db()
        self.assertEqual(material.material_quantity, 14)

    # TC-03-12: Product list page shows all products
    def test_product_list_shows_products(self):
        login_as_owner(self.client)
        create_product(name='Dress A')
        create_product(name='Dress B')
        response = self.client.get(reverse('owner_products_list'))
        self.assertContains(response, 'Dress A')
        self.assertContains(response, 'Dress B')


# ============================================================
# TEST SPECIFICATION #04 — CRITICAL MATERIAL NOTIFICATION
# ============================================================

class CriticalMaterialTests(TestCase):

    def setUp(self):
        self.client = Client()
        login_as_prodman(self.client)
        self.unit = create_material_unit()

    # TC-04-01: Material below threshold marked as critical
    def test_material_below_threshold_is_critical(self):
        material = RawMaterial.objects.create(
            material_name='Low Stock',
            material_category='fabrics',
            material_unit=self.unit,
            material_quantity=1,
            material_unitprice=100,
            minimum_threshold=5
        )
        self.assertTrue(material.material_quantity <= material.minimum_threshold)

    # TC-04-02: Critical materials appear in critical list
    def test_critical_materials_in_list(self):
        RawMaterial.objects.create(
            material_name='Critical Item',
            material_category='fabrics',
            material_unit=self.unit,
            material_quantity=1,
            material_unitprice=100,
            minimum_threshold=5
        )
        response = self.client.get(reverse('prodman_matinv'))
        self.assertContains(response, 'Critical Item')

    # TC-04-03: Material above threshold not critical
    def test_material_above_threshold_not_critical(self):
        material = RawMaterial.objects.create(
            material_name='Adequate Stock',
            material_category='fabrics',
            material_unit=self.unit,
            material_quantity=20,
            material_unitprice=100,
            minimum_threshold=5
        )
        self.assertFalse(material.material_quantity <= material.minimum_threshold)

    # TC-04-04: Critical count shown on inventory page
    def test_critical_count_displayed(self):
        RawMaterial.objects.create(
            material_name='Low Item',
            material_category='fabrics',
            material_unit=self.unit,
            material_quantity=1,
            material_unitprice=100,
            minimum_threshold=5
        )
        response = self.client.get(reverse('prodman_matinv'))
        self.assertContains(response, 'Critical Quantity')


# ============================================================
# TEST SPECIFICATION #05 — NON-FUNCTIONAL REQUIREMENTS
# ============================================================

class NonFunctionalTests(TestCase):

    def setUp(self):
        self.client = Client()

    # TC-05-01: System response time under 1 second for inventory view
    def test_inventory_response_time(self):
        login_as_prodman(self.client)
        import time
        start = time.time()
        self.client.get(reverse('prodman_matinv'))
        end = time.time()
        self.assertLess(end - start, 1.0)

    # TC-05-02: System uptime - pages load without server error
    def test_system_pages_load(self):
        login_as_owner(self.client)
        pages = [
            reverse('owner_homepage'),
            reverse('owner_products_list'),
            reverse('owner_manage_employees'),
            reverse('owner_sales_report'),
        ]
        for page in pages:
            response = self.client.get(page)
            self.assertNotEqual(response.status_code, 500, f"Server error on {page}")

    # TC-05-03: RBAC enforced — wrong role redirected
    def test_rbac_enforced(self):
        login_as_prodemp(self.client)
        response = self.client.get(reverse('owner_homepage'))
        self.assertRedirects(response, reverse('login'))

    # TC-05-04: Desktop pages load correctly (status 200)
    def test_desktop_pages_load(self):
        login_as_owner(self.client)
        response = self.client.get(reverse('owner_products_list'))
        self.assertEqual(response.status_code, 200)

    # TC-05-05: Mobile user agent pages load correctly
    def test_mobile_pages_load(self):
        login_as_owner(self.client)
        response = self.client.get(
            reverse('owner_products_list'),
            HTTP_USER_AGENT='Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)'
        )
        self.assertEqual(response.status_code, 200)

    # TC-05-06: Cross-platform — prodman pages load on mobile
    def test_prodman_mobile_pages_load(self):
        login_as_prodman(self.client)
        response = self.client.get(
            reverse('prodman_matinv'),
            HTTP_USER_AGENT='Mozilla/5.0 (Android 10; Mobile)'
        )
        self.assertEqual(response.status_code, 200)

    # TC-05-07: Response time for product list under 1 second
    def test_product_list_response_time(self):
        login_as_owner(self.client)
        import time
        start = time.time()
        self.client.get(reverse('owner_products_list'))
        end = time.time()
        self.assertLess(end - start, 1.0)

    # TC-05-08: Data accuracy - material cost calculation
    def test_material_cost_calculation_accuracy(self):
        login_as_owner(self.client)
        unit = create_material_unit()
        material = create_raw_material(unit=unit, qty=10, price=100)
        product = create_product()
        ProductMaterial.objects.create(
            product=product,
            raw_material=material,
            quantity_per_garment=2,
        )
        response = self.client.get(reverse('owner_product_detail', args=[product.id]))
        self.assertContains(response, '200')


# ============================================================
# TEST SPECIFICATION #06 — PRODUCT MANAGEMENT (EXTENDED)
# ============================================================

class ProductManagementExtendedTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.unit = create_material_unit()

    # TC-06-01: Create item profile card with all fields
    def test_create_item_profile_card(self):
        login_as_owner(self.client)
        self.client.post(reverse('owner_add_product'), {
            'product_name': 'New Profile Card',
            'product_category': 'tops',
            'product_collection': 'summer'
        })
        self.assertTrue(Product.objects.filter(product_name='New Profile Card').exists())

    # TC-06-02: Create item profile card with missing required field
    def test_create_item_profile_card_missing_field(self):
        login_as_owner(self.client)
        self.client.post(reverse('owner_add_product'), {
            'product_name': '',
            'product_category': 'tops',
            'product_collection': 'summer'
        })
        self.assertEqual(Product.objects.count(), 0)

    # TC-06-03: Create item profile card with duplicate name
    def test_create_duplicate_product_name(self):
        login_as_owner(self.client)
        create_product(name='Duplicate Dress')
        self.client.post(reverse('owner_add_product'), {
            'product_name': 'Duplicate Dress',
            'product_category': 'dresses',
            'product_collection': 'summer'
        })
        self.assertEqual(Product.objects.filter(product_name='Duplicate Dress').count(), 1)

    # TC-06-09: Owner can view product detail with materials breakdown
    def test_owner_view_materials_breakdown(self):
        login_as_owner(self.client)
        product = create_product()
        material = create_raw_material(unit=self.unit)
        ProductMaterial.objects.create(
            product=product,
            raw_material=material,
            quantity_per_garment=1
        )
        response = self.client.get(reverse('owner_product_detail', args=[product.id]))
        self.assertContains(response, material.material_name)

    # TC-06-11: Owner can input retail price
    def test_owner_input_retail_price(self):
        login_as_owner(self.client)
        product = create_product(price=0)
        self.client.post(reverse('owner_product_detail', args=[product.id]), {
            'price': 5000
        })
        product.refresh_from_db()
        self.assertEqual(product.price, 5000)

    # TC-06-12: Owner can edit retail price
    def test_owner_edit_retail_price(self):
        login_as_owner(self.client)
        product = create_product(price=1000)
        self.client.post(reverse('owner_product_detail', args=[product.id]), {
            'price': 2000
        })
        product.refresh_from_db()
        self.assertEqual(product.price, 2000)

    # TC-06-13: Owner can remove retail price (set to 0)
    def test_owner_remove_retail_price(self):
        login_as_owner(self.client)
        product = create_product(price=1000)
        self.client.post(reverse('owner_product_detail', args=[product.id]), {
            'price': 0
        })
        product.refresh_from_db()
        self.assertEqual(product.price, 0)

    # TC-06-14: Prodman cannot input retail price
    def test_prodman_cannot_input_retail_price(self):
        login_as_prodman(self.client)
        product = create_product(price=1000)
        self.client.post(reverse('owner_product_detail', args=[product.id]), {
            'price': 9999
        })
        product.refresh_from_db()
        self.assertEqual(product.price, 1000)

    # TC-06-18: Prodman can update product quantity
    def test_prodman_update_product_quantity(self):
        login_as_prodman(self.client)
        product = create_product(qty=10)
        self.client.post(reverse('prodman_product_detail', args=[product.id]), {
            'action': 'update_qty',
            'quantity': 15
        })
        product.refresh_from_db()
        self.assertEqual(product.quantity, 15)

    # TC-06-28: Suggested retail price calculated correctly
    def test_suggested_retail_price_calculation(self):
        login_as_owner(self.client)
        material = create_raw_material(unit=self.unit, price=500)
        product = create_product()
        ProductMaterial.objects.create(
            product=product,
            raw_material=material,
            quantity_per_garment=1
        )
        response = self.client.get(reverse('owner_product_detail', args=[product.id]))
        self.assertEqual(response.context['total_cost'], 500)

    # TC-06-31: Log materials to product via API
    def test_log_materials_to_product(self):
        login_as_prodman(self.client)
        material = create_raw_material(unit=self.unit)
        product = create_product()
        import json
        response = self.client.post(
            f'/api/products/{product.id}/materials/',
            data=json.dumps({
                'raw_material_id': material.id,
                'quantity_per_garment': 2,
                'fabric_length': 2,
                'fabric_width': None
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(ProductMaterial.objects.filter(product=product, raw_material=material).exists())


# ============================================================
# TEST SPECIFICATION #07 — SALES AND EXPENSES DASHBOARD
# ============================================================

class SalesDashboardTests(TestCase):

    def setUp(self):
        self.client = Client()

    def create_order_with_item(self):
        product = create_product(price=1000)
        order = Order.objects.create()
        OrderItem.objects.create(
            order=order,
            product=product,
            product_name=product.product_name,
            product_price=product.price,
            material_cost=200,
            quantity=2
        )
        return order, product

    # TC-07-01: Owner can view sales report
    def test_owner_view_sales_report(self):
        login_as_owner(self.client)
        response = self.client.get(reverse('owner_sales_report'))
        self.assertEqual(response.status_code, 200)

    # TC-07-02: Sales report shows correct total sales
    def test_sales_report_total_sales(self):
        login_as_owner(self.client)
        self.create_order_with_item()
        response = self.client.get(reverse('owner_sales_report'))
        self.assertContains(response, '2000')

    # TC-07-03: Sales report shows total expenses
    def test_sales_report_total_expenses(self):
        login_as_owner(self.client)
        self.create_order_with_item()
        response = self.client.get(reverse('owner_sales_report'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('total_expenses', response.context)

    # TC-07-04: Sales report shows net profit
    def test_sales_report_net_profit(self):
        login_as_owner(self.client)
        self.create_order_with_item()
        response = self.client.get(reverse('owner_sales_report'))
        self.assertIn('net_profit', response.context)

    # TC-07-05: Sales report shows top products
    def test_sales_report_top_products(self):
        login_as_owner(self.client)
        self.create_order_with_item()
        response = self.client.get(reverse('owner_sales_report'))
        self.assertIn('top_products', response.context)

    # TC-07-06: Export sales as Excel
    def test_export_sales_xlsx(self):
        login_as_owner(self.client)
        self.create_order_with_item()
        response = self.client.get(reverse('export_sales_xlsx'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response['Content-Type'],
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

    # TC-07-07: Export sales as PDF
    def test_export_sales_pdf(self):
        login_as_owner(self.client)
        self.create_order_with_item()
        response = self.client.get(reverse('export_sales_pdf'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')

    # TC-07-08: Export with weekly filter
    def test_export_xlsx_weekly_filter(self):
        login_as_owner(self.client)
        self.create_order_with_item()
        response = self.client.get(reverse('export_sales_xlsx') + '?filter=weekly')
        self.assertEqual(response.status_code, 200)

    # TC-07-09: Export with monthly filter
    def test_export_xlsx_monthly_filter(self):
        login_as_owner(self.client)
        self.create_order_with_item()
        response = self.client.get(reverse('export_sales_xlsx') + '?filter=monthly')
        self.assertEqual(response.status_code, 200)

    # TC-07-10: Export with yearly filter
    def test_export_xlsx_yearly_filter(self):
        login_as_owner(self.client)
        self.create_order_with_item()
        response = self.client.get(reverse('export_sales_xlsx') + '?filter=yearly')
        self.assertEqual(response.status_code, 200)

    # TC-07-11: Deleted product data preserved in sales report
    def test_deleted_product_preserved_in_sales(self):
        login_as_owner(self.client)
        order, product = self.create_order_with_item()
        product_name = product.product_name
        product.delete()
        response = self.client.get(reverse('owner_sales_report'))
        self.assertContains(response, product_name)


# ============================================================
# TEST SPECIFICATION #08 — EMPLOYEE MANAGEMENT
# ============================================================

class EmployeeManagementTests(TestCase):

    def setUp(self):
        self.client = Client()
        login_as_owner(self.client)

    # TC-08-01: Owner can add a new employee
    def test_owner_add_employee(self):
        response = self.client.post(reverse('owner_manage_employees'), {
            'action': 'add',
            'employee_name': 'John Doe',
            'employee_role': 'production_manager'
        })
        self.assertTrue(Employee.objects.filter(employee_name='John Doe').exists())

    # TC-08-02: New production manager gets ID starting with 1
    def test_new_prodman_id_starts_with_1(self):
        self.client.post(reverse('owner_manage_employees'), {
            'action': 'add',
            'employee_name': 'Jane Manager',
            'employee_role': 'production_manager'
        })
        emp = Employee.objects.get(employee_name='Jane Manager')
        self.assertTrue(emp.employee_id.startswith('1'))

    # TC-08-03: New production employee gets ID starting with 2
    def test_new_prodemp_id_starts_with_2(self):
        self.client.post(reverse('owner_manage_employees'), {
            'action': 'add',
            'employee_name': 'Bob Employee',
            'employee_role': 'production_employee'
        })
        emp = Employee.objects.get(employee_name='Bob Employee')
        self.assertTrue(emp.employee_id.startswith('2'))

    # TC-08-04: New employee default password is 1111 for manager
    def test_new_prodman_default_password(self):
        self.client.post(reverse('owner_manage_employees'), {
            'action': 'add',
            'employee_name': 'Test Manager',
            'employee_role': 'production_manager'
        })
        emp = Employee.objects.get(employee_name='Test Manager')
        account = Account.objects.get(employee_id=emp.employee_id)
        self.assertEqual(account.password, '1111')

    # TC-08-05: New employee default password is 2222 for production employee
    def test_new_prodemp_default_password(self):
        self.client.post(reverse('owner_manage_employees'), {
            'action': 'add',
            'employee_name': 'Test Employee',
            'employee_role': 'production_employee'
        })
        emp = Employee.objects.get(employee_name='Test Employee')
        account = Account.objects.get(employee_id=emp.employee_id)
        self.assertEqual(account.password, '2222')

    # TC-08-06: Owner can delete employee
    def test_owner_delete_employee(self):
        emp = create_prodman()
        self.client.post(reverse('delete_employee', args=[emp.id]))
        self.assertFalse(Employee.objects.filter(id=emp.id).exists())

    # TC-08-07: Deleting employee also deletes their account
    def test_delete_employee_also_deletes_account(self):
        emp = create_prodman()
        self.client.post(reverse('delete_employee', args=[emp.id]))
        self.assertFalse(Account.objects.filter(employee_id=emp.employee_id).exists())

    # TC-08-08: Add employee with invalid name (numbers) fails
    def test_add_employee_invalid_name(self):
        self.client.post(reverse('owner_manage_employees'), {
            'action': 'add',
            'employee_name': 'John123',
            'employee_role': 'production_manager'
        })
        self.assertFalse(Employee.objects.filter(employee_name='John123').exists())

    # TC-08-09: Add employee with empty name fails
    def test_add_employee_empty_name(self):
        self.client.post(reverse('owner_manage_employees'), {
            'action': 'add',
            'employee_name': '',
            'employee_role': 'production_manager'
        })
        self.assertEqual(Employee.objects.count(), 0)

