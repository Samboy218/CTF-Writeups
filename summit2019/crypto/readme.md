## DH
relevant files:
* dh.py

this problem involves breaking diffie helman key exchange

[From stackexchange](https://security.stackexchange.com/questions/45963/diffie-hellman-key-exchange-in-plain-english):

> The basic idea works like this:
>
> I come up with two prime numbers g and p and tell you what they are.
> You then pick a secret number (a), but you don't tell anyone. Instead you compute g^a % p and send that result back to me. (We'll call that A since it came from a)
> I do the same thing, but we'll call my secret number b and the computed number B. So I compute g^b % p and send you the result (called "B")
> Now, you take the number I sent you and do the exact same operation with it. So that's B^a % p.
> I do the same operation with the result you sent me, so: A^b % p.


we are given A, B, p, and g.  
we want A^b % p, which is the key, so first we need to find b.  
b is just a random number such that g^b % p = B.  
so we start i at 0 and calculate g^i % p, and if that equals B then i == b and we can calculate A^b % p.  

`` p = 522590389
g = 2164
 
A sends 492973999 to B
B sends 8199534 to A``


## Caesar in russian
relevant files:
* caesarRussian.py

we are given the russian string млб зрмли анлйэ, and the title of the challenge is "caesar in russian".  
this is clearly a caesar cipher, but it is more difficult because pretty much all caesar crackers use ASCII.  
After messing around with unicode in python for a while, I got a script to do all of the caesar combinations,
then I threw those into ggogle translate and one came out to "под купол громѐ : under the dome of thunder",
the theme of this competition was mad max's thunderdome, so that was definitely it.  
NOTE: unicode does not have the russian alphabet completely in order, so the last character is wrong
