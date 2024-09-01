# Development Assignment

## Level 1

At first I tried solving this with Google's gemma but it always had really poor results to the questions in `input.txt`. I tried with `gemma-2b` and `7b` but always received some gibberish. I was using the Inference API from Huggingface to do all my testing. Really not sure what's wrong with it, but even others on the internet seemed to get varying degrees of gibberish on using both of these models.

Ultimately I had to resort to using Groq API with `llama3-8b` which gave satisfactory results. From Groq I also tested `gemma-7b-it` and got very similar results to what I got from Llama. I'm really not sure what I was doing wrong while using the Huggingface API. I went back and tried `llama3-8b` on their inference api but it said it was too large to run on it. 

Run `main.py` by setting `export GROQ_API_KEY` to your API Key.

## Level 2

Extremely stupid and barebones server for L2. L2/main.py reads from a POST request and calls a modified version of L1/main.py. To use it, run L2/main.py, and on a separate terminal send a POST request using cURL to http://localhost:8000 like this: `curl http://localhost:8000 -X POST -d '{"inputs": <your-query-here>, "auth": <groq-api-key-here>}'`. To capture the output of cURL, one can put `>> output.json` at the end of the command, provided `output.json` is empty. 

Added a `client.sh` script to do the same. 
