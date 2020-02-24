from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from django.http import JsonResponse
from .models import Password, Candidate, Vote
# Create your views here.
def index(request):
    if request.method == "POST":
        current_password = get_object_or_404(Password, current = True)
        pwd = request.POST["password"]
        if pwd == current_password.password:
            current_candidates = get_list_or_404(Candidate, current = True)
            dic = {}
            for can in current_candidates:
                dic[str(can.no)] = can.name
            col_size = int(12/len(current_candidates))
            context = {
                "password":   pwd,
                "candidates": current_candidates,
                "dic": dic,
                "year": current_candidates[0],
                "classes": f'col-md-{col_size} col-sm-{col_size} col-lg-{col_size}'
            }
            return render(request, 'vote.html', context)
        return redirect("/")
    return render(request, 'index.html')


def vote(request):
    if request.method == "POST":
        current_password = get_object_or_404(Password, current = True)
        pwd  = request.POST["password"]
        if "no" in request.POST:
            no   = request.POST["no"]
        else:
            no = 69
        year = request.POST["year"]
        print(no, year)
        if pwd == current_password.password:
            vote = Vote.objects.create(no=no, year=year)
            return redirect("/")
    return redirect("/")


def quick_count(request):
    candidates = get_list_or_404(Candidate)
    count = {}
    for c in candidates:
        count[c.name] = len(Vote.objects.filter(no=c.no, year=c.year))
    return JsonResponse(count)
