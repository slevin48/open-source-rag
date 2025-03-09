# Open-Source Language Models for Retrieval-Augmented Generation (RAG)

[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=slevin48/open-source-rag)


Retrieval-Augmented Generation enables to generate answers and code snippets based on an index of documents (like a codebase stored in MATLAB Drive)

## Workflow

0. **Setup**: Install the required packages with `setup.m`
1. **Index**: Index the documents in the codebase with `index.m`
2. **Query**: Retrieve the relevant documents based on the query and generate the answer/code snippet with `query.m`

## Resources

- [SmolLM2: When Smol Goes Big -- Data-Centric Training of a Small Language Model](https://arxiv.org/abs/2502.02737)
- [Using pip to install a Large Language Model that’s under 100MB](https://simonwillison.net/2025/Feb/7/pip-install-llm-smollm2/)
- [SmolLM2](https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct)
- [SentenceTransformers](https://sbert.net/)
