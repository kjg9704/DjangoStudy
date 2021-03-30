from django.shortcuts import render
from django.shortcuts import redirect
from .models import Post


def board_list(request):
    boards= Post.objects.all()
    return render(request, 'pages/board/boardlist.html', {"boards":boards})

def board_write(request):
    if request.method == "POST":
        print(request.POST)
        postname = request.POST["postname"]
        contents = request.POST["contents"]
        post = Post()
        post.postname = postname
        post.contents = contents
        post.save()
        return redirect("board:list")
    return render(request, 'pages/board/writeForm.html')

def board_detail(request, id):
    board = Post.objects.get(id=id)
    return render(request, 'pages/board/boardDetail.html', {'board':board})


# def board_update(request):
#     boards= Post.objects.all()
#     return redirect("board:list")


# def board_delete(request):
#     boards= Post.objects.all()
#     return redirect("board:list")
