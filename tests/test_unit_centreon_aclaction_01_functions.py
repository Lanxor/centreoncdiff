
import logging
import unittest
import unittest.mock

import centreoncdiff.centreon.Aclaction as Aclaction


class TestCentreonAclaction01Function(unittest.TestCase):

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

    def test_object_init(self):
        aclaction = Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        self.assertIsInstance(aclaction, Aclaction.Aclaction)
        self.assertEqual(aclaction._name, 'aclactionName')
        self.assertEqual(aclaction._description, 'aclactionDescription')
        self.assertEqual(aclaction._activate, True)
        self.assertEqual(aclaction._grant, [])
        self.assertEqual(aclaction._revoke, [])

    def test_set_description(self):
        aclaction = Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.setDescription('newDescription')
        self.assertEqual(aclaction._description, 'newDescription')

    def test_enable(self):
        aclaction = Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.enable()
        self.assertEqual(aclaction._activate, True)

    def test_disable(self):
        aclaction = Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.disable()
        self.assertEqual(aclaction._activate, False)

    def test_set_grant(self):
        aclaction = Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.setGrant('firstAction')
        self.assertEqual(aclaction._grant, ['firstAction'])

    def test_set_two_grant(self):
        aclaction = Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.setGrant('firstAction')
        aclaction.setGrant('secondAction')
        self.assertEqual(aclaction._grant, ['firstAction', 'secondAction'])

    def test_set_grant_with_revoke_already_defined(self):
        aclaction = Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.setRevoke('firstAction')
        aclaction.setGrant('firstAction')
        self.assertEqual(aclaction._revoke, [])
        self.assertEqual(aclaction._grant, ['firstAction'])

    def test_set_grant_with_two_revoke_already_defined(self):
        aclaction = Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.setRevoke('firstAction')
        aclaction.setRevoke('secondAction')
        aclaction.setGrant('firstAction')
        self.assertEqual(aclaction._revoke, ['secondAction'])
        self.assertEqual(aclaction._grant, ['firstAction'])

    def test_set_revoke(self):
        aclaction = Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.setRevoke('firstAction')
        self.assertEqual(aclaction._revoke, ['firstAction'])

    def test_set_two_revoke(self):
        aclaction = Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.setRevoke('firstAction')
        aclaction.setRevoke('secondAction')
        self.assertEqual(aclaction._revoke, ['firstAction', 'secondAction'])

    def test_set_revoke_with_grant_already_defined(self):
        aclaction = Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.setGrant('firstAction')
        aclaction.setRevoke('firstAction')
        self.assertEqual(aclaction._grant, [])
        self.assertEqual(aclaction._revoke, ['firstAction'])

    def test_set_revoke_with_two_grant_already_defined(self):
        aclaction = Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.setGrant('firstAction')
        aclaction.setGrant('secondAction')
        aclaction.setRevoke('firstAction')
        self.assertEqual(aclaction._grant, ['secondAction'])
        self.assertEqual(aclaction._revoke, ['firstAction'])


if __name__ == '__main__':
    logging.disable = True
    unittest.main()
