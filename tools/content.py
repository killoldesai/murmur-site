"""All site copy lives here. build.py turns it into pages.

Claims must match what the app does (see the app repo's CLAUDE.md and store/listing.md).
No invented reviews, ratings, user counts or speed numbers.
"""

SITE = {
    "name": "Murmur",
    "domain": "https://murmur.netofficials.com",
    "tagline": "Private speech to text for iPhone, iPad, Mac and Apple Watch",
    # Set this to the App Store link once the app is live; every download button switches over.
    "app_store_url": "",
    "support_url": "https://github.com/killoldesai/murmur/issues",
    "updated": "2026-10-29",
    "updated_human": "October 29, 2026",
}

PRICES = {
    "yearly": "$19.99",
    "lifetime": "$39.99",
    "monthly": "$3.99",
    "trial_days": 3,
}

LANGUAGES = ["English", "Spanish", "French", "German", "Italian", "Portuguese", "Dutch",
             "Russian", "Japanese", "Korean", "Chinese", "Hindi", "Arabic"]

# ---------------------------------------------------------------- features
FEATURES = [
    {
        "slug": "on-device-transcription",
        "name": "On-device transcription",
        "icon": "wave", "color": "",
        "card": "Whisper runs on your iPhone, iPad or Mac. Your audio is turned into text without leaving the device.",
        "title": "On-device Whisper transcription for iPhone and Mac",
        "desc": "Murmur runs OpenAI's Whisper speech model on your own iPhone, iPad or Mac. Accurate transcripts with no uploads, no account and no server.",
        "h1": "Whisper transcription that runs <span class=\"hl\">on your device</span>",
        "lead": "Murmur puts a full Whisper speech model on your iPhone, iPad or Mac. You record or import audio, and the transcript is made right there, on the Neural Engine and GPU you already own.",
        "q": "What is on-device transcription?",
        "a": "On-device transcription means the speech-to-text model runs on your own phone or computer instead of a company's server. Murmur downloads the Whisper model once, then turns your audio into text locally. The recording is never uploaded, so nobody else can read or keep it.",
        "viz": "transcribe",
        "shot": ("iphone-note", "Murmur note screen showing a meeting transcript with speakers and timestamps", "phone"),
        "blocks": [
            ("Whisper Large v3 Turbo", "The recommended model is Whisper Large v3 Turbo in a compressed form, about 632 MB. It is the most accurate choice and still fits comfortably on a phone."),
            ("A lighter Small model", "On older devices, or when space is tight, pick the Small model (about 500 MB). You can switch models later in Settings."),
            ("13 languages and auto-detect", "Transcribe English, Spanish, French, German, Italian, Portuguese, Dutch, Russian, Japanese, Korean, Chinese, Hindi or Arabic, or let Murmur detect the language."),
            ("Timestamps on every line", "Each line of the transcript carries its time in the recording, so you can jump back to exactly where it was said."),
            ("Queues work for you", "Record several notes in a row or import a batch. Murmur transcribes them one after another and picks up where it left off if the app was closed."),
            ("Your words, spelled your way", "Add names and jargon to the custom dictionary and Murmur passes them to Whisper as vocabulary hints."),
        ],
        "steps": [
            ("Download the model once", "On first use, Murmur downloads the speech model over Wi-Fi. This is the only time it needs the internet to transcribe."),
            ("Record or import", "Tap record, or bring in audio and video files from Files, Photos or other apps."),
            ("Read the transcript", "Whisper runs on the device and the note fills with timestamped lines you can play, search and edit."),
        ],
        "faqs": [
            ("Is on-device transcription as accurate as cloud services?", "Murmur uses Whisper Large v3 Turbo, the same family of models many cloud services build on. Accuracy depends most on audio quality: a clear recording with one speaker close to the microphone gives the best results. The custom dictionary helps with names and technical terms."),
            ("Which devices can run Murmur's transcription?", "Murmur runs on iPhone and iPad, and on Macs with Apple silicon. Apple Watch records audio and sends it to your iPhone, which does the transcription."),
            ("How much storage does the speech model need?", "Large v3 Turbo needs about 632 MB and the Small model about 500 MB. You only need one of them."),
            ("Does transcription drain my battery?", "Speech recognition is demanding work, so long files use more power than normal app use. Murmur transcribes one note at a time and you can keep using your device while it works."),
        ],
        "related": ["offline-transcription", "custom-dictionary", "private-by-design"],
    },
    {
        "slug": "offline-transcription",
        "name": "Works offline",
        "icon": "plane", "color": "c1",
        "card": "After a one-time model download, Murmur transcribes in airplane mode, underground or anywhere without signal.",
        "title": "Offline transcription app that works in airplane mode",
        "desc": "Transcribe audio with no internet. Murmur downloads its Whisper model once, then records, transcribes and summarizes offline on iPhone, iPad and Mac.",
        "h1": "Transcribe anywhere, <span class=\"hl\">even in airplane mode</span>",
        "lead": "Murmur needs the internet once, to download its speech model. After that, recording, transcription, search, editing and export all work with no connection at all.",
        "q": "Can I transcribe audio without an internet connection?",
        "a": "Yes. Murmur downloads its Whisper speech model one time over Wi-Fi. From then on, transcription runs entirely on your iPhone, iPad or Mac, so it works in airplane mode, on a plane, underground or in a building with no signal. Nothing is sent anywhere while you work.",
        "viz": "offline",
        "shot": ("iphone-recording", "Murmur recording screen with a live waveform and timer", "phone"),
        "blocks": [
            ("No signal, no problem", "Lecture halls, courtrooms, hospitals, field sites and flights often have poor or no connection. Murmur does not care."),
            ("Nothing to wait on", "There is no upload queue and no server load. A transcript starts as soon as you stop recording."),
            ("No data plan used", "Long recordings are big files. Because nothing is uploaded, transcribing an hour of audio uses zero mobile data."),
            ("Wi-Fi-only download", "The one-time model download waits for Wi-Fi by default, so it never eats into your plan."),
            ("Summaries offline too", "On devices with Apple Intelligence, meeting and lecture summaries are made on the device as well."),
            ("Sync is optional", "iCloud sync is the only feature that uses the network, and it is off until you turn it on."),
        ],
        "steps": [
            ("Install and open Murmur", "Finish the short onboarding and allow the microphone."),
            ("Download the speech model on Wi-Fi", "Choose Large v3 Turbo or Small. This happens once."),
            ("Go offline", "Switch on airplane mode and record. The transcript appears when you stop."),
        ],
        "faqs": [
            ("Do I need internet to use Murmur?", "Only once, to download the speech model. Recording, transcription, search, editing and export all work offline after that."),
            ("Does Murmur work on a plane?", "Yes. Once the model is downloaded you can record and transcribe in airplane mode."),
            ("What still needs a connection?", "Buying or restoring Murmur Pro goes through the App Store, and optional iCloud sync needs a connection to copy notes between your devices. Transcription itself never does."),
        ],
        "related": ["on-device-transcription", "voice-recorder", "private-by-design"],
    },
    {
        "slug": "voice-recorder",
        "name": "Voice recorder with bookmarks",
        "icon": "mic", "color": "c5",
        "card": "One tap to record, bookmarks for the moments that matter, and recordings that survive the app being closed.",
        "title": "Voice recorder with bookmarks and transcription",
        "desc": "Record meetings, lectures and voice notes with one tap. Drop bookmarks while you record and get an on-device transcript when you stop. No account needed.",
        "h1": "Record with one tap. <span class=\"hl\">Mark what matters.</span>",
        "lead": "A big record button, a live waveform and a timer. Tap the bookmark while you record to flag a decision, a quote or a question, then jump straight to it in the transcript.",
        "q": "What is the best way to record and transcribe a meeting on iPhone?",
        "a": "Open Murmur, tap the record button and place your iPhone near the people speaking. Tap the bookmark button at key moments. When you stop, Murmur transcribes the recording on your iPhone with Whisper, so you get a timestamped transcript without uploading the audio anywhere.",
        "viz": "record",
        "shot": ("iphone-recording", "Murmur recording screen with pulsing record button, timer and live waveform", "phone"),
        "blocks": [
            ("Bookmarks while you record", "Flag a moment with one tap. Bookmarks show up on the timeline and in the transcript so you can find them later."),
            ("Pause and resume", "Pause during a break and carry on in the same note."),
            ("Safe if the app closes", "Murmur records in a format that stays readable even if the app is closed mid-recording, and recovers the note at the next launch."),
            ("Recorded for Whisper", "Audio is captured as 16 kHz mono, the format Whisper reads directly, then compacted to M4A after transcription to save space."),
            ("From your wrist or menu bar", "Start a recording from Apple Watch, or from the Mac menu bar and a global keyboard shortcut."),
            ("Haptics you can feel", "A light tap confirms that recording started, so you can trust it without looking."),
        ],
        "steps": [
            ("Tap record", "The waveform moves and the timer runs."),
            ("Bookmark key moments", "Tap the bookmark when something important is said."),
            ("Stop and read", "Murmur transcribes on the device and your bookmarks are waiting in the note."),
        ],
        "faqs": [
            ("Can I record for hours?", "Yes. Murmur is built for long meetings and lectures. Recording length is limited by your device's free storage."),
            ("What happens if my phone locks or the app closes during a recording?", "The audio is written in a crash-safe format. If the app is closed mid-recording, Murmur finds the note at the next launch and keeps what was captured."),
            ("Can I record on Apple Watch?", "Yes. The Murmur watch app records and sends the audio to your iPhone, which transcribes it."),
        ],
        "related": ["on-device-transcription", "transcript-editor", "import-audio-video"],
    },
    {
        "slug": "import-audio-video",
        "name": "Import audio and video",
        "icon": "upload", "color": "c4",
        "card": "Transcribe files you already have: voice memos, podcasts, Zoom recordings and videos from Photos.",
        "title": "Transcribe audio and video files on iPhone and Mac",
        "desc": "Import MP3, M4A, WAV and video files from Files, Photos or other apps and get private on-device transcripts. Batch queue, no upload, no account.",
        "h1": "Transcribe the files <span class=\"hl\">you already have</span>",
        "lead": "Bring in recordings from Files, videos from Photos, or open an audio file from another app with Murmur. Queue a whole batch and let it work through them on the device.",
        "q": "How do I transcribe an audio file on my iPhone?",
        "a": "In Murmur, tap Import and choose the file from Files, or a video from Photos. You can also open an audio or video file from another app and choose Murmur. Murmur converts it to the format Whisper needs, adds it to the queue and transcribes it on your iPhone. Nothing is uploaded.",
        "viz": "import",
        "shot": ("ipad-import", "Murmur on iPad with a drop zone and a queue of imported files", "tablet"),
        "blocks": [
            ("Audio and video", "Common audio formats and videos both work. Murmur pulls the soundtrack out of a video and transcribes it."),
            ("Long files, small memory", "Files are converted in chunks, so a two-hour recording does not overwhelm your device."),
            ("A batch queue", "Add several files and watch each one move from waiting to transcribing to ready."),
            ("Open in Murmur", "Murmur registers for audio and video files, so it appears when you share or open them from other apps."),
            ("Drag and drop on iPad and Mac", "Drop files onto the iPad import screen or anywhere in the Mac window."),
            ("Real-time speed on Mac", "The Mac queue shows how many times faster than real time each file is transcribing."),
        ],
        "steps": [
            ("Tap Import", "Choose Files, or Videos to pick from Photos."),
            ("Pick one file or many", "Each file joins the queue as its own note."),
            ("Get transcripts", "Murmur works through the queue on the device and each note appears in your library when it is ready."),
        ],
        "faqs": [
            ("Which file types can Murmur import?", "Murmur can import the audio and video formats Apple's frameworks read, such as M4A, MP3, WAV, AIFF, CAF, MP4 and MOV."),
            ("Can I transcribe a Voice Memo?", "Yes. In Voice Memos, share the recording and choose Murmur, or save it to Files and import it from there."),
            ("Can I transcribe a Zoom or Teams recording?", "Yes. Save the recording file to your device and import it. Murmur only transcribes the file; it never joins calls."),
        ],
        "related": ["export", "on-device-transcription", "search"],
    },
    {
        "slug": "ai-summaries",
        "name": "Private AI summaries",
        "icon": "sparkles", "color": "c2",
        "card": "Meeting, lecture and bullet-point summaries with action items, made on the device with Apple Intelligence.",
        "title": "Private AI meeting summaries made on your device",
        "desc": "Turn transcripts into meeting notes, lecture summaries and action items with Apple Intelligence, on the device. No cloud AI, no uploads.",
        "h1": "Summaries and action items, <span class=\"hl\">made on your device</span>",
        "lead": "Pick a template and Murmur writes a summary of the transcript with Apple Intelligence running on your device. Action items come out as a checklist you can tick off.",
        "q": "Can I get AI meeting summaries without uploading my recording?",
        "a": "Yes. On devices that support Apple Intelligence, Murmur summarizes the transcript with Apple's on-device model. Choose Meeting, Lecture or Bullet points, and Murmur returns a summary with action items. The transcript stays on the device the whole time.",
        "viz": "summary",
        "shot": ("iphone-summary", "Murmur summary tab with key points and action items", "phone"),
        "blocks": [
            ("Three templates", "Meeting (decisions and next steps), Lecture (key ideas and terms) or Bullet points (a quick skim)."),
            ("Action items you can tick", "Tasks pulled from the conversation become a checklist saved with the note."),
            ("Long recordings handled", "Murmur splits long transcripts into parts, summarizes each and then combines them."),
            ("Copy or export", "Copy the summary in one tap, or include it in a text or Markdown export."),
            ("Talk time on iPad and Mac", "See how much each labelled speaker talked, beside the summary."),
            ("Only where supported", "Summaries need a device with Apple Intelligence. On other devices the Summary tab is hidden, and transcripts work as normal."),
        ],
        "steps": [
            ("Open a transcribed note", "Switch from Transcript to Summary."),
            ("Choose a template", "Meeting, Lecture or Bullet points."),
            ("Read and act", "Tick off action items or copy the summary into your notes."),
        ],
        "faqs": [
            ("Which devices support Murmur summaries?", "Summaries use Apple Intelligence, so they need a device and OS version that support it. Murmur hides the Summary tab on devices without it."),
            ("Is my transcript sent to an AI service?", "No. Summaries are made with Apple's on-device Foundation Models. Murmur does not call any cloud AI service."),
            ("Can I edit a summary?", "You can copy it anywhere and edit it there, and the action items checklist is saved with the note."),
        ],
        "related": ["speaker-labels", "export", "on-device-transcription"],
    },
    {
        "slug": "speaker-labels",
        "name": "Speaker labels",
        "icon": "users", "color": "c1",
        "card": "Label who said what, give each speaker a colour, and see talk time on iPad and Mac.",
        "title": "Transcripts with speaker labels and talk time",
        "desc": "Label speakers in your transcripts so you know who said what. Colour-coded names, talk-time bars on iPad and Mac, and labels in every export.",
        "h1": "Know <span class=\"hl\">who said what</span>",
        "lead": "Give each line a speaker. Names get their own colour, appear in exports and add up to talk-time bars, so a meeting transcript reads like a script.",
        "q": "How do I add speaker names to a transcript?",
        "a": "Open the note in Murmur, tap Edit and choose a speaker for a line. Type a name once and reuse it on other lines. Murmur colours each speaker, shows the names in the transcript and includes them when you export to text or Markdown.",
        "viz": "speakers",
        "shot": ("ipad-note-wide", "Murmur on iPad with transcript, summary and talk time per speaker", "tablet"),
        "blocks": [
            ("Colour per speaker", "Each name gets a colour from the Murmur palette so you can scan a long transcript."),
            ("Reuse names", "Names you add in a note are offered again for its other lines."),
            ("Talk time", "On iPad and Mac, bars show each speaker's share of the conversation."),
            ("In every export", "Text and Markdown exports keep the names next to each line."),
        ],
        "steps": [
            ("Tap Edit on a note", "Each line shows its speaker."),
            ("Pick or type a name", "Apply it to the lines that person said."),
            ("Read and export", "Names and colours carry through to summaries and exports."),
        ],
        "faqs": [
            ("Does Murmur detect speakers automatically?", "Not today. You label speakers yourself in the editor, which takes a few taps and stays accurate."),
            ("How many speakers can a note have?", "As many as you need. Colours repeat after five speakers."),
        ],
        "related": ["transcript-editor", "ai-summaries", "export"],
    },
    {
        "slug": "transcript-editor",
        "name": "Transcript editor",
        "icon": "edit", "color": "",
        "card": "Tap any line to hear it. Fix words, split and merge lines, and undo anything.",
        "title": "Transcript editor with tap-to-play audio",
        "desc": "Tap any line of a transcript to play the audio from that moment. Edit text, split and merge lines, set speakers and undo changes, all on your device.",
        "h1": "Tap a line, <span class=\"hl\">hear it again</span>",
        "lead": "Every line in a Murmur transcript is linked to its moment in the audio. Tap to play from there, follow along as it plays, and fix anything Whisper misheard.",
        "q": "How do I check and correct a transcript against the audio?",
        "a": "In Murmur, tap any line to play the recording from that point. The current line is highlighted and the view scrolls with playback. Tap Edit to change the text, split a long line, merge short ones or set the speaker. Undo is always one tap away.",
        "viz": "transcribe",
        "shot": ("iphone-note", "Murmur transcript with the current line highlighted during playback", "phone"),
        "blocks": [
            ("Tap to play", "Start playback from any line. The playing line is highlighted and the list follows along."),
            ("Skip and speed", "Jump back or forward 15 seconds and listen at 1×, 1.5× or 2×."),
            ("Split and merge", "Break a long line in two or join short fragments."),
            ("Undo", "Changes can be undone, with quick edits grouped so one undo does what you expect."),
            ("Find and replace", "Fix a name everywhere in a transcript at once."),
            ("Arrow keys on Mac", "Step through lines with Up and Down, and press Space to play."),
        ],
        "steps": [
            ("Open a note", "The transcript and player are ready."),
            ("Tap a line to listen", "Check what was said."),
            ("Edit and save", "Fix the text; changes save to the note."),
        ],
        "faqs": [
            ("Can I edit a transcript after it is made?", "Yes. Edit text, speakers and line breaks at any time. Murmur Pro is needed to edit notes longer than two minutes."),
            ("Does editing change the audio?", "No. Edits change the transcript only. The recording stays as it was."),
        ],
        "related": ["search", "speaker-labels", "custom-dictionary"],
    },
    {
        "slug": "search",
        "name": "Search and find & replace",
        "icon": "search", "color": "c4",
        "card": "Search every note at once, jump to the exact moment, and replace a word across a transcript.",
        "title": "Search every transcript, with find and replace",
        "desc": "Find any word across all your recordings. Murmur searches transcripts and summaries, shows each hit with its timestamp, and replaces words across a transcript.",
        "h1": "Find any word <span class=\"hl\">in any recording</span>",
        "lead": "Search all your notes at once. Results show the matching line and its timestamp, and one tap takes you to that moment. Inside a note, find and replace fixes a word everywhere.",
        "q": "Can I search inside my voice recordings?",
        "a": "Yes. Once Murmur has transcribed your recordings, the search screen looks through every transcript and summary at once. It ignores case and accents, shows each matching line with its timestamp, and opens the note at that moment so you can play it.",
        "viz": "search",
        "shot": ("iphone-search", "Murmur search results with matching lines and timestamps", "phone"),
        "blocks": [
            ("All notes at once", "Search every transcript and summary, or narrow to just transcripts or just summaries."),
            ("Case and accent insensitive", "Search for \"cafe\" and find \"Café\"."),
            ("Timestamps on hits", "Each result shows when it was said, so you can jump straight there."),
            ("Find and replace", "Step through matches in a note and replace one or all of them."),
            ("Teach the dictionary", "When you replace a misheard word, Murmur can add the correct spelling to your dictionary for next time."),
            ("Search on Mac", "Press ⌘F in the Mac app to search the whole library."),
        ],
        "steps": [
            ("Tap Search in the library", "Type a word or phrase."),
            ("Pick a result", "The note opens at that line."),
            ("Replace if needed", "Use Find and replace from the note's menu."),
        ],
        "faqs": [
            ("Does search work on free notes?", "Yes. Search reads the full text of every note, including the parts beyond the free two-minute preview."),
            ("Can I replace a word in every note at once?", "Find and replace works inside one note at a time, so you can review each change."),
        ],
        "related": ["custom-dictionary", "transcript-editor", "export"],
    },
    {
        "slug": "custom-dictionary",
        "name": "Custom dictionary",
        "icon": "book", "color": "c2",
        "card": "Teach Murmur names, brands and jargon so they are spelled your way in every transcript.",
        "title": "Custom vocabulary for accurate transcription",
        "desc": "Add names, product terms and jargon to Murmur's custom dictionary. They are passed to Whisper as vocabulary so transcripts spell them correctly.",
        "h1": "Your names and jargon, <span class=\"hl\">spelled right</span>",
        "lead": "Speech models stumble on unusual names and technical terms. Add them to Murmur's dictionary once and they are given to Whisper as vocabulary for every transcription after that.",
        "q": "How do I make transcription spell names and technical terms correctly?",
        "a": "Add the words to Murmur's custom dictionary. Murmur gives these terms to Whisper as vocabulary hints when it transcribes, which makes it more likely to spell them your way. You can also add a word straight from Find and replace after correcting it.",
        "viz": "dictionary",
        "shot": ("iphone-dictionary", "Murmur custom dictionary with names and terms", "phone"),
        "blocks": [
            ("Names and terms", "Add people, places, brands, drug names, legal terms or code words."),
            ("No duplicates", "Murmur spots a word you already added."),
            ("Add while fixing", "Correct a word with Find and replace and add it to the dictionary in the same step."),
            ("Import and export a list on Mac", "Paste or save the whole list in one go."),
        ],
        "steps": [
            ("Open Dictionary in Settings", "Type a word and add it."),
            ("Record or import", "New transcriptions use your words as hints."),
            ("Keep refining", "Add more words as you spot them."),
        ],
        "faqs": [
            ("Does the dictionary fix old transcripts?", "It applies to new transcriptions. Use Find and replace to fix words in notes that are already transcribed."),
            ("Does iCloud sync include the dictionary?", "Yes, when you turn on iCloud sync your dictionary words sync along with your notes and folders."),
        ],
        "related": ["search", "on-device-transcription", "transcript-editor"],
    },
    {
        "slug": "export",
        "name": "Export TXT, Markdown, SRT",
        "icon": "share", "color": "c3",
        "card": "Export text with speakers and timestamps, Markdown, SRT subtitles or the audio itself.",
        "title": "Export transcripts as TXT, Markdown, SRT or audio",
        "desc": "Export Murmur transcripts as plain text with speakers and timestamps, Markdown, SRT subtitles, or M4A audio. Share to any app or copy to the clipboard.",
        "h1": "Take your words <span class=\"hl\">anywhere</span>",
        "lead": "Send a transcript to your notes app, a document, a video editor or a colleague. Choose the format, choose what to include, and share it like any other file.",
        "q": "How do I export a transcript as subtitles?",
        "a": "Open the note in Murmur, tap Share and choose Subtitles. Murmur writes an SRT file with each line's start and end time, which video editors such as Final Cut Pro, Premiere Pro, DaVinci Resolve and YouTube accept. You can also export text, Markdown or the audio.",
        "viz": "export",
        "shot": ("mac-export", "Murmur for Mac export sheet with Text, Subtitles, Audio and Markdown", "wide"),
        "blocks": [
            ("Text", "Plain text with optional speaker names, timestamps and the summary."),
            ("Markdown", "Headings, speakers and action items, ready for Obsidian, Notion or Bear."),
            ("Subtitles (SRT)", "Timed captions for video editors and YouTube."),
            ("Audio", "The recording as an M4A file."),
            ("Copy", "Put the text on the clipboard without making a file."),
            ("Share sheet or Finder", "Send to any app on iPhone and iPad, or save and reveal in Finder on Mac."),
        ],
        "steps": [
            ("Open a note", "Tap the Share button."),
            ("Choose a format", "Text, Markdown, Subtitles or Audio."),
            ("Share or save", "Pick an app, AirDrop, Mail or Files."),
        ],
        "faqs": [
            ("Is exporting free?", "Exporting notes up to two minutes long is free. Murmur Pro exports notes of any length."),
            ("Can I drag a note out on Mac?", "Yes. Drag a note from the list into Finder or Mail to get a text file."),
        ],
        "related": ["import-audio-video", "speaker-labels", "ai-summaries"],
    },
    {
        "slug": "icloud-sync",
        "name": "Optional iCloud sync",
        "icon": "sync", "color": "c4",
        "card": "Keep notes, transcripts and folders in step on iPhone, iPad and Mac through your own private iCloud.",
        "title": "Sync transcripts across iPhone, iPad and Mac with iCloud",
        "desc": "Optional iCloud sync keeps Murmur notes, transcripts, folders and dictionary in step across your Apple devices using your own private iCloud. Off by default.",
        "h1": "Your notes on every device, <span class=\"hl\">through your own iCloud</span>",
        "lead": "Turn on iCloud sync and your notes, transcripts, summaries, folders and dictionary appear on your other devices signed in to the same Apple ID. It uses your private iCloud database, which we cannot read.",
        "q": "Does Murmur sync between iPhone and Mac?",
        "a": "Yes, if you turn it on. Murmur's iCloud sync is off by default. When you switch it on in Settings, notes, transcripts, summaries, folders and dictionary words sync through your own private iCloud database to your iPhone, iPad and Mac. Audio files stay on the device that recorded them.",
        "viz": "sync",
        "shot": ("mac-main", "Murmur for Mac library with notes recorded on iPhone and Apple Watch", "wide"),
        "blocks": [
            ("Off until you choose", "Sync is opt-in. Murmur works fully on one device without it."),
            ("Your private iCloud", "Data goes to your own CloudKit private database. There is no Murmur server and we cannot see it."),
            ("Transcripts, not audio", "Audio stays on the device that recorded it, which keeps your iCloud storage light. Other devices show the transcript."),
            ("A backup first", "Before sync is first turned on, Murmur saves a local copy of your library."),
            ("No double work", "A note is only transcribed by the device that has its audio, so devices never fight over it."),
            ("Takes effect at next launch", "Turn it on, reopen Murmur, and your library starts syncing."),
        ],
        "steps": [
            ("Open Settings", "Turn on Sync with iCloud."),
            ("Reopen Murmur", "Sync starts at the next launch."),
            ("Open Murmur on another device", "Signed in to the same Apple ID, your notes appear."),
        ],
        "faqs": [
            ("Does sync upload my audio?", "No. Only notes, transcripts, summaries, folders and dictionary words sync. Audio stays where it was recorded."),
            ("Can Murmur read my synced notes?", "No. They live in your private iCloud database, which only your Apple ID can access."),
            ("What if I am not signed in to iCloud?", "Murmur keeps working on the device and Settings shows that you need to sign in to sync."),
        ],
        "related": ["private-by-design", "on-device-transcription", "export"],
    },
    {
        "slug": "private-by-design",
        "name": "Private by design",
        "icon": "shield", "color": "",
        "card": "No accounts, no analytics, no ads, no tracking. We have no server to send your data to.",
        "title": "Private transcription app: no account, no tracking",
        "desc": "Murmur is a private transcription app with no accounts, no analytics, no ads and no servers. Recordings and transcripts stay on your device.",
        "h1": "We built Murmur <span class=\"hl\">so we never see your words</span>",
        "lead": "Murmur has no account system, no analytics SDK, no advertising and no server of its own. Its App Store privacy label is Data Not Collected.",
        "q": "Is there a private transcription app that does not upload audio?",
        "a": "Murmur is built for exactly that. It transcribes with Whisper on your iPhone, iPad or Mac, has no accounts, no analytics and no ads, and never uploads your audio or transcripts. The only network use is the one-time model download, App Store purchases and optional iCloud sync to your own private iCloud.",
        "viz": "offline",
        "shot": ("ipad-settings", "Murmur settings on iPad with privacy and sync options", "tablet"),
        "blocks": [
            ("No account", "Open the app and record. There is nothing to sign up for."),
            ("No analytics or ads", "No tracking SDKs, no advertising IDs, no usage reporting."),
            ("Data Not Collected", "That is Murmur's answer on the App Store privacy label."),
            ("Delete audio after transcribing", "Optionally keep only the text and remove the recording once it is transcribed."),
            ("Your iCloud, if you want it", "Sync uses your private iCloud database, never a server of ours."),
            ("Readable policy", "Our privacy policy is short and written in plain English."),
        ],
        "steps": [
            ("Audio is captured on your device", "It is written to Murmur's own storage."),
            ("Whisper transcribes it locally", "The model runs on your device's chips."),
            ("You decide what leaves", "Only what you export or share goes anywhere."),
        ],
        "faqs": [
            ("Does Murmur upload my recordings?", "No. Recordings and transcripts are processed and stored on your device. We have no server to receive them."),
            ("Is Murmur suitable for confidential conversations?", "Because audio never leaves the device, Murmur suits sensitive work such as interviews, legal notes or patient conversations. Check your own organisation's rules for recording and storing such material."),
            ("What network connections does Murmur make?", "The one-time speech model download, App Store purchases through StoreKit, and iCloud if you turn on sync. Nothing else."),
        ],
        "related": ["offline-transcription", "icloud-sync", "on-device-transcription"],
    },
]

# ---------------------------------------------------------------- platforms
PLATFORMS = [
    {
        "slug": "iphone", "name": "iPhone", "icon": "phone",
        "title": "Murmur for iPhone: private speech to text app",
        "desc": "Record and transcribe on iPhone with Whisper running on the device. Summaries, search, export and Apple Watch recordings. No account, works offline.",
        "h1": "Murmur for <span class=\"hl\">iPhone</span>",
        "lead": "The whole Murmur experience in your pocket: one-tap recording, on-device Whisper transcripts, summaries, search and export.",
        "q": "What is the best offline transcription app for iPhone?",
        "a": "Murmur is an iPhone app that transcribes speech with Whisper on the device, so it works offline and never uploads audio. It records with bookmarks, imports audio and video, summarizes with Apple Intelligence on supported iPhones, and exports text, Markdown or SRT subtitles.",
        "shots": [("iphone-recording", "Recording"), ("iphone-note", "Transcript"), ("iphone-summary", "Summary"), ("iphone-library", "Library"), ("iphone-search", "Search"), ("iphone-dictionary", "Dictionary"), ("iphone-find-replace", "Find and replace")],
        "kind": "phone",
        "points": [
            ("Library with folders", "Notes grouped by day, folder chips, a From Watch smart folder and swipe to delete."),
            ("Record and transcribe", "One tap to record, bookmarks, and a transcript when you stop."),
            ("Read, play and fix", "Tap a line to play it, edit text and speakers, find and replace."),
            ("Summaries", "Meeting, Lecture and Bullet point summaries on iPhones with Apple Intelligence."),
            ("Import", "Files, videos from Photos, and audio shared from other apps."),
            ("Export", "Text, Markdown, SRT or audio through the share sheet."),
        ],
        "faqs": [
            ("Which iPhones can run Murmur?", "Murmur runs on recent iPhones. Summaries need an iPhone that supports Apple Intelligence; transcription works without it."),
            ("Can I use Murmur with my Apple Watch?", "Yes. Record on the watch and the audio is sent to your iPhone for transcription. New watch recordings are flagged in the library."),
        ],
    },
    {
        "slug": "ipad", "name": "iPad", "icon": "tablet",
        "title": "Murmur for iPad: transcription with summary side panel",
        "desc": "Murmur on iPad: a three-column library, transcript beside summary and talk time, drag-and-drop import and a large recording view. On-device Whisper.",
        "h1": "Murmur for <span class=\"hl\">iPad</span>",
        "lead": "More room to work. A sidebar, note list and transcript side by side, a summary panel with talk time, and drag-and-drop import.",
        "q": "Is there a transcription app for iPad that works offline?",
        "a": "Murmur runs on iPad with the same on-device Whisper engine as on iPhone, so it transcribes offline without uploading audio. The iPad layout puts the library, notes and transcript side by side, with a summary and talk-time panel and a drop zone for importing files.",
        "shots": [("ipad-note-wide", "Transcript and summary"), ("ipad-library", "Library"), ("ipad-recording", "Recording"), ("ipad-search", "Search with context"), ("ipad-import", "Drop to import"), ("ipad-settings", "Settings")],
        "kind": "tablet",
        "points": [
            ("Three-column library", "Folders, notes and the open note together."),
            ("Summary beside transcript", "Action items and talk-time bars next to the text."),
            ("Search with context", "Results beside a preview of the lines around each match."),
            ("Drag and drop", "Drop audio and video files from Files to transcribe them."),
            ("Big recording view", "A large timer and a bookmarks panel while you record."),
            ("Phone layout when narrow", "In Split View and Slide Over, Murmur switches to its compact layout."),
        ],
        "faqs": [
            ("Is the iPad app a separate purchase?", "No. Murmur is one universal app. Murmur Pro bought on one device unlocks it on your iPhone, iPad and Mac with the same Apple ID."),
        ],
    },
    {
        "slug": "mac", "name": "Mac", "icon": "laptop",
        "title": "Murmur for Mac: offline Whisper transcription app",
        "desc": "Transcribe audio on your Mac with Whisper on Apple silicon. Menu bar recorder, global shortcut, batch queue, drag and drop, Markdown export. No uploads.",
        "h1": "Murmur for <span class=\"hl\">Mac</span>",
        "lead": "Fast, private transcription on Apple silicon. Drop in a folder of recordings, start recording from the menu bar with a shortcut, and export straight to Markdown.",
        "q": "How can I transcribe audio offline on a Mac?",
        "a": "Install Murmur on a Mac with Apple silicon and download the Whisper model once. Then drag audio or video files into the window, or record from the menu bar with Control-Option-R. Murmur transcribes on your Mac and never uploads the audio.",
        "shots": [("mac-main", "Library and inspector"), ("mac-queue", "Batch queue"), ("mac-export", "Export"), ("mac-drop", "Drag and drop"), ("mac-settings", "Settings")],
        "kind": "wide",
        "points": [
            ("Menu bar recorder", "A timer in the menu bar and a floating recording window."),
            ("Global shortcut", "Start recording from any app with ⌃⌥R, or set your own."),
            ("Batch queue", "See each file's progress and speed in times real time, and pause the queue."),
            ("Inspector", "Playback, summary, action items, talk time and file info beside the transcript."),
            ("Markdown export", "Send transcripts to Obsidian or any notes app."),
            ("Microphone picker", "Record from a USB or audio-interface microphone, with fallback to the default."),
        ],
        "faqs": [
            ("Which Macs does Murmur support?", "Murmur for Mac needs a Mac with Apple silicon running macOS 15 or later."),
            ("Can Murmur run without a Dock icon?", "Yes. Settings can hide the Dock icon and keep Murmur in the menu bar."),
        ],
    },
    {
        "slug": "apple-watch", "name": "Apple Watch", "icon": "watch",
        "title": "Murmur for Apple Watch: record voice notes from your wrist",
        "desc": "Record voice notes and meetings on Apple Watch and get a private transcript on your iPhone. Complications, Action button support, works away from your phone.",
        "h1": "Murmur for <span class=\"hl\">Apple Watch</span>",
        "lead": "Capture a thought before it slips away. Record on your wrist, and the audio is sent to your iPhone to be transcribed on the device.",
        "q": "Can I record voice notes on Apple Watch and transcribe them?",
        "a": "Yes. The Murmur watch app records audio on your Apple Watch and sends it to your iPhone, which transcribes it with Whisper on the device. If your phone is out of range, recordings wait on the watch and send when it is back.",
        "shots": [("watch-home", "Home"), ("watch-recording", "Recording"), ("watch-saved", "Saved and sending"), ("watch-recent", "Recent"), ("watch-playback", "Playback"), ("watch-complications", "Complications")],
        "kind": "watch",
        "points": [
            ("One tap to record", "A big record button on the watch face app."),
            ("Sends when it can", "Recordings queue on the watch and transfer when your iPhone is in range, with no duplicates."),
            ("Complications", "Start recording from your watch face."),
            ("Action button", "Start a recording with the Action button on supported models."),
            ("Recent recordings", "See what was sent and play it back on the watch."),
            ("From Watch folder", "On iPhone, watch recordings collect in their own smart folder."),
        ],
        "faqs": [
            ("Does the watch transcribe the audio itself?", "No. The watch records; your iPhone does the transcription so the watch stays fast and saves battery."),
            ("Do I need my iPhone nearby to record?", "No. You can record away from your phone and the recordings send when the two are back in range."),
        ],
    },
]

# ---------------------------------------------------------------- use cases
USE_CASES = [
    {
        "slug": "meeting-transcription", "name": "Meetings", "icon": "briefcase",
        "title": "Private meeting transcription with notes and action items",
        "desc": "Record in-person meetings and get a transcript, summary and action items on your device. No bot joins the call, nothing is uploaded.",
        "h1": "Meeting notes that <span class=\"hl\">write themselves</span>, privately",
        "lead": "Put your phone on the table, tap record and stay in the conversation. Murmur gives you a transcript, a Meeting summary and a list of action items, without sending a word to a server.",
        "q": "How can I transcribe a meeting without uploading it to the cloud?",
        "a": "Record the meeting in Murmur on your iPhone, iPad or Mac, or import a recording file. Murmur transcribes it with Whisper on the device, and on devices with Apple Intelligence it writes a Meeting summary with action items. The audio and transcript stay on your device.",
        "pains": ["Typing notes means you stop listening.", "Cloud note-takers upload confidential discussions to someone else's servers.", "Bots in calls make people guarded."],
        "features": ["voice-recorder", "ai-summaries", "speaker-labels", "export"],
        "steps": [("Record or import", "Record in the room, or import a saved call recording."), ("Label speakers", "Tag who said what in a few taps."), ("Summarize", "Choose the Meeting template for decisions and action items."), ("Share", "Export Markdown or text to your team.")],
        "faqs": [("Can Murmur join my Zoom or Teams call?", "No. Murmur never joins calls. Record in person, or import a recording you saved from the call."), ("Is it legal to record a meeting?", "Recording laws differ by place, and some require everyone's consent. Always tell people you are recording.")],
    },
    {
        "slug": "lecture-transcription", "name": "Lectures", "icon": "graduation",
        "title": "Lecture transcription app for students",
        "desc": "Record lectures and get searchable transcripts and study summaries on your iPhone or Mac. Works offline in any lecture hall.",
        "h1": "Listen in class. <span class=\"hl\">Study from the transcript.</span>",
        "lead": "Record a whole lecture, bookmark the parts the professor says will be on the exam, and get a searchable transcript and Lecture summary afterwards, even with no Wi-Fi in the hall.",
        "q": "What is a good app to record and transcribe lectures?",
        "a": "Murmur records lectures on iPhone, iPad or Mac and transcribes them on the device with Whisper, so it works without Wi-Fi. Bookmarks mark key moments, search finds any term across all lectures, and the Lecture summary pulls out the main ideas.",
        "pains": ["Lecture halls often have weak Wi-Fi.", "Handwritten notes miss details.", "Finding one explanation in hours of audio is slow."],
        "features": ["voice-recorder", "search", "ai-summaries", "custom-dictionary"],
        "steps": [("Record the lecture", "Bookmark exam hints and examples."), ("Add course terms", "Put technical words in the dictionary."), ("Search to revise", "Find every mention of a topic across the term."), ("Summarize", "Use the Lecture template for key ideas.")],
        "faqs": [("Can I organise lectures by course?", "Yes. Create a folder for each course and file notes into it."), ("Should I ask before recording a lecture?", "Many schools have rules about recording classes. Check your school's policy and ask the lecturer.")],
    },
    {
        "slug": "interview-transcription", "name": "Interviews", "icon": "message",
        "title": "Interview transcription app for journalists and researchers",
        "desc": "Transcribe interviews on your device with Whisper. Keep sources confidential, label speakers, search quotes with timestamps and export text.",
        "h1": "Interviews transcribed, <span class=\"hl\">sources kept safe</span>",
        "lead": "For journalists, researchers and recruiters, the recording is sensitive. Murmur transcribes interviews on your own device so the audio never passes through a third-party server.",
        "q": "How do journalists transcribe interviews privately?",
        "a": "A private option is to transcribe on the device. With Murmur, you record or import the interview on an iPhone, iPad or Mac and Whisper transcribes it locally. Label the interviewer and the source, tap any line to check the quote against the audio, and export with timestamps.",
        "pains": ["Uploading a source's voice to a cloud service creates a copy you do not control.", "Checking quotes against audio takes ages.", "Paid human transcription is slow and costly."],
        "features": ["private-by-design", "speaker-labels", "transcript-editor", "search"],
        "steps": [("Record or import", "On the phone, Mac or from a recorder file."), ("Label speakers", "Interviewer and source."), ("Verify quotes", "Tap a line to hear exactly what was said."), ("Export", "Text with timestamps for your notes.")],
        "faqs": [("Can I delete the audio and keep the text?", "Yes. Turn on Delete audio after transcribing in Settings, or delete individual notes."), ("Does Murmur work with external recorders?", "Yes. Import the audio files from the recorder through Files or by dragging them onto the Mac app.")],
    },
    {
        "slug": "voice-memo-transcription", "name": "Voice notes", "icon": "mic",
        "title": "Transcribe voice memos and voice notes on iPhone",
        "desc": "Turn voice memos and spoken notes into searchable text on your iPhone or Apple Watch. On-device Whisper, no account, nothing uploaded.",
        "h1": "Think out loud. <span class=\"hl\">Read it later.</span>",
        "lead": "Ideas come on walks, in the car and in the shower. Capture them on your iPhone or Apple Watch and Murmur turns them into text you can search, file and share.",
        "q": "How can I turn voice memos into text on iPhone?",
        "a": "Record the note in Murmur, or share an existing Voice Memos recording to Murmur. Murmur transcribes it with Whisper on your iPhone and saves it as a searchable note. You can also record on Apple Watch and find the transcript on your iPhone.",
        "pains": ["Voice memos pile up unheard.", "You cannot search audio for that one idea.", "Typing on the go is slow."],
        "features": ["voice-recorder", "import-audio-video", "search", "custom-dictionary"],
        "steps": [("Capture", "Tap record on iPhone or Apple Watch."), ("Transcribe", "Murmur makes the text on your iPhone."), ("File and find", "Move notes into folders and search them later.")],
        "faqs": [("Can I transcribe old Voice Memos?", "Yes. Share them to Murmur or save them to Files and import them."), ("How do I record from my wrist?", "Use the Murmur watch app, its complication, or the Action button on supported watches.")],
    },
    {
        "slug": "video-subtitles", "name": "Subtitles", "icon": "captions",
        "title": "Make SRT subtitles from video on iPhone and Mac",
        "desc": "Create SRT subtitle files from your videos on device. Import a video, let Whisper transcribe it, fix any lines and export SRT for YouTube or your editor.",
        "h1": "Subtitles for your videos, <span class=\"hl\">made on your Mac or iPhone</span>",
        "lead": "Import a video, let Whisper transcribe it, tidy any lines and export an SRT file with timings. It is ready for YouTube, Final Cut Pro, Premiere Pro or DaVinci Resolve.",
        "q": "How do I make an SRT subtitle file from a video?",
        "a": "Import the video into Murmur from Photos, Files or by dragging it onto the Mac app. Murmur extracts the audio and transcribes it with Whisper on your device. Check the lines, then choose Share, Subtitles to export an SRT file you can upload to YouTube or add in your video editor.",
        "pains": ["Subtitle services charge per minute.", "Uploading unreleased footage is a risk.", "Typing captions by hand takes hours."],
        "features": ["import-audio-video", "transcript-editor", "export", "custom-dictionary"],
        "steps": [("Import the video", "From Photos, Files or drag and drop on Mac."), ("Review the lines", "Tap to play and fix any word."), ("Export SRT", "Share, Subtitles."), ("Upload", "Add the file to YouTube or your editor's timeline.")],
        "faqs": [("Can Murmur burn subtitles into the video?", "No. Murmur exports an SRT file; your video editor or YouTube displays it or burns it in."), ("Does it work for other languages?", "Yes, for the 13 languages Murmur supports, or set it to auto-detect.")],
    },
]

# ---------------------------------------------------------------- guides
GUIDES = [
    {
        "slug": "transcribe-voice-memos-iphone",
        "title": "How to transcribe Voice Memos on iPhone (private, offline)",
        "nav": "Transcribe Voice Memos on iPhone",
        "desc": "Step-by-step: turn iPhone Voice Memos into text with on-device Whisper. No upload, works offline, with tips for better accuracy.",
        "h1": "How to transcribe Voice Memos on iPhone",
        "lead": "A step-by-step guide to turning Voice Memos recordings into text on your iPhone, without uploading them anywhere.",
        "q": "How do I transcribe a Voice Memo on iPhone?",
        "a": "Open the recording in Voice Memos, tap the three-dot menu and choose Share. Pick Murmur if it is listed, or choose Save to Files and then import the file in Murmur. Murmur transcribes it with Whisper on your iPhone, and the text appears as a note you can search, edit and export.",
        "body": """
<h2 id="steps">Steps</h2>
<ol class="howto">
<li><strong>Install Murmur and download the speech model.</strong> Open Murmur, finish onboarding, and download the Whisper model on Wi-Fi. This happens once.</li>
<li><strong>Open the recording in Voice Memos.</strong> Tap the memo you want to transcribe.</li>
<li><strong>Tap the three-dot menu, then Share.</strong> If Murmur appears in the list of apps, tap it and skip to step 6.</li>
<li><strong>Otherwise choose Save to Files.</strong> Save the memo to a folder in On My iPhone or iCloud Drive.</li>
<li><strong>In Murmur, tap Import, then Files.</strong> Pick the memo you saved. You can select several at once.</li>
<li><strong>Wait for the transcript.</strong> The memo joins Murmur's queue and is transcribed on your iPhone. When it is ready, open the note to read and play it.</li>
</ol>
<h2 id="accuracy">Tips for better accuracy</h2>
<ul>
<li>Use the Large v3 Turbo model if your iPhone has space; it is Murmur's most accurate option.</li>
<li>Add names and jargon to the <a href="/features/custom-dictionary/">custom dictionary</a> before transcribing.</li>
<li>If a memo is in another language, set the language in Settings or leave it on Auto-detect.</li>
<li>Record new memos directly in Murmur so you can drop <a href="/features/voice-recorder/">bookmarks</a> as you go.</li>
</ul>
<h2 id="why">Why transcribe on the device?</h2>
<p>Voice memos are often personal: ideas, reminders, conversations. Murmur keeps them on your iPhone. The <a href="/features/on-device-transcription/">transcription runs locally</a>, there is no account, and the app works <a href="/features/offline-transcription/">offline</a> once the model is downloaded.</p>
""",
        "faqs": [
            ("Does Apple's Voice Memos app make transcripts?", "Recent versions of iOS can show transcripts in some apps and regions. Murmur adds speaker labels, search across all notes, summaries, custom vocabulary and SRT, Markdown and text export, all on the device."),
            ("Can I transcribe many voice memos at once?", "Yes. Save them to Files and select them together in Murmur's import screen. They are transcribed one after another."),
        ],
        "related": ["import-audio-video", "voice-recorder", "search"],
    },
    {
        "slug": "transcribe-audio-offline-mac",
        "title": "How to transcribe audio offline on Mac with Whisper",
        "nav": "Transcribe audio offline on Mac",
        "desc": "Transcribe audio and video files on your Mac without the internet using Whisper on Apple silicon. Drag-and-drop batch queue, Markdown and SRT export.",
        "h1": "How to transcribe audio offline on a Mac",
        "lead": "Run Whisper on your Mac's Apple silicon to transcribe recordings with no internet connection and no command line.",
        "q": "How do I transcribe audio on a Mac without uploading it?",
        "a": "Use an app that runs a speech model locally. With Murmur for Mac, download the Whisper model once, then drag audio or video files into the window. Each file joins a queue and is transcribed on your Mac's Apple silicon. Export the result as text, Markdown or SRT.",
        "body": """
<h2 id="steps">Steps</h2>
<ol class="howto">
<li><strong>Install Murmur for Mac.</strong> It needs a Mac with Apple silicon and macOS 15 or later.</li>
<li><strong>Download the speech model.</strong> Onboarding offers Whisper Large v3 Turbo (about 632 MB) or Small (about 500 MB). You only download it once.</li>
<li><strong>Drag files into the window.</strong> Drop one file or many anywhere in Murmur, or click Import.</li>
<li><strong>Watch the queue.</strong> Open Queue in the sidebar to see each file's progress and how many times faster than real time it is running. You can pause the queue.</li>
<li><strong>Read and check.</strong> Click a note, press Space to play, and use the Up and Down arrows to move between lines.</li>
<li><strong>Export.</strong> Click Share and choose Text, Markdown, Subtitles or Audio. Save it or reveal it in Finder.</li>
</ol>
<h2 id="record">Recording on the Mac</h2>
<p>To record instead, press <strong>⌃⌥R</strong> from any app (you can change the shortcut), or use the Murmur item in the menu bar. A small floating window shows the timer. Pick a USB microphone in Settings if you use one.</p>
<h2 id="cli">Do I need the command line?</h2>
<p>No. Running Whisper yourself usually means installing Python or building a C++ project and working in Terminal. Murmur packages Whisper (through the WhisperKit framework) as a normal Mac app with a library, editor and export.</p>
""",
        "faqs": [
            ("Is Whisper free to use on Mac?", "Whisper itself is open source. Murmur is free to download and shows the first two minutes of every note; Murmur Pro unlocks full transcripts and export."),
            ("Does Murmur work on Intel Macs?", "No. Murmur for Mac needs Apple silicon."),
        ],
        "related": ["import-audio-video", "export", "on-device-transcription"],
    },
    {
        "slug": "create-srt-subtitles-from-video",
        "title": "How to create SRT subtitles from a video for free on device",
        "nav": "Create SRT subtitles from a video",
        "desc": "Make an SRT caption file from any video on iPhone or Mac with Whisper on the device. Import, review, export and upload to YouTube or your editor.",
        "h1": "How to create SRT subtitles from a video",
        "lead": "Generate a timed SRT caption file from your video on your iPhone, iPad or Mac, without uploading the footage.",
        "q": "What is an SRT file and how do I make one?",
        "a": "An SRT file is a plain-text subtitle format: numbered captions, each with a start and end time and a line of text. To make one, import your video into Murmur, let it transcribe the audio on your device, check the lines, then choose Share, Subtitles to export the SRT.",
        "body": """
<h2 id="what">What an SRT file looks like</h2>
<p>Each caption has a number, a time range and the text, separated by blank lines:</p>
<div class="card"><pre style="margin:0;white-space:pre-wrap;font-size:15px;color:var(--text-2)">1
00:00:04,000 --&gt; 00:00:09,500
Okay, let's start with the Q4 roadmap.

2
00:00:15,000 --&gt; 00:00:21,000
Watch is smaller, and it's the most requested feature.</pre></div>
<h2 id="steps">Steps</h2>
<ol class="howto">
<li><strong>Import the video.</strong> On iPhone or iPad, tap Import, then Videos to pick from Photos, or Files. On Mac, drag the video into the window.</li>
<li><strong>Let Murmur transcribe it.</strong> Murmur extracts the soundtrack and transcribes it with Whisper on your device.</li>
<li><strong>Review the lines.</strong> Tap any line to play it, fix words, and split long lines so captions stay short.</li>
<li><strong>Export as Subtitles.</strong> Tap Share, choose Subtitles, and save or send the .srt file.</li>
<li><strong>Add it to your video.</strong> Upload the SRT in YouTube Studio's subtitles section, or import it into Final Cut Pro, Premiere Pro or DaVinci Resolve.</li>
</ol>
<h2 id="tips">Tips for readable captions</h2>
<ul>
<li>Keep each caption to one or two short lines; split long lines in the <a href="/features/transcript-editor/">editor</a>.</li>
<li>Add product and people names to the <a href="/features/custom-dictionary/">dictionary</a> before importing.</li>
<li>Clear audio gives the best timings; reduce music under speech where you can.</li>
</ul>
""",
        "faqs": [
            ("Is SRT supported by YouTube?", "Yes. YouTube Studio accepts SRT files as subtitles."),
            ("Can I translate subtitles with Murmur?", "No. Murmur transcribes in the spoken language. It does not translate."),
        ],
        "related": ["export", "import-audio-video", "transcript-editor"],
    },
    {
        "slug": "what-is-whisper",
        "title": "What is Whisper? OpenAI's speech recognition model explained",
        "nav": "What is Whisper?",
        "desc": "Whisper is OpenAI's open-source speech recognition model. Learn how it works, the model sizes including Large v3 Turbo, and how it runs on iPhone and Mac.",
        "h1": "What is Whisper?",
        "lead": "A plain-English explainer of the speech recognition model behind Murmur, and why it can run on a phone.",
        "q": "What is OpenAI Whisper?",
        "a": "Whisper is an open-source automatic speech recognition model released by OpenAI in September 2022. It was trained on 680,000 hours of multilingual audio collected from the web, and it can transcribe speech in many languages and translate it into English. Because the model weights are public, apps like Murmur can run it on your own device.",
        "body": """
<h2 id="how">How Whisper works</h2>
<p>Whisper is a transformer model with two halves. The <strong>encoder</strong> listens: it turns 30-second windows of audio into an internal representation. The <strong>decoder</strong> writes: it predicts the text one token at a time, along with timestamps. OpenAI describes the training data and results in its <a href="https://openai.com/index/whisper/" rel="noopener">Whisper announcement</a> and the paper <a href="https://arxiv.org/abs/2212.04356" rel="noopener">Robust Speech Recognition via Large-Scale Weak Supervision</a>.</p>
<h2 id="sizes">Model sizes</h2>
<p>Whisper comes in sizes from Tiny to Large. Bigger models are more accurate but need more memory and time.</p>
<div class="table-wrap"><table>
<thead><tr><th>Model</th><th>Use in Murmur</th></tr></thead>
<tbody>
<tr><td>Large v3 Turbo</td><td class="yes">Recommended. Compressed to about 632 MB.</td></tr>
<tr><td>Small</td><td>Lighter option, about 500 MB.</td></tr>
<tr><td>Tiny</td><td class="no">Not offered. Too inaccurate for real notes.</td></tr>
</tbody></table></div>
<p>Large v3 Turbo, released in 2024, keeps the large encoder but uses a much smaller decoder, which makes it far faster than Large v3 with only a small drop in accuracy.</p>
<h2 id="device">How Whisper runs on iPhone and Mac</h2>
<p>Murmur uses <strong>WhisperKit</strong>, an open-source framework from Argmax that converts Whisper to Core ML so it can use Apple's Neural Engine and GPU. That is what lets a full Large-class model transcribe on an iPhone, with no server involved. Read more about <a href="/features/on-device-transcription/">Murmur's on-device transcription</a>.</p>
<h2 id="limits">Limits to know</h2>
<ul>
<li>Accuracy drops with heavy background noise, crosstalk and strong music.</li>
<li>Rare names and jargon can be misspelled; a <a href="/features/custom-dictionary/">custom vocabulary</a> helps.</li>
<li>Whisper does not identify speakers by itself. In Murmur you <a href="/features/speaker-labels/">label speakers</a> in the editor.</li>
</ul>
""",
        "faqs": [
            ("Is Whisper free?", "Whisper's code and model weights are open source under the MIT license. Apps built on it may charge for their own features."),
            ("Does Whisper need the internet?", "No. Once the model is on your device it runs offline. Cloud APIs that use Whisper do need the internet, because they run it on their servers."),
        ],
        "related": ["on-device-transcription", "offline-transcription", "custom-dictionary"],
    },
    {
        "slug": "on-device-vs-cloud-transcription",
        "title": "On-device vs cloud transcription: privacy, cost and accuracy",
        "nav": "On-device vs cloud transcription",
        "desc": "Compare on-device and cloud speech-to-text: where your audio goes, offline use, cost, speed and accuracy. Learn which fits meetings, interviews and lectures.",
        "h1": "On-device vs cloud transcription",
        "lead": "Two ways to turn speech into text. Here is what changes when the model runs on your device instead of a server.",
        "q": "What is the difference between on-device and cloud transcription?",
        "a": "Cloud transcription uploads your audio to a company's servers, which run the speech model and send back text. On-device transcription runs the model on your own phone or computer, so the audio never leaves it. On-device works offline and keeps recordings private; cloud services can offer extras that need a server, such as joining calls.",
        "body": """
<h2 id="table">At a glance</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th class="us">On-device (Murmur)</th><th>Cloud services</th></tr></thead>
<tbody>
<tr><td>Where audio goes</td><td class="us yes">Stays on your device</td><td>Uploaded to the provider's servers</td></tr>
<tr><td>Works offline</td><td class="us yes">Yes, after a one-time model download</td><td>No</td></tr>
<tr><td>Account needed</td><td class="us yes">No</td><td>Usually</td></tr>
<tr><td>Speed</td><td class="us">Depends on your device's chip</td><td>Depends on upload speed and server load</td></tr>
<tr><td>Storage on device</td><td class="us">The model takes 500 to 632 MB</td><td>None for the model</td></tr>
<tr><td>Joins online calls</td><td class="us no">No</td><td>Some do, with a bot</td></tr>
<tr><td>Cost model</td><td class="us">One app, optional Pro</td><td>Often per minute or per seat</td></tr>
</tbody></table></div>
<h2 id="privacy">Privacy</h2>
<p>With a cloud service, a copy of your recording exists on someone else's computer, under their retention policy. With on-device transcription the recording and text are only where you put them. That matters for interviews, legal and medical notes, HR conversations and anything under NDA.</p>
<h2 id="accuracy">Accuracy</h2>
<p>Modern on-device models such as Whisper Large v3 Turbo are strong general-purpose recognisers. Audio quality matters more than where the model runs: a close microphone and one speaker at a time beat any setting.</p>
<h2 id="choose">Which should you choose?</h2>
<ul>
<li><strong>Choose on-device</strong> for confidential recordings, travel and poor connections, and if you do not want another account.</li>
<li><strong>Choose cloud</strong> if you need a bot to join and record online calls automatically, or you work only on very old hardware.</li>
</ul>
<p>Murmur is built for the first group. See <a href="/features/private-by-design/">how Murmur handles privacy</a>.</p>
""",
        "faqs": [
            ("Is on-device transcription slower?", "It depends on the device. Recent iPhones and Apple silicon Macs run Whisper with their Neural Engine and GPU, and there is no upload time."),
            ("Can on-device transcription handle long files?", "Yes. Murmur converts and transcribes long files in chunks, and queues several files one after another."),
        ],
        "related": ["private-by-design", "on-device-transcription", "offline-transcription"],
    },
]

# ---------------------------------------------------------------- site-wide FAQ
FAQ = [
    ("What is Murmur?", "Murmur is a speech-to-text app for iPhone, iPad, Mac and Apple Watch. It records or imports audio and transcribes it with OpenAI's Whisper model running on your own device. It also summarizes, searches and exports transcripts, with no account and no uploads."),
    ("Does Murmur upload my audio?", "No. Audio and transcripts are processed and stored on your device. Murmur has no server. If you turn on iCloud sync, notes (not audio) are stored in your own private iCloud database, which we cannot read."),
    ("Does Murmur work offline?", "Yes. After a one-time download of the speech model on Wi-Fi, recording, transcription, search, editing and export work with no internet connection."),
    ("Is Murmur free?", f"Murmur is free to download. Free notes show the first 2 minutes of each transcript. Murmur Pro unlocks full transcripts, editing, export, find and replace and summaries for every note, including older ones. Pro is {PRICES['yearly']} a year with a {PRICES['trial_days']}-day free trial, {PRICES['monthly']} a month, or {PRICES['lifetime']} once for lifetime."),
    ("Which languages does Murmur support?", "Murmur transcribes " + ", ".join(LANGUAGES[:-1]) + " and " + LANGUAGES[-1] + ", and can auto-detect the language. The app's interface is in English."),
    ("How accurate is Murmur?", "Murmur uses Whisper Large v3 Turbo, a high-accuracy speech model. Results depend mostly on audio quality. A custom dictionary helps with names and jargon, and you can fix any line in the editor."),
    ("Which devices does Murmur run on?", "iPhone, iPad, Macs with Apple silicon (macOS 15 or later) and Apple Watch. The watch records and sends audio to your iPhone for transcription. Summaries need a device with Apple Intelligence."),
    ("Does Murmur need an account?", "No. There is nothing to sign up for. Purchases are tied to your Apple ID through the App Store, and Restore purchases brings Pro back on a new device."),
    ("Can Murmur identify different speakers?", "You can label speakers yourself in the editor. Each speaker gets a colour, appears in exports, and adds up to talk-time bars on iPad and Mac. Murmur does not detect speakers automatically."),
    ("What file formats can I export?", "Plain text (with optional speakers, timestamps and summary), Markdown, SRT subtitles and M4A audio. You can also copy the text to the clipboard."),
    ("Does one purchase cover all my devices?", "Yes. Murmur is a universal purchase. Pro bought with your Apple ID works on your iPhone, iPad and Mac."),
    ("How do I cancel a subscription?", "Subscriptions are managed by Apple. Open Settings on your iPhone, tap your name, then Subscriptions, and choose Murmur Pro. Cancel at least 24 hours before the period ends to avoid renewal."),
]
