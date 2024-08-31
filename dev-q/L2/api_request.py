import time, json, os
from groq import Groq

def get_data():
    with open("input.txt", "r") as f:
        data = [x.strip('\n') for x in f.readlines()]
    print(data) 
    return tuple(data)

def write_data(data):
    with open("output.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=4))

def query(client, payload):
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

def main():

    data, GROQ_API_KEY = get_data()
    
    client = Groq(
            api_key=os.environ.get("GROQ_API_KEY"),
        )

    json_ = dict.fromkeys(["Prompt", "Message", "TimeSent", "TimeRecvd", "Source"])

    json_["TimeSent"] = int(time.time())
    res = query(client, data)
    json_["TimeRecvd"] = int(time.time())

    json_["Source"] = "llama"
    json_["Prompt"] = data
    json_["Message"] = res.choices[0].message.content

    return json_

if __name__ == "__main__":
    main()
