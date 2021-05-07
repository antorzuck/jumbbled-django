from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

words=[
	"programming",
	"python",
	"javascript",
	"html",
	"bangladesh",
	"canada",
	"america",
	"indonesia",
	"website",
	"android",
	"laptop",
	"computer",
	"camera",
	"nodejs",
	"linux",
	"hacking",
	"coffee",
	"jupiter",
	"mars"
]

def rword():
	global jword, word
	word = random.choice(words)
	jum= random.sample(word, len(word))
	jword= "".join(jum)

msg=""

def homepage(request):
	rword()
	global jword, msg
	return render(request, 'index.html', {'jumbble':jword, 'msg':msg})

		
def checkans(request):
	global word, msg, jword
	user_answer= request.GET['answer']
	if user_answer == word:
		msg="Correct Answer"
		homepage(request)
	else:
		msg="Wrong Answer"
	return render(request, 'index.html', {'jumbble':jword,  'msg':msg})