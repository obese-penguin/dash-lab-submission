import time, json, os
from groq import Groq

TIME_SENT, TIME_RECVD = 0, 0

def get_data():
    with open("input.txt", "r") as f:
        data = [x.strip('\n') for x in f.readlines()]
       
    return data

def write_data(data):
    with open("output.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=4))

def query(payload):
    chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"{payload}",
                    }
                ],
            model="llama3-8b-8192",
            )
    return chat_completion

data = get_data()

responses = []

client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

for i in data:
    json_ = dict.fromkeys(["Prompt", "Message", "TimeSent", "TimeRecvd", "Source"])

    json_["TimeSent"] = int(time.time())
    res = query(i)
    json_["TimeRecvd"] = int(time.time())

    json_["Source"] = "llama"
    json_["Prompt"] = i
    json_["Message"] = res.choices[0].message.content
    responses.append(json_)

write_data(responses)

