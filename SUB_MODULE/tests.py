from django.test import TestCase
from django.test import TestCase, TransactionTestCase

# Create your tests here.


class SampleTestCase(TestCase):
  def test_sample_page_response(self):
    response = self.client.get('/sample/')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.content, b'Sample App')
