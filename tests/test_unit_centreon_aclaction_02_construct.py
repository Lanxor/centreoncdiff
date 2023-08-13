
import logging
import unittest
import unittest.mock

import centreoncdiff.centreon.Aclaction as Aclaction


class TestCentreonAclaction02Construct(unittest.TestCase):

    def setUp(self):
        logging.disable(logging.CRITICAL)

    def test_construct_empty_data(self):
        data = {}
        aclaction = Aclaction.Aclaction.construct(data)
        self.assertIsNone(aclaction)

    def test_construct_wrong_object(self):
        data = {
            'object': 'wrongObject'
        }
        aclaction = Aclaction.Aclaction.construct(data)
        self.assertIsNone(aclaction)

    def test_construct_missing_name(self):
        data = {
            'object': 'aclaction',
            'description': 'aclactionDescription'
        }
        aclaction = Aclaction.Aclaction.construct(data)
        self.assertIsNone(aclaction)

    def test_construct_missing_description(self):
        data = {
            'object': 'aclaction',
            'name': 'aclactionName'
        }
        aclaction = Aclaction.Aclaction.construct(data)
        self.assertIsNone(aclaction)

    def test_construct_minimum(self):
        data = {
            'object': 'aclaction',
            'name': 'aclactionName',
            'description': 'aclactionDescription'
        }
        aclaction = Aclaction.Aclaction.construct(data)
        self.assertIsInstance(aclaction, Aclaction.Aclaction)
        self.assertEqual(aclaction._name, 'aclactionName')
        self.assertEqual(aclaction._description, 'aclactionDescription')
        self.assertEqual(aclaction._activate, True)
        self.assertEqual(aclaction._grant, [])
        self.assertEqual(aclaction._revoke, [])

    def test_construct_with_disable(self):
        data = {
            'object': 'aclaction',
            'name': 'aclactionName',
            'description': 'aclactionDescription',
            'activate': '0'
        }
        aclaction = Aclaction.Aclaction.construct(data)
        self.assertIsInstance(aclaction, Aclaction.Aclaction)
        self.assertEqual(aclaction._name, 'aclactionName')
        self.assertEqual(aclaction._description, 'aclactionDescription')
        self.assertEqual(aclaction._activate, False)
        self.assertEqual(aclaction._grant, [])
        self.assertEqual(aclaction._revoke, [])

    def test_construct_with_one_grant(self):
        data = {
            'object': 'aclaction',
            'name': 'aclactionName',
            'description': 'aclactionDescription',
            'grant': ['firstAction']
        }
        aclaction = Aclaction.Aclaction.construct(data)
        self.assertIsInstance(aclaction, Aclaction.Aclaction)
        self.assertEqual(aclaction._name, 'aclactionName')
        self.assertEqual(aclaction._description, 'aclactionDescription')
        self.assertEqual(aclaction._activate, True)
        self.assertEqual(aclaction._grant, ['firstAction'])
        self.assertEqual(aclaction._revoke, [])

    def test_construct_with_two_grant(self):
        data = {
            'object': 'aclaction',
            'name': 'aclactionName',
            'description': 'aclactionDescription',
            'grant': ['firstAction', 'secondAction']
        }
        aclaction = Aclaction.Aclaction.construct(data)
        self.assertIsInstance(aclaction, Aclaction.Aclaction)
        self.assertEqual(aclaction._name, 'aclactionName')
        self.assertEqual(aclaction._description, 'aclactionDescription')
        self.assertEqual(aclaction._activate, True)
        self.assertEqual(aclaction._grant, ['firstAction', 'secondAction'])
        self.assertEqual(aclaction._revoke, [])

    def test_construct_with_one_revoke(self):
        data = {
            'object': 'aclaction',
            'name': 'aclactionName',
            'description': 'aclactionDescription',
            'grant': ['firstAction']
        }
        aclaction = Aclaction.Aclaction.construct(data)
        self.assertIsInstance(aclaction, Aclaction.Aclaction)
        self.assertEqual(aclaction._name, 'aclactionName')
        self.assertEqual(aclaction._description, 'aclactionDescription')
        self.assertEqual(aclaction._activate, True)
        self.assertEqual(aclaction._grant, ['firstAction'])
        self.assertEqual(aclaction._revoke, [])

    def test_construct_with_two_revoke(self):
        data = {
            'object': 'aclaction',
            'name': 'aclactionName',
            'description': 'aclactionDescription',
            'revoke': ['firstAction', 'secondAction']
        }
        aclaction = Aclaction.Aclaction.construct(data)
        self.assertIsInstance(aclaction, Aclaction.Aclaction)
        self.assertEqual(aclaction._name, 'aclactionName')
        self.assertEqual(aclaction._description, 'aclactionDescription')
        self.assertEqual(aclaction._activate, True)
        self.assertEqual(aclaction._grant, [])
        self.assertEqual(aclaction._revoke, ['firstAction', 'secondAction'])


if __name__ == '__main__':
    logging.disable = True
    unittest.main()
