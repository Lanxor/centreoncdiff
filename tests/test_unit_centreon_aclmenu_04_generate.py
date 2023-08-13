
import logging
import io
import unittest
import unittest.mock

import centreoncdiff.centreon.Aclmenu


class TestCentreonAclmenu04Generate(unittest.TestCase):

    def setUp(self):
        logging.disable(logging.CRITICAL)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_minimal(self, mock_stdout):
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLMENU;ADD;aclmenuName;aclmenuAlias\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_minimal_with_set_alias(self, mock_stdout):
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.setAlias('newAlias')
        aclmenu.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLMENU;ADD;aclmenuName;newAlias\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_with_enable_status(self, mock_stdout):
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.enable()
        aclmenu.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLMENU;ADD;aclmenuName;aclmenuAlias\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_with_disable_status(self, mock_stdout):
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.disable()
        aclmenu.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLMENU;ADD;aclmenuName;aclmenuAlias\nACLMENU;SETPARAM;aclmenuName;activate;0\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_with_comment(self, mock_stdout):
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.setComment('commentValue')
        aclmenu.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLMENU;ADD;aclmenuName;aclmenuAlias\nACLMENU;SETPARAM;aclmenuName;comment;commentValue\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_with_none_comment(self, mock_stdout):
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.setComment(None)
        aclmenu.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLMENU;ADD;aclmenuName;aclmenuAlias\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_with_set_grantrw(self, mock_stdout):
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.setGrantRw('menuValue')
        aclmenu.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLMENU;ADD;aclmenuName;aclmenuAlias\nACLMENU;GRANTRW;aclmenuName;0;menuValue\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_with_set_grantrw_but_grantro_already_exist(self, mock_stdout):
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.setGrantRo('menuValue')
        aclmenu.setGrantRw('menuValue')
        aclmenu.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLMENU;ADD;aclmenuName;aclmenuAlias\nACLMENU;GRANTRW;aclmenuName;0;menuValue\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_with_set_grantrw_but_revoke_already_exist(self, mock_stdout):
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.setRevoke('menuValue')
        aclmenu.setGrantRw('menuValue')
        aclmenu.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLMENU;ADD;aclmenuName;aclmenuAlias\nACLMENU;GRANTRW;aclmenuName;0;menuValue\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_with_set_grantro(self, mock_stdout):
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.setGrantRo('menuValue')
        aclmenu.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLMENU;ADD;aclmenuName;aclmenuAlias\nACLMENU;GRANTRO;aclmenuName;0;menuValue\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_with_set_grantro_but_grantrw_already_exist(self, mock_stdout):
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.setGrantRw('menuValue')
        aclmenu.setGrantRo('menuValue')
        aclmenu.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLMENU;ADD;aclmenuName;aclmenuAlias\nACLMENU;GRANTRO;aclmenuName;0;menuValue\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_with_set_grantro_but_revoke_already_exist(self, mock_stdout):
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.setRevoke('menuValue')
        aclmenu.setGrantRo('menuValue')
        aclmenu.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLMENU;ADD;aclmenuName;aclmenuAlias\nACLMENU;GRANTRO;aclmenuName;0;menuValue\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_with_set_revoke(self, mock_stdout):
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.setRevoke('menuValue')
        aclmenu.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLMENU;ADD;aclmenuName;aclmenuAlias\nACLMENU;REVOKE;aclmenuName;0;menuValue\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_with_set_revoke_but_grantrw_already_exist(self, mock_stdout):
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.setGrantRw('menuValue')
        aclmenu.setRevoke('menuValue')
        aclmenu.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLMENU;ADD;aclmenuName;aclmenuAlias\nACLMENU;REVOKE;aclmenuName;0;menuValue\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_with_set_revoke_but_grantro_already_exist(self, mock_stdout):
        aclmenu = centreoncdiff.centreon.Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.setGrantRo('menuValue')
        aclmenu.setRevoke('menuValue')
        aclmenu.generate()
        self.assertEqual(mock_stdout.getvalue(), 'ACLMENU;ADD;aclmenuName;aclmenuAlias\nACLMENU;REVOKE;aclmenuName;0;menuValue\n')


if __name__ == '__main__':
    logging.disable = True
    unittest.main()
