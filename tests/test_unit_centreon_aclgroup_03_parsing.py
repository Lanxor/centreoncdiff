
import logging
import unittest
import unittest.mock

import centreoncdiff.centreon.Aclgroup


class TestCentreonAclgroup03Parsing(unittest.TestCase):

    def setUp(self):
        logging.disable(logging.CRITICAL)

    def test_parse_line_wrong_object(self):
        data = centreoncdiff.centreon.Aclgroup.Aclgroup.parse('OTHER;ADD;groupName;groupAlias')
        self.assertEqual(data, {})

    def test_parse_line_add(self):
        data = centreoncdiff.centreon.Aclgroup.Aclgroup.parse('ACLGROUP;ADD;groupName;groupAlias')
        self.assertEqual(data, {'object': 'ACLGROUP', 'name': 'groupName', 'alias': 'groupAlias'})

    def test_parse_line_setparam_alias(self):
        data = centreoncdiff.centreon.Aclgroup.Aclgroup.parse('ACLGROUP;SETPARAM;groupName;alias;newAlias')
        self.assertEqual(data, {'object': 'ACLGROUP', 'name': 'groupName', 'alias': 'newAlias'})

    def test_parse_line_setparam_comment(self):
        data = centreoncdiff.centreon.Aclgroup.Aclgroup.parse('ACLGROUP;SETPARAM;groupName;comment;newComment')
        self.assertEqual(data, {'object': 'ACLGROUP', 'name': 'groupName', 'comment': 'newComment'})

    def test_parse_line_setparam_activate_0(self):
        data = centreoncdiff.centreon.Aclgroup.Aclgroup.parse('ACLGROUP;SETPARAM;groupName;activate;0')
        self.assertEqual(data, {'object': 'ACLGROUP', 'name': 'groupName', 'activate': '0'})

    def test_parse_line_setparam_activate_1(self):
        data = centreoncdiff.centreon.Aclgroup.Aclgroup.parse('ACLGROUP;SETPARAM;groupName;activate;1')
        self.assertEqual(data, {'object': 'ACLGROUP', 'name': 'groupName', 'activate': '1'})

    def test_parse_line_setcontact_one(self):
        data = centreoncdiff.centreon.Aclgroup.Aclgroup.parse('ACLGROUP;SETCONTACT;groupName;contactOne')
        self.assertEqual(data, {'object': 'ACLGROUP', 'name': 'groupName', 'contact': ['contactOne']})

    def test_parse_line_setcontact_two(self):
        data = centreoncdiff.centreon.Aclgroup.Aclgroup.parse('ACLGROUP;SETCONTACT;groupName;contactOne|contactTwo')
        self.assertEqual(data, {'object': 'ACLGROUP', 'name': 'groupName', 'contact': ['contactOne', 'contactTwo']})

    def test_parse_line_setcontactgroup_one(self):
        data = centreoncdiff.centreon.Aclgroup.Aclgroup.parse('ACLGROUP;SETCONTACTGROUP;groupName;contactgroupOne')
        self.assertEqual(data, {'object': 'ACLGROUP', 'name': 'groupName', 'contactgroup': ['contactgroupOne']})

    def test_parse_line_setcontactgroup_two(self):
        data = centreoncdiff.centreon.Aclgroup.Aclgroup.parse('ACLGROUP;SETCONTACTGROUP;groupName;contactgroupOne|contactgroupTwo')
        self.assertEqual(data, {'object': 'ACLGROUP', 'name': 'groupName', 'contactgroup': ['contactgroupOne', 'contactgroupTwo']})

    def test_parse_line_setmenu_one(self):
        data = centreoncdiff.centreon.Aclgroup.Aclgroup.parse('ACLGROUP;SETMENU;groupName;menuOne')
        self.assertEqual(data, {'object': 'ACLGROUP', 'name': 'groupName', 'menu': ['menuOne']})

    def test_parse_line_setmenu_two(self):
        data = centreoncdiff.centreon.Aclgroup.Aclgroup.parse('ACLGROUP;SETMENU;groupName;menuOne|menuTwo')
        self.assertEqual(data, {'object': 'ACLGROUP', 'name': 'groupName', 'menu': ['menuOne', 'menuTwo']})

    def test_parse_line_setaction_one(self):
        data = centreoncdiff.centreon.Aclgroup.Aclgroup.parse('ACLGROUP;SETACTION;groupName;actionOne')
        self.assertEqual(data, {'object': 'ACLGROUP', 'name': 'groupName', 'action': ['actionOne']})

    def test_parse_line_setaction_two(self):
        data = centreoncdiff.centreon.Aclgroup.Aclgroup.parse('ACLGROUP;SETACTION;groupName;actionOne|actionTwo')
        self.assertEqual(data, {'object': 'ACLGROUP', 'name': 'groupName', 'action': ['actionOne', 'actionTwo']})

    def test_parse_line_setresource_one(self):
        data = centreoncdiff.centreon.Aclgroup.Aclgroup.parse('ACLGROUP;SETRESOURCE;groupName;resourceOne')
        self.assertEqual(data, {'object': 'ACLGROUP', 'name': 'groupName', 'resource': ['resourceOne']})

    def test_parse_line_setresource_two(self):
        data = centreoncdiff.centreon.Aclgroup.Aclgroup.parse('ACLGROUP;SETRESOURCE;groupName;resourceOne|resourceTwo')
        self.assertEqual(data, {'object': 'ACLGROUP', 'name': 'groupName', 'resource': ['resourceOne', 'resourceTwo']})


if __name__ == '__main__':
    logging.disable = True
    unittest.main()
