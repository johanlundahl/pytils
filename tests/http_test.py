from datetime import datetime
import unittest
import operator
from pytils.http import Filter
from pytils import http
from unittest.mock import patch, Mock


class FilterTest(unittest.TestCase):

    def test_value_parse_int(self):
        val = Filter.value_parse('12', ignore_type=False)
        self.assertEqual(val, 12)

    def test_value_parse_int_ignore_type(self):
        val = Filter.value_parse('11', ignore_type=True)
        self.assertEqual(val, '11')

    def test_value_parse_date(self):
        date = Filter.value_parse('2020-10-10', ignore_type=False)
        self.assertEqual(date, datetime.strptime('2020-10-10', '%Y-%m-%d'))

    def test_value_parse_date_ignore_type(self):
        val = Filter.value_parse('2020-01-23', ignore_type=True)
        self.assertEqual(val, '2020-01-23')

    @patch('requests.get')
    def test_get(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = 'Some response'
        mock_get.return_value = mock_response

        status_code, content = http.get('http://yadayada.blah')
        self.assertEqual(status_code, 200)
        self.assertTrue(isinstance(content, str))

    @patch('requests.get')
    def test_get_json(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json = Mock(return_value={'name': 'John', 'age': 42})
        mock_get.return_value = mock_response

        status_code, content = http.get_json('http://yadayada.blah')
        self.assertEqual(dict, type(content))
        self.assertEqual(status_code, 200)

    @patch('requests.post')
    def test_post_json(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = 'A responding text'
        mock_post.return_value = mock_response

        status_code, content = http.post_json('http://yadayada.blah',
                                              {'fake': 'value'})
        self.assertEqual(str, type(content))
        self.assertEqual(status_code, 200)

    def test_value_parse_datetime_ignore_type(self):
        pass

    def test_parse_datetime(self):
        pass

    def test_to_json_contains_keys(self):
        a_filter = Filter('date')
        result = a_filter.to_json()
        self.assertTrue('field' in result.keys())
        self.assertTrue('op' in result.keys())
        self.assertTrue('value' in result.keys())

    def test_to_json_field(self):
        a_filter = Filter('date')
        result = a_filter.to_json()
        self.assertEqual(result['field'], a_filter.name)

    def test_to_json_value(self):
        a_filter = Filter('date', value=12)
        result = a_filter.to_json()
        self.assertEqual(result['value'], a_filter.value)

    def test_to_json_default_operator(self):
        a_filter = Filter('date')
        result = a_filter.to_json()
        self.assertEqual(result['op'], '==')

    def test_to_json_operator(self):
        self.assertEqual(Filter('date', operator='lt').to_json()['op'], '<')
        self.assertEqual(Filter('date', operator='le').to_json()['op'], '<=')
        self.assertEqual(Filter('date', operator='eq').to_json()['op'], '==')
        self.assertEqual(Filter('date', operator='ne').to_json()['op'], '!=')
        self.assertEqual(Filter('date', operator='gt').to_json()['op'], '>')
        self.assertEqual(Filter('date', operator='ge').to_json()['op'], '>=')

    def test_split_name_without_operator(self):
        name, operator = Filter.split_name_operator('name')
        self.assertEqual('name', name)

    def test_split_name_with_operator(self):
        name, operator = Filter.split_name_operator('name[eq]')
        self.assertEqual('name', name)
        self.assertEqual('eq', operator)

    def test_filter_from_querystring(self):
        pass

    def test_filter_from_non_operator_arg(self):
        pair = Filter.from_arg('name', '12')
        self.assertEqual('name', pair.name)
        self.assertEqual(12, pair.value)
        self.assertEqual(operator.eq, pair.operator)

    def test_filter_from_gt_operator_arg(self):
        pair = Filter.from_arg('age[gt]', '18')
        self.assertEqual('age', pair.name)
        self.assertEqual(18, pair.value)
        self.assertEqual(operator.gt, pair.operator)

    def test_filter_evaluate(self):
        f = Filter('age', 'lt', 65)
        self.assertTrue(f.evaluate(64))
        self.assertFalse(f.evaluate(65))

    def test_filter_ags_matching(self):
        params = {'name': 12, 'age': 12,
                  'address': 'street', 'ages': 20, 'age[lt]': 65}
        args = Filter.args_matching(params, 'age')
        self.assertEqual(len(args), 2)

    @unittest.skip
    @patch('flask.request.args')
    def test_validate_querystring_positive(self, mock_args):

        @http.validate_querystrings(method='GET', parameters=['name', 'age'])
        def decorated():
            return 'fine', 200

        # with app.test_request_context():
        mock_args.return_value = {'name': 'john', 'age': 22}
        answer, status = decorated()
        self.assertEqual(answer, 'fine')
        self.assertEqual(status, 200)


if __name__ == '__main__':
    unittest.main()
