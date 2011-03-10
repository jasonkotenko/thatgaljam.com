from django.contrib.syndication.views import Feed
from thatgaljam.posts.models import Post

class PostFeed(Feed):
  title = "Jam Regis' Blog"
  link = "/"
  description = "Churning awesomeness since 1984."
  description_template = 'feeds/post_description.html'
  
  def items(self):
    return Post.objects.order_by('-pub_date')[:5]

  def item_title(self, item):
    return item.title

  def item_description(self, item):
    return item.body

  def item_link(self, item):
    return "/posts/" + item.slug
