# Class 9 - Text Generation with LLMs, in-context learning, and model fine-tuning

Last week, we worked with models which can be run (for inference) on local machines or UCloud CPUs. Some of them were doing a reasonable jobs in some tasks, but, overall, we saw a lot of room for improvement. Today, we focus on three ways to achieve better instruction-based performance:
- Using large language models in a zero-shot fashion: as these models are prohibitively big, we will use a brand new library (`Petals`) to access them in a distributed fashion, and get a sense for what these models are capable of;
- In-context learning (one- or few-shot)
- Instruction fine-tuning

This mirrors the content of the latest lecture, which focused on advanced approaches to NLG.
Note that, to access GPUs, we will be running the notebooks on Google Colab.
