### Summary
- GPT4を性能評価で超えたとされる中国製のOpenSourceLLM
- GPTQやGGUFなどの量子化の利用法が確立されている。

### Keyworkds
- GPT4
- LLM
- GPTQ
- AWQ

### Architecture
- llama2 baseの言語モデルに対して、以下の手法を用いてLLMを学習
    - supervised fine tuning(SFT)
    - reward models(RM)
    - reject sampling
    - reinforcement learning from human feedback(RLHF)

### Results

prompt
```
日本語で簡潔にAIについて教えて
```

日本語output
```
AI（人工知能）は、コンピュータが人間の知能や思考を模倣し、問題解決や処理を自動的に行う技術です。AIは、機械学習、深層学習、自然言語処理など、様々な分野で活躍しています。

最近では、AIが人間の会話を真似てchatbotとして登場し、多くの人々に楽しんでもらえています。また、AIが画像や音声を生成することで、新たなアートやエンターテインメントが誕生することも期待されています。

しかし、AIには潜在的な問題もあります。例えば、バイアスや不平等が生じる恐れがあるため、社会的に適切な使い方をすることが重要です。また、AIの開発や使用に伴うエネルギー消費も環境に与える影響を考慮する必要があります。

AIは、人類の未来を変える革命的な技術であり、その潜在力は限定されていません。ただし、その権限と使い方を考慮し、社会的に責任を果たすことが重要です。
```

### Related Algorithm
