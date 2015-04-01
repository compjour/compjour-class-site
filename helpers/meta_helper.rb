def page_title
  data_title = current_page.data.title
  if data_title.blank? || data_title == config[:site_title]
    # e.g. Move Fast and Blah | Stuff for Blah
    [config[:site_title], config[:site_deck]].join(' | ')
  else
    # e.g. This Page | Move Fast and Blah
    "#{data_title} | #{config[:site_title]}"
  end
end


def page_author
  current_page.data.author || config[:site_author]
end

def page_description
  current_page.data.description || config[:site_description]
end


def current_lede_image_url
  if (m = current_page.data.metax)
    if (img = m.lede_image)
      return img
    end
  end
end

def current_lede_image_caption
  if (m = current_page.data.metax)
    if (txt = m.lede_caption)
      return make_markdown txt
    end
  end
end
