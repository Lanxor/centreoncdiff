
import logging
import unittest
import unittest.mock

import centreoncdiff.centreon.Aclmenu


class TestCentreonAclmenu03Parsing(unittest.TestCase):

    def setUp(self):
        logging.disable(logging.CRITICAL)

    def test_parse_line_wrong_object(self):
        data = centreoncdiff.centreon.Aclmenu.Aclmenu.parse('OTHER;ADD;menuName;menuAlias')
        self.assertEqual(data, {})

    def test_parse_line_add(self):
        data = centreoncdiff.centreon.Aclmenu.Aclmenu.parse('ACLMENU;ADD;menuName;menuAlias')
        self.assertEqual(data, {'object': 'ACLMENU', 'name': 'menuName', 'alias': 'menuAlias'})

    def test_parse_line_setparam_alias(self):
        data = centreoncdiff.centreon.Aclmenu.Aclmenu.parse('ACLMENU;SETPARAM;menuName;alias;newAlias')
        self.assertEqual(data, {'object': 'ACLMENU', 'name': 'menuName', 'alias': 'newAlias'})

    def test_parse_line_setparam_comment(self):
        data = centreoncdiff.centreon.Aclmenu.Aclmenu.parse('ACLMENU;SETPARAM;menuName;comment;newComment')
        self.assertEqual(data, {'object': 'ACLMENU', 'name': 'menuName', 'comment': 'newComment'})

    def test_parse_line_setparam_activate_0(self):
        data = centreoncdiff.centreon.Aclmenu.Aclmenu.parse('ACLMENU;SETPARAM;menuName;activate;0')
        self.assertEqual(data, {'object': 'ACLMENU', 'name': 'menuName', 'activate': '0'})

    def test_parse_line_setparam_activate_1(self):
        data = centreoncdiff.centreon.Aclmenu.Aclmenu.parse('ACLMENU;SETPARAM;menuName;activate;1')
        self.assertEqual(data, {'object': 'ACLMENU', 'name': 'menuName', 'activate': '1'})

    def test_parse_line_grantrw(self):
        data = centreoncdiff.centreon.Aclmenu.Aclmenu.parse('ACLMENU;GRANTRW;menuName;0;firstMenu')
        self.assertEqual(data, {'object': 'ACLMENU', 'name': 'menuName', 'grantrw': ['firstMenu']})

    def test_parse_line_grantro(self):
        data = centreoncdiff.centreon.Aclmenu.Aclmenu.parse('ACLMENU;GRANTRO;menuName;0;firstMenu')
        self.assertEqual(data, {'object': 'ACLMENU', 'name': 'menuName', 'grantro': ['firstMenu']})

    def test_parse_line_revoke(self):
        data = centreoncdiff.centreon.Aclmenu.Aclmenu.parse('ACLMENU;REVOKE;menuName;0;firstMenu')
        self.assertEqual(data, {'object': 'ACLMENU', 'name': 'menuName', 'revoke': ['firstMenu']})


if __name__ == '__main__':
    logging.disable = True
    unittest.main()
