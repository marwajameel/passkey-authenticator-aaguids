import openai
import os
from github import Github

# آپ کی فراہم کردہ ID اور دیگر کنفیگریشن
USER_KEY_ID = "4a3b615c-2c82-4297-b7e4-59c7fe6ee4b2"
REPO_NAME = "jamilkalyal/sdn-news-portal" # یہاں اپنا درست گٹ ہب یوزر نیم لکھیں

# Replit Secrets سے اصل Keys حاصل کرنا
openai.api_key = os.environ.get('OPENAI_API_KEY')
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')

def process_news_with_ai(raw_text):
    """خبر کو خوبصورت اردو میں تبدیل کرنا اور SDN News کی برانڈنگ شامل کرنا"""
    prompt = f"آپ SDN News کے چیف ایڈیٹر ہیں۔ اس خبر کا پروفیشنل اردو خلاصہ لکھیں:\n\n{raw_text}\n\nآخر میں یہ معلومات شامل کریں:\nSDN News: باخبر، ہر لمحہ\nرپورٹ: جمیل احمد کلیال"
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"OpenAI Error: {e}"

def update_github_website(new_content):
    """گٹ ہب پر SDN News کی ویب سائٹ اپ ڈیٹ کرنا"""
    try:
        g = Github(GITHUB_TOKEN)
        repo = g.get_repo(REPO_NAME)
        file = repo.get_contents("index.html")
        
        # نئی خبر کو RTL (دائیں سے بائیں) فارمیٹ میں شامل کرنا
        news_html = f"\n<div dir='rtl' style='text-align: right; border-bottom: 1px solid #ccc; padding: 10px;'>{new_content}</div>"
        updated_html = file.decoded_content.decode() + news_html
        
        repo.update_file(file.path, "SDN News Auto Update", updated_html, file.sha)
        print("✅ SDN News ویب سائٹ کامیابی سے اپ ڈیٹ ہو گئی ہے!")
    except Exception as e:
        print(f"❌ GitHub Error: {e}")

# پروگرام چلانے کا حصہ
if __name__ == "__main__":
    print(f"سسٹم فعال ہے (ID: {USER_KEY_ID})")
    raw_input = input("کچی خبر یا مواد یہاں پیسٹ کریں: ")
    if raw_input:
        print("AI خبر تیار کر رہا ہے...")
        urdu_news = process_news_with_ai(raw_input)
        print("-" * 30)
        print(urdu_news)
        print("-" * 30)
        update_github_website(urdu_news)

