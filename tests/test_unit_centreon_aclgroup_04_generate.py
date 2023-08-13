
import logging
import io
import unittest
import unittest.mock

import centreoncdiff.centreon.Aclgroup


class TestCentreonAclgroup04Generate(unittest.TestCase):

    def setUp(self):
        logging.disable(logging.CRITICAL)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_minimal(self, mock_stdout):
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        aclgroup.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLGROUP;ADD;aclgroupName;aclgroupAlias\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_minimal_with_set_alias(self, mock_stdout):
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        aclgroup.setAlias('newAlias')
        aclgroup.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLGROUP;ADD;aclgroupName;newAlias\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_with_enable_status(self, mock_stdout):
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        aclgroup.enable()
        aclgroup.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLGROUP;ADD;aclgroupName;aclgroupAlias\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_with_disable_status(self, mock_stdout):
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        aclgroup.disable()
        aclgroup.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLGROUP;ADD;aclgroupName;aclgroupAlias\nACLGROUP;SETPARAM;aclgroupName;activate;0\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_with_set_contact(self, mock_stdout):
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        aclgroup.setContact(['firstContact'])
        aclgroup.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLGROUP;ADD;aclgroupName;aclgroupAlias\nACLGROUP;SETCONTACT;aclgroupName;firstContact\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_with_set_contactgroup(self, mock_stdout):
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        aclgroup.setContactGroup(['firstContactGroup'])
        aclgroup.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLGROUP;ADD;aclgroupName;aclgroupAlias\nACLGROUP;SETCONTACTGROUP;aclgroupName;firstContactGroup\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_with_set_menu(self, mock_stdout):
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        aclgroup.setMenu(['firstMenu'])
        aclgroup.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLGROUP;ADD;aclgroupName;aclgroupAlias\nACLGROUP;SETMENU;aclgroupName;firstMenu\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_with_set_action(self, mock_stdout):
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        aclgroup.setAction(['firstAction'])
        aclgroup.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLGROUP;ADD;aclgroupName;aclgroupAlias\nACLGROUP;SETACTION;aclgroupName;firstAction\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_with_set_resource(self, mock_stdout):
        aclgroup = centreoncdiff.centreon.Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        aclgroup.setResource(['firstResource'])
        aclgroup.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLGROUP;ADD;aclgroupName;aclgroupAlias\nACLGROUP;SETRESOURCE;aclgroupName;firstResource\n')


if __name__ == '__main__':
    logging.disable = True
    unittest.main()
