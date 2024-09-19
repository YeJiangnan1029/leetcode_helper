import os
import json
from collect_problemset_info import query_problem
from utils import query_from_graphql

problem_id = 15
output_folder = './'
assert os.path.isdir(output_folder), f"{output_folder}不是文件夹或者不存在"

code_type = 'Python3'
code_type_allowed = ['Python3']  # 目前只支持Python3类型的代码模板
assert code_type in code_type_allowed, f"暂不支持{code_type}语言"
base_url = 'https://leetcode.cn/'

# 查询问题信息
query_result = query_problem(problem_id)
titleSlug = query_result['titleSlug']
titleCn = query_result['titleCn']

# 查询 sample 和 code template
query_sample_json = {
    "operationName": "consolePanelConfig",
    "variables": {
                "titleSlug": titleSlug,
            },
    "query": '''query consolePanelConfig($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    metaData
    sampleTestCase
  }
}'''
}

query_editor_json = {
    "operationName": "questionEditorData",
    "variables": {
                "titleSlug": titleSlug,
            },
    "query": '''query questionEditorData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    codeSnippets {
      lang
      code
    }
  }
}'''
}

# 查询样例和模板代码
test_sample_data = json.loads(query_from_graphql(base_url, query_sample_json).text).get('data').get('question')
editors = json.loads(query_from_graphql(base_url, query_editor_json).text).get('data').get('question')

# 提取 code_template
code_template = ""
is_match_codelang = False
for item in editors['codeSnippets']:
    if item['lang'] == code_type:
        code_template = item['code']
        is_match_codelang = True
        break

if not is_match_codelang:
    raise Exception(f'没有匹配{code_type}的模板！')

# 解析测试样例
sample_testcase = test_sample_data.get('sampleTestCase')
meta_data = json.loads(test_sample_data.get('metaData'))

# 根据测试样例生成变量定义
test_vars = ""
param_list = meta_data['params']
test_values = sample_testcase.split("\n")
for i, param in enumerate(param_list):
    test_vars += f"{param['name']} = {test_values[i]}\n"

# 检查是否需要导入 List
requires_list_import = any('[]' in param['type'] for param in param_list)

# 检查是否需要导入 Optional
requires_opt_import = "Optional" in code_template

import_statement = ""
# 生成完整的 Python 代码
if requires_list_import:
    import_statement = "from typing import List"
    if requires_opt_import:
        import_statement += ", Optional"
elif requires_opt_import:
    import_statement = "from typing import Optional"
if import_statement:
    import_statement+="\n\n"

final_code = f"{import_statement}{code_template}\n        pass\n\n{test_vars}solution = Solution()\nprint(solution.{meta_data['name']}({', '.join([p['name'] for p in param_list])}))"

# 将代码写入文件
output_path = os.path.join(output_folder, f"leetcode_{problem_id}.py")
with open(output_path, 'w') as f:
    f.write(final_code)

print(f"代码已成功生成并保存到 {output_path}")
