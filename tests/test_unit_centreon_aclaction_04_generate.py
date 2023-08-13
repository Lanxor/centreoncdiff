
import logging
import io
import unittest
import unittest.mock

import centreoncdiff.centreon.Aclaction


class TestCentreonAclaction04Generate(unittest.TestCase):

    def setUp(self):
        logging.disable(logging.CRITICAL)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_minimal(self, mock_stdout):
        aclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLACTION;ADD;aclactionName;aclactionDescription\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_minimal_with_set_description(self, mock_stdout):
        aclmenu = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclmenu.setDescription('newDescription')
        aclmenu.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLACTION;ADD;aclactionName;newDescription\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_with_enable_status(self, mock_stdout):
        aclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.enable()
        aclaction.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLACTION;ADD;aclactionName;aclactionDescription\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_with_disable_status(self, mock_stdout):
        aclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.disable()
        aclaction.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLACTION;ADD;aclactionName;aclactionDescription\nACLACTION;SETPARAM;aclactionName;activate;0\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_with_set_grant(self, mock_stdout):
        aclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.setGrant('actionValue')
        aclaction.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLACTION;ADD;aclactionName;aclactionDescription\nACLACTION;GRANT;aclactionName;actionValue\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_with_two_set_grant(self, mock_stdout):
        aclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.setGrant('firstAction')
        aclaction.setGrant('secondAction')
        aclaction.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLACTION;ADD;aclactionName;aclactionDescription\nACLACTION;GRANT;aclactionName;firstAction|secondAction\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_with_set_grant_but_revoke_already_exist(self, mock_stdout):
        aclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.setRevoke('actionValue')
        aclaction.setGrant('actionValue')
        aclaction.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLACTION;ADD;aclactionName;aclactionDescription\nACLACTION;GRANT;aclactionName;actionValue\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_with_set_revoke(self, mock_stdout):
        aclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.setRevoke('actionValue')
        aclaction.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLACTION;ADD;aclactionName;aclactionDescription\nACLACTION;REVOKE;aclactionName;actionValue\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_with_two_set_revoke(self, mock_stdout):
        aclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.setRevoke('firstAction')
        aclaction.setRevoke('secondAction')
        aclaction.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLACTION;ADD;aclactionName;aclactionDescription\nACLACTION;REVOKE;aclactionName;firstAction|secondAction\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_with_set_revoke_but_grant_already_exist(self, mock_stdout):
        aclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.setGrant('actionValue')
        aclaction.setRevoke('actionValue')
        aclaction.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLACTION;ADD;aclactionName;aclactionDescription\nACLACTION;REVOKE;aclactionName;actionValue\n')


if __name__ == '__main__':
    logging.disable = True
    unittest.main()
