import unittest
from flask import Flask
from flask_restful import Api
from stock_inventory import (
    ProductResource,
    CategoryResource,
    ProductNameResource,
    DateAddedResource,
    InventoryResource,
)


class FlaskApiTests(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(ProductResource, '/product', methods=['POST'])
        self.api.add_resource(CategoryResource, '/category/<string:category>')
        self.api.add_resource(ProductNameResource, '/product_name/<string:product_name>')
        self.api.add_resource(DateAddedResource, '/date_added/<int:days>')
        self.api.add_resource(InventoryResource, '/inventory')
        self.client = self.app.test_client()

    def test_add_product(self):
        response = self.client.post('/product', data={
            'category': 'Electronics',
            'name': 'iPhone',
            'price': '999.99',
            'quantity': '10',
            'date_added': '2023-07-10'
        })
        self.assertEqual(response.status_code, 409)
        #print(response.get_data(as_text=True))
        # Add more assertions to test the response data

    def test_filter_by_category(self): 
        response = self.client.get('/category/Electronics')
        self.assertEqual(response.status_code, 200)
        # Add more assertions to test the response data

    def test_filter_by_product_name(self):
        response = self.client.get('/product_name/iPhone')
        self.assertEqual(response.status_code, 200)
        # Add more assertions to test the response data

    def test_filter_by_date_added(self):
        response = self.client.get('/date_added/7')
        self.assertEqual(response.status_code, 200)
        # Add more assertions to test the response data

    def test_display_inventory(self):
        response = self.client.get('/inventory')
        self.assertEqual(response.status_code, 200)
        # Add more assertions to test the response data


if __name__ == '__main__':
    unittest.main()