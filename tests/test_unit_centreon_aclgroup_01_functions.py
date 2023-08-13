
import logging
import unittest
import unittest.mock

import centreoncdiff.centreon.Aclgroup


class TestCentreonAclgroup01Functions(unittest.TestCase):

    def setUp(self):
        logging.disable(logging.CRITICAL)

    def test_object_init(self):
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        self.assertIsInstance(aclgroup, centreoncdiff.centreon.Aclgroup.Aclgroup)
        self.assertEqual(aclgroup._name, 'aclgroupName')
        self.assertEqual(aclgroup._alias, 'aclgroupAlias')
        self.assertEqual(aclgroup._activate, True)

    def test_set_alias(self):
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        aclgroup.setAlias('newAlias')
        self.assertEqual(aclgroup._alias, 'newAlias')

    def test_enable(self):
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        aclgroup.enable()
        self.assertEqual(aclgroup._activate, True)

    def test_disable(self):
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        aclgroup.disable()
        self.assertEqual(aclgroup._activate, False)

    def test_set_contact(self):
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        aclgroup.setContact(['firstContact'])
        self.assertEqual(aclgroup._contact, ['firstContact'])

    def test_set_two_contact(self):
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        aclgroup.setContact(['firstContact', 'secondContact'])
        self.assertEqual(aclgroup._contact, ['firstContact', 'secondContact'])

    def test_set_contactgroup(self):
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        aclgroup.setContactGroup(['firstContactgroup'])
        self.assertEqual(aclgroup._contactGroup, ['firstContactgroup'])

    def test_set_two_contactgroup(self):
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        aclgroup.setContactGroup(['firstContactgroup', 'secondContactgroup'])
        self.assertEqual(aclgroup._contactGroup, ['firstContactgroup', 'secondContactgroup'])

    def test_set_menu(self):
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        aclgroup.setMenu(['firstMenu'])
        self.assertEqual(aclgroup._menu, ['firstMenu'])

    def test_set_two_menu(self):
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        aclgroup.setMenu(['firstMenu', 'secondMenu'])
        self.assertEqual(aclgroup._menu, ['firstMenu', 'secondMenu'])

    def test_set_action(self):
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        aclgroup.setAction(['firstAction'])
        self.assertEqual(aclgroup._action, ['firstAction'])

    def test_set_two_action(self):
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        aclgroup.setAction(['firstAction', 'secondAction'])
        self.assertEqual(aclgroup._action, ['firstAction', 'secondAction'])

    def test_set_resource(self):
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        aclgroup.setResource(['firstResource'])
        self.assertEqual(aclgroup._resource, ['firstResource'])

    def test_set_two_resource(self):
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        aclgroup.setResource(['firstResource', 'secondResource'])
        self.assertEqual(aclgroup._resource, ['firstResource', 'secondResource'])


if __name__ == '__main__':
    logging.disable = True
    unittest.main()
