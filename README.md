# mailboy 📬

Lightweight and dead-simple API client. 
Parody of Postman out of frustations.
No account required.
No cloud-connections.
No bloat present. if there, tell me. I'll nuke it out. 

Built with Python, SQLite, Tkinter(WIP).

---

## Structure

```
mailboy/
├── mailboy.py          # entry point of the thing. But Nothing in there..
├── cli/
│   └── cli.py          # terminal interface. Current entry point
├── core/
│   ├── requester.py    # sends HTTP requests and fetches response.
│   ├── formatter.py    # pretty prints response to terminal.
│   └── dbm.py          # sqlite db manager.
├── gui/
│   └── app.py          # dark mode tkinter UI (WIP)
└── mailboy.db          # auto-created on first run.
```

---

## Install

```bash
[git clone https://github.com/yourname/mailboy](https://github.com/damonkern-Ux/mailboy.git)
cd mailboy
pip install requests
```

---

## Usage

### GUI (default) {Work in progress.}
```bash
python mailboy.py
python mailboy.py --gui
```

### CLI
Go to the cli.py in mailboy/cli/cli.py and run this.
```bash
python cli.py GET https://jsonplaceholder.typicode.com/posts/1
python cli.py POST https://api.example.com -b '{"name":"test"}'
python cli.py GET https://api.example.com -H "Authorization:Bearer token"
```

### Flags
```
-H, --header     Header in Key:Value format. Repeatable.
-b, --body       Request body as JSON string.
-l, --list       List request history.
-d, --delete     Delete all history.
--gui            Launch GUI. (work in progress)
```

---

## Examples

```bash
# Simple GET
python cli.py GET https://jsonplaceholder.typicode.com/posts/1

# POST with body
python cli.py POST https://jsonplaceholder.typicode.com/posts \
  -b '{"title":"foo","body":"bar","userId":1}'

# With auth header
python cli.py GET https://api.example.com/me \
  -H "Authorization:Bearer abc123"

# View history
python cli.py -l

# Clear history
python cli.py -d
```

---

## Output

```
STATUS: 200
TIME: 0.2053s
TOTAL TIME: 0.2152s
BODY:
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere...",
  "body": "quia et suscipit..."
}
```

---

## Why mailboy?

Postman forces an account. 
Bruno is getting bloated. 
mailboy does one thing — 
  1. send requests
  2. show response
  3. save history.

That's it!!

- No account required
- Stores history locally in SQLite
- Works in terminal and GUI(WIP)

---

## Support

If mailboy saves you time → [UPI](srilaxmi84@ybl)

---

## License

MIT
