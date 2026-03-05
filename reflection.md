# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
It had hard mode 1-50 and normal 1-100 so 
it would always print guess from 1-100 even if in easy mode
It would tell you to go higher if you actually had to go lower
it would generate an out of range secret 
It would allow numbers that are our of range like 200
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

- it would always print guess from 1-100 even if in easy mode
- It would tell you to go higher if you actually had to go lower
---


## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

- I used Claude
- The AI suggested having high and low variables be the range of the randomly generated secret number instead of a fixed 1 - 100. This helped with generating numbers that are in range.
- The AI kept the range of medium as 1 - 100 and high as 1 - 50 instead of switching the two. In this case, I wouldn't say it was misleading, but it kept building code on wrong assumptions. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

- I would run streamlit and play the game to see if I would run into the same issue. 
- For the bug where it would have the secret word out of the level range, I played the game in hard mode first and checked if the secret number was in range. I switched modes to normal and played multiple times checking if the correct answer was in-range. I did the same for easy mode. 
- For this projectm I did not write any tests, but I played the ga
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
