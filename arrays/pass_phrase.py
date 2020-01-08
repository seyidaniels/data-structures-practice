def passphraseStrength(passphrase):
    # Write your code here
    if len(passphrase) > 0:
        passphrase = passphrase.split(' ')
        passes = {}
        for p in passphrase:
            p = p.lower()
            if p == '':
                continue
            if p in passes:
                return 'weak'
            else:
                passes[p] = True
        return 'strong'
    return 'n/a'


a = passphraseStrength("'jack', 'jack")
print(a)
