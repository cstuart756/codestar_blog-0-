from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import Post
from .forms import CommentForm


def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)  # if your project uses status=1 for published
    post = get_object_or_404(queryset, slug=slug)

    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()

            messages.add_message(
                request,
                messages.SUCCESS,
                "Comment submitted and awaiting approval",
            )

            # Optional UX improvement (not in your steps, but recommended):
            # Re-instantiate form so the textarea clears after submission.
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )
