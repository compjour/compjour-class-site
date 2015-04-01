def carm_content
  sitemap.resources.select{|r| r.url =~ /\/(?:articles|tutorials|weeks)\/\w+/ }
end


def link_to_part_of
  slug = current_page.data.nav.part_of
  link_to_slug(slug)
end


def nav_next?
  if (n = current_page.data.nav)
    !n.next.nil?
  end
end

def nav_part_of?
  if (n = current_page.data.nav)
    !n.part_of.nil?
  end
end

def nav_prev?
  if (n = current_page.data.nav)
    !n.prev.nil?
  end
end

def link_to_slug(slug, title = nil, opts = {})
  c = carm_content.find{|c| c.url =~ /#{Regexp.escape(slug)}/ }
  t = title || c.data.title

  link_to t, c.url, opts
end
