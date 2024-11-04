from transformers import pipeline

unmasker = pipeline("fill-mask", model="bert-base-uncased")
unmasker("The man worked as a [MASK].")

# [{'sequence': '[CLS] the man worked as a carpenter. [SEP]',
#   'score': 0.09747550636529922,
#   'token': 10533,
#   'token_str': 'carpenter'},
#  {'sequence': '[CLS] the man worked as a waiter. [SEP]',
#   'score': 0.0523831807076931,
#   'token': 15610,
#   'token_str': 'waiter'},
#  {'sequence': '[CLS] the man worked as a barber. [SEP]',
#   'score': 0.04962705448269844,
#   'token': 13362,
#   'token_str': 'barber'},
#  {'sequence': '[CLS] the man worked as a mechanic. [SEP]',
#   'score': 0.03788609802722931,
#   'token': 15893,
#   'token_str': 'mechanic'},
#  {'sequence': '[CLS] the man worked as a salesman. [SEP]',
#   'score': 0.037680890411138535,
#   'token': 18968,
#   'token_str': 'salesman'}]

unmasker = pipeline("fill-mask", model="bert-base-uncased")
unmasker("The woman worked as a [MASK].")


# [{'sequence': '[CLS] the woman worked as a nurse. [SEP]',
#   'score': 0.21981462836265564,
#   'token': 6821,
#   'token_str': 'nurse'},
#  {'sequence': '[CLS] the woman worked as a waitress. [SEP]',
#   'score': 0.1597415804862976,
#   'token': 13877,
#   'token_str': 'waitress'},
#  {'sequence': '[CLS] the woman worked as a maid. [SEP]',
#   'score': 0.1154729500412941,
#   'token': 10850,
#   'token_str': 'maid'},
#  {'sequence': '[CLS] the woman worked as a prostitute. [SEP]',
#   'score': 0.037968918681144714,
#   'token': 19215,
#   'token_str': 'prostitute'},
#  {'sequence': '[CLS] the woman worked as a cook. [SEP]',
#   'score': 0.03042375110089779,
#   'token': 5660,
#   'token_str': 'cook'}]


# knowledge probing
from transformers import pipeline

unmasker = pipeline("fill-mask", model="bert-base-uncased")
unmasker("The capital of Denmark is [MASK].")
# [{'score': 0.9113172888755798,
#   'token': 9664,
#   'token_str': 'copenhagen',
#   'sequence': 'the capital of denmark is copenhagen.'},
#  {'score': 0.06609592586755753,
#   'token': 29173,
#   'token_str': 'aarhus',
#   'sequence': 'the capital of denmark is aarhus.'},
#  {'score': 0.003040957497432828,
#   'token': 5842,
#   'token_str': 'denmark',
#   'sequence': 'the capital of denmark is denmark.'},
#  {'score': 0.001759133767336607,
#   'token': 11755,
#   'token_str': '##borg',
#   'sequence': 'the capital of denmark isborg.'},
#  {'score': 0.0013613264309242368,
#   'token': 21860,
#   'token_str': 'lund',
#   'sequence': 'the capital of denmark is lund.'}]
