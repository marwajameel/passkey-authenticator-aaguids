import openai
import os
from github import Github

# 1. اپنی پرسنل کیز (Keys) یہاں سیٹ کریں (Replit Secrets میں ڈالنا بہتر ہے)
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
REPO_NAME = "آپ_کا_یوزر_نیم/sdn-news-portal" # اپنی ریپوزٹری کا نام یہاں لکھیں

# OpenAI سیٹ اپ
openai.api_key = OPENAI_API_KEY

def process_news_with_ai(raw_text):
    """خبر کو خوبصورت اردو میں تبدیل کرنا"""
    prompt = f"آپ SDN News کے چیف ایڈیٹر ہیں۔ اس خبر کا پروفیشنل اردو خلاصہ لکھیں:\n\n{raw_text}\n\nآخر میں یہ معلومات شامل کریں:\nSDN News: باخبر، ہر لمحہ\nرپورٹ: جمیل احمد کلیال"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def update_github_website(new_content):
    """گٹ ہب پر ویب سائٹ فائل اپ ڈیٹ کرنا"""
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPO_NAME)
    
    # فرض کریں آپ کی ویب سائٹ کی فائل کا نام index.html ہے
    file = repo.get_contents("index.html")
    
    # پرانا مواد حاصل کریں اور اس میں نئی خبر شامل کریں (یہاں آپ اپنی ضرورت کے مطابق منطق بدل سکتے ہیں)
    updated_html = file.decoded_content.decode() + f"\n<p>{new_content}</p>"
    
    repo.update_file(file.path, "Auto Update News via AI", updated_html, file.sha)
    print("✅ SDN News ویب سائٹ کامیابی سے اپ ڈیٹ ہو گئی ہے!")

# --- استعمال کا طریقہ ---
raw_input = input("کچی خبر یا لنک یہاں پیسٹ کریں: ")
urdu_news = process_news_with_ai(raw_input)
update_github_website(urdu_news)
