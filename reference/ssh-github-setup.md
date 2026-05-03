# SSH GitHub Setup

How to generate a new SSH key and connect to GitHub for `git push`.

## Steps

### 1. Generate a new ED25519 key

```bash
ssh-keygen -t ed25519 -C "loriamichaelj"
```

- Accept the default file path (`~/.ssh/id_ed25519`)
- Press Enter twice for no passphrase

### 2. Copy the public key to your clipboard

```bash
pbcopy < ~/.ssh/id_ed25519.pub
```

### 3. Add the key to GitHub

1. Go to **github.com → Settings → SSH and GPG keys**
2. Click **New SSH key**
3. Title: e.g. `MacBook`
4. Key type: **Authentication Key**
5. Paste the key and click **Add SSH key**

### 4. Load the key into the SSH agent

```bash
ssh-add ~/.ssh/id_ed25519
```

### 5. Test the connection

```bash
ssh -T git@github.com
# Hi loriamichaelj! You've successfully authenticated...
```

### 6. Push

```bash
git push
```

## Notes

- The `-C` flag is just a label — it doesn't affect which GitHub account the key connects to.
- If you see `Permission denied (publickey)`, your key isn't loaded — run `ssh-add` again.
- To check loaded keys: `ssh-add -l`
