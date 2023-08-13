
import logging
import unittest
import unittest.mock

from centreoncdiff.centreon.Aclaction import Aclaction
from centreoncdiff.centreon.Aclgroup import Aclgroup
from centreoncdiff.centreon.Aclmenu import Aclmenu
from centreoncdiff.parser import parse_export


class TestCentreonExportparser(unittest.TestCase):

    def setUp(self):
        logging.disable(logging.CRITICAL)

    def test_parse_aclaction_export(self):
        with open('tests/data/export_aclaction.txt', 'rt') as exportData:
            data = parse_export(exportData.read())
        self.assertIn('ACLACTION', data)
        self.assertIn('actionName', data['ACLACTION'])
        self.assertIsInstance(data['ACLACTION']['actionName'], Aclaction)
        self.assertEqual(data['ACLACTION']['actionName']._name, 'actionName')
        self.assertEqual(data['ACLACTION']['actionName']._description, 'actionDescription')
        self.assertEqual(data['ACLACTION']['actionName']._grant, ['firstAction', 'secondAction'])
        self.assertEqual(data['ACLACTION']['actionName']._revoke, ['thirdAction', 'fourthAction'])

    def test_parse_aclgroup_export(self):
        with open('tests/data/export_aclgroup.txt', 'rt') as exportData:
            data = parse_export(exportData.read())
        self.assertIn('ACLGROUP', data)
        self.assertIn('groupName', data['ACLGROUP'])
        self.assertIsInstance(data['ACLGROUP']['groupName'], Aclgroup)
        self.assertEqual(data['ACLGROUP']['groupName']._name, 'groupName')
        self.assertEqual(data['ACLGROUP']['groupName']._alias, 'groupAlias')

    def test_parse_aclmenu_export(self):
        with open('tests/data/export_aclmenu.txt', 'rt') as exportData:
            data = parse_export(exportData.read())
        self.assertIn('ACLMENU', data)
        self.assertIn('menuName', data['ACLMENU'])
        self.assertIsInstance(data['ACLMENU']['menuName'], Aclmenu)
        self.assertEqual(data['ACLMENU']['menuName']._name, 'menuName')
        self.assertEqual(data['ACLMENU']['menuName']._alias, 'menuAlias')
        self.assertEqual(data['ACLMENU']['menuName']._activate, False)
        self.assertEqual(data['ACLMENU']['menuName']._comment, 'menuComment')
        self.assertEqual(data['ACLMENU']['menuName']._grantrw, ['firstMenu', 'secondMenu'])
        self.assertEqual(data['ACLMENU']['menuName']._grantro, ['thirdMenu', 'fourthMenu'])
        self.assertEqual(data['ACLMENU']['menuName']._revoke, ['fifthMenu', 'sixthMenu'])

    def test_parse_complete_export(self):
        with open('tests/data/export_complete_export.txt', 'rt') as exportData:
            data = parse_export(exportData.read())

        self.assertIn('ACLACTION', data)
        self.assertIn('actionName', data['ACLACTION'])
        self.assertIsInstance(data['ACLACTION']['actionName'], Aclaction)
        self.assertEqual(data['ACLACTION']['actionName']._name, 'actionName')
        self.assertEqual(data['ACLACTION']['actionName']._description, 'actionDescription')
        self.assertEqual(data['ACLACTION']['actionName']._grant, ['firstAction', 'secondAction'])
        self.assertEqual(data['ACLACTION']['actionName']._revoke, ['thirdAction', 'fourthAction'])

        self.assertIn('ACLGROUP', data)
        self.assertIn('groupName', data['ACLGROUP'])
        self.assertIsInstance(data['ACLGROUP']['groupName'], Aclgroup)
        self.assertEqual(data['ACLGROUP']['groupName']._name, 'groupName')
        self.assertEqual(data['ACLGROUP']['groupName']._alias, 'groupAlias')

        self.assertIn('ACLMENU', data)
        self.assertIn('menuName', data['ACLMENU'])
        self.assertIsInstance(data['ACLMENU']['menuName'], Aclmenu)
        self.assertEqual(data['ACLMENU']['menuName']._name, 'menuName')
        self.assertEqual(data['ACLMENU']['menuName']._alias, 'menuAlias')
        self.assertEqual(data['ACLMENU']['menuName']._activate, False)
        self.assertEqual(data['ACLMENU']['menuName']._comment, 'menuComment')
        self.assertEqual(data['ACLMENU']['menuName']._grantrw, ['firstMenu', 'secondMenu'])
        self.assertEqual(data['ACLMENU']['menuName']._grantro, ['thirdMenu', 'fourthMenu'])
        self.assertEqual(data['ACLMENU']['menuName']._revoke, ['fifthMenu', 'sixthMenu'])


if __name__ == '__main__':
    unittest.main()
