import os
import json
import unittest
from test_dz.app import check_document_existance
from mock import patch

class TestApp(unittest.TestCase):

    def setUp(self):
        current_path = os.getcwd()
        f_dir = os.path.join(current_path, 'fixtures\directories.json')
        f_doc = os.path.join(current_path, 'fixtures\documents.json')
        with open(f_dir, 'r') as file:
            self.directories = json.load(file)
        with open(f_doc, 'r') as file:
            self.documents = json.load(file)


    def test_check_document_existance(self):
        documents = self.documents
        check_document_existance("10006")
