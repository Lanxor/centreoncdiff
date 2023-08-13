
import logging
import io
import unittest
import unittest.mock

import centreoncdiff.centreon.Aclmenu


class TestCentreonAclmenu05GenerateDiff(unittest.TestCase):

    def setUp(self):
        logging.disable(logging.CRITICAL)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_minimal_same(self, mock_stdout):
        currentAclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.generate(currentAclmenu)
        self.assertEqual(mock_stdout.getvalue(), '')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_minimal_alias_update(self, mock_stdout):
        currentAclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'newAlias')
        aclmenu.generate(currentAclmenu)
        self.assertEqual(mock_stdout.getvalue(), 'ACLMENU;SETPARAM;aclmenuName;alias;newAlias\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_enable_when_already_enabled(self, mock_stdout):
        currentAclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        currentAclmenu.enable()
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.enable()
        aclmenu.generate(currentAclmenu)
        self.assertEqual(mock_stdout.getvalue(), '')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_enable_when_disabled(self, mock_stdout):
        currentAclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        currentAclmenu.disable()
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.enable()
        aclmenu.generate(currentAclmenu)
        self.assertEqual(mock_stdout.getvalue(), 'ACLMENU;SETPARAM;aclmenuName;activate;1\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_comment_when_already_defined_and_same(self, mock_stdout):
        currentAclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        currentAclmenu.setComment('commentValue')
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.setComment('commentValue')
        aclmenu.generate(currentAclmenu)
        self.assertEqual(mock_stdout.getvalue(), '')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_comment_when_already_defined_and_different(self, mock_stdout):
        currentAclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        currentAclmenu.setComment('commentValue')
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.setComment('newValue')
        aclmenu.generate(currentAclmenu)
        self.assertEqual(mock_stdout.getvalue(), 'ACLMENU;SETPARAM;aclmenuName;comment;newValue\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_grantrw_when_already_defined_and_same(self, mock_stdout):
        currentAclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        currentAclmenu.setGrantRw('Home')
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.setGrantRw('Home')
        aclmenu.generate(currentAclmenu)
        self.assertEqual(mock_stdout.getvalue(), '')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_grantrw_new_value(self, mock_stdout):
        currentAclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        currentAclmenu.setGrantRw('Home')
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.setGrantRw('Home')
        aclmenu.setGrantRw('Configuration')
        aclmenu.generate(currentAclmenu)
        self.assertEqual(mock_stdout.getvalue(), 'ACLMENU;GRANTRW;aclmenuName;0;Configuration\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_grantrw_replace_from_grantro(self, mock_stdout):
        currentAclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        currentAclmenu.setGrantRo('Home')
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.setGrantRw('Home')
        aclmenu.generate(currentAclmenu)
        self.assertEqual(mock_stdout.getvalue(), 'ACLMENU;GRANTRW;aclmenuName;0;Home\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_grantrw_replace_from_revoke(self, mock_stdout):
        currentAclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        currentAclmenu.setRevoke('Home')
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.setGrantRw('Home')
        aclmenu.generate(currentAclmenu)
        self.assertEqual(mock_stdout.getvalue(), 'ACLMENU;GRANTRW;aclmenuName;0;Home\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_grantro_when_already_defined_and_same(self, mock_stdout):
        currentAclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        currentAclmenu.setGrantRo('Home')
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.setGrantRo('Home')
        aclmenu.generate(currentAclmenu)
        self.assertEqual(mock_stdout.getvalue(), '')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_grantro_new_value(self, mock_stdout):
        currentAclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        currentAclmenu.setGrantRo('Home')
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.setGrantRo('Home')
        aclmenu.setGrantRo('Configuration')
        aclmenu.generate(currentAclmenu)
        self.assertEqual(mock_stdout.getvalue(), 'ACLMENU;GRANTRO;aclmenuName;0;Configuration\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_grantro_replace_from_grantrw(self, mock_stdout):
        currentAclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        currentAclmenu.setGrantRw('Home')
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.setGrantRo('Home')
        aclmenu.generate(currentAclmenu)
        self.assertEqual(mock_stdout.getvalue(), 'ACLMENU;GRANTRO;aclmenuName;0;Home\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_grantro_replace_from_revoke(self, mock_stdout):
        currentAclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        currentAclmenu.setRevoke('Home')
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.setGrantRo('Home')
        aclmenu.generate(currentAclmenu)
        self.assertEqual(mock_stdout.getvalue(), 'ACLMENU;GRANTRO;aclmenuName;0;Home\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_revoke_when_already_defined_and_same(self, mock_stdout):
        currentAclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        currentAclmenu.setRevoke('Home')
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.setRevoke('Home')
        aclmenu.generate(currentAclmenu)
        self.assertEqual(mock_stdout.getvalue(), '')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_revoke_new_value(self, mock_stdout):
        currentAclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        currentAclmenu.setRevoke('Home')
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.setRevoke('Home')
        aclmenu.setRevoke('Configuration')
        aclmenu.generate(currentAclmenu)
        self.assertEqual(mock_stdout.getvalue(), 'ACLMENU;REVOKE;aclmenuName;0;Configuration\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_revoke_replace_from_grantrw(self, mock_stdout):
        currentAclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        currentAclmenu.setGrantRw('Home')
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.setRevoke('Home')
        aclmenu.generate(currentAclmenu)
        self.assertEqual(mock_stdout.getvalue(), 'ACLMENU;REVOKE;aclmenuName;0;Home\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_diff_revoke_replace_from_grantro(self, mock_stdout):
        currentAclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        currentAclmenu.setGrantRo('Home')
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.setRevoke('Home')
        aclmenu.generate(currentAclmenu)
        self.assertEqual(mock_stdout.getvalue(), 'ACLMENU;REVOKE;aclmenuName;0;Home\n')


if __name__ == '__main__':
    logging.disable = True
    unittest.main()
