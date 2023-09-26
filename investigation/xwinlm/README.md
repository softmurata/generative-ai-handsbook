### Summary
- GPT4を性能評価で超えたとされる中国製のOpenSourceLLM
- GPTQやGGUFなどの量子化の利用法が確立されている。

### Examples
- GPTQを用いるとGPUのメモリは8GB, CPUのメモリは3.5GBに収まる
- 推論時では10GB前後までGPUメモリは上昇を確認

### Results

prompt
```
tell me about latetst AI
```

output
```
As of my knowledge cutoff date in September 2021, the latest advancements in AI can be categorized into several areas:

1. Improved machine learning algorithms: Researchers continue to refine and develop machine learning algorithms, making them more efficient, accurate, and adaptable. Some examples include Transformers, which have been successful in natural language processing tasks, and GPT-3, a language model that can generate human-like text.
2. Advanced neural networks: The development of more sophisticated neural networks, such as convolutional neural networks (CNNs) and recurrent neural networks (RNNs), has enabled AI systems to better understand and process data with complex structures, such as images, audio, and time-series data.
3. Reinforcement learning: This area of AI focuses on developing algorithms that enable agents to learn from experience and make decisions that maximize their long-term reward. DeepMind's AlphaGo Zero and AlphaStar are examples of successful reinforcement learning applications.
4. Explainable AI: There is a growing interest in developing AI systems that can provide explanations for their decisions, making them more transparent and trustworthy. Explainable AI aims to bridge the gap between human understanding and AI-driven decision-making.
5. AI ethics: As AI becomes more prevalent, concerns about its ethical implications have gained attention. Researchers and practitioners are working on addressing issues such as fairness, accountability, transparency, and privacy in AI systems.
6. AI for good: Researchers and organizations are exploring ways to harness AI technology for social good, addressing challenges in areas such as healthcare, education, environmental sustainability, and poverty alleviation.
7. AI and the workforce: The impact of AI on the labor market is a significant area of research. AI is expected to transform various industries, leading to job displacement and the emergence of new job opportunities. Understanding these changes and their implications is crucial for policymakers and workforce planners.
8. AI governance: As AI systems become more integrated into our lives, there is a growing need for effective governance and regulation to ensure their safe and responsible deployment. This
```

日本語output
```
AI（人工知能）は、コンピュータが人間の知能や思考を模倣し、問題解決や処理を自動的に行う技術です。AIは、機械学習、深層学習、自然言語処理など、様々な分野で活躍しています。

最近では、AIが人間の会話を真似てchatbotとして登場し、多くの人々に楽しんでもらえています。また、AIが画像や音声を生成することで、新たなアートやエンターテインメントが誕生することも期待されています。

しかし、AIには潜在的な問題もあります。例えば、バイアスや不平等が生じる恐れがあるため、社会的に適切な使い方をすることが重要です。また、AIの開発や使用に伴うエネルギー消費も環境に与える影響を考慮する必要があります。

AIは、人類の未来を変える革命的な技術であり、その潜在力は限定されていません。ただし、その権限と使い方を考慮し、社会的に責任を果たすことが重要です。
```

### Related Links
- [thebloke/xwinlm GPTQ](https://huggingface.co/TheBloke/Xwin-LM-13B-V0.1-GPTQ)
- [thebloke/xwinlm AWQ](https://huggingface.co/TheBloke/Xwin-LM-13B-V0.1-AWQ)



### Related Notebooks

### ToDo
- awqバージョンをどのようにして動かすのか