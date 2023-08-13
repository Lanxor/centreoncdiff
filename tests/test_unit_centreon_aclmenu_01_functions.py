
import logging
import unittest
import unittest.mock

import centreoncdiff.centreon.Aclmenu as Aclmenu


class TestCentreonAclmenu01Functions(unittest.TestCase):

    def setUp(self):
        logging.disable(logging.CRITICAL)

    def test_object_init(self):
        aclmenu = Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        self.assertEqual(aclmenu._name, 'aclmenuName')
        self.assertEqual(aclmenu._alias, 'aclmenuAlias')
        self.assertEqual(aclmenu._activate, True)
        self.assertEqual(aclmenu._comment, None)
        self.assertEqual(aclmenu._grantrw, [])
        self.assertEqual(aclmenu._grantro, [])
        self.assertEqual(aclmenu._revoke, [])

    def test_set_alias(self):
        aclmenu = Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.setAlias('newAlias')
        self.assertEqual(aclmenu._alias, 'newAlias')

    def test_enable(self):
        aclmenu = Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.enable()
        self.assertEqual(aclmenu._activate, True)

    def test_disable(self):
        aclmenu = Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.disable()
        self.assertEqual(aclmenu._activate, False)

    def test_set_comment(self):
        aclmenu = Aclmenu.Aclmenu('aclmenuName', 'aclmenuAlias')
        aclmenu.setComment('myComment')
        self.assertEqual(aclmenu._comment, 'myComment')

    def test_set_grantrw(self):
        aclmenu = Aclmenu.Aclmenu('aclmenuName', 'aclmenuDescription')
        aclmenu.setGrantRw('firstMenu')
        self.assertEqual(aclmenu._grantrw, ['firstMenu'])
        self.assertEqual(aclmenu._grantro, [])
        self.assertEqual(aclmenu._revoke, [])

    def test_set_two_grantrw(self):
        aclmenu = Aclmenu.Aclmenu('aclmenuName', 'aclmenuDescription')
        aclmenu.setGrantRw('firstMenu')
        aclmenu.setGrantRw('secondMenu')
        self.assertEqual(aclmenu._grantrw, ['firstMenu', 'secondMenu'])
        self.assertEqual(aclmenu._grantro, [])
        self.assertEqual(aclmenu._revoke, [])

    def test_set_grantrw_with_grantro_already_defined(self):
        aclmenu = Aclmenu.Aclmenu('aclmenuName', 'aclmenuDescription')
        aclmenu.setGrantRo('firstMenu')
        aclmenu.setGrantRw('firstMenu')
        self.assertEqual(aclmenu._grantrw, ['firstMenu'])
        self.assertEqual(aclmenu._grantro, [])
        self.assertEqual(aclmenu._revoke, [])

    def test_set_grantrw_with_two_grantro_already_defined(self):
        aclmenu = Aclmenu.Aclmenu('aclmenuName', 'aclmenuDescription')
        aclmenu.setGrantRo('firstMenu')
        aclmenu.setGrantRo('secondMenu')
        aclmenu.setGrantRw('firstMenu')
        self.assertEqual(aclmenu._grantrw, ['firstMenu'])
        self.assertEqual(aclmenu._grantro, ['secondMenu'])
        self.assertEqual(aclmenu._revoke, [])

    def test_set_grantrw_with_revoke_already_defined(self):
        aclmenu = Aclmenu.Aclmenu('aclmenuName', 'aclmenuDescription')
        aclmenu.setRevoke('firstMenu')
        aclmenu.setGrantRw('firstMenu')
        self.assertEqual(aclmenu._grantrw, ['firstMenu'])
        self.assertEqual(aclmenu._grantro, [])
        self.assertEqual(aclmenu._revoke, [])

    def test_set_grantrw_with_two_revoke_already_defined(self):
        aclmenu = Aclmenu.Aclmenu('aclmenuName', 'aclmenuDescription')
        aclmenu.setRevoke('firstMenu')
        aclmenu.setRevoke('secondMenu')
        aclmenu.setGrantRw('firstMenu')
        self.assertEqual(aclmenu._grantrw, ['firstMenu'])
        self.assertEqual(aclmenu._grantro, [])
        self.assertEqual(aclmenu._revoke, ['secondMenu'])

    def test_set_grantro(self):
        aclmenu = Aclmenu.Aclmenu('aclmenuName', 'aclmenuDescription')
        aclmenu.setGrantRw('firstMenu')
        self.assertEqual(aclmenu._grantrw, ['firstMenu'])
        self.assertEqual(aclmenu._grantro, [])
        self.assertEqual(aclmenu._revoke, [])

    def test_set_two_grantro(self):
        aclmenu = Aclmenu.Aclmenu('aclmenuName', 'aclmenuDescription')
        aclmenu.setGrantRo('firstMenu')
        aclmenu.setGrantRo('secondMenu')
        self.assertEqual(aclmenu._grantrw, [])
        self.assertEqual(aclmenu._grantro, ['firstMenu', 'secondMenu'])
        self.assertEqual(aclmenu._revoke, [])

    def test_set_grantro_with_grantrw_already_defined(self):
        aclmenu = Aclmenu.Aclmenu('aclmenuName', 'aclmenuDescription')
        aclmenu.setGrantRw('firstMenu')
        aclmenu.setGrantRo('firstMenu')
        self.assertEqual(aclmenu._grantrw, [])
        self.assertEqual(aclmenu._grantro, ['firstMenu'])
        self.assertEqual(aclmenu._revoke, [])

    def test_set_grantro_with_two_grantrw_already_defined(self):
        aclmenu = Aclmenu.Aclmenu('aclmenuName', 'aclmenuDescription')
        aclmenu.setGrantRw('firstMenu')
        aclmenu.setGrantRw('secondMenu')
        aclmenu.setGrantRo('firstMenu')
        self.assertEqual(aclmenu._grantrw, ['secondMenu'])
        self.assertEqual(aclmenu._grantro, ['firstMenu'])
        self.assertEqual(aclmenu._revoke, [])

    def test_set_grantro_with_revoke_already_defined(self):
        aclmenu = Aclmenu.Aclmenu('aclmenuName', 'aclmenuDescription')
        aclmenu.setRevoke('firstMenu')
        aclmenu.setGrantRo('firstMenu')
        self.assertEqual(aclmenu._grantrw, [])
        self.assertEqual(aclmenu._grantro, ['firstMenu'])
        self.assertEqual(aclmenu._revoke, [])

    def test_set_grantro_with_two_revoke_already_defined(self):
        aclmenu = Aclmenu.Aclmenu('aclmenuName', 'aclmenuDescription')
        aclmenu.setRevoke('firstMenu')
        aclmenu.setRevoke('secondMenu')
        aclmenu.setGrantRo('firstMenu')
        self.assertEqual(aclmenu._grantrw, [])
        self.assertEqual(aclmenu._grantro, ['firstMenu'])
        self.assertEqual(aclmenu._revoke, ['secondMenu'])

    def test_set_revoke(self):
        aclmenu = Aclmenu.Aclmenu('aclmenuName', 'aclmenuDescription')
        aclmenu.setRevoke('firstMenu')
        self.assertEqual(aclmenu._grantrw, [])
        self.assertEqual(aclmenu._grantro, [])
        self.assertEqual(aclmenu._revoke, ['firstMenu'])

    def test_set_two_revoke(self):
        aclmenu = Aclmenu.Aclmenu('aclmenuName', 'aclmenuDescription')
        aclmenu.setRevoke('firstMenu')
        aclmenu.setRevoke('secondMenu')
        self.assertEqual(aclmenu._grantrw, [])
        self.assertEqual(aclmenu._grantro, [])
        self.assertEqual(aclmenu._revoke, ['firstMenu', 'secondMenu'])

    def test_set_revoke_with_grantrw_already_defined(self):
        aclmenu = Aclmenu.Aclmenu('aclmenuName', 'aclmenuDescription')
        aclmenu.setGrantRw('firstMenu')
        aclmenu.setRevoke('firstMenu')
        self.assertEqual(aclmenu._grantrw, [])
        self.assertEqual(aclmenu._grantro, [])
        self.assertEqual(aclmenu._revoke, ['firstMenu'])

    def test_set_revoke_with_two_grantrw_already_defined(self):
        aclmenu = Aclmenu.Aclmenu('aclmenuName', 'aclmenuDescription')
        aclmenu.setGrantRw('firstMenu')
        aclmenu.setGrantRw('secondMenu')
        aclmenu.setRevoke('firstMenu')
        self.assertEqual(aclmenu._grantrw, ['secondMenu'])
        self.assertEqual(aclmenu._grantro, [])
        self.assertEqual(aclmenu._revoke, ['firstMenu'])

    def test_set_revoke_with_grantro_already_defined(self):
        aclmenu = Aclmenu.Aclmenu('aclmenuName', 'aclmenuDescription')
        aclmenu.setGrantRo('firstMenu')
        aclmenu.setRevoke('firstMenu')
        self.assertEqual(aclmenu._grantrw, [])
        self.assertEqual(aclmenu._grantro, [])
        self.assertEqual(aclmenu._revoke, ['firstMenu'])

    def test_set_revoke_with_two_grantro_already_defined(self):
        aclmenu = Aclmenu.Aclmenu('aclmenuName', 'aclmenuDescription')
        aclmenu.setGrantRo('firstMenu')
        aclmenu.setGrantRo('secondMenu')
        aclmenu.setRevoke('firstMenu')
        self.assertEqual(aclmenu._grantrw, [])
        self.assertEqual(aclmenu._grantro, ['secondMenu'])
        self.assertEqual(aclmenu._revoke, ['firstMenu'])


if __name__ == '__main__':
    logging.disable = True
    unittest.main()
