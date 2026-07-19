# Building `reading.html`

`reading.html` is generated — edit the data, not the HTML.

    python3 build/gen_reading.py

## Adding a book

Add a line to `ROWS` in `gen_reading.py`:

    <group>|<中文书名>|<English Title>|<中文作者>|<English Author>|<zh_nat>|<en_nat>

Groups are keyed by **language of composition**: `en ru fr de jp es sv da pl it bn`.
To add a language, add an entry to `GROUPS` (order there = display order).

The last two columns are nationality. They are **not currently rendered** —
the site deliberately shows no nationality labels — but the data is kept in
case that changes. Fill them in or leave them blank.

## Adding a Nobel laureate

Add a line to `NOBEL`:

    <year>|<中文名>|<English name>|<zh_nat>|<en_nat>|<中文作品>|<English works>

Multiple works are separated by ` · `. Nationality columns are again unrendered.

## Adding an excerpt

Append an object to `quotes_full.json`:

```json
{
  "i": 99,
  "zh": ["段落一", "段落二"],
  "en": ["Paragraph one", "Paragraph two"],
  "source": "original",
  "zh_title": "书名", "en_title": "Title",
  "zh_author": "作者", "en_author": "Author",
  "orig": "optional original-language text",
  "orig_label": "French original"
}
```

`source` is `"original"` when the text is quoted verbatim from a work written
in English, and `"rendering"` when it is an English rendering of the Chinese
translation. This drives the badge on the page — please keep it honest.
Keep `zh` and `en` the same length so the paragraphs line up.

## Styles

`assets/style.css` is shared with `index.html`; `assets/reading.css` is
specific to this page. `index.html` is hand-written, not generated.
