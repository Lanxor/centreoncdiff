
import logging
import io
import unittest
import unittest.mock

import centreoncdiff.centreon.Aclgroup as Aclgroup


class TestCentreonAclgroup05GenerateDiff(unittest.TestCase):

    def setUp(self):
        logging.disable(logging.CRITICAL)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_minimal_same(self, mock_stdout):
        currentAclgroup = Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        aclgroup = Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        aclgroup.generate(currentAclgroup)
        self.assertEqual(mock_stdout.getvalue(), '')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_minimal_alias_update(self, mock_stdout):
        currentAclgroup = Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        aclgroup = Aclgroup.Aclgroup('aclgroupName', 'newAlias')
        aclgroup.generate(currentAclgroup)
        self.assertEqual(mock_stdout.getvalue(), 'ACLGROUP;SETPARAM;aclgroupName;alias;newAlias\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_enable_when_already_enabled(self, mock_stdout):
        currentAclgroup = Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        currentAclgroup.enable()
        aclgroup = Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        aclgroup.enable()
        aclgroup.generate(currentAclgroup)
        self.assertEqual(mock_stdout.getvalue(), '')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_enable_when_disabled(self, mock_stdout):
        currentAclgroup = Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        currentAclgroup.disable()
        aclgroup = Aclgroup.Aclgroup('aclgroupName', 'aclgroupAlias')
        aclgroup.enable()
        aclgroup.generate(currentAclgroup)
        self.assertEqual(mock_stdout.getvalue(), 'ACLGROUP;SETPARAM;aclgroupName;activate;1\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_contact_when_already_defined_and_same(self, mock_stdout):
        currentAclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        currentAclaction.setContact('contactValue')
        aclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction.setContact('contactValue')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), '')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_contact_when__two_already_defined_and_same(self, mock_stdout):
        currentAclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        currentAclaction.setContact('firstContact')
        currentAclaction.setContact('secondContact')
        aclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction.setContact('firstContact')
        aclaction.setContact('secondContact')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), '')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_contact_new_value_01(self, mock_stdout):
        currentAclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction.setContact('firstContact')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), 'ACLGROUP;SETCONTACT;aclactionName;firstContact\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_contact_new_value_02(self, mock_stdout):
        currentAclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction.setContact('firstContact')
        aclaction.setContact('secondContact')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), 'ACLGROUP;SETCONTACT;aclactionName;firstContact|secondContact\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_contact_two_new_value(self, mock_stdout):
        currentAclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        currentAclaction.setContact('firstContact')
        aclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction.setContact('firstContact')
        aclaction.setContact('secondContact')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), 'ACLGROUP;SETCONTACT;aclactionName;firstContact|secondContact\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_contactgroup_when_already_defined_and_same(self, mock_stdout):
        currentAclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        currentAclaction.setContactGroup('contactgroupValue')
        aclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction.setContactGroup('contactgroupValue')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), '')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_contactgroup_when__two_already_defined_and_same(self, mock_stdout):
        currentAclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        currentAclaction.setContactGroup('firstContactGroup')
        currentAclaction.setContactGroup('secondContactGroup')
        aclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction.setContactGroup('firstContactGroup')
        aclaction.setContactGroup('secondContactGroup')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), '')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_contactgroup_new_value_01(self, mock_stdout):
        currentAclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction.setContactGroup('firstContactGroup')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), 'ACLGROUP;SETCONTACTGROUP;aclactionName;firstContactGroup\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_contactgroup_new_value_02(self, mock_stdout):
        currentAclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction.setContactGroup('firstContactGroup')
        aclaction.setContactGroup('secondContactGroup')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), 'ACLGROUP;SETCONTACTGROUP;aclactionName;firstContactGroup|secondContactGroup\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_contactgroup_two_new_value(self, mock_stdout):
        currentAclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        currentAclaction.setContactGroup('firstContactGroup')
        aclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction.setContactGroup('firstContactGroup')
        aclaction.setContactGroup('secondContactGroup')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), 'ACLGROUP;SETCONTACTGROUP;aclactionName;firstContactGroup|secondContactGroup\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_menu_when_already_defined_and_same(self, mock_stdout):
        currentAclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        currentAclaction.setMenu('menuValue')
        aclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction.setMenu('menuValue')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), '')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_menu_when__two_already_defined_and_same(self, mock_stdout):
        currentAclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        currentAclaction.setMenu('firstMenu')
        currentAclaction.setMenu('secondMenu')
        aclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction.setMenu('firstMenu')
        aclaction.setMenu('secondMenu')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), '')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_menu_new_value_01(self, mock_stdout):
        currentAclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction.setMenu('firstMenu')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), 'ACLGROUP;SETMENU;aclactionName;firstMenu\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_menu_new_value_02(self, mock_stdout):
        currentAclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction.setMenu('firstMenu')
        aclaction.setMenu('secondMenu')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), 'ACLGROUP;SETMENU;aclactionName;firstMenu|secondMenu\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_menu_two_new_value(self, mock_stdout):
        currentAclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        currentAclaction.setMenu('firstMenu')
        aclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction.setMenu('firstMenu')
        aclaction.setMenu('secondMenu')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), 'ACLGROUP;SETMENU;aclactionName;firstMenu|secondMenu\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_action_when_already_defined_and_same(self, mock_stdout):
        currentAclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        currentAclaction.setAction('actionValue')
        aclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction.setAction('actionValue')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), '')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_action_when__two_already_defined_and_same(self, mock_stdout):
        currentAclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        currentAclaction.setAction('firstAction')
        currentAclaction.setAction('secondAction')
        aclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction.setAction('firstAction')
        aclaction.setAction('secondAction')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), '')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_action_new_value_01(self, mock_stdout):
        currentAclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction.setAction('firstAction')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), 'ACLGROUP;SETACTION;aclactionName;firstAction\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_action_new_value_02(self, mock_stdout):
        currentAclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction.setAction('firstAction')
        aclaction.setAction('secondAction')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), 'ACLGROUP;SETACTION;aclactionName;firstAction|secondAction\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_action_two_new_value(self, mock_stdout):
        currentAclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        currentAclaction.setAction('firstAction')
        aclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction.setAction('firstAction')
        aclaction.setAction('secondAction')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), 'ACLGROUP;SETACTION;aclactionName;firstAction|secondAction\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_resource_when_already_defined_and_same(self, mock_stdout):
        currentAclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        currentAclaction.setResource('resourceValue')
        aclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction.setResource('resourceValue')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), '')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_resource_when__two_already_defined_and_same(self, mock_stdout):
        currentAclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        currentAclaction.setResource('firstResource')
        currentAclaction.setResource('secondResource')
        aclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction.setResource('firstResource')
        aclaction.setResource('secondResource')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), '')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_resource_new_value_01(self, mock_stdout):
        currentAclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction.setResource('firstResource')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), 'ACLGROUP;SETRESOURCE;aclactionName;firstResource\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_resource_new_value_02(self, mock_stdout):
        currentAclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction.setResource('firstResource')
        aclaction.setResource('secondResource')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), 'ACLGROUP;SETRESOURCE;aclactionName;firstResource|secondResource\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_resource_two_new_value(self, mock_stdout):
        currentAclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        currentAclaction.setResource('firstResource')
        aclaction = Aclgroup.Aclgroup('aclactionName', 'aclactionDescription')
        aclaction.setResource('firstResource')
        aclaction.setResource('secondResource')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), 'ACLGROUP;SETRESOURCE;aclactionName;firstResource|secondResource\n')


if __name__ == '__main__':
    logging.disable = True
    unittest.main()
