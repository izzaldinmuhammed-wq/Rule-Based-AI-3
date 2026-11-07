import random
import string
print("==============================")
print("       RULE BASED AI 3.0")
print("==============================")
print("100 Words | 10 Categories | 20 Responses")
print("Type 'exit' to terminate the AI.")
categories = {
    0: ["hello", "hi", "hey", "greetings", "howdy", "welcome", "hola", "bonjour", "morning", "hiya"],
    1: ["joke", "funny", "humor", "comedy", "laugh", "hilarious", "giggle", "pun", "meme", "riddle"],
    2: ["goodbye", "bye", "farewell", "later", "ciao", "adios", "goodnight", "leaving", "depart", "peace"],
    3: ["what", "why", "when", "where", "who", "which", "how", "explain", "describe", "clarify"],
    4: ["thanks", "thank", "appreciate", "grateful", "thankful", "kindness", "generous", "assistance", "blessing", "cheers"],
    5: ["sorry", "apologies", "apologize", "regret", "mistake", "fault", "forgive", "pardon", "oops", "remorse"],
    6: ["yes", "yeah", "yep", "yup", "agree", "absolutely", "correct", "exactly", "certainly", "definitely"],
    7: ["no", "nope", "nah", "disagree", "incorrect", "false", "never", "reject", "opposed", "negative"],
    8: ["help", "assist", "support", "guide", "teach", "learn", "advice", "problem", "solution", "instructions"],
    9: ["happy", "sad", "angry", "excited", "scared", "nervous", "lonely", "confused", "worried", "tired"]
}
vocabulary = {}
for category, words in categories.items():
    for word in words:
        weights = [0.0] * 10
        weights[category] = 0.9
        vocabulary[word] = weights
biases = [0.0] * 10
responses = {
    0: ["Hello! How can I help you today?", "Hey there! It's nice to meet you!"],
    1: ["Why did the computer get cold? It left its Windows open!", "What do you call a robot that takes the long way around? R2-Detour!"],
    2: ["Goodbye! Have a wonderful day!", "See you later! Come back anytime!"],
    3: ["That's an interesting question! Tell me more.", "I'd love to help you understand that!"],
    4: ["You're very welcome! Happy to help!", "No problem! I appreciate your kindness!"],
    5: ["That's okay! Everyone makes mistakes.", "No worries! There's always room for improvement."],
    6: ["Absolutely! I'm glad we agree.", "Exactly! That's what I was thinking."],
    7: ["Interesting! We don't always have to agree.", "I respect your opinion! Let's discuss it."],
    8: ["Of course! What do you need help with?", "I'm here to assist you. Tell me your problem!"],
    9: ["I'm listening. Would you like to tell me more?", "Emotions are important. How can I support you?"]
}
print("\nVocabulary size:", len(vocabulary))
print("Number of categories:", len(categories))
print("Number of possible responses:", sum(len(r) for r in responses.values()))
print("\nAI is ready!\n")
print("===============================================================================================================================================")
print("Try using words related to greeting, jokes, goodbyes, question words, appreciating, apologising, agreeing, disagreeing, helping, and emotions.")
print("===============================================================================================================================================")
while True:
    user_input = input("You: ").lower().strip()
    if user_input == "exit":
        print("AI: Goodbye! Have a great day!")
        break
    cleaned_input = user_input.translate(str.maketrans("", "", string.punctuation))
    words = cleaned_input.split()
    scores = biases.copy()
    for word in words:
        if word in vocabulary:
            for i in range(10):
                scores[i] += vocabulary[word][i]
    if not any(word in vocabulary for word in words):
        print("AI: I'm not sure what you mean. Could you rephrase?")
        continue
    prediction = scores.index(max(scores))
    ai_response = random.choice(responses[prediction])
    print("AI:", ai_response, "\n")