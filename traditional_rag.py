"""
traditional rag follows 'retrive and generate' paradigm - just grabs info from a set sources and answers based on that

- retreives semantically similar but contextually irrelevant info
- misses multi-hop reasoning and deep contextual understanding
- scalability issues as knowledge base grows: context window limits and high computational overhead
- lacks dynamic retrieval: cannot adapt to new info or changing user intents or feedback or evolving contexts

"""