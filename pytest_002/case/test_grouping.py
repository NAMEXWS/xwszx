import pytest

from pytest_002.API.api_grouping import Grouping


class TestGrouping:
    def setup_class(self):
        """调用类"""
        self.group = Grouping()

    @pytest.mark.somke
    @pytest.mark.parametrize('check', [200], ids=['通过'])
    def test_create_group(self, check):
        """创建分组"""

        a = self.group.create_group()
        assert a.status_code == 200

    def test_add_company(self):
        """添加公司"""
        a = self.group.add_company()

    def test_del_group(self):
        """删除分组"""
        a = self.group.del_group()
