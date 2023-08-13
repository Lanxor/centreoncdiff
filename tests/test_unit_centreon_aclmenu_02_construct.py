
import logging
import unittest
import unittest.mock

import centreoncdiff.centreon.Aclmenu as Aclmenu


class TestCentreonAclmenu02Construct(unittest.TestCase):

    def setUp(self):
        logging.disable(logging.CRITICAL)

    def test_construct_empty_data(self):
        data = {}
        aclmenu = Aclmenu.Aclmenu.construct(data)
        self.assertIsNone(aclmenu)

    def test_construct_wrong_object(self):
        data = {
            'object': 'wrongObject'
        }
        aclmenu = Aclmenu.Aclmenu.construct(data)
        self.assertIsNone(aclmenu)

    def test_construct_missing_name(self):
        data = {
            'object': 'aclmenu',
            'alias': 'aclmenuAlias'
        }
        aclmenu = Aclmenu.Aclmenu.construct(data)
        self.assertIsNone(aclmenu)

    def test_construct_missing_alias(self):
        data = {
            'object': 'aclmenu',
            'name': 'aclmenuName'
        }
        aclmenu = Aclmenu.Aclmenu.construct(data)
        self.assertIsNone(aclmenu)

    def test_construct_minimum(self):
        data = {
            'object': 'aclmenu',
            'name': 'aclmenuName',
            'alias': 'aclmenuAlias'
        }
        aclmenu = Aclmenu.Aclmenu.construct(data)
        self.assertIsInstance(aclmenu, Aclmenu.Aclmenu)
        self.assertEqual(aclmenu._name, 'aclmenuName')
        self.assertEqual(aclmenu._alias, 'aclmenuAlias')
        self.assertEqual(aclmenu._activate, True)
        self.assertEqual(aclmenu._comment, None)
        self.assertEqual(aclmenu._grantrw, [])
        self.assertEqual(aclmenu._grantro, [])
        self.assertEqual(aclmenu._revoke, [])

    def test_construct_with_disable(self):
        data = {
            'object': 'aclmenu',
            'name': 'aclmenuName',
            'alias': 'aclmenuAlias',
            'activate': '0'
        }
        aclmenu = Aclmenu.Aclmenu.construct(data)
        self.assertIsInstance(aclmenu, Aclmenu.Aclmenu)
        self.assertEqual(aclmenu._name, 'aclmenuName')
        self.assertEqual(aclmenu._alias, 'aclmenuAlias')
        self.assertEqual(aclmenu._activate, False)
        self.assertEqual(aclmenu._comment, None)
        self.assertEqual(aclmenu._grantrw, [])
        self.assertEqual(aclmenu._grantro, [])
        self.assertEqual(aclmenu._revoke, [])

    def test_construct_with_one_grantrw(self):
        data = {
            'object': 'aclmenu',
            'name': 'aclmenuName',
            'alias': 'aclmenuAlias',
            'grantrw': ['firstMenu']
        }
        aclmenu = Aclmenu.Aclmenu.construct(data)
        self.assertIsInstance(aclmenu, Aclmenu.Aclmenu)
        self.assertEqual(aclmenu._name, 'aclmenuName')
        self.assertEqual(aclmenu._alias, 'aclmenuAlias')
        self.assertEqual(aclmenu._activate, True)
        self.assertEqual(aclmenu._comment, None)
        self.assertEqual(aclmenu._grantrw, ['firstMenu'])
        self.assertEqual(aclmenu._grantro, [])
        self.assertEqual(aclmenu._revoke, [])

    def test_construct_with_two_grantrw(self):
        data = {
            'object': 'aclmenu',
            'name': 'aclmenuName',
            'alias': 'aclmenuAlias',
            'grantrw': ['firstMenu', 'secondMenu']
        }
        aclmenu = Aclmenu.Aclmenu.construct(data)
        self.assertIsInstance(aclmenu, Aclmenu.Aclmenu)
        self.assertEqual(aclmenu._name, 'aclmenuName')
        self.assertEqual(aclmenu._alias, 'aclmenuAlias')
        self.assertEqual(aclmenu._activate, True)
        self.assertEqual(aclmenu._comment, None)
        self.assertEqual(aclmenu._grantrw, ['firstMenu', 'secondMenu'])
        self.assertEqual(aclmenu._grantro, [])
        self.assertEqual(aclmenu._revoke, [])

    def test_construct_with_one_grantro(self):
        data = {
            'object': 'aclmenu',
            'name': 'aclmenuName',
            'alias': 'aclmenuAlias',
            'grantro': ['firstMenu']
        }
        aclmenu = Aclmenu.Aclmenu.construct(data)
        self.assertIsInstance(aclmenu, Aclmenu.Aclmenu)
        self.assertEqual(aclmenu._name, 'aclmenuName')
        self.assertEqual(aclmenu._alias, 'aclmenuAlias')
        self.assertEqual(aclmenu._activate, True)
        self.assertEqual(aclmenu._comment, None)
        self.assertEqual(aclmenu._grantrw, [])
        self.assertEqual(aclmenu._grantro, ['firstMenu'])
        self.assertEqual(aclmenu._revoke, [])

    def test_construct_with_two_grantro(self):
        data = {
            'object': 'aclmenu',
            'name': 'aclmenuName',
            'alias': 'aclmenuAlias',
            'grantro': ['firstMenu', 'secondMenu']
        }
        aclmenu = Aclmenu.Aclmenu.construct(data)
        self.assertIsInstance(aclmenu, Aclmenu.Aclmenu)
        self.assertEqual(aclmenu._name, 'aclmenuName')
        self.assertEqual(aclmenu._alias, 'aclmenuAlias')
        self.assertEqual(aclmenu._activate, True)
        self.assertEqual(aclmenu._comment, None)
        self.assertEqual(aclmenu._grantrw, [])
        self.assertEqual(aclmenu._grantro, ['firstMenu', 'secondMenu'])
        self.assertEqual(aclmenu._revoke, [])

    def test_construct_with_one_revoke(self):
        data = {
            'object': 'aclmenu',
            'name': 'aclmenuName',
            'alias': 'aclmenuAlias',
            'revoke': ['firstMenu']
        }
        aclmenu = Aclmenu.Aclmenu.construct(data)
        self.assertIsInstance(aclmenu, Aclmenu.Aclmenu)
        self.assertEqual(aclmenu._name, 'aclmenuName')
        self.assertEqual(aclmenu._alias, 'aclmenuAlias')
        self.assertEqual(aclmenu._activate, True)
        self.assertEqual(aclmenu._comment, None)
        self.assertEqual(aclmenu._grantrw, [])
        self.assertEqual(aclmenu._grantro, [])
        self.assertEqual(aclmenu._revoke, ['firstMenu'])

    def test_construct_with_two_revoke(self):
        data = {
            'object': 'aclmenu',
            'name': 'aclmenuName',
            'alias': 'aclmenuAlias',
            'revoke': ['firstMenu', 'secondMenu']
        }
        aclmenu = Aclmenu.Aclmenu.construct(data)
        self.assertIsInstance(aclmenu, Aclmenu.Aclmenu)
        self.assertEqual(aclmenu._name, 'aclmenuName')
        self.assertEqual(aclmenu._alias, 'aclmenuAlias')
        self.assertEqual(aclmenu._activate, True)
        self.assertEqual(aclmenu._comment, None)
        self.assertEqual(aclmenu._grantrw, [])
        self.assertEqual(aclmenu._grantro, [])
        self.assertEqual(aclmenu._revoke, ['firstMenu', 'secondMenu'])


if __name__ == '__main__':
    logging.disable = True
    unittest.main()
