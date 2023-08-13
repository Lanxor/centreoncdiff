
import logging
import io
import unittest
import unittest.mock

import centreoncdiff.centreon.Aclaction


class TestCentreonAclaction05GenerateDiff(unittest.TestCase):

    def setUp(self):
        logging.disable(logging.CRITICAL)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_minimal_same(self, mock_stdout):
        currentAclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), '')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_minimal_description_update(self, mock_stdout):
        currentAclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'newDescription')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), 'ACLACTION;SETPARAM;aclactionName;description;newDescription\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_enable_when_already_enabled(self, mock_stdout):
        currentAclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        currentAclaction.enable()
        aclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.enable()
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), '')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_enable_when_disabled(self, mock_stdout):
        currentAclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        currentAclaction.disable()
        aclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.enable()
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), 'ACLACTION;SETPARAM;aclactionName;activate;1\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_grant_when_already_defined_and_same(self, mock_stdout):
        currentAclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        currentAclaction.setGrant('actionValue')
        aclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.setGrant('actionValue')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), '')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_grant_when_two_already_defined_and_same(self, mock_stdout):
        currentAclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        currentAclaction.setGrant('firstAction')
        currentAclaction.setGrant('secondAction')
        aclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.setGrant('firstAction')
        aclaction.setGrant('secondAction')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), '')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_grant_new_value_01(self, mock_stdout):
        currentAclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.setGrant('actionValue')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), 'ACLACTION;GRANT;aclactionName;actionValue\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_grant_new_value_02(self, mock_stdout):
        currentAclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        currentAclaction.setGrant('firstAction')
        aclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.setGrant('firstAction')
        aclaction.setGrant('secondAction')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), 'ACLACTION;GRANT;aclactionName;firstAction|secondAction\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_grant_two_new_value(self, mock_stdout):
        currentAclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        currentAclaction.setGrant('firstAction')
        aclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.setGrant('firstAction')
        aclaction.setGrant('secondAction')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), 'ACLACTION;GRANT;aclactionName;firstAction|secondAction\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_grant_replace_from_revoke(self, mock_stdout):
        currentAclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        currentAclaction.setRevoke('actionValue')
        aclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.setGrant('actionValue')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), 'ACLACTION;GRANT;aclactionName;actionValue\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_revoke_when_already_defined_and_same(self, mock_stdout):
        currentAclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        currentAclaction.setRevoke('actionValue')
        aclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.setRevoke('actionValue')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), '')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_revoke_when_two_already_defined_and_same(self, mock_stdout):
        currentAclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        currentAclaction.setRevoke('firstAction')
        currentAclaction.setRevoke('secondAction')
        aclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.setRevoke('firstAction')
        aclaction.setRevoke('secondAction')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), '')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_revoke_new_value_01(self, mock_stdout):
        currentAclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.setRevoke('actionValue')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), 'ACLACTION;REVOKE;aclactionName;actionValue\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_revoke_new_value_02(self, mock_stdout):
        currentAclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        currentAclaction.setRevoke('firstAction')
        aclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.setRevoke('firstAction')
        aclaction.setRevoke('secondAction')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), 'ACLACTION;REVOKE;aclactionName;firstAction|secondAction\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_revoke_two_new_value(self, mock_stdout):
        currentAclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.setRevoke('firstAction')
        aclaction.setRevoke('secondAction')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), 'ACLACTION;REVOKE;aclactionName;firstAction|secondAction\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_revoke_replace_from_grant(self, mock_stdout):
        currentAclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        currentAclaction.setGrant('actionValue')
        aclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
        aclaction.setRevoke('actionValue')
        aclaction.generate(currentAclaction)
        self.assertEqual(mock_stdout.getvalue(), 'ACLACTION;REVOKE;aclactionName;actionValue\n')

    # @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    # def test_generate_diff_revoke_replace_from_grantro(self, mock_stdout):
    #     currentAclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
    #     currentAclaction.setGrantRo('Home')
    #     aclaction = centreoncdiff.centreon.Aclaction.Aclaction('aclactionName', 'aclactionDescription')
    #     aclaction.setRevoke('Home')
    #     aclaction.generate(currentAclaction)
    #     self.assertEqual(mock_stdout.getvalue(), 'ACLACTION;REVOKE;aclactionName;0;Home\n')


if __name__ == '__main__':
    logging.disable = True
    unittest.main()
