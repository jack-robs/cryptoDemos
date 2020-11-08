# Caesar Cipher Project

- this is a demo of a caesar cipher, pretty simple cipher but using the simple enryption/decryption to work with OOD approaches, especially in python, and see if I can figure out frequency analysis decryption (programmatically and from UX perspective) 

- Also, putting some focus in to building OO-focused testing suite, see test_CaesarCipher.p

## Design Approach TODO sync this given some more building work
- Class `CaesarCipher`
    - an instance of caesar cipher use
    - instantiation:
        - message: str `message
            - TODO make message class
        - key: int `key` 
            - TODO: DHM exchange? that would be neat
    - encrypt using `instance.encrypt()`
        - TODO: strategy pattern, other encryption strats?
    - decrypt using `instance.decrypt()`
        - TODO: sort out key storage? I gueess if `null` in `key` then 
        throw error 
    - break using (freq analysis) `instance.breakCipher()`
    - get fiels using instance.fieldname (vs. getters/setters)

- to do: how to represent alphabet, not sure if ascii math works on python

## Docs
- Class: `CaesarCipher()`
    - instantiate: 
        - `message` (str)
        - `key` (int)
    - fields;
        - `key`: set by instantiation
        - `message`: record of message, as `plaintext` mutates 
        - `plaintext`: set by instantiation
        - `ciphertext`: set by `encrypt`

    - methods:
        - `encrypt()`
            - does: encrypts provided plaintext (field set by `message`), sets `self.ciphertext`
        - `decrypt()`
            - does: ..., sets `self.plaintext`
        - `break()`
            - does: attempts frequency analysis, probably some interaction with the user from this
            - sets `self.breakAttempt`
            - also, could just return a value, once freq analys works...
        














