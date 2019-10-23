from django.test import SimpleTestCase, TestCase


class PageTests(SimpleTestCase):
    def test_myview(self):
        response = self.client.get('/class-based-views/view')
        self.assertEqual(response.status_code, 200)


class PageTestsDB(TestCase):
    def test_myviewtemplate(self):
        response = self.client.get('/class-based-views/template-view')
        self.assertEqual(response.status_code, 200)

    def test_mylistview(self):
        response = self.client.get('/class-based-views/list-view')
        self.assertEqual(response.status_code, 200)
