import json
import csv
import time
import os  # 用于检查文件是否存在
from tqdm import tqdm # 导入 tqdm 库

from utils import query_from_graphql

def fetch_problems(base_url, fetch_problem_list_json, csv_filename):
    all_questions = []
    skip = 0
    limit = fetch_problem_list_json['variables']['limit']

    # 第一次请求获取 total
    response = query_from_graphql(base_url, fetch_problem_list_json)
    problemsetQuestionList = json.loads(response.text).get('data').get('problemsetQuestionList')
    total = problemsetQuestionList['total']  # 获取总题目数量
    questions = problemsetQuestionList['questions']
    
    # 初始化进度条
    progress_bar = tqdm(total=total, desc="Fetching problems", unit="questions")

    # 将当前 batch 的问题追加到 all_questions
    all_questions.extend(questions)
    progress_bar.update(len(questions))  # 更新进度条

    # 循环继续请求，直到拉取完所有数据
    while problemsetQuestionList['hasMore']:
        skip += limit
        fetch_problem_list_json['variables']['skip'] = skip

        # 发送请求
        response = query_from_graphql(base_url, fetch_problem_list_json)
        problemsetQuestionList = json.loads(response.text).get('data').get('problemsetQuestionList')
        questions = problemsetQuestionList['questions']
        
        # 将新的问题追加到 all_questions
        all_questions.extend(questions)
        
        # 更新进度条
        progress_bar.update(len(questions))

        # 间隔100ms再请求
        time.sleep(0.1)

    # 关闭进度条
    progress_bar.close()

    # 将所有题目信息保存到 CSV 文件中
    save_to_csv(all_questions, csv_filename)

def save_to_csv(questions, csv_filename):
    # 打开 CSV 文件，写入题目信息
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # 写入 CSV 标题
        writer.writerow(['frontendQuestionId', 'titleSlug', 'titleCn'])

        # 写入每一行题目信息
        for q in questions:
            writer.writerow([q['frontendQuestionId'], q['titleSlug'], q['titleCn']])

def query_problem(id):
    current_file_path = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file_path)
    csv_filename = os.path.join(current_dir, 'problem_info.csv')

    # 判断 CSV 文件是否存在
    if not os.path.exists(csv_filename):
        print(f"{csv_filename} 不存在，正在生成...")
        base_url = 'https://leetcode.cn/'
        fetch_problem_list_json = {
            "operationName": "problemsetQuestionList",
            "variables": {
                "categorySlug": "all-code-essentials",
                "skip": 0,
                "limit": 50,
                "filters": {}
            },
            "query": '''query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
              problemsetQuestionList(
                categorySlug: $categorySlug
                limit: $limit
                skip: $skip
                filters: $filters
              ) {
                hasMore
                total
                questions {
                  frontendQuestionId
                  titleCn
                  titleSlug
                }
              }
            }'''
        }
        fetch_problems(base_url, fetch_problem_list_json, csv_filename)

    # 读取 CSV 文件并进行查询
    with open(csv_filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['frontendQuestionId'] == str(id):
                return {'titleSlug': row['titleSlug'], 'titleCn': row['titleCn']}

    # 如果找不到该题目ID，抛出自定义异常
    raise Exception(f'没有找到匹配{id}的题目')
