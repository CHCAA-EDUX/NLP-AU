from transformers import BertTokenizer, BertModel

# download model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained("bert-base-uncased")

# encode text
text = "Replace me by any text you'd like."

# convert text to token ids
encoded_input = tokenizer(text, return_tensors='pt')

encoded_input.input_ids.shape # torch.Size([1, 12])

# embed ids and contextualize 
output = model(**encoded_input)

output.last_hidden_state.shape # torch.Size([1, 12, 768])