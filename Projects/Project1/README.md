# Project 1: Cryptographic Attacks

## Introduction

In this project, you will investigate vulnerabilities in widely used cryptographic hash functions, including length-extension attacks and collision vulnerabilities, and an implementation vulnerability in a popular digital signature scheme.
In Part 1, we will guide you through attacking the authentication capability of an imaginary server API.
The attack will exploit the length-extension vulnerability of hash functions in the MD5 and SHA family.
In Part 2, you will use a cutting-edge tool to generate different messages with the same MD5 hash value (collisions).
You'll then investigate how that capability can be exploited to conceal malicious behavior in software.
In Part 3, you will learn about an attack against certain implementations of RSA padding; then, you will forge a digital signature using your own implementation of this attack.

### Objectives
* Understand how to apply basic cryptographic integrity and authentication primitives.
* Investigate how cryptographic failures can compromise the security of applications.
* Appreciate why you should use HMAC-SHA256 as a substitute for common hash functions.
* Understand why padding schemes are integral to cryptographic security.

## Part 1. Length Extension

In most applications, you should use MACs such as HMAC-SHA256 instead of plain cryptographic hash functions (e.g. MD5, SHA-1, or SHA-256), because hashes, also known as digests, fail to match our intuitive security expectations.
What we really want is something that behaves like a pseudorandom function, which HMACs seem to approximate and hash functions do not.
One difference between hash functions and pseudorandom functions is that many hashes are subject to **length extension**.
All the hash functions we've discussed use a design called the Merkle-Damgård construction.
Each is built around a **compression function** *f* and maintains an internal state *s*, which is initialized to a fixed constant.
Messages are processed in fixed-sized blocks by applying the compression function to the current state and current block to compute an updated internal state, *s*<sub>*i* + 1</sub> = *f*(*s*<sub>*i*</sub>, *b*<sub>*i*</sub>).
The result of the final application of the compression function becomes the output of the hash function.

A consequence of this design is that if we know the hash of an *n*-block message, we can find the hash of longer messages by applying the compression function for each *b*<sub>*n* + 1</sub>, *b*<sub>*n* + 2</sub>, ... that we want to add.
This process is called length extension, and it can be used to attack many applications of hash functions.

### 1.1 Experiment with Length Extension in Python

To experiment with this idea, we'll use a Python implementation of the MD5 hash function, though SHA-1 and SHA-256 are vulnerable to length extension too.
You can download the `pymd5` at https://www.eecs.umich.edu/courses/eecs388/static/project1/pymd5.py and learn how to use it by running `$ pydoc pymd5`.
To follow along with these examples, run Python in interactive mode (`$ python -i`) and run the command `from pymd5 import md5`, padding.
Consider the string "Use HMAC, not hashes".
We can compute its MD5 hash by running:
```python
m = "Use HMAC, not hashes"
h = md5()
h.update(m)
print h.hexdigest()

```
or, more compactly, `print md5(m).hexdigest()`.
The output should be:
```python
3ecc68efa1871751ea9b0b1a5b25004d
```
MD5 processes messages in 512-bit blocks, so, internally, the hash function pads *m* to a multiple of that length.
The padding consists of the bit 1, followed by as many 0 bits as necessary, followed by a 64-bit count of the number of bits in the unpadded message.
(If the 1 and count won't fit in the current block, an additional block is added.)
You can use the function `padding(count)` in the `pymd5` module to compute the padding that will be added to a `count`-bit message.

Even if we didn't know `m`, we could compute the hash of longer messages of the general form
`m + padding(len(m)*8) + suffix`
by setting the initial internal state of our MD5 function to `MD5(m)`, instead of the default initialization value, and setting the function's message length counter to the size of `m` plus the padding (a multiple of the block size).
To find the padded message length, guess the length of `m` and run
`bits = (length_of_m + len(padding(length_of_m *8)))*8`.

The `pymd5` module lets you specify these parameters as additional arguments to the `md5` object:
```python
h = md5(state="3ecc68efa1871751ea9b0b1a5b25004d".decode("hex"), count=512)
```
Now you can use length extension to find the hash of a longer string that appends the suffix "Good advice."
Simply run:
```python
x = "Good advice"
h.update(x)
print h.hexdigest()
```
to execute the compression function over `x` and output the resulting hash.
Verify that it equals the MD5 hash of `m + padding(len(m)*8) + x`.
Notice that, due to the length-extension property of MD5, we didn't need to know the value of `m` to compute the hash of the longer string--all we needed to know was `m`'s length and its MD5 hash.

This component is intended to introduce length extension and familiarize you with the Python MD5 module we will be using; you will not need to submit anything for it.


### 1.2 Conduct a Length Extension Attack

Length extension attacks can cause serious vulnerabilities when people mistakenly try to construct something like an HMAC by using `hash(secret || message)`.
The National Bank of EECS 388, which is not up-to-date on its security practices, hosts an API that allows its client-side applications
to perform actions on behalf of a user by loading URLs of the form: https://eecs388.org/project1/api?token=dfedf63833fcfe1221223a83185ca81c&user=admin&command1=ListFiles&command2=NoOp
where `token` is `MD5(user's 8-character password || user= ...[the rest of the URL starting from user= and ending with the last command])`.
Using the techniques that you learned in the previous section and without guessing the password, apply length extension to create a URL ending with `&command3=UnlockAllSafes` that is treated as valid by the server API.
You have permission to use our server to check whether your command is accepted.

*Hint:* You might want to use the `quote()` function from Python's `urllib` module to encode non-ASCII characters in the URL.

> Historical fact: In 2009, security researchers found that the API used by the photo-sharing site Flickr suffered from a length-extension vulnerability almost exactly like the one in this exercise.


#### What to submit 
A Python 2.x script named `len_ext_attack.py` that:

1. Accepts a valid URL in the same form as the one above as a command line argument.
2. Modifies the URL so that it will execute the `UnlockAllSafes` command as the user.
3. Successfully performs the command on the server and prints the server's response.

You should make the following assumptions:
* The input URL will have the same form as the sample above, but we may change the server hostname and the values of `token`, `user`,` command1`, and `command2` (although they will remain in the same order).
These values may be of substantially different lengths than in the
sample.
* The input URL may be for a user with a different password, but the length of the password will be unchanged.
* The server's output might not exactly match what you see during testing.

You can base your code on the following example:
```python
import httplib, urlparse, sys
url = sys.argv[1]
# Your code to modify url goes here
parsedUrl = urlparse.urlparse(url)
conn = httplib.HTTPSConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()
```
