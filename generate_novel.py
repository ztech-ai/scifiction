
import time
import uuid
import os
from config import OPENAI_API_KEY, MAX_RETRIES, RETRY_DELAY, MAX_TOKENS
from prompts import PROMPT_CONFIG
import requests
from openai import OpenAI
def generate_sci_fi_story(template_name, params):

    client = OpenAI(api_key=OPENAI_API_KEY, base_url="https://api.deepseek.com")


    for attempt in range(MAX_RETRIES):
        try:
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": PROMPT_CONFIG['templates'][template_name]['system']},
                    {"role": "user", "content": PROMPT_CONFIG['templates'][template_name]['user_template'].format(**params)}
                ],
                stream=False,
                temperature=0.7,
                max_tokens=MAX_TOKENS
            )
            content = response.choices[0].message.content
            title = PROMPT_CONFIG['templates'][template_name].get('label', '科幻小说')
            return f"# {title}\n\n{content}"
            
        except (requests.exceptions.RequestException, KeyError) as e:
            if attempt == MAX_RETRIES - 1:
                raise
            time.sleep(RETRY_DELAY * (attempt + 1))

def save_to_markdown(content):
    os.makedirs("novels", exist_ok=True)
    filename = f"{int(time.time())}_{uuid.uuid4().hex[:8]}.md"
    filepath = os.path.join("novels", filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath

# 修复主程序缩进问题
if __name__ == "__main__":
    try:
        print("可用故事模板：")
        for name, template in PROMPT_CONFIG['templates'].items():
            if name != 'default':
                print(f"{name}: {template['label']}")

        # 获取用户输入
        template_name = input("\n请输入模板名称: ")
        params = {}
        for param in PROMPT_CONFIG['templates'][template_name].get('params', []):
            params[param] = input(f"请输入{param}: ")

        print(template_name, params)
        # 生成并保存故事
        story = generate_sci_fi_story(template_name, params)

        saved_path = save_to_markdown(story)
        print(f"\n小说已生成并保存至：{saved_path}")

    except Exception as e:
        print(f"生成失败：{str(e)}")