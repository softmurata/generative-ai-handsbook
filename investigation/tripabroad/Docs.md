### Summary
- 海外旅行などのシーンを想定して会話を作成
- その会話から実際の音声を作成
- スロースピードの作成も可能

### Data Preparation
- chatgptを利用して会話のテンプレートを作成
- chatgptからテンプレートを会話順に分別する。
prompt
```
以下のような文章にあります。
あなたがレストランに着き、テーブルに座りました。ウェイターがメニューを持ってきます。

Y: Good evening. Could you recommend any specialties of the house?

W: Of course! Our chef's specials tonight are the seafood paella and the grilled sirloin steak. They are both highly recommended.

Y: That sounds great. I'll go with the seafood paella, please. And may I have a glass of red wine to go with it?

W: Excellent choice! A glass of red wine with the seafood paella it is. Anything else for you?

Y: No, that should be it for now, thank you.

料理が提供され、あなたは美味しい食事を楽しんでいます。

W: (After the meal) How was your meal? Is there anything else I can get for you?

Y: The paella was delicious, thank you. Could you please bring the check?

W: Of course. I'll bring it right away.

ウェイターが会計を済ませ、お釣りを持ってきます。

W: Here's your check, sir. Is there anything else I can assist you with tonight?

Y: No, everything was perfect, thank you. By the way, are there any interesting places around here that you would recommend visiting?

W: Certainly! If you're interested in local history, there's a museum just a few blocks away, and the waterfront promenade is also quite beautiful in the evening.

Y: Thank you for the recommendations. I'll check those out.

W: You're welcome. Enjoy the rest of your evening!

あなたはウェイターに感謝の意を示し、レストランを後にします。\ 以下の文章をYの英文のリストとWの英文のリストに並べ替えて出力してください。出力のフォーマットは以下です。
Y: [英文]
W: [英文]
```

- YのリストとWのリストを作成します。

### Keyworkds
- TTS
- voice cloning
- voice conversion
- trip

### Another Prompt

街中
```
海外旅行に行った際、街中でのシーンを英語で再現してください。
以下の条件を含んでください。
・道案内の聞き方
・電車のチケットの買い方
・荷物をなくしてしまった時

上記のシーンで利用されている英文からTravelerに必要な英文を抜き出して、類似の表現で利用できそうな英文を10個添えて例文集を作成してください。

上記の例文集を利用して、街中でのシーン以外で海外旅行で想定できそうなシーン（空港とホテル）を用いた英会話のシーンを１０回ラリー程度で作成してください

```

### Results

normal speed

[audioscript.wav.webm](https://github.com/softmurata/generative-ai-handsbook/assets/67137475/a89b4e2e-be26-4b4c-9998-81768414043d)


slow speed


[output.webm](https://github.com/softmurata/generative-ai-handsbook/assets/67137475/28e4c4f9-d476-4bdd-bdb2-6691de50d0c8)

### Related Algorithm
