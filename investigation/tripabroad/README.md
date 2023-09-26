### Summary
- 海外旅行の練習用に会話シーンを限定して、それの会話を作成する

### Examples
レストランシーンをもとに作成

#### chatgptを利用した会話スクリプトの作成

prompt
```
海外旅行に行った際、レストランでの注文のシーンを英語で再現してください。
以下の条件を含んでください。
・おすすめの料理を聞く
・会計はどうすればいいか
・最後にこの辺りで行ってみたほうがいい場所について聞く
```

scene script
```
登場人物： あなた (Y) とウェイター (W)

シーン：

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

あなたはウェイターに感謝の意を示し、レストランを後にします。
```

#### chatgptを利用した例文集の作成
prompt
```
上記の会話からYの文章のみを抜き出し、似たような文章を含めて10この例文集にしてください。
出力の形式は以下のようにお願いします。
J: {日本語訳}
E: {英語の文章}
```

例文集
```
J: 料理のおすすめは何ですか？
E: What are the recommended dishes?

J: パエリアにします。それと、赤ワインを一杯お願いします。
E: I'll have the paella, and a glass of red wine, please.

J: お釣りを持ってきてもらえますか？
E: Could you bring the check, please?

J: 何か他に必要なものはありますか？
E: Is there anything else I can get for you?

J: 今日の食事はとても美味しかったです。ありがとう。
E: The meal was delicious today. Thank you.

J: これで結構です。
E: No, that should be it for now, thank you.

J: 何かこの辺りで行ってみるべき場所はありますか？
E: Are there any interesting places around here that you would recommend visiting?

J: お勧めの料理は何ですか？
E: What are your recommended dishes?

J: それでは、そのおすすめの料理をお願いします。
E: Alright, then I'll go with the recommended dish.

J: チェックをお願いします。
E: Can I have the bill, please?
```

#### chatgptを利用した他のシーンスクリプトの作成
prompt
```
上記の例文集を利用して、レストラン注文以外でのシーンで想定できる英会話のシーンサンプルを2つ作成してください。英語で１０回程度の会話のラリーにしてください。
```

other scene scripts

1. cafe order
```
あなたはカフェに座り、ウェイターがメニューを持ってきます。

Y: Hi there! What do you recommend for coffee?

W: Good morning! Our house blend is always a popular choice. It has a smooth and rich flavor.

Y: Sounds good. I'll have a cup of the house blend, please. And can I get a chocolate croissant to go with it?

W: Of course, one house blend and a chocolate croissant. Anything else for you?

Y: No, that'll be all for now, thanks.

料理が提供され、あなたは美味しいコーヒーとクロワッサンを楽しんでいます。

W: (After the meal) How was your coffee and croissant? Is there anything else I can get for you?

Y: Everything was delicious, thank you. Could you please bring the check?

W: Certainly, I'll bring it right away.

ウェイターが会計を済ませ、お釣りを持ってきます。

W: Here's your check, sir. Is there anything else I can assist you with today?

Y: No, I'm good. By the way, are there any interesting shops or parks around here worth checking out?

W: Absolutely! There's a lovely park just a few blocks away, and there are some unique boutiques on the main street as well.

Y: Thanks for the recommendations. I'll explore those.

W: You're welcome. Enjoy the rest of your day!
```

2. hotel checkin
```
あなたはホテルのフロントデスクに立っています。フロントデスクのスタッフ（F）が対応しています。

Y: Good afternoon. I'm staying in room 302, and I was wondering if you could recommend a good local restaurant for dinner?

F: Good afternoon, sir. Of course, we have a few great options nearby. There's an Italian restaurant just around the corner, or if you prefer seafood, there's a fantastic seafood grill about a 10-minute walk from here.

Y: Thanks for the suggestions. I'll check those out. By the way, what time is breakfast served here?

F: Breakfast is served from 7:00 AM to 10:00 AM in our restaurant on the ground floor. Is there anything else I can assist you with?

Y: No, that's all for now. Thanks for your help.

あなたは情報を受け取り、ホテル内を探索し始めます。

F: You're welcome, sir. If you need anything else during your stay, please don't hesitate to ask. Enjoy your evening!

Y: Thank you, I will. Have a great day!

これらのシーンは、カフェでの注文とホテルのフロントデスクでの問い合わせという異なる状況での英会話サンプルを提供しています。
```

### Results

normal speed

[audioscript.wav.webm](https://github.com/softmurata/generative-ai-handsbook/assets/67137475/a89b4e2e-be26-4b4c-9998-81768414043d)


slow speed


[output.webm](https://github.com/softmurata/generative-ai-handsbook/assets/67137475/28e4c4f9-d476-4bdd-bdb2-6691de50d0c8)



### Related Links
- [elevenlabs](https://github.com/elevenlabs/elevenlabs-python)
- [voicevox](https://voicevox.hiroshiba.jp/)

### Related Notebooks
