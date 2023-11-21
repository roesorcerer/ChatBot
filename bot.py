# bot.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus
from cleaner import extract_questions_and_answers
from datasets import load_dataset

CORPUS_FILE = "chat.txt"


# Load the dataset using the datasets library https://huggingface.co/datasets/ambig_qa
dataset = load_dataset("ambig_qa")

questions, answers = extract_questions_and_answers(dataset["train"])

chatbot = ChatBot("Chatpot")
trainer = ListTrainer(chatbot)

cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(cleaned_corpus)


exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        response = chatbot.get_response(query)
        print(f"🪴 {response}")