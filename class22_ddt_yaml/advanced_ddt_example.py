# advanced_ddt_example.py
import unittest
from ddt import ddt, data, idgenerator
import yaml
from pathlib import Path


def load_yaml_data(filepath):
    with open(Path(filepath), 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


@ddt
class TestAdvancedFeatures(unittest.TestCase):

    @idgenerator(lambda x: f"test_{x['name'].lower().replace(' ', '_')}")
    @data(*load_yaml_data('test_data.yaml'))
    def test_with_custom_id(self, test_case):
        """带自定义ID的测试"""
        print(f"执行: {test_case['name']}")
        self.assertTrue(isinstance(test_case, dict))
        self.assertIn('url', test_case)
        self.assertIn('search_term', test_case)

    def custom_id_func(test_case):
        """自定义ID函数"""
        return f"{test_case['name']}_{test_case['search_term']}"

    @data(*load_yaml_data('test_data.yaml'))
    def test_normal_case(self, test_case):
        """普通测试用例"""
        # 可以在这里添加实际的测试逻辑
        print(f"运行测试: {test_case['name']}")

        # 示例断言
        assert isinstance(test_case, dict)
        assert 'url' in test_case
        assert 'search_term' in test_case
        assert test_case['timeout'] > 0


# 运行测试
if __name__ == '__main__':
    # 可以使用不同的运行方式
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestAdvancedFeatures)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)