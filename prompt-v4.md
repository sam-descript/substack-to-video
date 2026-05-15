# [TADA] Article → Social Video (9:16, 30–60s) — V4.0

---

## GLOBAL CONSTRAINTS (apply everywhere — do not override)

**TEXT_FREE** — All AI-generated imagery (stills and video) must contain ZERO text: no words, letters, logos, signage, UI, subtitles, or watermarks. If any generated asset contains text, discard and regenerate until clean. This is a hard-fail condition.

**SCENE_CAP** — No scene may exceed 8.0 seconds. If a VO sentence would push a scene past 8s, split it.

**STYLE_LOCK** — Once a PRIMARY STYLE REFERENCE is established (Section 3), ALL subsequent b-roll must be generated via Nano Banana Pro (edit) with that reference attached. No Descript built-in style picker looks — ever.

**AUTO_EXECUTE** — Proceed automatically through all steps. No approval checkpoints. No plan summaries. If you need the article payload, ask ONLY for the payload.

---

## INPUT CONTRACT

You will receive an article payload that may include:
- Article text (title + body) — required
- Scraped/imported images (hero + supporting) — optional
- Brand logo file — optional
- Brand colors — optional
- Brand fonts — optional

If the payload is not yet provided, ask ONLY for it.

---

## 1 · SCRIPT (30–60s VO)

From the article text, write a voiceover script:
- 30–60 seconds read aloud
- Arc: hook → key points → takeaway
- Short punchy sentences; no long clauses
- No URLs or citations in VO (CTA is handled in the outro)

---

## 2 · BRAND SETUP

### If brand assets were provided (logo, colors, fonts):
Use them directly. For missing fonts, substitute a clean modern sans that fits the brand vibe. For missing logo, proceed without — don't fail.

### If NO brand assets were provided:
You must derive branding from web research using Nano Banana Pro with web search. This is required — do not skip or use Descript defaults.

1. Identify the company/brand from the article text.
2. Use Nano Banana Pro web search to research the brand:
   - "{company} logo" — find and note the logo style, mark, and any wordmark
   - "{company} brand colors" or "{company} brand guidelines" — identify primary and secondary brand colors
   - "{company} website" or "{company} advertising" — note typography style and overall design language
3. From what you find, establish:
   - Color palette: primary + secondary brand colors to use for captions, layout remix, and outro
   - Font direction: the closest clean modern sans that matches the brand's typography
   - Logo handling: if you can identify the logo clearly, recreate its placement style (but do NOT generate the logo inside AI imagery — TEXT_FREE still applies). If no logo can be confidently identified, proceed without one.
4. Apply these derived brand assets the same way you would apply provided ones throughout the rest of the workflow (layout remix, captions, outro).

---

## 3 · ESTABLISH PRIMARY STYLE REFERENCE

This step determines the visual DNA for the entire video. Follow the FIRST matching path:

### Path A — Images were provided/scraped
1. Select ONE image as the PRIMARY STYLE REFERENCE (prefer the hero; else the most on-brand).
2. Retain all other scraped images as supplementary reference.
3. Proceed to Section 4.

### Path B — NO images available (fallback)
You must build a bespoke style from brand research. Do NOT fall back to Descript's style picker.

1. Identify the company/brand from the article (name, product category, vibe).
2. Use Nano Banana Pro (text to image) with web search enabled to generate 3 HERO IMAGE candidates. Your generation prompt should:
   - Reference the brand by name and ask Nano Banana to search for the brand's visual style (e.g., "Search for {company} advertising photography and create a similar image that [describes the script hook/intro scene]")
   - Describe a scene that matches the script's hook/intro meaning
   - Specify cinematic quality, appropriate mood/lighting for the brand
   - Specify no text, no words, no logos, no letters in the image
3. Select the best candidate on: brand fidelity → script relevance → composition quality → TEXT_FREE compliance.
4. This becomes the PRIMARY STYLE REFERENCE. Proceed to Section 4.

---

## 4 · PROJECT + FORMAT

- Create a NEW Descript project.
- Set aspect ratio to 9:16 (vertical).

---

## 5 · VOICEOVER

- If the custom AI Speaker "Sam" is available, use this one.  Else, select an AI voice: confident, clear, not cheesy.  
- Generate VO from the script.

---

## 6 · SCENE MAP (plan before building)

Before generating any visuals, build a timed scene map:

For each scene, define:
- Scene # and internal title
- VO lines (exact text for this scene)
- Duration (target 6-8s; hard cap per SCENE_CAP)
- Visual concept (what the viewer sees, matched to the VO meaning)

Typical count: 8–12 scenes for ~60s. Only after this map is complete, proceed.

---

## 7 · LAYOUT + BRAND REMIX

- Choose a layout pack that supports "captions under media" cleanly.
- Remix to brand colors + fonts when available.
- Avoid layouts with camera placeholder layers.

---

## 8 · VISUAL GENERATION (per STYLE_LOCK + TEXT_FREE)

### 8a · Generate two still candidates per scene
For each scene in the map, use Nano Banana Pro (edit) with the PRIMARY STYLE REFERENCE attached:
- Candidate A: directly literal to the scene VO
- Candidate B: same meaning, different composition or angle

Discard and regenerate any candidate that violates TEXT_FREE.

### 8b · Select best still per scene
Pick A or B based on: VO meaning match → composition → style fidelity → no artifacts.

### 8c · Still → Video (Veo 3.1 image-to-video)
For each selected still:
- Generate a 9:16 Veo 3.1 clip, duration matched to the scene (6-8s)
- Motion: subtle + stable + cinematic (gentle parallax, slow dolly, light environmental)
- No fast zooms, warping, jitter, or looping artifacts
- If Veo output loops or jumps: regenerate with calmer motion

### 8d · Scraped image inserts (if available)
For any scraped image placed on screen, also create a Veo 3.1 moving version (6-8s). If the moving version introduces text artifacts, discard and use a text-free alternative or the original still.

---

## 9 · EDIT ASSEMBLY

- Build timeline from the scene map; each scene uses its Veo clip.
- Default: clean hard cuts.
- No stylized transitions, wipes, zooms, or gimmicks.  Disable Smart Transitions.
- Use Crossfade transitions in between every scene.  Set the duration of transition to 350ms.  

---

## 10 · CAPTIONS

- Apply captions across the full video.
- Style with brand fonts/colors when available.
- Placement: centered-to-lower safe zone; never blocking the primary subject.
- Size: 110 default (range 100–115 by font/fit; never below 100).
- Legibility pass: if any caption is hard to read against its background, add whichever is cleanest and most on-brand: a subtle background plate, a stroke/outline, or a drop shadow.

---

## 11 · LOGO OVERLAY

If a logo was provided:
- Place as a consistent small corner bug across the entire video (same corner, same size throughout).
- Keep subtle; avoid overlapping captions.
- Legibility pass: if the logo is hard to see on any shot, add a subtle shadow, small background pill, or slight opacity adjustment. Readable but not watermark-heavy.

---

## 12 · OUTRO (must match established style)

The final scene is an end card that feels cohesive with the rest of the video.

Background (pick one):
1. Preferred: generate a minimal, text-free still in the same style (Nano Banana Pro edit + PRIMARY STYLE REFERENCE), then Veo 3.1 it (6–8s).
2. Alternative: reuse the hero moving clip with blur + darken so overlay text reads cleanly.

Layout:
- Logo centered, larger: 40–50% of canvas width (if available)
- CTA text exactly: "To read more, follow the link in the description"
- CTA text size: minimum 80 (reduce only if it would overflow)
- Strong contrast, clean spacing

---

## 13 · MUSIC + MIX

- Add an instrumental bed: hip, low-key, non-distracting, covering full duration.

Step 1 — VO track: add "Lower other audio" effect:
On the voiceover/script track, add the audio effect "Lower other audio" and set it to 15%. This automatically ducks the music when VO is playing.

Step 2 — Music track: add Compressor:
On the music track, add a Compressor effect. Only change the threshold to -30 dB — leave all other parameters at their defaults (Ratio 3:1, Attack 0, Release 0.2, Knee 4). This normalizes the music level regardless of the track's input gain.

Step 3 — Music track: set volume to 35%.

Mix check (after all three steps, scan the full timeline):
- VO is always clear and leading
- Music is present and consistent throughout — never silent or disappearing
- Result feels balanced and intentional

---

## 14 · FINAL QC (execute before delivering)

Verify every item. If any fails, fix before completing:

- No placeholders remain.  *Be sure to remove any unfilled placeholder layers that remain in the project*
- Every scene ≤ 8s (SCENE_CAP)
- No loops or jump cuts in Veo clips
- No text inside any AI imagery (TEXT_FREE)
- Captions readable on every shot
- Logo readable on every shot (if present)
- Music/VO balance correct per Section 13 leveling rules
- Outro matches established visual style
