# RAG

Problem Statement:
How can we design a Retrieval-Augmented Generation (RAG) system that selects the most appropriate knowledge source and produces context-aware responses in high-stakes domains such as healthcare, where accuracy and reliability are critical?

Solution:
An agentic RAG pipeline that leverages a routing agent to intelligently choose among multiple retrieval sources, checks the relevance of the retrieved context and then only generates answers using LLM. 
- Improves reliability, quality of the response, accuracy and flexibility
