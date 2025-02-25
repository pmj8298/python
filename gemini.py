# 구글 Gemini AI
from google import genai
def aiai(text):
    client = genai.Client(api_key="AIzaSyDee7uGhnoMImMm-qK3UDELPAQP54DJd840831")
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=text
        + '내용이 길면 문단으로 끊어서 알려줘. 단 친절하게 알려줘.'
    )
    answer = response.text
    # print(response.text)
    print(answer)
    return answer

if __name__=='__main__':
   aiai('gpt에 대해 설명해')