from django.test import SimpleTestCase
from django.urls import reverse, resolve
from shop.views import category_list, subcategory_list, product_list

class TestUrls(SimpleTestCase):

    def test_category_list_url_resolves(self):
        url = reverse('category_list')
        self.assertEquals(resolve(url).func, category_list)

    def test_subcategory_list_url_resolves(self):
        url = reverse('subcategory_list', args=['some-category-slug'])
        self.assertEquals(resolve(url).func, subcategory_list)

    def test_product_list_url_resolves(self):
        url = reverse('product_list', args=['some-category-slug', 'some-subcategory-slug'])
        self.assertEquals(resolve(url).func, product_list)