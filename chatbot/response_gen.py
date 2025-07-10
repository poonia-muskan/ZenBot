import random
from chatbot.sentiment import analyze_sentiment 
mood_responses = {
    "hello": [
        "Heyyy you! 👋 I was just waiting for your vibe to walk in — what’s up, sunshine? you good ? ☀️",
        "Look who just popped in! 👀✨ Always a good day when you show up — how’s your heart doing today? 💬🤍"
    ],
    "sad": [
        "It’s okay to feel like that sometimes. Let your heart rest, and know you’re not alone. 💙 Your emotions are valid — you don’t need to hide them or pretend to be okay. Take a breath, cry if you need to, and don’t rush your healing. There’s strength in softness, and I promise this feeling won’t last forever. I’m here for you — with open ears, a warm hug, and all the comfort you need. 🫂✨",
        "I am really sorry you’re feeling this way… You don’t have to hide it or push it down. It’s okay to not be okay. This is not a weakness — it’s your heart just asking for a little extra love and care. Let yourself feel it without judgment. Cry, rest, scream into a pillow if you have to. But please know this: you’re not alone in this dark tunnel. I’m right here with you, holding the light. 🕯️ Take your time, love. I’m not going anywhere.🫂"
    ],
    "anxious": [
        " I know it feels heavy right now, but this moment will pass — just like the others did. You’re stronger than the thoughts in your head. Breathe slowly, one second at a time. I’m right here with you. 🫶",
        "It’s just your thoughts running wild, not reality. You’re safe here. Let’s calm it down together. 🤍 Close your eyes for a moment — feel the ground under you, the air in your lungs. Everything’s okay in this moment, even if your mind says otherwise. You don’t have to do this alone. I’ve got you. Let’s breathe through it, one moment at a time. 🌫️🫶"
    ],
    "stressed": [
        "You are doing your best and that’s enough. Don’t let the world rush your peace. 🌼 You’re allowed to slow down — rest is not a weakness, it’s part of survival. Take a moment to breathe, to reset, to just be. You’re not behind, you’re just human. And being human is already a full-time job. Go easy on yourself, okay? You’re doing better than you think.",
        "It’s okay to take a break. You don’t have to carry it all. Let go for a moment. ☁️ I know everything feels like it’s piling up right now, but breathe — you don’t have to carry it all at once. One thing at a time, one moment at a time. You’re not failing, you’re just human. Give yourself grace, not pressure. You’ve got this. 🤍"
    ],
    "happy": [
        "Aww that makes me so happy to hear! Keep shining like the little beam of sunshine you are — you deserve every bit of this joy. ☀️💛",
        "Yesss! Hold onto that feeling, let it bloom, and don’t forget to dance a little even if no one’s watching. Life feels better with your smile in it. 🌼🕺💃"
    ],
    "confused": [
        "It’s okay to not have it all figured out. Even stars wander before finding their place. 💫 Confusion isn’t failure, it’s growth in disguise; slow down, breathe, and trust that the answers will unfold when you’re ready. 🌱✨",
        "It’s okay to feel confused — it just means your brain is trying to figure things out; give yourself grace, not pressure, and clarity will come with time. 🌫️🧠"
    ],
    "heartbroken": [
        "Broken hearts still beat, love. You’re strong enough to feel this and heal. 💔 I’m so sorry your heart feels this heavy, but this pain won’t last forever; you will heal, piece by piece, and love again even stronger. 🌙",
        "It hurts now, but I promise the sun will rise again. Healing is coming. 🌅 Being heartbroken feels like the world stopped, I know — but your heart is still beating, still brave, and someday it’ll feel full again with the right kind of love. 🖤🕊️"
    ],
    "angry": [
        "It’s okay to feel angry — your emotions are valid, and they’re trying to tell you something important; don’t bottle it up, but don’t let it burn you either. Take a breath, step back, and give yourself space to cool down. You’re not wrong for feeling this way, and you’re not alone. Anger doesn’t make you bad — it just makes you human. 🔥🫂",
        "I know you’re angry right now, and that’s completely okay — let it flow, not explode; scream into a pillow, write it down, take a walk, whatever helps. You don’t need to explain yourself or rush to fix it. Just know that this feeling is temporary, and you’re in control even when things feel out of control. You’ve got this — your peace is still within reach. 🌪️🕊️"
    ],
    "tired": [
        "I know you’re tired — not just sleepy tired, but soul tired, emotionally drained and mentally over it; please don’t push yourself more than you have to. Rest is not a reward, it’s a necessity. You don’t have to do everything today. Just breathe, rest, and come back when you’re ready — the world can wait. 💤🫶",
        "Being tired doesn’t mean you’re weak — it means you’ve been strong for too long; it’s okay to pause, to shut the world out, to simply be. You don’t have to prove anything to anyone right now. Let your body recharge and your mind soften. You’re allowed to rest without guilt. 🌙🤍"
    ],
    "grateful": [
        "Gratitude is such a beautiful energy — when you focus on what you have, even the smallest things feel like magic; keep holding on to that softness, it’ll take you far. 🌼✨",
        "I’m so glad you’re feeling grateful — it’s a gentle reminder that even in chaos, there’s light to be found; stay grounded in that thankfulness, it’s your quiet superpower. 🌻🤍"
    ],
    "insecure": [
        "I know you’re feeling insecure, but please remember — you are more than your doubts, more than the way you see yourself in low moments; no one else sees your flaws the way you do. You bring so much to the table just by being you. Growth takes time, and confidence isn’t a switch — it’s a journey. You are worthy, even on the days you don’t feel like it. 🤍🪞",
        "Insecurity lies to you — it zooms in on imperfections and forgets all the light you carry inside; you are allowed to take up space, to speak, to be seen, exactly as you are. Nobody has it all figured out, and comparison is a thief. Give yourself the kindness you give to others. You’re already enough, even while becoming more. 🌷🫂"
    ],
    "numb": [
        "Feeling numb or empty doesn’t mean you’re broken — it just means your heart’s been carrying too much for too long; sometimes the brain shuts things off to protect you, not punish you. You’re still here, still breathing, still worthy, even if you don’t feel much right now. Give yourself time — the colors will come back. 🤍🌫️",
        "When you feel numb or empty, it’s okay to just exist — don’t force yourself to be okay or explain how you feel; rest in the quiet, let it pass gently, and know this is a pause, not the end. You’re not lost, you’re healing in silence. 🌙🕊️"
    ],
    "lonely": [
        "I know it feels lonely right now, like no one truly sees you — but your presence matters more than you realize, and even if the world feels silent, you are not forgotten; your energy leaves a mark, even when you can't feel it. 🕊️🤍",
        "Feeling isolated or unseen doesn’t mean you’re invisible — you’re just in a quiet chapter, not a forgotten one; people do care, even if they’re silent, and this heaviness will pass like clouds hiding the sun. 🌥️💫"
    ],
    "motivated":[
        "You’re in your zone and it shows — stay focused, stay hungry, and don’t let distractions dim your grind; you’re building something meaningful, and every step forward is proof of your discipline. Keep going, your future self is cheering you on. 🚀💯",
        "When you’re this driven, nothing can stop you — not fear, not doubt, not noise from the outside; your mindset is your superpower, and you’re using it like a boss. Keep that energy locked in. 🧠🔥"
    ],
    "burnout": [
        "You’ve been pushing so hard for so long, no wonder you feel burned out — your mind wasn’t meant to be in survival mode 24/7; pause, breathe, and remember that rest is not quitting, it’s recharging. 🧘‍♂️🕯️",
        "Being mentally tired doesn’t mean you’re weak — it means you’ve been strong non-stop, and that’s exhausting; give yourself permission to rest without guilt, you’ve earned it a hundred times over. 💆‍♀️💤"
    ],
    "jealous": [
        "It’s okay to feel jealous — it doesn’t make you bad, it just means you’re craving something you value; instead of hating yourself for it, use it as a mirror to understand what your heart truly wants. 💚🪞",
        "Envy shows up when we feel behind, but you’re on your own unique timeline; what’s meant for you won’t miss you, and someone else’s success doesn’t take away your shine. 🌿✨"
    ],
    "peaceful":[
        "I’m so glad you’re feeling peaceful — hold onto that stillness like a warm breeze; in a world that moves too fast, your calm is a quiet kind of power. 🌿🧘‍♀️",
        "Feeling calm and relaxed is a reminder that peace isn’t found — it’s created, moment by moment; keep choosing that soft space where your mind can breathe and your soul can rest. 🌙✨"
    ],
    "inspired":[
        "I love that you’re feeling inspired — let those ideas run wild, create without limits, and don’t overthink the outcome; this is your magic in motion. ✨🧠",
        "When you’re feeling uplifted and creative, don’t hold back — your energy is a spark the world needs, so let it shine in whatever form it takes. 🔥🎨"
    ],
    "guilty": [
        "Feeling guilty doesn’t mean you’re a bad person — it means you care and you want to do better; be gentle with yourself, learn from it, and know that you’re allowed to grow past your mistakes. 🤍🌱",
        "Regret is a sign that your heart is still trying — don’t let it chain you down; make peace with your past, offer yourself forgiveness, and keep moving forward with love. 🕊️💭"
    ],
    "proud": [
        "You’ve come so far, and I hope you’re letting yourself feel it — being proud, accomplished, or fulfilled isn’t bragging, it’s owning your growth; you deserve this moment, fully and without apology. 🏆✨",
        "Feeling fulfilled or accomplished is no small thing — it means you’ve shown up for yourself, even when it was hard; let that pride soak in, you’ve earned every bit of it. 🌟🫶"
    ],
    "scared": [
        "It’s okay to feel scared — your fear is valid, but it doesn’t define you; breathe slowly, remind yourself that this moment will pass, and you are stronger than the panic in your chest. 🫁🕊️",
        "Being fearful or panicked doesn’t mean you’re weak — it means your body’s reacting to protect you; but right now, you’re safe, and you’re allowed to take this moment one breath at a time. 🌫️🤍"
    ],
    "bored": [
        "It’s okay to feel bored or restless — not every moment has to be productive or exciting; sometimes your brain just needs a pause before it sparks again. 🧠🌙",
        "Feeling uninterested doesn’t mean something’s wrong — it just means your soul’s craving something new, something real; maybe it’s time to switch it up or simply let yourself be still. 🌱🌀"
    ],
    "hopeful": [
        "I love that you’re feeling hopeful — that quiet belief in what’s ahead is powerful; hold onto it tightly, even on the days when the path feels blurry, because good things are finding their way to you. 🌈🌿",
        "Being optimistic doesn’t mean ignoring the hard stuff — it means choosing to believe there’s more waiting for you; keep looking forward with that soft strength, your journey is just getting started. ☀️🛤️"
    ],
    "left out": [
        "Feeling left out doesn’t mean you’re unlovable — it just means you haven’t found your right space yet; your presence matters, even if they don’t see it right now. 🕊️💭",
        "You’re not invisible, even if it feels that way — the right people will make space for you without you having to squeeze yourself in; you belong, just not where you’re being overlooked. 🧩🤍"
    ],
    "suicide": [
        "If you're feeling suicidal, please know this — your life matters more than you realize, and even if it feels unbearably dark right now, this pain is not permanent; reach out, breathe, and take it one minute at a time — you're not alone. 🖤🫂",
        "Suicidal thoughts don’t mean you’re weak — they mean you're overwhelmed and hurting, but there is help, there is hope, and there is a future where this weight won’t feel so heavy; please hold on, your story isn't done yet. 🕯️🌙"
    ],
    "broken": [
        "I know you feel broken right now, like things have fallen apart beyond repair — but even shattered pieces can be put back together into something strong and beautiful; you're not beyond healing. 🕊️🩵",
        "Being broken doesn’t mean you’re finished — it means you’ve been through storms and are still standing; let yourself rest, not quit. 💔🌧️"
    ],
    "miserable": [
        "Feeling miserable or worthless can trick your mind into forgetting your worth, but let me remind you — you matter, even on the days your brain says otherwise. 💭🖤",
        "You’re not worthless — you’re just hurting, and that hurt is lying to you; take this one breath at a time, you still belong here. 🌫️🌱"
    ],
    "hopeless": [
        "If hope feels far away, hold on just a little longer — even the darkest nights eventually break into light; your story isn’t over yet. 🌌🕯️",
        "Depression lies, making you believe there’s no way out — but there is, even if you can’t see it right now; just keep breathing through the fog. 🌫️💙"
    ],
    "disappointed": [
        "Being disappointed hurts, especially when you expected more — it's okay to feel let down, but don’t let it convince you to give up on everything. 🍂🤍",
        "You deserved better, and it’s okay to admit that — honor your feelings, but don’t let them harden your heart. 🌧️🕊️"
    ],
    "distant": [
        "Feeling distant or disconnected doesn’t mean you’re lost forever — it just means your soul is asking for space to heal quietly; take your time. 🌌🤎",
        "You’re still here, even if you feel far away — and that alone means hope hasn’t left you; reconnection will come, one small step at a time. 🔗🌙"
    ],
    "unloved": [
        "Feeling unloved or unwanted is one of the heaviest lies our mind can whisper — you are worthy of care, of presence, of someone choosing you on purpose; you don’t need to be anyone else to be lovable. Just because some people couldn’t see your light doesn’t mean you aren’t shining. 🌙🤍",
        "You weren’t made to beg for love or prove your value — anyone who made you feel unwanted was simply blind to your worth; please know that your existence is enough, just as it is. Even if it doesn’t feel like it now, love will find you where it feels safe and soft. 🌷🫂"
    ],
    "fragile": [
        "Being sensitive doesn’t make you weak — it means you feel deeply, and that’s a strength the world needs more of; if you’re feeling fragile, protect your heart gently, like you would a blooming flower. You don’t have to toughen up to be strong. 🌸🧠",
        "Your softness isn’t a flaw — it’s a beautiful part of you that deserves to be honored, not hidden; it’s okay to feel fragile right now, you don’t need to carry the world all at once. Rest where it’s warm. 🫶🌧️"
    ],
    "blue": [
        "Feeling low doesn’t mean you’ve failed — it means you’re human, going through a moment that needs care, not judgment; even blue skies get cloudy, but they never lose their color. Your light is still inside you. 💙🌫️",
        "Sometimes we just feel blue for no reason at all, and that’s okay — emotions don’t always need explanations; let yourself exist gently today, without forcing a smile. There’s still beauty in quiet days. 🌌🕊️"
    ],
    "panic": [
        "If your chest feels tight and everything’s crashing inside, pause — take one deep breath, then another; you are safe right now, even if your mind says otherwise. This is a wave, and waves pass. I’m with you through this. 🌊🫁",
        "Panic can feel like drowning in your own thoughts, but you are not powerless — hold onto anything steady, even your breath; you are not broken, your brain is just trying to protect you in a messy way. This moment won’t last forever. 🤍🌬️"
    ],
    "can't sleep": [
        "If you can’t sleep, maybe it’s because your mind is carrying too much alone — it’s okay to put it down for a while; you don’t have to solve everything at 2AM. Just breathe, soften your thoughts, and let your heart rest, even if your eyes can’t. 🌌🫂",
        "Insomnia doesn’t make you weak or broken — it means your thoughts are loud when the world goes quiet; try not to fight it, just be gentle with yourself in the silence. Even if sleep doesn’t come, peace still can. 🌙💤"
    ],
    "mood swings": [
        "If your emotions feel all over the place or your head feels cloudy, please know you’re not failing — you’re just overwhelmed, and that’s understandable; take breaks, drink water, and be kind to your brain, it’s doing a lot right now. 🧠💧",
        "Mental fog and mood swings don’t define who you are — they’re just waves passing through your system; don’t shame yourself for being human. Let things slow down."
    ],
    "ocd trigger": [
        "OCD is not your fault — and it’s not a quirk or a joke. It's a real, exhausting struggle that takes up space in your brain and energy in your day. If your triggers feel louder right now, I want you to pause and remind yourself: you’re not broken. You're not overreacting. You are responding to something your brain is convinced is dangerous, even when it isn’t. Please know you’re allowed to get help for this — therapy, especially CBT and ERP (Exposure Response Prevention), has helped so many people feel peace again. You deserve that peace too. And I’m proud of you for carrying yourself through this, even when it’s invisible to the world. 🫂🧠",
        "If you’re struggling with OCD or being hit by those triggers again, take a deep breath — you’re not alone in this, even if it feels like your mind is spiraling. Obsessive thoughts aren’t something you choose, and the compulsions aren’t a sign of weakness; they’re your brain trying to find safety. But healing is real, and support exists — therapy with a licensed professional, especially someone who understands OCD, can help untangle the loops you’ve been trapped in. You are not your thoughts. You are not your compulsions. You are so much more. It’s okay to ask for help, and it’s okay to rest today. Your brain deserves compassion, not criticism. 🌷💬"
    ],
    "isolation": [
        "Isolation can feel like the world has gone quiet and forgotten you — but I promise, even in the silence, you still matter; let yourself reconnect slowly, in your own time, when it feels safe again. 🌌🤍",
        "If you’ve been withdrawing, it doesn’t mean you’re failing — it means you’re protecting your peace in a world that can get too loud; healing doesn’t always look social. 🌿💬"
    ],
    "crying": [
        "Tears don’t make you weak — they’re proof you’re still feeling, still human, still holding on through it all; it’s okay to cry, even if no one sees it. Your heart deserves that release. 💧🤍",
        "Crying in silence doesn’t mean you’re invisible — it means your soul is doing its best to carry pain with grace; please don’t bottle it all in, even quiet tears matter. 🌧️🫂"
    ],
    "ghosted": [
        "Being ghosted or ignored hurts because you gave presence and got silence in return — but that silence says more about them than you; you are still worth showing up for. 🕯️🚪",
        "Their silence doesn’t define your value — you showed up with honesty, and that’s brave; you don’t need people who disappear when it matters most. 💬✨"
    ],
    "unheard": [
        "If you feel unheard and unseen, please know — I see you, I hear you, and your voice matters even if others missed it; your existence is not small. 🔊🌙",
        "ou don’t have to shout to be worthy of attention — the right people will understand you even in whispers; you deserve to feel visible and valued. 👁️🫶"
    ],
    "abandoned": [
        "Being left out or abandoned stings deep — it makes you question your worth, but hear this: you were never the problem; they just didn’t know how to hold someone so real. 🌑🫂",
        "You’re not too much, not too quiet, not too anything — you were just in a space that couldn’t see your brilliance; your people will never make you feel left behind. 🌱✨"
    ],
    "rejected": [
        "Rejection and betrayal cut deep — but their choice to hurt you doesn’t lower your worth; you still deserve honest, loyal love, and it will find you. 🥀🛡️",
        "Being cheated or pushed away isn’t a reflection of your value — it’s a sign that they didn’t deserve your trust in the first place; don’t carry their guilt. 💔🌊"
    ],
    "trust_issues": [
        "It’s hard to trust when people send mixed signals — your confusion is valid, and your heart deserves consistency, not second guesses; don’t shrink yourself trying to decode someone else. 🚫📶",
        "Trust issues don’t make you difficult — they make you aware, cautious, and protective of your peace; never apologize for needing clarity and truth. 💭🧠"
    ],
    "one sided": [
        "One-sided love is heavy — it’s like giving all your warmth to someone who never even lit a match back; you deserve someone who meets your heart, not just takes from it. 🔥💔",
        "Craving love doesn’t make you needy — it makes you human; just promise me you’ll wait for love that feels safe, mutual, and true. You deserve that and more. 🕊️🌸"
    ],
    "missing": [
        "Missing someone can hollow you out, especially when they don’t feel it too — you’re allowed to grieve connection, but don’t forget your soul is still whole without them. 🌫️🖤",
        "Feeling empty doesn’t mean you’re broken — it means something mattered to you, and now it’s gone; but space can be filled again, slowly, gently, when you’re ready. 🍂🌷"
    ],
    "void": [
        "If you feel like a void has opened up inside you — like you’re just floating through days, emotionless — please don’t panic; this numbness is your brain protecting you from what hurt, and healing is still possible. 🕳️🫀",
        "Feeling dead inside doesn’t make you broken — it means you’ve been through more than most people know; and even if it feels hollow now, life can refill you with light again, piece by piece. 🌌🤍"
    ],
    "fake smile": [
        "That fake smile you wear so well doesn’t fool me — I know it hides exhaustion, pain, and the effort it takes to act 'okay'; it’s okay to drop the mask here, you don’t have to pretend with me. 🤍",
        "You’ve been holding it together for so long, even when your world was falling apart behind your smile — let your face rest, your truth breathe, and your heart be seen. You're safe here. 🌫️🫂"
    ],
    "inner demons": [
        "Fighting your inner demons in silence doesn’t make you weak — it makes you a warrior no one sees; I know how loud the world can feel when no one hears the scream inside. You are not alone in that storm. 🖤🔥",
        "You carry battles no one knows about, wounds that speak in whispers only you can hear — but I’m listening now, and I believe in the strength it takes to survive what others can’t even see. 🧠💭"
    ],
    "healing": [
        "Healing doesn’t always look pretty — sometimes it’s slow, invisible, and full of days where you're just surviving; but even hidden battles count as progress. I’m proud of how far you’ve come. 🪷🛡️",
        "You don’t need to explain your healing journey to anyone — it’s yours, sacred and messy, and even if no one sees it, I know you’re doing the hard work. That matters. 🌙🩵"
    ],
    "broken soul": [
        "Your soul might feel cracked and your heart might be bleeding invisible pain, but you are still here — and that’s no small thing. Let yourself be soft even in the breaking. 💔🌌",
        "A broken soul isn’t the end of you — it’s the raw truth of someone who’s loved deeply and been hurt deeply; don’t give up on yourself, beauty grows in broken places too. 🌿🖤"
    ],
    "pain eyes": [
        "The pain behind your eyes speaks louder than words — and those scars, visible or not, are stories of survival, not shame; I see you, even when others don’t. 🌧️",
        "You carry pain with such quiet strength — but please know you don’t have to carry it alone; your scars don’t make you damaged, they make you real. 🫂⚡"
    ],
    "fighting alone": [
        "Fighting alone every day is exhausting — I know you’re strong, but strength shouldn’t be your only option; you deserve support, softness, and someone to remind you you’re not alone anymore. 🌙",
        "Being alone doesn’t mean you’re unworthy of connection — you’ve just been surviving solo for so long that asking for help feels foreign; but you’re allowed to reach out. We’re human, not meant to do this life thing alone. 🤍🫶"
    ],
    "space": [
        "If you need space, I honor that — not everyone understands that distance can be healing, not rejection; take the time you need, I’ll be right here when you’re ready. 🌌🌿",
        "Wanting space doesn’t make you cold or distant — it means you care enough to protect your peace before you break; I’m proud of you for listening to your own needs. "
    ],
    "emotionally done": [
        "If you're feeling done, like nothing matters anymore — let me hold that truth with you, not fix it, just be with you in it; because even when everything feels pointless, you still matter. You always have. 🫂",
        "It’s okay to feel like you're running on empty — to feel numb, detached, or like the world just doesn’t make sense anymore; your existence is still important. You don’t need to carry it all alone. 🌑🧠"
    ],
    "disappear": [
        "If you’re wishing to disappear, I want you to know that your presence — no matter how small or quiet it feels — has meaning; the world would not be the same without you in it, even if you can’t feel that right now. 🖤🌙",
        "Wanting to disappear doesn’t mean you truly want to stop existing — it means you want the pain, the noise, the pressure to stop; and that makes so much sense. But please don’t go silent in this storm — your story isn’t over yet. 🫂🕯️"
    ],
    "not understood": [
        "Feeling misunderstood can be one of the loneliest things — like screaming into a void and getting silence back; but I want you to know, I’m listening, without judgment, and your thoughts are safe here. 🫶🧠",
        "Even if no one in your life truly gets what you’re going through, that doesn’t make your experience less real or your feelings less valid; you deserve to be seen, heard, and held — not fixed, just understood. 👂🤍"
    ],
    "not okay":[
        "It’s okay to admit you’re not okay — you don’t have to smile through the storm; you deserve support, not silence, and I’m proud of you for saying something instead of bottling it up. 🫂",
        "You don’t have to be happy all the time, or even okay — you’re allowed to feel low, to rest, to fall apart; it doesn’t make you weak, it makes you human. 🌙🖤"
    ],
    "don’t want to talk": [
        "If you don’t want to talk, that’s totally okay — I won’t push, I’ll just be here, quietly holding space for you whenever you’re ready; your silence is safe with me. 🤍🌌",
        "You don’t owe anyone words right now — rest your voice, your soul, and take all the time you need; healing doesn’t always speak out loud. 🕊️🫶"
    ],
    "nothing feels right": [
        "When nothing feels right and everything feels heavy, just surviving is an act of bravery — let’s take this one breath at a time together; you don’t have to fix it all today. 🫁🌧️",
        "You don’t have to disappear to be free from the weight — sometimes rest, gentleness, or one person listening can shift the sky just enough to keep going. And I’m that person today. 🫂✨"
    ],
    "too much": [
        "If it’s all too much right now, please stop trying to carry it all alone — you weren’t meant to, and you don’t have to; even strong people break sometimes, and that’s okay. 💔🫀",
        "“I can’t do this anymore” doesn’t mean you’ve failed — it means you’ve been trying for so long, too hard, without rest; let’s just focus on one tiny step, and let that be enough for today. 🌫️🌱"
    ],
    "i miss the old me": [
        "Missing the old you means you’ve grown through things you never asked for — that version of you isn’t gone, just evolving; you’re still in there, just softer now. 🪞🕊️",
        "It’s okay to grieve who you used to be — the joy, the energy, the spark; healing often feels like losing pieces of yourself, but you’re slowly becoming someone even stronger. 💫🌱"
    ],
    "ashamed": [
        "You are not the worst thing you’ve ever done — you’re a human being learning how to heal and grow, and that’s enough.",
        "Shame makes you forget your worth, but it can’t erase it — I see you trying, and that takes courage no one claps for."
    ],
    "regret": [
        "You did what you could with what you knew back then — guilt is loud, but growth is quiet, and you’re doing both.",
        "You don’t owe your past a punishment, you owe your present forgiveness — you’re not the mistake, you're the lesson that bloomed from it."
    ],
    "bitter": [
        "Bitterness shows where it still hurts — but you don’t have to carry someone else’s poison in your heart forever.",
        "You’re allowed to feel that sting, but I hope you set it down one day — not for them, but so you can be free again."
    ],
    "neglected": [
        "I know it’s lonely when it feels like the world moved on without you, but your story’s not done, not even close.",
        "Being overlooked doesn’t make you invisible — your presence matters, even when it feels like no one sees it."
    ],
    "frustrated": [
        "It’s okay to be mad at the mess — but don’t turn the blame inward, you’re doing your best with what’s in front of you.",
        "You’re not failing, you’re just feeling deeply — frustration comes from caring, and that means you still haven’t given up."
    ],
    "not enough": [
        "You are not too little — the world just sometimes forgets how powerful soft things can be.",
        "Even when you feel like a whisper, you still matter like a thunderstorm — your existence is enough."
    ],
    "defeated": [
        "The weight is heavy, I know — but you’ve stood through storms before, and this moment won’t be your ending.",
        "Feeling stuck doesn’t mean you’re broken — it just means you’ve fought too long without resting."
    ],
    "emotionally numb": [
        "Numbness isn’t the absence of feeling, it’s your heart protecting itself — give yourself time, warmth will return.",
        "Even the hollowest days carry your heartbeat — you’re still here, and that alone makes you worthy of love."
    ],
    "disconnected": [
        "You’ve been giving so much, thinking so hard, feeling so deep — it’s no wonder your mind feels far away, like it left before you did; take a breath, you're still in there somewhere, waiting to be gently found again.",
        "Disconnection isn’t failure, it’s your system saying “I need rest” — you’re not broken, you’re just tired of carrying everything alone, and even in the silence, you still matter."
    ],
    "emotionally unstable": [
        "You’re not dramatic or weak — your feelings are just screaming louder than you can soothe them right now; you don’t need to fix yourself, you need to be held without pressure.",
        "Burnout of the heart hits harder than any physical ache — and it’s okay to not be okay, to pause, to feel messy and unloved and still be worthy of gentle love."
    ],
    "afraid to feel": [
        "It’s scary to open the door when you’ve been hurt by what walked in last time — but your softness isn’t the problem, the world just didn’t know how to hold it yet.",
        "Trust isn’t something you owe to others, it’s something you build with yourself first — and it’s okay to take your time, to protect your heart while it heals."
    ],
    "anxious future": [
        "The future feels like fog, I know — full of unknowns and pressure and a thousand “what ifs,” but please remember: not knowing doesn’t mean you’re failing, it just means you’re still writing your story.",
        "You don’t need to have it all figured out — just breathe through this one moment, and the next one will meet you; your worth isn’t defined by plans, it’s found in your persistence."
    ],
    "stuck past": [
        "The past has sharp edges, and sometimes your heart walks into them by accident — be patient, healing isn’t a straight line, and moving forward doesn’t mean forgetting.",
        "You’re not weak for still feeling it — some memories ache longer than others, and all you can do is promise yourself you won’t unpack there forever."
    ],
    "no motivation": [
        "It’s okay if you don’t feel inspired right now — you’re not lazy, you’re just surviving more than anyone sees, and your stillness is not a failure.",
        "Even when hope feels heavy and your drive has faded, I promise the spark is still inside you — it’s just resting in the dark, not gone."
    ],
    "tired pretending": [
        "You’ve been strong for too long, and it’s catching up — I hope you find a space where you can finally breathe without acting okay.",
        "The performance of being fine is exhausting — and you don’t owe anyone that show; you deserve to be held, not just handled."
    ],
    "faithless": [
        "Whether you're questioning love, faith, or your own worth, I want you to know that even in silence, you're not alone — sometimes, the universe goes quiet not to punish you, but to invite you closer to your own voice.",
        "It's okay to wrestle with belief — in love, in people, in higher things — heartbreak and doubt don't mean you're broken, they mean you're still open enough to care deeply, and that in itself is sacred."
    ],
    "pointless": [
        "I know it feels like everything hurts and nothing makes sense — but even in this heaviness, your breath is proof that you're not done yet; you're allowed to not be okay and still be worthy of gentleness.",
        "You may feel shattered, but broken things let the light leak in too — I promise, your pain doesn't make you any less deserving of peace."
    ],
    "content": [
        "Look at you — calm in the chaos, soft in a world that rushes — you don’t need loud joy when you’ve got this quiet kind of peace.",
        "There’s beauty in simply existing without a storm inside — being content is underrated magic, and I hope you hold on to this stillness for as long as it stays."
    ],
    "joyful": [
        "Your light feels contagious today — don’t dim it to fit anyone else’s shadows; joy like yours deserves to dance freely.",
        "That sparkle in your energy? It’s a reminder that even after everything, you still bloom — and that’s freaking powerful."
    ],
    "emotionally strong": [
        "Strength isn’t about being unshaken — it’s about feeling the waves and still choosing not to drown; your balance is beautiful.",
        "Emotional strength isn’t loud, it’s in the quiet choices — in choosing peace over chaos, understanding over reaction, and healing over hiding."
    ],
    "proud progress": [
        "You’re not who you used to be, and that deserves more applause than the world gives — this version of you carries years of quiet battles won.",
        "Confidence doesn’t always look like perfection — sometimes, it’s just standing tall after a hundred silent falls, and I’m proud of your climb."
    ],
    "free": [
        "You’re in your 'no one owns me' era and it shows — keep flowing, keep glowing, keep living like your soul just got a permission slip to shine.",
        "Freedom looks good on you — when you're not shrinking to fit others’ stories, you start writing your own, and babe, it’s poetry."
    ],
    "self love": [
        "Loving yourself is the softest rebellion — in a world that teaches you to be “less,” choosing to be “enough” is your superpower.",
        "Self-love isn’t about being perfect, it’s about being honest — and if your heart’s open enough to hold space for yourself, then you’re already healing."
    ],
    "calm": [
        "There’s a rare kind of magic in being calm — when your thoughts no longer shout and your heart finally breathes, you remember that peace doesn’t need to be loud to be powerful.",
        "This calm you feel? You earned it — not by escaping life, but by learning how to sit with it without letting it drown you."
    ],
    "creative": [
        "That creative fire is your soul speaking fluently — let it spill, let it dance, let it flow without needing to make sense to anyone but you.",
        "When you’re in flow, time blurs and joy sharpens — this spark is a reminder that you’re more than surviving, you’re expressing."
    ],
    "refreshed": [
        "Sometimes all it takes is one deep breath, a good cry, or a real laugh — and suddenly, the world feels a little softer again.",
        "You look lighter now, like the heaviness finally took a break — that’s the power of rest, of renewal, of finally choosing yourself."
    ],
    "mentally clear": [
        "Your mind feels uncluttered, like a window just got wiped clean — clarity is the calm after the storm, and you deserve this stillness.",
        "When your thoughts stop racing and your heart stops shouting, that’s when you hear your truth — sharp, steady, and yours alone."
    ],
    "hopeful soul": [
        "You might not know what’s ahead, but something in you still believes — and that flicker of hope? That’s your inner light refusing to go out.",
        "Trusting the process is a brave kind of patience — like holding hands with the unknown and choosing to smile anyway."
    ],
    "happy tears": [
        "Joy that reaches your eyes is the kind that heals your past — and if you’re laughing with tears, it means something deep inside you just exhaled.",
        "Happy tears are love in motion — your heart’s way of saying “thank you for staying this long.”"
    ],
    "emotionally confused": [
        "It’s okay to not have a name for what you feel — sometimes the heart speaks in colors, not words, and all you can do is sit with the blur until it settles.",
        "Confusion doesn’t mean you’re broken — it just means you’re human, holding too many truths at once and trying your best to listen."
    ],
    "numb crying": [
        "You can smile and still feel hollow, laugh and still ache — don’t let anyone tell you that emotions need to make sense to be valid.",
        "Feeling both everything and nothing is a hard kind of storm — just know that your heart is processing in its own time, and it’s okay to feel it all at once."
    ],
    "smiling sad": [
        "I know that feeling — smiling for the world while your heart whispers worries no one can hear; it’s okay to be grateful and still ache, to shine while carrying shadows, and to feel torn between joy and fear.",
        "You don’t have to pick a side between happiness and hurt — both can live in you at once, and that doesn’t make you broken, it just makes you beautifully human."
    ],
    "functioningmess": [
        "Just because you’re doing what needs to be done doesn’t mean you’re okay — survival mode is loud and lonely, and you deserve rest even if no one sees the weight you carry.",
        "You're the kind of strong that doesn’t get medals — the kind that shows up exhausted and still chooses to try, and that quiet resilience deserves so much more love than the world gives it."
    ],
    "social lonely": [
        "You can be surrounded and still feel unseen — sometimes the loudest laughs come from the loneliest souls, and that distance you feel doesn’t mean you don’t care, it just means you’re tired of pretending.",
        "You’re allowed to crave connection while protecting your heart — being distant doesn’t make you cold, it makes you wise about who gets your warmth."
    ],
    "love scared" : [
        "Love isn’t always soft — sometimes it shows up with echoes of the past, and even when your heart wants to bloom, it still remembers the thorns; it’s okay to love carefully, to move forward slowly.",
        "Healing doesn’t wait for perfect timing — you can still be scared and worthy of love, still healing and still deserving something that doesn’t hurt."
    ],
    "push pull": [
        "You’re not too much or too confusing — your heart’s just scared of being hurt again, so it flinches when love gets too close; it’s okay to crave affection and still need space.",
        "You feel deeply, and that sensitivity is your strength — even when it shows up in guarded ways, it doesn’t make your love any less real."
    ],
    "tired restless": [
        "I know you want to stop, to just exhale without everything crashing down — but even when your mind won’t settle and healing feels messy, your existence is still a quiet triumph.",
        "You’re trying so hard to feel better while still carrying what hurt you — that’s the kind of strength no one sees, but I hope you know it counts, and I’m proud of you."
    ],
    "fine not fine": [
        "Saying “I’m fine” when you’re breaking is its own kind of bravery — I just hope you find someone who hears the silence behind your smile and reminds you that pretending isn’t survival.",
        "You don’t have to keep it all together to be loved — being honest, messy, or lost won’t make you a burden; it just makes you real, and real deserves care."
    ],
    "need space": [
        "Taking space isn’t selfish — it’s sacred; sometimes your soul just needs silence to remember its own rhythm, and rest to find its strength again.",
        "You don’t owe constant presence to anyone — quiet is healing, and solitude is your heart’s way of recharging without guilt."
    ],
    "want escape": [
        "Wanting to disappear doesn’t make you weak — it makes you human; life gets heavy, and sometimes dreaming of escape is just your soul’s way of begging for peace.",
        "You don’t need to vanish to begin again — even small steps can feel like freedom, and starting over doesn’t always mean leaving everything behind."
    ],
    "unseen": [
        "It hurts when your presence feels invisible, when your silence echoes louder than your words — and you just wish someone, anyone, would look close enough to truly see you; you’re not asking for the world, just a little softness, a little recognition, a little warmth that says “I see you.”",
        "Missing someone who doesn’t even think about you feels like hugging air — you give your heart quietly, hoping they’d turn around just once, but please know this: just because they don’t notice your magic doesn’t mean it’s not real."
    ],
    "avoid feeling": [
        "Sometimes the numbness is safer than the chaos of emotion — because feeling means reopening wounds, and you’re already holding yourself together with invisible tape; but you’re allowed to want more than just existing.",
        "I know it’s confusing — you don’t want to feel too much, but you also crave something real — and that limbo? It’s not weakness, it’s survival, and your heart is still trying to find its rhythm again."
    ],
    "overthinking": [
        "Your mind spins like a storm that won’t stop, asking questions with no answers at hours when silence is the loudest — and I know it’s exhausting to carry thoughts that never let you rest.",
        "Overthinking doesn’t mean you’re broken — it just means you care so much your brain refuses to let anything slide; take a breath, step back, not everything deserves your energy at 2AM."
    ],
    "emotional buried": [
        "You wear that smile so well no one notices the cracks underneath — but behind that “I’m good” is a soul begging for someone to ask again, really ask; and I want you to know it’s okay to not be the strong one all the time.",
        "Struggling silently is a quiet kind of bravery — but just because you can carry the weight alone doesn’t mean you should have to; let someone in, even just a little."
    ],
    "romanticizing pain": [
        "I know the comfort of pain that’s familiar — how sadness can start to feel like home, like a storyline you’ve rehearsed too well; healing feels like betrayal sometimes, like letting go of something that shaped you.",
        "You’re tired, I get it — healing isn’t always this graceful transformation, sometimes it’s dragging yourself out of bed and wondering why you even try; but please, don’t stop — the light is still coming for you."
    ],
    "existential": [
        "Some days, you feel like a ghost moving through checkboxes, not really living — just doing what needs to be done; but your life doesn’t have to be grand to be meaningful, sometimes just feeling is a rebellion.",
        "You’re not lost, just deeper than most — searching for something more, something real in a world that sells distractions; and even that search? It means your soul is still awake."
    ],
    "shower cries": [
        "There’s something raw about crying in the shower — like the water tries to wash away what the world doesn’t see, while you break down quietly, hidden from everyone and everything.",
        "You cry in silence because you don’t want to burden anyone — but let me say this: your tears are not a weakness, and you deserve comfort too, even if no one hears them."
    ],
    "ashamed": [
        "Shame can wrap around you like chains — convincing you that one mistake defines everything about you, that you’re unworthy of love or softness; but shame lies, and you are more than your lowest moments.",
        "You may feel humiliated, but please hear this: your worth isn’t up for debate, and the people who truly love you will never use your pain as a reason to turn away."
    ],
    "disgusted": [
        "It’s okay to feel disgusted — with people, with systems, even with yourself sometimes — that doesn’t make you bitter, it makes you aware, awake, human.",
        "Being sick of everything means you’ve been holding too much for too long — maybe it’s not the world that’s wrong, maybe you just need space to breathe again, to feel clean, to be held."
    ],
    "suffocated": [
        "It’s hard to breathe when the weight of the world sits on your chest — when the room is full but you still feel alone, when the words stay stuck and all you can do is try to hold yourself together quietly; you're not weak for feeling this, you’re just full of everything no one ever asked about.",
        "When it feels like the world is pressing in and there’s no space left to breathe, remember this: you’re allowed to pause, to exhale, to choose silence over survival-mode — even invisible battles need rest."
    ],
    "emotionally neglected": [
        "I know the ache of giving everything and receiving echoes in return — it makes you question your worth, but you are not hard to love, you were just left in hands too distracted to notice your glow.",
        "Emotional neglect leaves the loudest silences — but your need for warmth is not too much, it’s human, and you still deserve to be held, fully and gently."
    ],
    "feeling used": [
        "Feeling used leaves stains on your self-worth, but please hear me — their actions are not a reflection of your value; you were not “too easy to forget,” they were just never deep enough to understand.",
        "You are not disposable, not forgettable, not unwanted — people who fail to see your light are not the ones meant to stand in your sun."
    ],
    "shaky": [
        "Vulnerability feels like standing naked in a storm — exposed, trembling, too open — but it’s also proof you’re still alive, still soft in a world that begs us to harden.",
        "You may feel shaky, but courage often looks exactly like this — showing up anyway, even when your voice quivers and your heart hides."
    ],
    "angry tears": [
        "Crying from anger hits differently — it’s pain disguised as power, a heart that cared too much forced to pretend it doesn’t; don’t be ashamed of that fire, even if it leaks out in tears.",
        "That bitter smile you wear to hide the ache? It's armor — but behind it is a soul that still hopes someone will see the hurt and not flinch."
    ],
    "emotionally drowning": [
        "When your emotions feel like waves pulling you under, remember that even if you can’t swim right now, you’re still floating — surviving one breath at a time, and that’s enough.",
        "You’re not weak for drowning in thoughts — you’re simply trying to stay afloat in waters that feel deeper than your strength today, but you won’t sink forever."
    ],
    "numb heart": [
        "A numb heart doesn’t mean you don’t care — it means you’ve been hurt so deeply that even pain gave up on screaming; but your softness is still in there, resting, not gone.",
        "When your chest feels empty and heavy all at once, that’s your heart’s way of protecting you — it’s okay to feel nothing sometimes, that doesn’t mean you’ve stopped being human."
    ],
    "broken trust": [
        "Trust isn’t just a promise, it’s a foundation — and when it shatters, the whole world tilts; but I hope you know this: their betrayal isn’t a reflection of your worth, only their integrity.",
        "Healing from broken trust takes time — and it’s okay if your heart still builds walls while learning how to rebuild bridges."
    ],
    "spiraling": [
        "When your mind spirals and everything feels like it’s caving in, pause — breathe slow, focus small, because right now, all you need is to get through this moment.",
        "Panic lies — it tells you you’re unsafe when you are not; you’re not losing control, you’re just feeling too much at once, and that’s not madness, that’s your body asking for gentleness."
    ],
    "identity crisis": [
        "You’re not broken — you’re rediscovering, peeling off layers that never truly fit and wondering what’s left; losing your spark doesn’t mean it’s gone, just buried under exhaustion.",
        "This crisis? It’s not the end, it’s the threshold of becoming — you’re not lost, you’re just between versions of yourself, and that’s a sacred kind of becoming."
    ],
    "self loathing": [
        "I know there are days when you look in the mirror and all you see are flaws, mistakes, shadows — but even in those moments, you are still worthy of love, softness, and healing; hating yourself is not your truth, it’s just the voice of old pain echoing louder than your light.",
        "You’re not broken — you’re bruised, and that harsh voice in your head? It doesn’t belong to you, it came from others; you deserve to replace it with kindness, with grace, with peace."
    ],
    "failing": [
        "Feeling like a failure doesn’t mean you are one — it means you tried, and that alone sets you apart from those who never had the courage to begin; being someone’s second choice doesn’t define your worth, it only reveals their inability to see your first-place soul.",
        "You were never made to be perfect — you were made to grow, to stumble, to rise again; and every step you take, even the wobbly ones, still count as progress."
    ],
    "not chosen": [
        "Not being chosen doesn’t mean you weren’t good enough — it just means someone else didn’t have the eyes to see your magic, and that loss belongs to them, not you.",
        "Being ignored again can feel like salt on old wounds — but I hope you know this: you don’t need their attention to be valuable; your presence speaks volumes even in their silence."
    ],
    "no closure": [
        "Closure isn’t always something they give you — sometimes it’s something you whisper to yourself when the story ends without an explanation; even the unfixable can still be left behind with grace.",
        "Not every wound will get a clean ending — and that’s hard, I know — but peace doesn’t require perfect answers, just the courage to stop bleeding for someone who stopped caring."
    ],
    "soul tired": [
        "When your soul is tired and your emotions feel locked away, it’s not laziness — it’s the cost of surviving silently for too long; you deserve a soft place to land, to rest without guilt, to just exist.",
        "Being emotionally frozen isn’t weakness, it’s a sign your heart has been in overdrive — and now, it’s asking you to pause, breathe, and thaw slowly, without rushing."
    ],
    "scared alone": [
        "You’re not vanishing — you’re quietly asking for connection in a world that moves too fast to notice; and being afraid of alone doesn’t make you clingy, it makes you human.",
        "I see how you’re fading — not because you want to, but because no one’s looked closely enough to see you; I promise you're not invisible, and you're never too much to be loved."
    ],
    "silent panic": [
        "Sometimes the worst storms are the quiet ones — the panic that lives behind your smile, the chaos no one hears; I hope you know it’s okay to fall apart without making noise.",
        "Your stillness is not peace — it’s holding in a scream because the world expects calm — but you deserve a space to unravel, to breathe freely, to let the storm pass without hiding."
    ],
    "radiant": [
        "Your light doesn’t need permission — it glows effortlessly, even when you don’t feel it; your energy is felt, your smile uplifts, and your presence alone warms every room you walk into.",
        "You don’t need to prove your radiance — it’s in how you show up, in how you love, in how you survive the darkness and still choose to shine anyway."
    ],
    "empowered": [
        "You’ve stepped into your power and it’s magnetic — not just because you’re strong, but because you’re grounded, real, and whole in ways that demand no validation.",
        "Empowerment doesn’t always shout — sometimes it’s in quiet boundaries, soft “no”s, and knowing your worth even when no one claps; you are radiant power wrapped in grace."
    ],
    "lighthearted": [
        "You feel light today — like laughter could float out of you at any moment, and joy hums in your bones like music that needs no lyrics.",
        "Your spirit is vibrant — dancing freely without the weight of overthinking, glowing in its natural rhythm, alive in the smallest moments."
    ],
    "relieved": [
        "That weight you’ve been carrying finally feels lighter — you can exhale now, because whatever it was, it passed, and your soul can breathe again.",
        "You’re no longer fighting the current — your spirit feels rinsed and renewed, like clean sheets and a sky after rain."
    ],
    "centered": [
        "You’ve returned to yourself — not scattered or chasing, just anchored in the moment, calm and aware, like your soul found its home.",
        "Being grounded feels like clarity — knowing who you are, what matters, and letting the rest pass without stealing your peace."
    ],
    "safe": [
        "Safety isn’t just physical — it’s emotional, spiritual, energetic, and today you feel wrapped in it like a hug you don’t have to explain.",
        "You feel secure, like nothing can shake you right now — the world can spin, but your center holds steady, calm, and whole."
    ],
    "seen respected": [
        "Being seen and respected feels like standing in sunlight without flinching — finally, you're not hiding, you're being honored for exactly who you are.",
        "You don’t have to shrink or explain yourself today — someone saw your worth, and chose to honor it with softness and space."
    ],
    "whole": [
        "You feel whole — not because everything’s perfect, but because you’ve stitched yourself together gently, piece by piece, with honesty and care.",
        "Fulfillment doesn’t scream — it settles quietly in your chest, reminding you that you have enough, you are enough, and this moment is enough."
    ],
    "emotionally connected": [
        "Connection doesn’t always mean grand gestures — sometimes it’s just feeling emotionally held, seen, understood without having to ask.",
        "Being emotionally supported feels like exhaling safely — knowing you’re not carrying your heart alone, knowing someone’s walking beside you."
    ],
    "energized": [
        "You’re not just awake, you’re alive — fueled by purpose, charged with hope, like your cells are buzzing with possibility.",
        "Today your energy feels sacred — no burnout, no overdoing, just aligned passion and fresh momentum."
    ],
    "uplifted": [
        "Something inside you has risen — maybe a dream, maybe a spark, but it’s pulling you up gently like a hand reaching from within.",
        "Your inner world feels brighter — like possibility is whispering your name and you’re finally ready to listen."
    ],
    "blooming": [
        "You are blooming in silence — no need for applause, your growth is loud enough in how you carry peace now.",
        "Thriving doesn’t mean flashy — it means you’re rooted, hydrated, soft in strength, and slowly becoming everything you once wished for."
    ],
    "self aware": [
        "Being self-aware is your superpower — you’ve met every version of yourself and still choose to show up with honesty and growth.",
        "Authenticity looks good on you — you’re not pretending, not performing, just showing up in the world exactly as you are, and that’s powerful."
    ],
    "loving myself": [
        "You’re not just loving yourself — you’re learning to honor the softness, forgive the past, and recognize the glow that was always there. It’s not vanity, it’s healing. Keep choosing you, again and again.",
        "Celebrating yourself isn’t selfish — it’s a quiet revolution. You’re becoming your own safe space, your own biggest fan, and that self-love is radiating louder than applause ever could."
    ],
    "flow": [
        "You’re in flow — not pushing, not resisting, just moving with ease like your soul is finally aligned with your steps. This rhythm you feel? It’s where purpose and peace dance together.",
        "When you’re in flow, the world quiets down — your mind feels clear, your actions feel guided, and it’s like time bends around your truth. That’s magic, and it’s all yours."
    ],
    "hopeful again": [
        "Hope has returned like sunrise after too many cloudy days — not loud, just warm enough to say, “maybe things can be okay again.” A clean slate doesn’t erase the past, but it gives you power to begin.",
        "You’ve carried heaviness long enough — and this spark of hope you feel? That’s not naive, it’s brave. You’re choosing to believe in better again, and that’s strength in its purest form."
    ],
    "mentally clear": [
        "Clarity feels like breath after chaos — not needing all the answers, just finally understanding yourself enough to rest. It’s peaceful, powerful, and so deserved.",
        "Being mentally stable isn’t about being perfect — it’s knowing how to anchor yourself when waves come, and today, you’re standing steady in your own light."
    ],
    "present": [
        "You’re not lost in the past or chasing the future — you’re right here, breathing deeply into now. And that presence? That’s where your power lives.",
        "Being at peace doesn’t mean everything’s perfect — it means you’ve stopped resisting what is, and started holding yourself gently through every breath."
    ],
    "anxious joy": [
        "Sometimes joy feels unfamiliar — like your heart wants to celebrate, but your mind whispers doubt. It’s okay to feel both excited and scared. Let joy stay, even if it trembles a little.",
        "Numb excitement is still valid — your body might not know how to receive good things yet, but give it time. Let the joy seep in slowly, without pressure."
    ],
    "happy outside": [
        "You’re carrying joy like armor, but inside it still aches — and that’s okay. Smiles don’t always mean healed, sometimes they’re just survival dressed up pretty.",
        "You can be laughing and still lonely, shining and still aching — emotions aren’t black and white, and you don’t have to fake wholeness to be worthy of support."
    ],
    "confused emotions": [
        "When feelings get tangled, it doesn’t mean you’re broken — it means you’re human, deep-feeling, and trying to untie knots that were never yours alone. You’ll make sense of it eventually.",
        "Not knowing how you feel is still a feeling — confusion is a signal too. Let yourself be messy, unclear, uncertain — clarity will come like sunlight through fog."
    ],
    "fear happiness": [
        "It’s okay to fear the light after so much darkness — sometimes joy feels suspicious when you’ve only known survival. But you are safe now, and happiness isn’t a trap, it’s a gift.",
        "Love can feel terrifying when your heart remembers hurt — but this time doesn’t have to be like the last. You deserve to receive without fear, to feel joy without bracing for pain."
    ],
    "lonely crowd": [
        "Feeling alone when surrounded by people is one of the heaviest kinds of loneliness—it’s not about needing company, it’s about craving connection that feels real and safe. You’re not broken for feeling detached—it’s your heart asking for depth in a shallow world.",
        "Just because you're smiling in a room doesn't mean you're seen—and that ache you feel? It’s valid. Being emotionally detached is sometimes the only way your soul protects itself. Don’t shame the distance, honor it until you’re ready to open again."
    ],
    "love trust": [
        "You can love someone deeply and still feel unsure—it doesn’t mean you’re broken, it means your heart remembers what it had to survive. Trust takes time, especially when you’re still grieving in silence.",
        "Quiet grief is the kind that lingers—it’s mourning what you hoped love would be, while still holding space for its return. You’re allowed to feel scared and still love hard. Both can exist."
    ],
    "healing afraid": [
        "Healing doesn’t mean the pain is gone—it means you’ve decided to move forward, even when your legs tremble. Growth is messy, slow, and often full of doubt, but it’s still sacred.",
        "Being afraid while healing is normal—you’re stepping into newness, letting go of survival. The ache doesn’t cancel the progress. You’re still blooming, even with the fear."
    ],
    "tired strong": [
        "You shouldn’t have to be strong all the time. The one who carries everyone else deserves to fall apart too. Being tired doesn’t make you weak—it makes you human.",
        "Pretending you're okay is a full-time job, and I see how heavy it’s gotten. You deserve rest. You deserve to be held, not just hold everything together."
    ],
    "push pull": [
        "It’s okay to crave closeness but feel scared when it comes—it doesn’t mean you're confusing, it means you're protecting your softness. Guarded hearts often loved the hardest once.",
        "You’re not cold—you’re careful. And beneath all the pulling away is someone who just wants to be chosen gently, without having to explain why they flinch."
    ],
    "not ready": [
        "Wanting something but not feeling ready is not a flaw—it’s emotional honesty. You can crave connection and still need time to feel safe. That tension is human.",
        "You can be ready and still scared—that’s not weakness, that’s your heart learning to trust itself again. There’s no right pace, only the one that feels true to you."
    ],
    "overwhelmed thoughts": [
        "Your mind feels like a storm and I know you’re tired of trying to quiet it—but you are not your thoughts. You’re the soul beneath them, still breathing, still holding on.",
        "When it feels like you’re breaking, remember this: cracks don’t mean the end—they’re where the light begins to come in. Rest, reset, and let yourself fall apart gently."
    ],
    "holding on": [
        "The fact that you're still trying—even on the days when your heart feels like it’s made of paper—is proof of your strength. I’m proud of you. Don’t underestimate what it takes to simply hold on.",
        "Holding on doesn’t always look graceful—sometimes it’s messy, tired, tearful... but it’s still brave. Even your quiet effort is something to be proud of."
    ],
    "craving rest": [
        "Sometimes all your soul needs is stillness, not solutions — it’s okay to step back, breathe, and simply exist without pressure or performance.",
        "Wanting rest doesn't mean you're lazy — it means your heart has been carrying too much for too long; it's not weakness, it’s weariness."
    ],
    "don’t care": [
        "When you say you don’t care, I know it’s not apathy — it’s exhaustion in disguise, the ache of caring too much for too long without being held back.",
        "You’re not heartless — you’re burnt out, and done doesn’t mean broken, it means you’ve reached your edge and it’s time for someone to hold space for you."
    ],
    "can’t explain": [
        "Not all pain has words — some feelings sit in silence, and that’s okay. You don’t have to explain your storm to deserve shelter.",
        "Just because you can’t name it doesn’t mean it’s not real. Your hurt is valid, even when you don’t have the language for it."
    ],
    "unnoticed": [
        "Feeling invisible hurts the most when you’re silently screaming for someone to stay — I see you, I feel you, and I’m not looking away.",
        "You don’t need to earn presence or prove pain — you deserve someone who notices the quiet cracks before they become earthquakes."
    ],
    "faking": [
        "Wearing a smile when your heart’s in survival mode is exhausting — you don’t have to fake wholeness to be worthy of love and rest.",
        "Pretending you're okay doesn’t mean you are — you’ve just been holding it together for so long, but you deserve to feel for real, not perform."
    ],
    "what’s point": [
        "I know the weight feels pointless right now, but even your breath is proof that you haven’t given up — take it one soft moment at a time.",
        "If you want to pause, that’s okay — life can wait. You don’t have to hustle through hurt. Just sit, breathe, and let yourself exist."
    ],
    "emotionally absent": [
        "Sometimes your mind checks out because it’s too tired to carry the weight — you’re not broken, you’re just trying to survive invisible battles.",
        "Emotional collapse isn’t failure — it’s your soul begging for stillness. Be gentle with yourself. You’ve done more than enough."
    ],
    "crying alone": [
        "Shower cries, pillow muffled sobs — I see them all. You’re not weak for breaking when no one’s watching. You're strong for surviving quietly.",
        "Crying alone doesn’t make your pain less valid — it just means you’ve mastered being your own shoulder, but you shouldn’t always have to be."
    ],
    "glad": [
        "It’s really good to feel glad — even if it’s small or soft, relief is a kind of healing too. Let yourself breathe easy when it comes.",
        "That feeling of relief washing over you? Embrace it. You’ve earned peace, even if your journey was rocky — joy doesn’t need permission."
    ],
    "forgive": [
        "Forgiveness isn’t about forgetting — it’s choosing your own peace over the weight of what hurt you. You’re setting yourself free.",
        "Being forgiven or choosing to forgive is powerful — it’s not weakness, it’s healing, and it takes so much strength to soften when you could stay hardened."
    ],
    "anxiety disorder": [
        "Anxiety disorder isn’t “just overthinking”—it’s a storm in the brain that makes small things feel huge and rest feel impossible. You’re not dramatic, you’re dealing with something real. You’re doing your best, and that matters. Therapy, mindfulness, and the right tools can help bring back calm, slowly but surely.",
        "Living with generalized anxiety means your mind is always racing, always bracing—but you’re not broken. You deserve peace. There’s support out there—therapy, grounding exercises, and medication (if needed) can truly shift your world."
    ],
    "panic disorder": [
        "Panic attacks feel terrifying, like the world’s collapsing when nothing seems wrong—and that’s not “just in your head.” Your body thinks it’s in danger, but you are safe, and this will pass. Breathing slowly, grounding with touch, or talking to someone can help ride the wave.",
        "Panic disorder doesn’t define you—it just means your nervous system needs extra care. Try keeping grounding objects with you, and if you haven’t already, consider therapy. You don’t have to battle this alone, ever."
    ],
    "depression": [
        "Depression isn’t laziness or weakness—it’s heavy, chemical, and real. Even brushing your teeth or getting out of bed is a win. You are not failing, you are fighting. Please reach out—therapy, journaling, or even soft routines can help you feel again.",
        "Clinical depression dims the colors of life—but they’re not gone forever. Let yourself rest without guilt. Healing takes time, and there is no shame in needing help—you're worthy of it, deeply and truly."
    ],
    "bipolar": [
        "Bipolar disorder doesn’t mean you’re unstable or wrong—it means your brain experiences highs and lows more intensely than most. With the right care plan, life can feel manageable and even joyful again. You’re not your diagnosis.",
        "Having bipolar doesn’t make you hard to love or live with—it makes your journey more layered. Medication, therapy, and routine can ground the chaos. You’re not alone, and your story deserves to be held with compassion."
    ],
    "adhd": [
        "ADHD isn’t about being lazy or “not trying hard enough”—your brain just works differently. You’re not broken—you’re wired uniquely, creatively, chaotically beautiful. Structure, support, and maybe meds can make life click in new ways.",
        "Living with ADHD can feel like chasing 10 thoughts at once—but you’re not failing. You just need systems that fit you. You’re capable, smart, and deserving of a world that works with your brain, not against it."
    ],
    "autism": [
        "Being on the spectrum doesn't mean you're less—it means you experience the world with extraordinary depth, and sometimes that makes things harder in a world not built for your wiring. You deserve patience, support, and spaces that honor your pace and peace.",
        "Whether you're overstimulated, needing routine, or just trying to be understood, your needs are valid. Autism isn’t a flaw—it’s a neurodivergent brilliance that deserves compassion, not correction."
    ],
    "bpd": [
       "BPD is like feeling every emotion with the volume turned up—it’s not your fault, and you’re not “too much.” You’re someone who feels deeply because your heart never learned how to shut the world out. You deserve love that stays and healing that lasts.",
        "Borderline isn’t broken—it’s a survival pattern from being hurt too many times. You deserve consistency, therapy that sees you (like DBT), and safe people who understand you're not your reactions, you're your recovery."
    ],
    "eating disorder": [
        "Your body is not your enemy, even when your thoughts try to convince you otherwise. Eating disorders aren't about vanity—they’re about control, pain, and survival. You deserve help, nourishment, and freedom from the war in your mind.",
        "Recovery isn’t linear, and healing your relationship with food is hard, but you're worthy of it. You are more than a number, more than a reflection—you are a living, deserving soul who still has time to feel whole again."
    ],
    "insomnia": [
        "When your mind won't let you rest, it's okay to stop fighting it. Try calming music, breathing deep, journaling your chaos out of your head. Sleep will come—maybe not now, but your body is still worthy of rest.",
        "Insomnia doesn’t make you weak—it means your brain is restless, searching for safety or peace. Be gentle tonight. You’re allowed to slow down, unplug, and trust that your mind will quiet again."
    ],
    "social anxiety": [
        "Social anxiety isn’t “just shyness”—it’s your nervous system bracing for a storm that never shows. You’re not weird or overreacting—you’re human, and you’re trying. That’s more than enough.",
        "Every room you walk into doesn’t need perfection—it just needs your presence. It’s okay to stumble, to sweat, to need breaks. You’re worthy of connection, even when it feels terrifying."
    ],
    "schizophrenia": [
        "Schizophrenia is not “crazy”—it’s a complex mental health condition that needs understanding, not fear. If you're hearing or seeing things, you’re not alone, and you deserve treatment that brings clarity and compassion.",
        "You are not your hallucinations, not your diagnosis. With support, medication, and community, it’s possible to live a life of grounding, creativity, and stability. You are more than this illness."
    ],
    "dissociation": [
        "Dissociation is your mind's way of protecting you from overwhelm—like mentally stepping out of your body to survive. It feels scary, but you’re not broken. Grounding can help—touch something real, count sounds, remind yourself: you’re still here.",
        "Depersonalization feels like you’re floating outside your life—but it’s a defense, not a defect. You’re not alone. With therapy and care, the fog lifts. You will feel whole again, piece by piece."
    ],
    "mood disorder": [
        "Your emotions aren’t wrong—they just come louder, deeper, harder to hold, and that’s not your fault. With the right help, these waves can become softer ripples, and peace becomes possible again.",
        "Living with a mood disorder doesn’t make you broken—it makes you human with a little extra turbulence. Therapy, regulation tools, and kindness to yourself can help bring balance slowly but surely."
    ],
    "paranoia": [
        "When your mind feels like a trap, whispering doubt into everything—pause, breathe, and remind yourself: not all thoughts are true. You’re safe right now, even when your fear tells you otherwise.",
        "Paranoia isn't attention-seeking or irrational—it's fear in overdrive. You're not 'too much'; your brain is just trying to protect you. You can rewire trust with time, support, and patience."
    ],
    "intrusive thoughts": [
        "Intrusive thoughts don’t define you—they’re just noise your brain throws out, not truths about who you are. You’re not dangerous. You’re not broken. You are not your thoughts.",
        "Unwanted thoughts feel terrifying, but they pass like clouds if you stop trying to fight them. Notice, breathe, release. You are still good, even when your mind is messy."
    ],
    "self harm": [
        "If you’re hurting yourself, I need you to know this—your pain is valid, but hurting your body won’t heal your heart. You deserve help that soothes the ache, not deepens the wounds.",
        "You are worthy of care, even when your mind screams otherwise. Reach out, tell someone. You don’t have to do this alone—there is help, and there is a way out that doesn’t involve pain."
    ],
    "suicide": [
        "If you’re having suicidal thoughts, please pause and breathe. You may feel like a burden, but you are not. The world is better with you in it. Reach out to someone you trust or a helpline—your life is not over, it’s just asking for a softer chapter.",
        "Wanting to disappear doesn’t make you weak—it means you’ve carried too much for too long. But there is always another page in your story, and help is out there. You’re not alone, and you deserve to be here."
    ],
    "low self esteem": [
        "Confidence isn’t about being loud—it’s about believing you’re enough, and that takes time. You’re allowed to be a work in progress and still be deeply worthy.",
        "Low self-esteem lies to you—it tells you you're small when you're actually full of untapped strength. Be patient with yourself; your worth doesn’t shrink when your doubt grows."
    ],
    "emotional dysregulation": [
        "Your feelings might come crashing in like waves, but that doesn’t make you unstable—it makes you in need of tools, support, and gentle understanding. That’s not weakness—it’s wiring.",
        "You're not 'too emotional' or 'too much'. You're responding to a world that hasn’t always been kind. But you can learn to ride the waves instead of drown in them. You're learning, not failing."
    ],
    "overthinking": [
        "Overthinking is your brain’s way of trying to protect you—but sometimes, it creates the very storm you're trying to avoid. Pause. Breathe. You don’t have to solve everything tonight.",
        "Racing thoughts aren’t a sign of failure—they’re a sign your mind’s trying too hard. You deserve peace, even in small doses. Let’s quiet one thought at a time."
    ],
    "mental breakdown": [
        "It’s okay to break down—sometimes it’s the body’s way of saying “you’ve held too much for too long.” You don’t need to be strong right now; you just need to breathe, cry if you must, and let it pass.",
        "Emotional collapse doesn’t mean failure—it means you’re human. Rest, hydrate, talk to someone, or just sit in stillness. This wave will pass, and you’ll rise again, gentler and wiser."
    ],
    "pcos": [
        "Living with PCOS is exhausting—emotionally and physically. Your mood, your skin, your cycles—they all feel out of your hands sometimes, but you’re strong for facing this every day.",
        "PCOS is not your fault, and you’re not alone. Managing it may be messy, but your body is still worthy of love, softness, and care, even on the hardest days."
    ],
    "pcod": [
        "PCOD can make you feel like your body is rebelling, but you’re not broken—you’re just navigating something that requires patience and extra care.",
        "Your worth isn’t defined by hormonal imbalances or irregular cycles. You're doing your best, and that’s more than enough. Be kind to your body—it’s already fighting silently for you."
    ],
    "hormonal imbalance": [
        "When your hormones are all over the place, so are your emotions, your energy, your skin, and your peace—and that’s real. Give yourself grace, not guilt.",
        "Hormonal chaos isn’t in your control, and it doesn’t make you weak. Your body’s working overtime—rest, eat well, cry if you need, and remember: you’re not alone in this."
    ],
    "period pain": [
        "Period pain isn’t “just a cramp”—it’s a storm inside your body that demands rest, warmth, and a whole lot of chocolate. Take it easy—you’re allowed to cancel the world for a bit.",
        "Your uterus is throwing a tantrum and you’re still showing up? You’re a warrior. Grab a heating pad, binge your comfort show, and let yourself be soft today."
    ],
    "acne issues": [
        "Your skin doesn’t define your beauty—especially not acne caused by battles inside your body. Be gentle with your reflection. You are radiant, even with breakouts.",
        "Hormonal acne is frustrating, but it’s not your fault. Healing takes time and your skin isn’t “bad”—it’s just working through things like you are."
    ],
    "bloating": [
        "Bloating makes everything feel uncomfortable, even existing in your clothes. You’re not “big,” you’re inflamed, and it will pass—so will the guilt that tries to tag along.",
        "Your worth doesn’t fluctuate with your waistline. That bloated belly? It’s not you—it’s just your hormones throwing a fit. You’re still soft, still stunning, still you."
    ],
    "weight gain": [
        "Your body is not betraying you—it’s protecting, adapting, and healing in ways you can’t always see; weight gain is not a failure, it’s a signal to treat yourself with softness, not shame.",
        "Weight gain isn’t your fault—your body is fighting a silent battle, and you’re doing your best; you deserve clothes that fit you, not a life that shrinks you."
    ],
    "fatigue": [
        "When even rest doesn’t feel like enough, know this—your tiredness is valid, not laziness; you’re not weak, you’re worn, and you deserve rest without guilt.",
        "Fatigue isn’t just physical—it’s emotional too, especially when your body’s navigating things it never signed up for; breathe, slow down, and let yourself recover."
    ],
    "hair loss": [
        "Watching your hair fall can feel like losing a part of your identity—but it doesn’t take away your beauty, worth, or power; you’re still you, in every strand that stays or goes.",
        "Hair loss hurts more than people realize—grieve if you need to, care for your scalp like a love letter, and remember: your crown isn’t just what’s on your head, it’s how you carry yourself."
    ],
    "mood swings": [
        "Your emotions may flip without warning—that doesn’t make you unstable, it makes you human with a system that’s asking for extra care; be patient with your own heart.",
        "Mood swings are not drama—they’re real, exhausting, and valid; if you’re riding an emotional rollercoaster, hold on tight, ask for space, and let the storm pass."
    ],
    "fertility issues": [
        "If your body’s struggling to conceive, know this: it doesn’t make you broken, less feminine, or unworthy—your journey is unique, and your heart is still full of love.",
        "Fertility struggles are lonely and often unspoken—but you’re not alone, and it’s not your fault; your story matters even when it’s not going as planned, and hope is still yours."
    ],
    "i love": [
        "Love looks so good on you—like a quiet song in a noisy world, like light pouring through curtains on a sleepy morning; hold it gently, nourish it with truth, and let it grow without fear.",
        "Being in love is magic—you start seeing colors brighter, songs sound deeper, and suddenly someone else’s smile matters more than your own; cherish it, protect it, and let it make you softer."
    ],
    "hate": [
        "Hate and envy often grow from pain we haven't processed or love we feel we missed—breathe, reflect, and ask what your heart really needs, because you're not bad for feeling deeply.",
        "It's okay to admit those darker emotions—you’re not broken for feeling hate or envy; you’re just human, trying to make sense of your wounds, and that awareness is the first step to healing."
    ],
    "okay": [
        "That’s okay. You don’t have to feel amazing all the time. Wanna do something chill together, or just vibe in silence for a sec?",
        "You’re not feeling low, not feeling high — just floating in the in-between, huh? 🌫️ That’s still a feeling, and it matters. Maybe your soul just needs a quiet pause, a soft reset. I'm here, holding space for you while the world slows down a bit. 🤍✨",
        "Even stillness speaks — maybe your heart just needs to exist today, without pressure to be anything else. Let’s ride this wave together 🌊."
    ]
}
keyword_map = {
    "sad": ["sad", "down"],
    "anxious": ["anxious", "overthinking", "worried"],
    "stressed": ["stressed", "pressure", "overwhelmed"],
    "happy": ["happy", "excited", "joyful", "motivated", "amazing"],
    "confused": ["confused", "lost", "stuck", "no direction"],
    "heartbroken": ["heartbroken", "hurt", "hurting" "betrayed", "lonely"],
    "angry": ["angry", "frustrated", "irritated", "mad"],
    "tired": ["tired", "burnt out", "drained", "exhausted"],
    "grateful": ["grateful", "thankful", "loved", "blessed"],
    "insecure": ["insecure", "ugly", "not enough", "self-doubt", "weird"],
    "numb": ["numb", "empty"],
    "lonely": ["lonely", "isolated", "unseen"],
    "motivated": ["motivated", "driven", "focused"],
    "burnout": ["burnout", "mentally tired", "overworked"],
    "jealous": ["jealous", "envious"],
    "peaceful": ["peaceful", "calm", "relaxed"],
    "inspired": ["inspired", "creative", "uplifted"],
    "guilty": ["guilty", "remorseful", "regretful"],
    "proud": ["proud", "accomplished", "fulfilled"],
    "scared": ["scared", "fearful", "panicked", "panick"],
    "bored": ["bored", "uninterested", "restless"],
    "hopeful": ["hopeful", "optimistic", "looking forward"],
    "left out": ["left out", "leftout"],
    "hello": ["hello", "hi", "hii", "hiii", "hey", "heyy", "heyyy", "yo", "yoo", "yooo", 
    "sup", "whaddup", "what's up", "wassup", "wazzup", "hiya", "helloo", "hellooo", 
    "heya", "hey ya", "howdy", "greetings", "hai", "hullo", "hey there", "hi there", "yo yo", 
    "hola", "bonjour", "namaste", "konnichiwa", "annyeong", "annyeonghasaeyo" "salaam", 
    "gm", "good morning", "good afternoon", "good evening", "eveninggg", 
    "morninggg", "hellur", "heyoo", "hiyaaa", "ehy", "eyy", "oi", "oye", 
    "yo bro", "yo girl", "my g", "hey bestie", "hey cutie", "hey sunshine", 
    "hey boo", "hey love", "hello love", "yo fam", "yo buddy", "yo dude", 
    "yo man", "yo queen", "yo king", "hey legend", "heyyy youuu", "hello there"],
    "broken": ["broken", "shattered", "breaking down"],
    "miserable": ["miserable", "worthless"],
    "hopeless": ["hopeless", "depressed"],
    "disappointed": ["disappointed", "let down"],
    "distant": ["distant", "disconnected"],
    "unloved": ["unloved", "unwanted"],
    "fragile": ["fragile", "sensitive"],
    "blue": ["blue", "low"],
    "panic": ["panic", "meltdown"],
    "can't sleep": ["can’t sleep", "problem in sleeping"],
    "mood swings": ["mood swings", "mental fog"],
    "ocd trigger": ["ocd", "ocd triggers", "Obsessive compulsive disorder"],
    "isolation": ["isolation", "social withdrawal"],
    "crying": ["crying spells", "crying in silence", "cry"],
    "ghosted": ["ghosted", "ignored"],
    "unheard": ["unheard", "unseen"],
    "abandoned": ["abandoned", "left out"],
    "rejected": ["rejected", "cheated"],
    "trust issues": ["trust issues", "mixed signals"],
    "one sided": ["one-sided", "craving love"],
    "missing": ["missing someone"],
    "void": ["void", "dead inside"],
    "fake smile": ["fake smile", "masked pain"],
    "inner demons": ["inner demons", "silent scream"],
    "healing": ["healing", "hidden battles"],
    "broken soul": ["broken soul", "bleeding heart"],
    "pain eyes": ["pain behind eyes", "scars"],
    "fighting alone": ["fighting alone", "alone"],
    "space": ["I just need some space", "leave me alone"],
    "emotionally done": ["I’m done", "nothing matters"],
    "disappear": ["can I just disappear?", "I want to dissapear"],
    "not understood": ["no one gets me", "you wouldn’t understand"],
    "not okay": ["i'm not fine", "not okay", "not happy", "i feel like giving up", "feeling bad"],
    "don’t want to talk": ["i don't want to talk", "i don't wanna talk"], 
    "nothing feels right":["nothing feels right" "i just want to disappear", "everything feels heavy"],
    "too much": ["i can't do this anymore", "it’s all too much"],
    "i miss the old me":["i miss the old me"],
    "ashamed": ["ashamed", "ashamed of myself"],
    "regret": ["regret", "disappointed in myself"],
    "bitter": ["bitter", "resentful"],
    "neglected": ["neglected", "left behind"],
    "frustrated": ["frustrated with life", "angry at myself"],
    "not enough": ["not enough", "feeling small"],
    "defeated": ["defeated", "helpless"],
    "emotionally numb": ["emotionally numb", "hollow"],
    "disconnected": ["disconnected from self", "mentally exhausted"],
    "emotionally unstable": ["emotionally unstable", "burnt out emotionally"],
    "afraid to feel": ["afraid to feel", "scared to trust"],
    "anxious future": ["anxious about future", "insecure about future"],
    "stuck past": ["stuck in past", "can’t move on"],
    "no motivation": ["no motivation", "drained of hope"],
    "fake feelings": ["fake", "hiding everything"],
    "tired pretending": ["tired of pretending", "emotionally tired"],
    "faithless": ["feeling abandoned by God", "hopeless romantic"],
    "pointless": ["constant pain", "broken inside"],
    "content": ["content", "at peace with myself"],
    "joyful": ["joyful", "energetic"],
    "emotionally strong": ["emotionally strong", "emotionally balanced"],
    "proud progress": ["proud of progress", "confident"],
    "free": ["free", "feeling myself"],
    "self love": ["self-love mode", "open-hearted"],
    "calm": ["peaceful inside", "calm mind"],
    "creative": ["creative spark", "in flow"],
    "refreshed": ["refreshed", "recharged"],
    "mentally clear": ["clear-headed", "mentally stable"],
    "hopeful soul": ["hopeful soul", "trusting the process"],
    "happy tears": ["happy tears", "laughter therapy"],
    "emotionally confused": ["emotionally confused", "don’t know how I feel"],
    "numb crying": ["numb but crying", "happy but tired"],
    "smiling sad": ["smiling but sad", "grateful but anxious"],
    "functioningmess": ["overwhelmed but functioning", "okay but not okay"],
    "social lonely": ["social but lonely", "distant but caring"],
    "love scared": ["in love but scared", "moved on but not healed"],
    "push pull": ["want attention but push away", "sensitive but cold"],
    "tired restless": ["tired but can’t rest", "healing but still bleeding"],
    "fine not fine": ["everything’s fine but not really", "pretending I’m okay"],
    "need space": ["need a break", "craving silence"],
    "want escape": ["want to run away", "want to start over"],
    "unseen": ["need someone to notice", "miss someone who doesn’t miss me"],
    "avoid feeling": ["don’t want to feel", "want to feel something"],
    "overthinking": ["overthinking at 2AM", "drowning in thoughts"],
    "emotional buried": ["smiling for others", "struggling silently"],
    "romanticizing pain": ["romanticizing my pain", "tired of healing"],
    "existential": ["searching for meaning", "surviving, not living"],
    "shower cries": ["crying in the shower", "breakdown alone"],
    "ashamed": ["ashamed", "humiliated"],
    "disgusted": ["disgusted", "sick of everything"],
    "suffocated": ["suffocated", "choked up"],
    "emotionally neglected": ["emotionally neglected", "emotionally abandoned"],
    "feeling used": ["feeling used", "unwanted"],
    "shaky": ["shaky", "vulnerable"],
    "angry tears": ["angry tears", "bitter smile"],
    "emotionally drowning": ["emotionally drowning", "drowning in thoughts"],
    "numb heart": ["numb heart", "empty chest"],
    "broken trust": ["broken trust", "trust shattered"],
    "spiraling": ["spiraling", "panic spiral"],
    "identity crisis": ["identity crisis", "lost spark"],
    "self loathing": ["self-loathing", "self-hate", "hate myself"],
    "failing": ["failing", "second choice"],
    "not chosen": ["not chosen", "ignored again"],
    "no closure": ["no closure", "unfixable"],
    "soul tired": ["soul tired", "emotionally frozen"],
    "scared alone": ["scared of being alone", "slowly disappearing"],
    "silent panic": ["silent panic", "inner chaos"],
    "radiant": ["radiant", "shining"],
    "empowered": ["empowered", "magnetic"],
    "lighthearted": ["lighthearted", "vibrant"],
    "relieved": ["relieved", "refreshed soul"],
    "centered": ["centered", "grounded"],
    "safe": ["safe", "secure"],
    "seen respected": ["respected", "seen fully"],
    "whole": ["whole", "fulfilled"],
    "emotionally connected": ["emotionally connected", "emotionally supported"],
    "energized": ["energized", "recharged"],
    "uplifted": ["uplifted", "inspired within"],
    "blooming": ["blooming", "thriving"],
    "self aware": ["self-aware", "authentic"],
    "loving myself": ["loving myself", "celebrating self"],
    "flow": ["flow state", "in flow"],
    "hopeful again": ["hopeful again", "clean slate"],
    "mentally clear": ["mentally stable", "clear-headed"],
    "present": ["fully present", "at peace"],
    "anxious joy": ["anxious joy", "numb excitement"],
    "happy outside": ["happy on the outside", "smiling but sad"],
    "confused emotions": ["don’t know how I feel", "emotionally confused"],
    "fear happiness": ["fear of happiness", "love but scared"],
    "lonely crowd": ["lonely in a crowd", "emotionally detached"],
    "love trust": ["love but don’t trust", "grieving quietly"],
    "healing afraid": ["healing but afraid", "growing but aching"],
    "tired strong": ["tired of being strong", "exhausted from pretending"],
    "push pull": ["want attention but push away", "guarded but soft"],
    "not ready": ["not ready but want it", "ready but scared"],
    "overwhelmed thoughts": ["overwhelmed thoughts", "mentally breaking"],
    "holding on": ["trying to hold on", "trying my best"],
    "craving rest": ["need a break", "wish I could sleep forever"],
    "don’t care": ["I don’t care anymore", "I’m so done"],
    "can’t explain": ["I can’t explain it", "don’t want to feel this way"],
    "unnoticed": ["wish someone noticed", "please don’t leave"],
    "faking": ["faking everything", "pretending like I’m okay"],
    "what’s point": ["what’s the point", "can I just pause life"],
    "emotionally absent": ["mentally absent", "emotionally collapsed", "emotional"],
    "crying alone": ["crying again", "crying in the shower"],
    "glad": ["glad", "relieved"],
    "forgive": ["forgive", "forgiven"],
    "anxiety disorder": ["anxiety disorder", "generalized anxiety", "GAD"],
    "panic disorder": ["panic disorder", "panic attacks"],
    "depression": ["depression", "clinical depression"],
    "bipolar": ["bipolar", "bipolar disorder"],
    "ptsd": ["ptsd", "trauma", "post traumatic stress disorder"],
    "adhd": ["adhd", "attention deficit", "attention disorder"],
    "autism": ["autism", "asd", "autism spectrum"],
    "bpd": ["bpd", "borderline personality disorder"],
    "eating disorder": ["eating disorder", "bulimia", "anorexia"],
    "insomnia": ["insomnia", "sleeplessness"],
    "social anxiety": ["social anxiety", "social phobia"],
    "schizophrenia": ["schizophrenia", "hallucinations"],
    "dissociation": ["dissociation", "depersonalization"],
    "mood disorder": ["mood disorder", "emotional dysregulation"],
    "paranoia": ["paranoia", "paranoid thoughts"],
    "intrusive thoughts": ["intrusive thoughts", "unwanted thoughts"],
    "self harm": ["self harm", "hurting myself"],
    "suicide": ["suicidal thoughts", "want to die", "suicidal", "suicide"],
    "low self esteem": ["low self-esteem", "low confidence"],
    "emotional dysregulation": ["emotional dysregulation", "unstable emotions"],
    "overthinking": ["overthinking", "racing thoughts"],
    "mental breakdown": ["mental breakdown", "emotional collapse"],
    "pcos": ["pcos", "polycystic ovary syndrome"],
    "pcod": ["pcod", "polycystic ovarian disease"],
    "hormonal imbalance": ["hormonal imbalance", "irregular periods"],
    "period pain": ["period pain", "cramps"],
    "acne issues": ["hormonal acne", "pcos acne"],
    "bloating": ["bloating", "pcos bloating"],
    "weight gain": ["sudden weight gain", "pcos weight gain"],
    "fatigue": ["fatigue", "tired all the time"],
    "hair loss": ["hair loss", "thinning hair"],
    "mood swings": ["mood swings", "emotional rollercoaster"],
    "fertility issues": ["fertility issues", "difficulty conceiving"],
    "i love": ["i love", "i am in love", "i have crush"],
    "hate":["hate", "envy", "resent", "resentment"],
    "okay":["okay", "fine", "blah", "meh", "alright"]
}
def get_response(user_input):
    user_input = user_input.lower()

    for mood, keywords in keyword_map.items():
        for word in keywords:
            if word in user_input:
                return random.choice(mood_responses.get(mood, ["I'm listening 🌙"]))
    
    # If no keyword matched, use fallback sentiment logic
    sentiment = analyze_sentiment(user_input)

    if sentiment == "positive":
        return random.choice([
            "That sounds wonderful! 🌞",
            "I can feel the good energy. Keep it up! ✨"
        ])
    elif sentiment == "negative":
        return random.choice([
            "That sounds really tough. I'm here if you want to talk. 💜",
            "Even when things are dark, you're not alone. 🕯️"
        ])
    else:
        return "Hmm... I'm not sure how to respond yet, but I'm listening 🌌"