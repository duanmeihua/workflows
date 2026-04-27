import tweepy
import os

# 从环境变量中读取密钥，保证安全性
api_key = os.environ["X_API_KEY"]
api_secret = os.environ["X_API_SECRET"]
access_token = os.environ["X_ACCESS_TOKEN"]
access_token_secret = os.environ["X_ACCESS_TOKEN_SECRET"]

def post_tweet():
    # 初始化客户端 (V2 版本 API)
    client = tweepy.Client(
        consumer_key=api_key, consumer_secret=api_secret,
        access_token=access_token, access_token_secret=access_token_secret
    )
    
    # 你可以在这里读取一个 txt 文件，或者随机生成一句话
    tweet_text = "这是来自 GitHub Actions 的每日自动问候！"
    
    try:
        client.create_tweet(text=tweet_text)
        print("发布成功！")
    except Exception as e:
        print(f"发布失败: {e}")

if __name__ == "__main__":
    post_tweet()
