def codepiece(fpath, opts = {})
  fname = File.join("/files/code/", fpath)
  raw_content = get_raw_content_from_file(fname)
  splits = raw_content.split(/^# ----$/)
  if splits.count > 1
    polished_content = splits[1..-1].join("\n# ----\n").strip
  else
    polished_content = raw_content
  end

  # determine language
  lang = opts[:lang] || case File.extname(fpath)
  when /rb/   ; 'ruby'
  when /py$/  ; 'python'
  when /sh$/  ; 'shell'
  when /html/ ; 'html'
  when /xml/  ;  'xml'
  when /css/  ;  'css'
  when /json/ ;  'json'
  when /yaml/ ;  'yaml'
  else
    nil
  end

  display_class = opts[:display_class]

  partial "/layouts/site/codepiece",
    locals: { content: polished_content, display_class: display_class,
              lang: lang, path: fname, url: fname, }

end


# hacky!
# was having trouble with getting files in /code
def get_raw_content_from_file(path)
  if contains_leading_underscore?(path)
    # attempt absolute path
    z = File.expand_path(path, sitemap.app.source_dir)
    File.read(z)
  else
    sitemap.find_resource_by_path(path).render
  end
end


def contains_leading_underscore?(path)
  path.to_s.split('/').any?{|p| p =~ /^_/ }
end
