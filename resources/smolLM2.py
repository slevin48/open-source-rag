from transformers import AutoModelForCausalLM, AutoTokenizer
checkpoint = "HuggingFaceTB/SmolLM2-135M-Instruct"

device = "cpu" # "cuda" for GPU usage or "cpu" for CPU usage
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
# for multiple GPUs install accelerate and do `model = AutoModelForCausalLM.from_pretrained(checkpoint, device_map="auto")`
model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)

messages = [{"role": "user", "content": "What is the meaning of life?"}]
input_text=tokenizer.apply_chat_template(messages, tokenize=False)
print(input_text)
# Get the tokenizer outputs as a dictionary
inputs = tokenizer(input_text, return_tensors="pt")
# Send each tensor to the target device
inputs = {key: value.to(device) for key, value in inputs.items()}

outputs = model.generate( inputs["input_ids"],attention_mask=inputs["attention_mask"], max_new_tokens=1000, temperature=0.2, top_p=0.9, do_sample=True)
print(tokenizer.decode(outputs[0]))