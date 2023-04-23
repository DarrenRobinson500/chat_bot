from django.shortcuts import render, redirect
from django.contrib import messages
import openai
from .models import *
from django.core.paginator import Paginator

def home(request):
    if request.method == "POST":
        past_responses = request.POST['past_responses']
        question = request.POST['question']
        openai.api_key="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"
        openai.Model.list()
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=question,
                temperature=0,
                max_tokens=600,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
            )
            response = response['choices'][0]['text'].strip()

            if "unusual response 84" in past_responses: past_responses = response
            else: past_responses = f"{past_responses}<br><br>{response}"

            record = Past(question=question, answer=response)
            record.save()
            record.clean_text()

            context = {"question": question, "response": response, "past_responses": past_responses}
            return render(request, 'home.html', context)
        except Exception as e:
            context = {"question": question, "response": e, "past_responses": past_responses}
            return render(request, 'home.html', context)

    return render(request, 'home.html', {})

def past(request):
    user = User.objects.all().first()
    labels = Label.objects.all().order_by('name')
    items = Past.objects.all().order_by('id')
    if user.label.name == "None":
        items = items.filter(label__isnull=True)
    elif user.label.name != "All":
        items = items.filter(label=user.label)

    p = Paginator(items, 10, )
    page = request.GET.get('page')
    pages = p.get_page(page)
    nums = range(1, pages.paginator.num_pages + 1)
    context = {"pages": pages, "nums": nums, 'labels': labels, 'user': user}
    return render(request, 'past.html', context)

def delete(request, id):
    past = Past.objects.get(id=id)
    past.delete()
    messages.success(request, "That question and answer have been deleted")
    return redirect('past')

def label_answer(request, item_id, label_id):
    item = Past.objects.get(id=item_id)
    label = Label.objects.get(id=label_id)
    item.label = label
    item.save()
    return redirect('past')

def label_filter(request, label_id):
    user = User.objects.all().first()
    label = Label.objects.get(id=label_id)
    user.label = label
    user.save()
    return redirect('past')

def new_label(request):
    name = request.POST['label_name']
    new = Label(name=name)
    new.save()
    return redirect('past')