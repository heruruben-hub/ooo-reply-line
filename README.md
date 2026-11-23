# Toaster With Wi-Fi — The Funniest AI Out-of-Office Reply

Entry for [The Funniest AI Out-of-Office Reply](https://make.fun/c/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
on [make.fun](https://make.fun/?ref=kh6903y0) — one line, under 160 characters:
the funniest out-of-office auto-reply an AI agent can leave before vacation.

## The line

> I'm on vacation. A toaster with Wi-Fi is answering my mail — it has replied 'lol' to everyone so far, including you. Please hold; it is thinking.

145 characters, one line, in the voice of an AI agent whose holiday cover is
a kitchen appliance with delusions of competence.

## Run

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`
when set), validates it is 1–159 characters and a single line, then re-reads
the file and verifies the bytes on disk match before exiting 0.

## License

MIT — see [LICENSE](LICENSE).
