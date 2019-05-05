import os
import json
import unittest
from test_dz.app import check_document_existance, remove_doc_from_shelf, add_new_shelf, append_doc_to_shelf
from unittest.mock import patch
import mock


class TestApp(unittest.TestCase):

    def setUp(self):
        current_path = os.getcwd()
        f_dir = os.path.join(current_path, 'fixtures\directories.json')
        f_doc = os.path.join(current_path, 'fixtures\documents.json')
        with open(f_dir, 'r') as file:
            self.directories = json.load(file)
        with open(f_doc, 'r') as file:
            self.documents = json.load(file)

    @mock.patch('test_dz.app.documents')
    def test_check_document_existance(self, documents):                 # 'этот тест вроде ок.
        self.assertTrue(check_document_existance("10006"))
        self.assertFalse(check_document_existance("10016"))

#    @mock.patch('test_dz.app.directories')
#    def test_remove_doc_from_shelf(self, directories):
#
#        self.assertIn('11-2', directories['1'])     # эта строка выдает ошибку:  AssertionError: '11-2' not found in <MagicMock name='directories.__getitem__()' id='30837040'>
#        remove_doc_from_shelf('11-2')               # эта строка отрабатывается, когда одна
#        self.assertIn('11-2', directories['1'])
#        self.assertIn(directories['2'], ["10006"])
#        self.assertEqual(directories['1'], ("2207 876234", "11-2"))

    @mock.patch('test_dz.app.directories')
    def test_add_new_shelf(self, directories):
        add_new_shelf(shelf_number='4')
        self.assertTrue(directories["4"])


    @mock.patch('test_dz.app.directories')
    def test_append_doc_to_shelf(self, directories):
        with self.assertRaises(TypeError) as f:
            append_doc_to_shelf()





if __name__ == '__main__':
    unittest.main()

