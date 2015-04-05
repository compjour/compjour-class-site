# TK todo, make this a singleton
def carm
  Carm.new(sitemap)
end

def current_content_article
  carm.get_content_article(current_page)
end



# not used directly
# def carm_content
#   carm.content
# end

def carm_curriculum
  carm.curriculum
end



def link_to_slug(slug, title = nil, opts = {})
  c = carm.find_content(slug)
  t = title || c.title

  link_to t, c.url, opts
end
