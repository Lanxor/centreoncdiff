
import logging
import unittest
import unittest.mock

import centreoncdiff.centreon.Aclgroup


class TestCentreonAclgroup02Construct(unittest.TestCase):

    def setUp(self):
        logging.disable(logging.CRITICAL)

    def test_construct_empty_data(self):
        data = {}
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup.construct(data)
        self.assertIsNone(aclgroup)

    def test_construct_wrong_object(self):
        data = {
            'object': 'wrongObject'
        }
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup.construct(data)
        self.assertIsNone(aclgroup)

    def test_construct_missing_name(self):
        data = {
            'object': 'aclgroup',
            'alias': 'aclgroupAlias'
        }
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup.construct(data)
        self.assertIsNone(aclgroup)

    def test_construct_missing_alias(self):
        data = {
            'object': 'aclgroup',
            'name': 'aclgroupName'
        }
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup.construct(data)
        self.assertIsNone(aclgroup)

    def test_construct_minimum(self):
        data = {
            'object': 'aclgroup',
            'name': 'aclgroupName',
            'alias': 'aclgroupAlias'
        }
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup.construct(data)
        self.assertIsInstance(aclgroup, centreoncdiff.centreon.Aclgroup.Aclgroup)
        self.assertEqual(aclgroup._name, 'aclgroupName')
        self.assertEqual(aclgroup._alias, 'aclgroupAlias')
        self.assertEqual(aclgroup._activate, True)
        self.assertEqual(aclgroup._contact, [])
        self.assertEqual(aclgroup._contactGroup, [])
        self.assertEqual(aclgroup._menu, [])
        self.assertEqual(aclgroup._action, [])
        self.assertEqual(aclgroup._resource, [])

    def test_construct_with_disable(self):
        data = {
            'object': 'aclgroup',
            'name': 'aclgroupName',
            'alias': 'aclgroupAlias',
            'activate': '0'
        }
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup.construct(data)
        self.assertIsInstance(aclgroup, centreoncdiff.centreon.Aclgroup.Aclgroup)
        self.assertEqual(aclgroup._name, 'aclgroupName')
        self.assertEqual(aclgroup._alias, 'aclgroupAlias')
        self.assertEqual(aclgroup._activate, False)
        self.assertEqual(aclgroup._contact, [])
        self.assertEqual(aclgroup._contactGroup, [])
        self.assertEqual(aclgroup._menu, [])
        self.assertEqual(aclgroup._action, [])
        self.assertEqual(aclgroup._resource, [])

    def test_construct_with_str_contact(self):
        data = {
            'object': 'aclgroup',
            'name': 'aclgroupName',
            'alias': 'aclgroupAlias',
            'contact': 'contact'
        }
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup.construct(data)
        self.assertIsInstance(aclgroup, centreoncdiff.centreon.Aclgroup.Aclgroup)
        self.assertEqual(aclgroup._name, 'aclgroupName')
        self.assertEqual(aclgroup._alias, 'aclgroupAlias')
        self.assertEqual(aclgroup._activate, True)
        self.assertEqual(aclgroup._contact, ['contact'])
        self.assertEqual(aclgroup._contactGroup, [])
        self.assertEqual(aclgroup._menu, [])
        self.assertEqual(aclgroup._action, [])
        self.assertEqual(aclgroup._resource, [])

    def test_construct_with_one_contact(self):
        data = {
            'object': 'aclgroup',
            'name': 'aclgroupName',
            'alias': 'aclgroupAlias',
            'contact': ['firstContact']
        }
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup.construct(data)
        self.assertIsInstance(aclgroup, centreoncdiff.centreon.Aclgroup.Aclgroup)
        self.assertEqual(aclgroup._name, 'aclgroupName')
        self.assertEqual(aclgroup._alias, 'aclgroupAlias')
        self.assertEqual(aclgroup._activate, True)
        self.assertEqual(aclgroup._contact, ['firstContact'])
        self.assertEqual(aclgroup._contactGroup, [])
        self.assertEqual(aclgroup._menu, [])
        self.assertEqual(aclgroup._action, [])
        self.assertEqual(aclgroup._resource, [])

    def test_construct_with_two_contact(self):
        data = {
            'object': 'aclgroup',
            'name': 'aclgroupName',
            'alias': 'aclgroupAlias',
            'contact': ['firstContact', 'secondContact']
        }
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup.construct(data)
        self.assertIsInstance(aclgroup, centreoncdiff.centreon.Aclgroup.Aclgroup)
        self.assertEqual(aclgroup._name, 'aclgroupName')
        self.assertEqual(aclgroup._alias, 'aclgroupAlias')
        self.assertEqual(aclgroup._activate, True)
        self.assertEqual(aclgroup._contact, ['firstContact', 'secondContact'])
        self.assertEqual(aclgroup._contactGroup, [])
        self.assertEqual(aclgroup._menu, [])
        self.assertEqual(aclgroup._action, [])
        self.assertEqual(aclgroup._resource, [])

    def test_construct_with_str_contactgroup(self):
        data = {
            'object': 'aclgroup',
            'name': 'aclgroupName',
            'alias': 'aclgroupAlias',
            'contactGroup': 'contactGroup'
        }
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup.construct(data)
        self.assertIsInstance(aclgroup, centreoncdiff.centreon.Aclgroup.Aclgroup)
        self.assertEqual(aclgroup._name, 'aclgroupName')
        self.assertEqual(aclgroup._alias, 'aclgroupAlias')
        self.assertEqual(aclgroup._activate, True)
        self.assertEqual(aclgroup._contact, [])
        self.assertEqual(aclgroup._contactGroup, ['contactGroup'])
        self.assertEqual(aclgroup._menu, [])
        self.assertEqual(aclgroup._action, [])
        self.assertEqual(aclgroup._resource, [])

    def test_construct_with_one_contactgroup(self):
        data = {
            'object': 'aclgroup',
            'name': 'aclgroupName',
            'alias': 'aclgroupAlias',
            'contactGroup': ['firstContactGroup']
        }
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup.construct(data)
        self.assertIsInstance(aclgroup, centreoncdiff.centreon.Aclgroup.Aclgroup)
        self.assertEqual(aclgroup._name, 'aclgroupName')
        self.assertEqual(aclgroup._alias, 'aclgroupAlias')
        self.assertEqual(aclgroup._activate, True)
        self.assertEqual(aclgroup._contact, [])
        self.assertEqual(aclgroup._contactGroup, ['firstContactGroup'])
        self.assertEqual(aclgroup._menu, [])
        self.assertEqual(aclgroup._action, [])
        self.assertEqual(aclgroup._resource, [])

    def test_construct_with_two_contactgroup(self):
        data = {
            'object': 'aclgroup',
            'name': 'aclgroupName',
            'alias': 'aclgroupAlias',
            'contactGroup': ['firstContactGroup', 'secondContactGroup']
        }
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup.construct(data)
        self.assertIsInstance(aclgroup, centreoncdiff.centreon.Aclgroup.Aclgroup)
        self.assertEqual(aclgroup._name, 'aclgroupName')
        self.assertEqual(aclgroup._alias, 'aclgroupAlias')
        self.assertEqual(aclgroup._activate, True)
        self.assertEqual(aclgroup._contact, [])
        self.assertEqual(aclgroup._contactGroup, ['firstContactGroup', 'secondContactGroup'])
        self.assertEqual(aclgroup._menu, [])
        self.assertEqual(aclgroup._action, [])
        self.assertEqual(aclgroup._resource, [])

    def test_construct_with_str_menu(self):
        data = {
            'object': 'aclgroup',
            'name': 'aclgroupName',
            'alias': 'aclgroupAlias',
            'menu': 'menu'
        }
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup.construct(data)
        self.assertIsInstance(aclgroup, centreoncdiff.centreon.Aclgroup.Aclgroup)
        self.assertEqual(aclgroup._name, 'aclgroupName')
        self.assertEqual(aclgroup._alias, 'aclgroupAlias')
        self.assertEqual(aclgroup._activate, True)
        self.assertEqual(aclgroup._contact, [])
        self.assertEqual(aclgroup._contactGroup, [])
        self.assertEqual(aclgroup._menu, ['menu'])
        self.assertEqual(aclgroup._action, [])
        self.assertEqual(aclgroup._resource, [])

    def test_construct_with_one_menu(self):
        data = {
            'object': 'aclgroup',
            'name': 'aclgroupName',
            'alias': 'aclgroupAlias',
            'menu': ['firstMenu']
        }
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup.construct(data)
        self.assertIsInstance(aclgroup, centreoncdiff.centreon.Aclgroup.Aclgroup)
        self.assertEqual(aclgroup._name, 'aclgroupName')
        self.assertEqual(aclgroup._alias, 'aclgroupAlias')
        self.assertEqual(aclgroup._activate, True)
        self.assertEqual(aclgroup._contact, [])
        self.assertEqual(aclgroup._contactGroup, [])
        self.assertEqual(aclgroup._menu, ['firstMenu'])
        self.assertEqual(aclgroup._action, [])
        self.assertEqual(aclgroup._resource, [])

    def test_construct_with_two_menu(self):
        data = {
            'object': 'aclgroup',
            'name': 'aclgroupName',
            'alias': 'aclgroupAlias',
            'menu': ['firstMenu', 'secondMenu']
        }
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup.construct(data)
        self.assertIsInstance(aclgroup, centreoncdiff.centreon.Aclgroup.Aclgroup)
        self.assertEqual(aclgroup._name, 'aclgroupName')
        self.assertEqual(aclgroup._alias, 'aclgroupAlias')
        self.assertEqual(aclgroup._activate, True)
        self.assertEqual(aclgroup._contact, [])
        self.assertEqual(aclgroup._contactGroup, [])
        self.assertEqual(aclgroup._menu, ['firstMenu', 'secondMenu'])
        self.assertEqual(aclgroup._action, [])
        self.assertEqual(aclgroup._resource, [])

    def test_construct_with_str_action(self):
        data = {
            'object': 'aclgroup',
            'name': 'aclgroupName',
            'alias': 'aclgroupAlias',
            'action': 'action'
        }
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup.construct(data)
        self.assertIsInstance(aclgroup, centreoncdiff.centreon.Aclgroup.Aclgroup)
        self.assertEqual(aclgroup._name, 'aclgroupName')
        self.assertEqual(aclgroup._alias, 'aclgroupAlias')
        self.assertEqual(aclgroup._activate, True)
        self.assertEqual(aclgroup._contact, [])
        self.assertEqual(aclgroup._contactGroup, [])
        self.assertEqual(aclgroup._menu, [])
        self.assertEqual(aclgroup._action, ['action'])
        self.assertEqual(aclgroup._resource, [])

    def test_construct_with_one_action(self):
        data = {
            'object': 'aclgroup',
            'name': 'aclgroupName',
            'alias': 'aclgroupAlias',
            'action': ['firstAction']
        }
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup.construct(data)
        self.assertIsInstance(aclgroup, centreoncdiff.centreon.Aclgroup.Aclgroup)
        self.assertEqual(aclgroup._name, 'aclgroupName')
        self.assertEqual(aclgroup._alias, 'aclgroupAlias')
        self.assertEqual(aclgroup._activate, True)
        self.assertEqual(aclgroup._contact, [])
        self.assertEqual(aclgroup._contactGroup, [])
        self.assertEqual(aclgroup._menu, [])
        self.assertEqual(aclgroup._action, ['firstAction'])
        self.assertEqual(aclgroup._resource, [])

    def test_construct_with_two_action(self):
        data = {
            'object': 'aclgroup',
            'name': 'aclgroupName',
            'alias': 'aclgroupAlias',
            'action': ['firstAction', 'secondAction']
        }
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup.construct(data)
        self.assertIsInstance(aclgroup, centreoncdiff.centreon.Aclgroup.Aclgroup)
        self.assertEqual(aclgroup._name, 'aclgroupName')
        self.assertEqual(aclgroup._alias, 'aclgroupAlias')
        self.assertEqual(aclgroup._activate, True)
        self.assertEqual(aclgroup._contact, [])
        self.assertEqual(aclgroup._contactGroup, [])
        self.assertEqual(aclgroup._menu, [])
        self.assertEqual(aclgroup._action, ['firstAction', 'secondAction'])
        self.assertEqual(aclgroup._resource, [])

    def test_construct_with_str_resource(self):
        data = {
            'object': 'aclgroup',
            'name': 'aclgroupName',
            'alias': 'aclgroupAlias',
            'resource': 'resource'
        }
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup.construct(data)
        self.assertIsInstance(aclgroup, centreoncdiff.centreon.Aclgroup.Aclgroup)
        self.assertEqual(aclgroup._name, 'aclgroupName')
        self.assertEqual(aclgroup._alias, 'aclgroupAlias')
        self.assertEqual(aclgroup._activate, True)
        self.assertEqual(aclgroup._contact, [])
        self.assertEqual(aclgroup._contactGroup, [])
        self.assertEqual(aclgroup._menu, [])
        self.assertEqual(aclgroup._action, [])
        self.assertEqual(aclgroup._resource, ['resource'])

    def test_construct_with_one_resource(self):
        data = {
            'object': 'aclgroup',
            'name': 'aclgroupName',
            'alias': 'aclgroupAlias',
            'resource': ['firstResource']
        }
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup.construct(data)
        self.assertIsInstance(aclgroup, centreoncdiff.centreon.Aclgroup.Aclgroup)
        self.assertEqual(aclgroup._name, 'aclgroupName')
        self.assertEqual(aclgroup._alias, 'aclgroupAlias')
        self.assertEqual(aclgroup._activate, True)
        self.assertEqual(aclgroup._contact, [])
        self.assertEqual(aclgroup._contactGroup, [])
        self.assertEqual(aclgroup._menu, [])
        self.assertEqual(aclgroup._action, [])
        self.assertEqual(aclgroup._resource, ['firstResource'])

    def test_construct_with_two_resource(self):
        data = {
            'object': 'aclgroup',
            'name': 'aclgroupName',
            'alias': 'aclgroupAlias',
            'resource': ['firstResource', 'secondResource']
        }
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup.construct(data)
        self.assertIsInstance(aclgroup, centreoncdiff.centreon.Aclgroup.Aclgroup)
        self.assertEqual(aclgroup._name, 'aclgroupName')
        self.assertEqual(aclgroup._alias, 'aclgroupAlias')
        self.assertEqual(aclgroup._activate, True)
        self.assertEqual(aclgroup._contact, [])
        self.assertEqual(aclgroup._contactGroup, [])
        self.assertEqual(aclgroup._menu, [])
        self.assertEqual(aclgroup._action, [])
        self.assertEqual(aclgroup._resource, ['firstResource', 'secondResource'])


if __name__ == '__main__':
    logging.disable = True
    unittest.main()
