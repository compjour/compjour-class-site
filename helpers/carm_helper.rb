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

  str = link_to t, c.url, opts
  if opts[:include_description]
    str = "#{str} &ndash; <span class=\"description\">#{c.description}</span>"
  end

  return str


end


def homework_due_date
  friendly_date current_page.data.due_date
end
