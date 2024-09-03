from django.test import TestCase, Client
from django.urls import reverse
from shop.models import Category, SubCategory, Product

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Test Category', slug='test-category')
        self.subcategory = SubCategory.objects.create(name='Test SubCategory', slug='test-subcategory', category=self.category)
        self.product = Product.objects.create(name='Test Product', slug='test-product', description='Test Description', price=10.99, subcategory=self.subcategory)

    def test_category_list_view(self):
        response = self.client.get(reverse('category_list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_list.html')

    def test_subcategory_list_view(self):
        response = self.client.get(reverse('subcategory_list', args=[self.category.slug]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'subcategory_list.html')
        self.assertEqual(response.context['category'], self.category)
        self.assertQuerysetEqual(response.context['subcategories'], self.category.subcategories.all())

    def test_product_list_view(self):
        response = self.client.get(reverse('product_list', args=[self.category.slug, self.subcategory.slug]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_list.html')
        self.assertEqual(response.context['subcategory'], self.subcategory)
        self.assertQuerysetEqual(response.context['products'], self.subcategory.products.all())