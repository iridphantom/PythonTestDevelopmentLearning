# conftest.py是文件固定名称，不允许修改。否则不生效。
# 所有的hook函数都是写在conftest之中的。hook函数的作用可以理解为对pytest的二次定义。
# 例：为了让ids解析中文，正常显示中文内容的设置定义，可以通过hook函数来实现。所有代码内容都是固定的，不需要做任何修改
def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode_escape')  # 改变pytest编码识别
        item._nodeid = item._nodeid.encode('utf-8').decode('unicode_escape')