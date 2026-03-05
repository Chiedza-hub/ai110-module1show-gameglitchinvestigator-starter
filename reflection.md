# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

- Answers
- It looked pretty straight forward and simple. It had clear instructions. 

- Bugs
- it would always print guess from 1-100 even if in easy mode where range is 1-20
- It would tell you to go higher if you actually had to go lower and vice versa
- It would generate out of range secret numbers. 
---


## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

- Answers
- I used Claude.
- The AI suggested having high and low variables be the range of the randomly generated secret number instead of a fixed 1 - 100. This helped with generating numbers that are in range.
- The AI kept the range of medium as 1 - 100 and high as 1 - 50 instead of switching the two. In this case, I wouldn't say it was misleading, but it kept building code on wrong assumptions. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

- Answers
- I would run streamlit and play the game to see if I would run into the same issue. 
- For the bug where it would have the secret word out of the level range, I played the game in hard mode first and checked if the secret number was in range. I switched modes to normal and played multiple times checking if the correct answer was in-range. I did the same for easy mode. 
- For testing, I prompted claude to make tests for edge cases that we were discussing. It made the tests and ran them and passed. To verify, I played the game to see if I was running into the same issue. 
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

- Answers
- Everytime we started a game, streamlit would run app.py and generate a random number for secret. This made sure that each game had a random number. 
- when we say StreamLit reruns we mean that everytime we enter our guess, we start executing our code from the start. It is like refreshing a webpage. But, in order for us not to lose the guess value, we use session_state. Session_state contains the values we keep even if we refresh a page.
- I changed the range from 1-100 to low-high. low and high being the bounds of the level. For example, if low is 1 and high is 20 for the easy level. I also changed secret to be recomputed with a new bound each time we changed the difficulty level. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

- Answers
- I am happy I am now somehow comfortable with git. That is something I want to continue being better at
- I want to be better at testing. The syntax was kinda new like session_state so I just accepted edits without being really confident in them. 
- AI generated code needs human intervention. As such, AI cannot replace software engineers, but it can only make them faster. 
