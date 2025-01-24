from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Specify the model wanted
model_name = "gpt2" 

model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

model.save_pretrained('/home/nemolabs/nemo_app/encyclopedia/Memory/core_stuff/')
tokenizer.save_pretrained('/home/nemolabs/nemo_app/encyclopedia/Memory/core_stuff/')

