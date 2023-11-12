import openai
import pdfplumber
from openai import OpenAI
import tiktoken
from dotenv import load_dotenv
import os
load_dotenv()
# import time



# PDFファイルを読み込み、テキストに変換する関数
def pdf_to_text(file_path):
    with pdfplumber.open(file_path) as pdf:
        return ''.join(page.extract_text() for page in pdf.pages)

# OpenAI APIを使用してテキストを要約する関数
def summarize_paper(paper_text):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI()  # OpenAIクライアントの初期化

    res_sum = client.chat.completions.create(
        model="gpt-4-1106-preview",  # モデルの指定
        messages=[
            {"role": "system", "content": "This is a tool to summarize academic papers."},
            {"role": "system", "content": "Outputs should be generated in step by step."},
            {"role": "user", "content": f"Summarize this paper: {paper_text}\n\nInclude:\n- Overview\n- Novelty\n- Methodology\n- Results"}
        ],
        temperature=0.8
    )
    
    text = res_sum.choices[0].message.content
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",  # モデルの指定
        messages = [
            {"role": "system", "content": "This tool translates text from English to Japanese."},
            {"role": "user", "content": f"Translate the following text to Japanese: {text}"}
        ],
        temperature=0.8
    )
    return response.choices[0].message.content
    
    # 5秒間待機する
    # time.sleep(5)
    # return str("概要：\nこの論文は、自然言語インタフェースを介して多次元データセットを可視化するために設計された革新的な会話型AI、AIThreadsを紹介しています。AIThreadsは、Matt-Heun HongとAnamaria Crisanによって開発された、大規模言語モデル（LLM）を使用して、ユーザーの発話に応じて視覚的およびテキスト出力を生成するマルチスレッド解析チャットボットです。\n\n革新性：\nAIThreadsの革新的な側面は、メッセージングアプリと同様に複数の会話スレッドを管理する能力にあります。これにより、分析者が会話の文脈を積極的に管理し、分析の進行に合わせて組織を改善することができます。この機能は、これまでの分析会話を直線的に扱った以前のシステムとは異なる点です。\n\n方法論：\n会話インタフェースを介して視覚化を作成および改善するAIThreadsの機能について調査されました。著者は、視覚的分析のためのチャットボットを調査した以前のウィザード・オブ・オズの研究を再分析するためにLLMを使用しました。彼らは、LLM駆動の解析チャットボットの強みと弱点を明らかにし、進行的な視覚化の改善をサポートすることができないことを発見しました。これらの結果に基づいて、AIThreadsが開発され、40人の参加者によるクラウドソーシング調査と10人の専門アナリストによる詳細なインタビューを通じてその使いやすさが評価されました。AIThreadsはまた、LLMのトレーニングコーパス外のデータセットでテストされました。\n\n結果：\nAIThreadsは、データ分析と視覚化におけるLLMの可能性を実証しましたが、課題も明らかにしました。ユーザースタディの参加者は、AIThreadsに対して全体的に肯定的な印象を持ち、分析の文脈を管理するために有能で役立つと感じました。しかし、システムは依然として誤った応答をすることがありました。専門家の参加者は、AIチャットボットが彼らの既存の分析プロセスと比較してどのようなインサイトを提供したかを示しました。これらの研究結果は、将来の研究における有望な方向を示唆しており、マルチスレッドの会話型解析エージェントの開発や、そのようなエージェントがデータ分析プラクティスに与える影響などが含まれます。")
