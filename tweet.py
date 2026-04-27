import tweepy
import os
import sys

# 获取环境变量
api_key = os.environ.get("X_API_KEY")
api_secret = os.environ.get("X_API_SECRET")
access_token = os.environ.get("X_ACCESS_TOKEN")
access_token_secret = os.environ.get("X_ACCESS_TOKEN_SECRET")

def post_tweet():
    print("正在尝试连接 X API...")
    try:
        # 显式使用 V2 接口
        client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        
        # 加上时间戳确保内容不重复（X 禁止短时间内发重复推文）
        import datetime
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        content = f"来自 GitHub Actions 的自动测试：{now}"
        
        print(f"准备发布内容: {content}")
        response = client.create_tweet(text=content)
        print(f"✅ 发布成功！推文 ID: {response.data['id']}")
        
    except Exception as e:
        print(f"❌ 发布失败，错误详情: \n{str(e)}")
        # 强制脚本以错误状态退出，这样 GitHub Actions 会显示红叉
        sys.exit(1)

if __name__ == "__main__":
    post_tweet()
