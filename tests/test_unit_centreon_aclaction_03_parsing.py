
import logging
import unittest
import unittest.mock

import centreoncdiff.centreon.Aclaction


class TestCentreonAclaction03Parsing(unittest.TestCase):

    def setUp(self):
        logging.disable(logging.CRITICAL)

    def test_parse_line_wrong_object(self):
        data = centreoncdiff.centreon.Aclaction.Aclaction.parse('OTHER;ADD;actionName;actionDescription')
        self.assertEqual(data, {})

    def test_parse_line_add(self):
        data = centreoncdiff.centreon.Aclaction.Aclaction.parse('ACLACTION;ADD;actionName;actionDescription')
        self.assertEqual(data, {'object': 'ACLACTION', 'name': 'actionName', 'description': 'actionDescription'})

    def test_parse_line_setparam_description(self):
        data = centreoncdiff.centreon.Aclaction.Aclaction.parse('ACLACTION;SETPARAM;actionName;description;newDescription')
        self.assertEqual(data, {'object': 'ACLACTION', 'name': 'actionName', 'description': 'newDescription'})

    def test_parse_line_setparam_activate_0(self):
        data = centreoncdiff.centreon.Aclaction.Aclaction.parse('ACLACTION;SETPARAM;actionName;activate;0')
        self.assertEqual(data, {'object': 'ACLACTION', 'name': 'actionName', 'activate': '0'})

    def test_parse_line_setparam_activate_1(self):
        data = centreoncdiff.centreon.Aclaction.Aclaction.parse('ACLACTION;SETPARAM;actionName;activate;1')
        self.assertEqual(data, {'object': 'ACLACTION', 'name': 'actionName', 'activate': '1'})

    def test_parse_line_grant(self):
        data = centreoncdiff.centreon.Aclaction.Aclaction.parse('ACLACTION;GRANT;actionName;firstAction')
        self.assertEqual(data, {'object': 'ACLACTION', 'name': 'actionName', 'grant': ['firstAction']})

    def test_parse_line_two_grant(self):
        data = centreoncdiff.centreon.Aclaction.Aclaction.parse('ACLACTION;GRANT;actionName;firstAction|secondAction')
        self.assertEqual(data, {'object': 'ACLACTION', 'name': 'actionName', 'grant': ['firstAction', 'secondAction']})

    def test_parse_line_revoke(self):
        data = centreoncdiff.centreon.Aclaction.Aclaction.parse('ACLACTION;REVOKE;actionName;firstAction')
        self.assertEqual(data, {'object': 'ACLACTION', 'name': 'actionName', 'revoke': ['firstAction']})

    def test_parse_line_two_revoke(self):
        data = centreoncdiff.centreon.Aclaction.Aclaction.parse('ACLACTION;REVOKE;actionName;firstAction|secondAction')
        self.assertEqual(data, {'object': 'ACLACTION', 'name': 'actionName', 'revoke': ['firstAction', 'secondAction']})


if __name__ == '__main__':
    logging.disable = True
    unittest.main()
