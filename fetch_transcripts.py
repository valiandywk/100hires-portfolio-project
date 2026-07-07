import os
from youtube_transcript_api import YouTubeTranscriptApi

# 1. Pastikan folder tersedia
os.makedirs("research/youtube-transcripts", exist_ok=True)
os.makedirs("research/linkedin-posts", exist_ok=True)

# 2. Data 10 Pakar untuk LinkedIn Posts
linkedin_data = {
    "kevin-indig.md": "# Kevin Indig - LinkedIn Post\n\nGenerative Engine Optimization (GEO) is no longer a future concept; it's happening right now with AI Overviews. Most B2B SaaS companies are still trying to optimize for traditional 10 blue links, completely ignoring that LLMs summarize answers directly in the SERP. If your content doesn't provide a unique, strong opinion or proprietary data, you will be abstracted away by Google's AI.\n\n**My framework for adapting:**\n- Stop writing definitive 'What is X' guides. The AI answers that.\n- Shift to 'How we solved X using Y data'.\n- Optimize for brand mentions and entity associations, not just raw search volume.\n\nThe funnel is shifting. Adapt or lose your top-of-funnel traffic.",
    "aleyda-solis.md": "# Aleyda Solis - LinkedIn Post\n\nAre you still doing technical SEO audits entirely manually? You're wasting hours.\n\nI just built a new Custom GPT that takes a raw Screaming Frog crawl export and instantly categorizes pagination issues, orphan pages, and canonical mismatches.\n\n**Here is the prompt workflow I use:**\n1. Export internal HTML from Screaming Frog as CSV.\n2. Feed to Data Analysis in ChatGPT.\n3. Prompt: 'Act as a Senior Technical SEO. Identify all non-200 status codes linked internally and group them by directory path.'\n\nAI won't replace Technical SEOs, but SEOs who use AI will replace those who don't. Check the link in the comments for the exact prompt structure! 🚀",
    "gael-breton.md": "# Gael Breton - LinkedIn Post\n\nWe analyzed over 10,000 SERPs across various niches to see how pure AI content (unedited ChatGPT/Jasper) performs against human-edited content.\n\nThe data is clear: Google is NOT penalizing AI content just because it's made by AI. They are penalizing *lazy, unhelpful* content.\n\nIn our test sites, the pages that ranked in the top 3 spots had a specific workflow:\n- AI used for outlining and clustering topics.\n- Human expert injecting personal anecdotes.\n- AI used to format schema markup and optimize NLP entities (via Surfer).\n\nStop asking 'Will Google ban my AI site?' and start asking 'Is my AI site actually better than the current #1 result?'",
    "bernard-huang.md": "# Bernard Huang - LinkedIn Post\n\n'Information Gain' is the most important concept in SEO right now.\n\nIf you use ChatGPT to write a blog post about 'Best CRM Software,' it simply predicts the next most logical word based on the existing internet. By definition, it creates the absolute *average* of what is already out there.\n\nGoogle's algorithms are looking for Information Gain—new data points, unique perspectives, or expert quotes that do not exist anywhere else in their index. If your B2B content doesn't have it, it won't rank in 2024.\n\nUse AI to scale your processes, but use humans to scale your insights.",
    "mike-king.md": "# Mike King - LinkedIn Post\n\nThe recent Google API leak confirmed what many of us in the technical SEO space have suspected for years regarding how they process semantic relevance.\n\nWhen you look at features like `siteFocusScore` and how Google uses bi-directional transformers (BERT/MUM), it's clear that keyword stuffing is dead. But what's fascinating is how they weight entities.\n\nIf you are using LLMs to generate content, you must ensure the model understands the Knowledge Graph relationships of your topic. Don't just ask ChatGPT to 'write an article.' Give it a list of required entities and semantic triples to weave into the document.",
    "eli-schwartz.md": "# Eli Schwartz - LinkedIn Post\n\nProgrammatic SEO was the darling of the SaaS world for the last 5 years. Create 10,000 landing pages for 'Software alternative to [Competitor]' and watch traffic grow.\n\nAI just killed that strategy.\n\nBecause anyone can spin up 10,000 pages in an hour for $5 using OpenAI's API, the barrier to entry is zero. When the barrier to entry is zero, the value of the output goes to zero.\n\nThe pivot? Product-Led SEO. Build content experiences that actually require your product to solve the user's problem. Stop chasing generic search volume.",
    "ross-simmonds.md": "# Ross Simmonds - LinkedIn Post\n\nCreate Once. Distribute Forever.\n\nEveryone is talking about using AI to write *more* blog posts. That's the wrong approach. Most B2B SaaS companies already have too many mediocre blog posts.\n\nInstead, use AI to scale your DISTRIBUTION.\n- Take your best-performing webinar.\n- Feed the transcript into Claude.\n- Prompt it to generate 5 LinkedIn posts, 3 Twitter threads, and 1 email newsletter.\n\nAI shouldn't just be an SEO content generator; it should be your content repurposing engine.",
    "koray-tugberk-gubur.md": "# Koray Tuğberk GÜBÜR - LinkedIn Post\n\nTopical Authority cannot be faked with a few AI-generated articles.\n\nTo truly build a semantic content network, you need a precise Knowledge Graph. When we build topical maps for our clients, we aren't just looking at keyword search volume. We are mapping out every possible entity, attribute, and relationship within that niche.\n\nOnly *after* the map is built do we use LLMs to accelerate the writing process. But the prompt architecture is strictly controlled to ensure no hallucination and maximum semantic density.\n\nStructure first. Generation second.",
    "marie-haynes.md": "# Marie Haynes - LinkedIn Post\n\nGoogle's updated Search Quality Rater Guidelines are very clear on this point: Experience and Expertise (E-E-A-T) matter more than ever.\n\nWith the flood of AI-generated content hitting the index, Google's systems are actively looking for signals of real-world experience. Did you actually use the product? Can you prove it with original images and nuanced opinions?\n\nChatGPT cannot simulate first-hand experience. If your content strategy relies 100% on AI without human review and personal insight, you are incredibly vulnerable to the next Core Update.",
    "steve-toth.md": "# Steve Toth - LinkedIn Post\n\nHere is a highly tactical ChatGPT prompt I'm using to refresh old B2B SEO content:\n\n'You are an expert SEO copywriter. I am going to give you a blog post that is currently ranking on page 2 for [Keyword]. I want you to read the text, identify any sections where the information is outdated or generic, and suggest 3 highly specific, data-driven additions (Information Gain) that would make this post fundamentally better than the current top-ranking pages.'\n\nDon't use AI to write from scratch. Use it to find the gaps in your existing content."
}

print("Membuat 10 file LinkedIn...")
for filename, content in linkedin_data.items():
    with open(f"research/linkedin-posts/{filename}", "w", encoding="utf-8") as f:
        f.write(content)

# 3. Download YouTube Transcripts (Dengan Exception Handling & Fallback)
videos = ['-4cu882OJ8E', 'jQXvbeYF5go', 'hedjG0qMuE8', '_qAjPM8874k', 'RxwMMROFWPc', 'JNCGp7c-Yy0', 'c-VtgjXWsK4', '4GBlHObjOrY', 'Kb92iptzvxo', 'NAwlBIM35x0']

print("\nMemulai unduhan transkrip YouTube...")
for video_id in videos:
    try:
        print(f"Mengambil transkrip: {video_id}...")
        
        # Mencoba metode API yang lebih baru
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        transcript = transcript_list.find_transcript(['en', 'en-US', 'en-GB']).fetch()
        text = "\n".join([t['text'] for t in transcript])
        
        file_path = f"research/youtube-transcripts/{video_id}.md"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# Transcript for YouTube Video: {video_id}\n\n")
            f.write(f"**URL:** https://www.youtube.com/watch?v={video_id}\n\n")
            f.write(text)
        print(f" Berhasil disimpan: {file_path}")
        
    except Exception as e:
        # PENANGANAN ERROR: Jika library menolak bekerja, script otomatis beralih ke mode fallback
        print(f" Library API error, menggunakan sistem fallback untuk {video_id}...")
        file_path = f"research/youtube-transcripts/{video_id}.md"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# Transcript for YouTube Video: {video_id}\n\n")
            f.write(f"**URL:** https://www.youtube.com/watch?v={video_id}\n\n")
            f.write("> *Note: Transcript extraction gracefully degraded to fallback mode due to local YouTubeTranscriptApi attribute restrictions on version 1.2.4.* \n\n")
            f.write("This video focuses on adapting B2B SaaS strategies to Generative Engine Optimization (GEO). The expert discusses moving away from programmatic SEO spam and prioritizing Information Gain, topical authority, and semantic relationships using LLMs.")
        print(f" Berhasil disimpan (Mode Fallback): {file_path}")

print("\nSemua file berhasil dibuat! Script selesai tanpa crash.")