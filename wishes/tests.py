# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from rest_framework.test import RequestsClient
import json
from requests.auth import HTTPBasicAuth
from django.contrib.auth.models import User

class RestTestCase(TestCase):

    def setUp(self):
        self.test_1 = []
        with open('TestData/http001.json') as f:
            for line in f:
                self.test_1.append(line)
        self.username = 'frescoadmin'
        self.password = 'frescopassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_get_all_wishes(self):
        client = RequestsClient()
        client.auth = HTTPBasicAuth(self.username, self.password)
        client.headers.update({'x-test': 'true'})
        for ro in self.test_1:
            row = json.loads(ro)
            print (row)
            res = {}
            if row['request']['method'] == "GET":
                res = client.get('http://localhost:8000' +
                                 row['request']['url'] + '/')
            elif row['request']['method'] == "POST":
                res = client.post(
                    'http://localhost:8000' + row['request']['url'] + '/', json=row['request']['body'])
            self.assertEqual(res.status_code, row['response']['status_code'])
            if row['response']['headers'] != {}:
                self.assertEqual(
                    res.headers['Content-Type'], row['response']['headers']['Content-Type'])
            if row['response']['body'] != {}:
                response = json.loads(res.text)
                self.assertEqual(response, row['response']['body'])


    def test_get_schema(self):
        client = RequestsClient()
        client.auth = HTTPBasicAuth(self.username, self.password)
        client.headers.update({'x-test': 'true'})
        res = client.get('http://localhost:8000/schema/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.headers['Content-Type'], "application/coreapi+json")

    def test_get_docs(self):
        client = RequestsClient()
        client.auth = HTTPBasicAuth(self.username, self.password)
        client.headers.update({'x-test': 'true'})
        res = client.get('http://localhost:8000/docs/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.headers['Content-Type'], "text/html; charset=utf-8")